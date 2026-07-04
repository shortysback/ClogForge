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

        layout = QVBoxLayout(self)
        layout.setSpacing(8)

        title = QLabel(name)
        title.setObjectName("CardTitle")

        progress = QProgressBar()
        progress.setRange(0, 100)
        progress.setValue(int(percent))
        progress.setTextVisible(False)

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