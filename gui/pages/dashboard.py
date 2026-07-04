from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)

from core.settings import load_settings
from engine.parser import load_player


class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("<h1>Dashboard</h1>")
        layout.addWidget(title)

        settings = load_settings()
        player_name = settings.get("player")

        if not player_name:
            layout.addWidget(QLabel("No player configured."))
            self.setLayout(layout)
            return

        try:
            player = load_player(player_name)

            layout.addWidget(QLabel(f"<b>Player</b><br>{player['player']}"))

            layout.addWidget(
                QLabel(
                    f"<b>Collection Progress</b><br>"
                    f"{player['completed']} / {player['available']}"
                )
            )

            layout.addWidget(
                QLabel(
                    f"<b>Completion</b><br>"
                    f"{player['percent']:.2f}%"
                )
            )

            layout.addWidget(
                QLabel(
                    f"<b>Last Temple Sync</b><br>"
                    f"{player['last_checked']}"
                )
            )

        except Exception as e:
            layout.addWidget(QLabel(f"Error loading player:\n{e}"))

        layout.addStretch()

        self.setLayout(layout)