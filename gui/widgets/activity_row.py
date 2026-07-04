from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
)


class ActivityRow(QWidget):

    def __init__(self, name, percent):
        super().__init__()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)

        self.name = QLabel(name)

        self.percent = QLabel(f"{percent:.1f}%")
        self.percent.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        if percent >= 100:
            color = "#2ECC71"
        elif percent >= 75:
            color = "#6FCF97"
        elif percent >= 50:
            color = "#F2C94C"
        elif percent >= 25:
            color = "#F2994A"
        else:
            color = "#EB5757"

        self.percent.setStyleSheet(f"""
            QLabel {{
                color: {color};
                font-weight: bold;
            }}
        """)

        layout.addWidget(self.name)
        layout.addStretch()
        layout.addWidget(self.percent)