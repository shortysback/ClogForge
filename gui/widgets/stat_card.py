from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class StatCard(QFrame):
    def __init__(self, title, value):
        super().__init__()

        self.setObjectName("StatCard")

        layout = QVBoxLayout()

        title_label = QLabel(title)
        title_label.setObjectName("CardTitle")

        value_label = QLabel(str(value))
        value_label.setObjectName("CardValue")
        value_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(title_label)
        layout.addStretch()
        layout.addWidget(value_label)
        layout.addStretch()

        self.setLayout(layout)