from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
)


class ActivityDetailPage(QWidget):

    def __init__(self):
        super().__init__()

        self.activity_key = None

        layout = QVBoxLayout()

        self.back_button = QPushButton("← Back")

        self.title = QLabel("Activity")
        self.title.setObjectName("CardTitle")

        self.progress = QLabel("")
        self.progress.setAlignment(Qt.AlignCenter)

        self.list = QListWidget()

        layout.addWidget(self.back_button)
        layout.addWidget(self.title)
        layout.addWidget(self.progress)
        layout.addWidget(self.list)

        self.setLayout(layout)

    def load_activity(self, player, activity_key):

        self.activity_key = activity_key

        self.title.setText(
            activity_key.replace("_", " ").title()
        )

        self.list.clear()

        items = player["activities"][activity_key]

        total = len(items)

        complete = sum(
            1 for item in items
            if item["count"] > 0
        )

        self.progress.setText(
            f"{complete}/{total} Items"
        )

        for item in items:

            if item["count"] == 0:
                self.list.addItem(f"☐ {item['name']}")
            else:
                self.list.addItem(f"☑ {item['name']}")