from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QScrollArea,
    QLabel,
)

from core.settings import load_settings
from engine.parser import load_player
from gui.widgets.activity_card import ActivityCard


class CollectionPage(QWidget):

    def __init__(self):
        super().__init__()

        settings = load_settings()
        self.player = load_player(settings["player"])

        root = QVBoxLayout()

        title = QLabel("<h1>Collection</h1>")
        root.addWidget(title)

        subtitle = QLabel(
            "Browse every collection activity and your completion progress."
        )
        root.addWidget(subtitle)

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search activities...")
        self.search.textChanged.connect(self.filter)

        root.addWidget(self.search)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.NoFrame)

        container = QWidget()
        self.layout = QVBoxLayout(container)
        self.layout.setSpacing(12)

        self.cards = []

        for activity, items in sorted(self.player["activities"].items()):

            total = len(items)
            complete = sum(1 for i in items if i["count"] > 0)

            nice_name = activity.replace("_", " ").title()

            card = ActivityCard(
                nice_name,
                complete,
                total,
            )

            self.layout.addWidget(card)

            self.cards.append((nice_name.lower(), card))

        self.layout.addStretch()

        scroll.setWidget(container)

        root.addWidget(scroll)

        self.setLayout(root)

    def filter(self, text):

        text = text.lower()

        for name, card in self.cards:
            card.setVisible(text in name)