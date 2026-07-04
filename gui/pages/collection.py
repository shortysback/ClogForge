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

        self.items = QListWidget()

        right.addWidget(self.title)
        right.addWidget(self.progress)
        right.addWidget(self.percent)
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

                item = QListWidgetItem(
                    f"{activity['name']}\n"
                    f"{activity['complete']}/{activity['total']} "
                    f"({activity['percent']:.1f}%)"
                )

                item.setData(Qt.UserRole, activity)

                self.activityList.addItem(item)

    def load_activity(self, current, previous):

        if current is None:
            return

        activity = current.data(Qt.UserRole)

        self.title.setText(activity["name"])

        self.progress.setValue(int(activity["percent"]))

        self.percent.setText(
            f"{activity['complete']} / {activity['total']} Items"
        )

        self.items.clear()

        for item in activity["items"]:

            if item["count"]:
                self.items.addItem(f"☑ {item['name']}")
            else:
                self.items.addItem(f"☐ {item['name']}")