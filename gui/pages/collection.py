from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
)

from core.settings import load_settings
from engine.parser import load_player


class CollectionPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("<h1>Collection</h1>")
        layout.addWidget(title)

        settings = load_settings()
        player = load_player(settings["player"])

        self.list = QListWidget()

        activities = []

        for activity in player["activities"]:

            items = player["activities"][activity]

            total = len(items)

            complete = sum(
                1
                for item in items
                if item["count"] > 0
            )

            percent = (complete / total) * 100 if total else 0

            if percent >= 90:
                icon = "🟢"
            elif percent >= 50:
                icon = "🟡"
            else:
                icon = "🔴"

            activities.append(
                (
                    percent,
                    f"{icon} {activity.replace('_',' ').title()}\n"
                    f"    {complete}/{total} items ({percent:.0f}%)"
                )
            )

        activities.sort(reverse=True)

        for _, text in activities:
            self.list.addItem(text)

        layout.addWidget(self.list)

        self.setLayout(layout)