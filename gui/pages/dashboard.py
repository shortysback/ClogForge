from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QProgressBar,
)

from core.settings import load_settings
from engine.parser import load_player


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        root = QVBoxLayout()
        root.setSpacing(20)
        root.setContentsMargins(20, 20, 20, 20)

        settings = load_settings()
        player_name = settings.get("player")

        if not player_name:
            root.addWidget(QLabel("No player loaded."))
            self.setLayout(root)
            return

        player = load_player(player_name)

        #
        # HERO
        #

        hero = QFrame()
        hero.setObjectName("StatCard")

        heroLayout = QVBoxLayout()

        title = QLabel("Overall Collection Progress")
        title.setObjectName("CardTitle")

        progress = QProgressBar()
        progress.setValue(int(player["percent"]))
        progress.setFixedHeight(28)
        progress.setTextVisible(False)

        percent = QLabel(f"{player['percent']:.2f}%")
        percent.setObjectName("CardValue")
        percent.setAlignment(Qt.AlignCenter)

        slots = QLabel(
            f"{player['completed']} / {player['available']} Collection Slots"
        )
        slots.setAlignment(Qt.AlignCenter)

        heroLayout.addWidget(title)
        heroLayout.addSpacing(8)
        heroLayout.addWidget(progress)
        heroLayout.addWidget(percent)
        heroLayout.addWidget(slots)

        hero.setLayout(heroLayout)

        root.addWidget(hero)

        #
        # Bottom Row
        #

        row = QHBoxLayout()
        row.setSpacing(20)

        row.addWidget(self.card("Estimated Hours", "Coming Soon"))
        row.addWidget(self.card("Best Next Activity", "Coming Soon"))
        row.addWidget(self.card("Closest To Completion", "Coming Soon"))

        root.addLayout(row)

        self.setLayout(root)

    def card(self, title, value):

        frame = QFrame()
        frame.setObjectName("StatCard")

        layout = QVBoxLayout()

        t = QLabel(title)
        t.setObjectName("CardTitle")

        v = QLabel(value)
        v.setObjectName("CardValue")
        v.setAlignment(Qt.AlignCenter)

        layout.addWidget(t)
        layout.addStretch()
        layout.addWidget(v)
        layout.addStretch()

        frame.setLayout(layout)

        return frame