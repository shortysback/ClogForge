from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)


class ActivitiesPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        title = QLabel("<h1>Activities</h1>")
        layout.addWidget(title)

        layout.addWidget(
            QLabel("Activities page coming soon.")
        )

        layout.addStretch()

        self.setLayout(layout)