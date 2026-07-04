from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
)


class ActivityDetailPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.backButton = QPushButton("← Back")

        self.title = QLabel()
        self.title.setObjectName("CardTitle")

        self.progress = QLabel()
        self.progress.setAlignment(Qt.AlignCenter)

        self.items = QListWidget()

        layout.addWidget(self.backButton)
        layout.addWidget(self.title)
        layout.addWidget(self.progress)
        layout.addWidget(self.items)

        self.setLayout(layout)

    def load_activity(self, player, activity):

        self.items.clear()

        self.title.setText(
            activity.replace("_", " ").title()
        )

        entries = player["activities"][activity]

        total = len(entries)
        complete = sum(i["count"] > 0 for i in entries)

        self.progress.setText(f"{complete}/{total} Items")

        for item in entries:

            icon = "☑" if item["count"] else "☐"

            self.items.addItem(
                f"{icon} {item['name']}"
            )