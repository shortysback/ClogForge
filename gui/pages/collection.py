from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QListWidgetItem,
    QLabel,
    QLineEdit,
    QProgressBar,
    QCheckBox,
)

from core.settings import load_settings
from engine.parser import load_player


class CollectionPage(QWidget):

    def __init__(self):
        super().__init__()

        settings = load_settings()
        self.player = load_player(settings["player"])

        root = QHBoxLayout(self)

        #
        # LEFT PANEL
        #

        left = QVBoxLayout()

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search activities...")
        self.search.textChanged.connect(self.filter)

        self.activityList = QListWidget()
        self.activityList.currentItemChanged.connect(self.load_activity)

        left.addWidget(self.search)
        left.addWidget(self.activityList)

        #
        # RIGHT PANEL
        #

        right = QVBoxLayout()

        self.title = QLabel("Select an Activity")
        self.title.setObjectName("CardTitle")

        self.progress = QProgressBar()
        self.progress.setTextVisible(False)
        self.progress.setFixedHeight(24)

        self.percent = QLabel("")
        self.percent.setAlignment(Qt.AlignCenter)

        self.remaining = QLabel("")
        self.remaining.setAlignment(Qt.AlignCenter)

        self.hideOwned = QCheckBox("Hide Owned Items")
        self.hideOwned.stateChanged.connect(self.refresh_items)

        self.items = QListWidget()

        right.addWidget(self.title)
        right.addWidget(self.progress)
        right.addWidget(self.percent)
        right.addWidget(self.remaining)
        right.addWidget(self.hideOwned)
        right.addWidget(self.items)

        root.addLayout(left, 1)
        root.addLayout(right, 2)

        self.activities = []

        for activity, items in sorted(self.player["activities"].items()):

            total = len(items)
            complete = sum(i["count"] > 0 for i in items)
            percent = (complete / total * 100) if total else 0

            self.activities.append({
                "key": activity,
                "name": activity.replace("_", " ").title(),
                "items": items,
                "complete": complete,
                "total": total,
                "percent": percent,
            })

        self.populate()

    def populate(self):

        self.activityList.clear()

        for activity in self.activities:

            text = (
                f"{activity['name']}\n"
                f"{activity['complete']}/{activity['total']} "
                f"({activity['percent']:.1f}%)"
            )

            item = QListWidgetItem(text)
            item.setData(Qt.UserRole, activity)

            self.activityList.addItem(item)

        if self.activityList.count():
            self.activityList.setCurrentRow(0)

    def filter(self, text):

        text = text.lower()

        self.activityList.clear()

        for activity in self.activities:

            if text in activity["name"].lower():

                text = (
                    f"{activity['name']}\n"
                    f"{activity['complete']}/{activity['total']} "
                    f"({activity['percent']:.1f}%)"
                )

                item = QListWidgetItem(text)
                item.setData(Qt.UserRole, activity)

                self.activityList.addItem(item)

        if self.activityList.count():
            self.activityList.setCurrentRow(0)

    def load_activity(self, current, previous):

        if current is None:
            return

        self.currentActivity = current.data(Qt.UserRole)

        activity = self.currentActivity

        self.title.setText(activity["name"])

        self.progress.setValue(int(activity["percent"]))

        remaining = activity["total"] - activity["complete"]

        self.percent.setText(
            f"{activity['complete']} / {activity['total']} Items\n"
            f"{activity['percent']:.1f}% Complete"
        )

        if remaining == 0:
            self.remaining.setText("🟢 Green Logged")
        elif remaining == 1:
            self.remaining.setText("🔴 Remaining: 1 Item")
        else:
            self.remaining.setText(f"🔴 Remaining: {remaining} Items")

        self.refresh_items()

    def refresh_items(self):

        if not hasattr(self, "currentActivity"):
            return

        activity = self.currentActivity

        self.items.clear()

        self.items.addItem("🔴 Missing Items")
        self.items.addItem("────────────────")

        for item in activity["items"]:
            if item["count"] == 0:
                self.items.addItem(f"☐ {item['name']}")

        if self.hideOwned.isChecked():
            return

        self.items.addItem("")

        self.items.addItem("🟢 Owned Items")
        self.items.addItem("────────────────")

        for item in activity["items"]:
            if item["count"] > 0:
                self.items.addItem(f"☑ {item['name']}")