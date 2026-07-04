from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QProgressBar,
    QVBoxLayout,
)


class ActivityCard(QFrame):

    clicked = Signal(str)

    def __init__(self, name, complete, total):
        super().__init__()

        self.name = name

        self.setObjectName("StatCard")
        self.setCursor(Qt.PointingHandCursor)

        percent = (complete / total * 100) if total else 0

        if percent == 100:
            color = "#2ECC71"
        elif percent >= 75:
            color = "#7ED957"
        elif percent >= 50:
            color = "#F1C40F"
        elif percent >= 25:
            color = "#E67E22"
        else:
            color = "#E74C3C"

        layout = QVBoxLayout(self)

        title = QLabel(name)
        title.setObjectName("CardTitle")

        progress = QProgressBar()
        progress.setRange(0, 100)
        progress.setValue(int(percent))
        progress.setTextVisible(False)

        progress.setStyleSheet(f"""
            QProgressBar {{
                border:none;
                background:#1E1F22;
                border-radius:8px;
                height:18px;
            }}

            QProgressBar::chunk {{
                background:{color};
                border-radius:8px;
            }}
        """)

        value = QLabel(f"{complete}/{total} items")
        value.setAlignment(Qt.AlignCenter)

        percentLabel = QLabel(f"{percent:.1f}% Complete")
        percentLabel.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(progress)
        layout.addWidget(value)
        layout.addWidget(percentLabel)

    def mousePressEvent(self, event):
        self.clicked.emit(self.name)
        super().mousePressEvent(event)

    def enterEvent(self, event):
        self.setStyleSheet("""
            QFrame{
                background:#383C45;
                border-radius:14px;
            }
        """)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet("")
        super().leaveEvent(event)