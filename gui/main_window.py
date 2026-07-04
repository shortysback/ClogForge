from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QListWidget,
    QMainWindow,
    QSplitter,
    QStackedWidget,
    QStatusBar,
    QToolBar,
    QLabel,
    QPushButton,
    QInputDialog,
    QMessageBox,
)

from core.settings import load_settings, save_settings
from core.api.temple import sync_player

from gui.pages.dashboard import DashboardPage
from gui.pages.collection import CollectionPage
from gui.pages.reports import ReportsPage
from gui.pages.settings import SettingsPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.settings = load_settings()

        self.setWindowTitle("ClogForge")
        self.resize(1400, 850)

        #
        # Toolbar
        #

        toolbar = QToolBar()
        toolbar.setMovable(False)

        self.sync_button = QPushButton("Sync Temple")
        self.sync_button.clicked.connect(self.sync_temple)
        toolbar.addWidget(self.sync_button)

        toolbar.addSeparator()

        player = self.settings.get("player", "Not Loaded")
        self.player_label = QLabel(f"Player: {player}")
        toolbar.addWidget(self.player_label)

        self.addToolBar(toolbar)

        #
        # Sidebar
        #

        self.sidebar = QListWidget()
        self.sidebar.addItems([
            "Dashboard",
            "Collection",
            "Reports",
            "Settings",
        ])
        self.sidebar.setMaximumWidth(180)

        #
        # Pages
        #

        self.pages = QStackedWidget()
        self.pages.addWidget(DashboardPage())
        self.pages.addWidget(CollectionPage())
        self.pages.addWidget(ReportsPage())
        self.pages.addWidget(SettingsPage())

        self.sidebar.currentRowChanged.connect(self.pages.setCurrentIndex)
        self.sidebar.setCurrentRow(0)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.sidebar)
        splitter.addWidget(self.pages)
        splitter.setStretchFactor(1, 1)

        self.setCentralWidget(splitter)

        #
        # Status Bar
        #

        self.status = QStatusBar()
        self.status.showMessage("Ready | LogForge v0.0.4")
        self.setStatusBar(self.status)

    def sync_temple(self):
        player = self.settings.get("player")

        #
        # Ask for username if we don't have one yet
        #

        if not player:
            player, ok = QInputDialog.getText(
                self,
                "Temple Username",
                "Enter your Temple username:",
            )

            if not ok:
                return

            player = player.strip()

            if not player:
                return

            self.settings["player"] = player
            save_settings(self.settings)

        #
        # Sync Temple
        #

        try:
            file_path = sync_player(player)

            self.player_label.setText(f"Player: {player}")

            self.status.showMessage(
                f"Temple sync complete - {player}"
            )

            QMessageBox.information(
                self,
                "Temple Sync",
                f"Temple data downloaded successfully!\n\nSaved to:\n{file_path}",
            )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Temple Sync Failed",
                str(e),
            )