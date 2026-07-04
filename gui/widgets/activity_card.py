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

        title = QLabel(name)
        title.setObjectName("CardTitle")

        progress = QProgressBar()
        progress.setRange(0, 100)
        progress.setValue(int(percent))
        progress.setTextVisible(False)

        value = QLabel(f"{complete}/{total} items ({percent:.1f}%)")
        value.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(progress)
        layout.addWidget(value)

    def mousePressEvent(self, event):
        self.clicked.emit(self.name)
        super().mousePressEvent(event)