from PySide6.QtWidgets import QLineEdit


class SearchBar(QLineEdit):

    def __init__(self, placeholder="Search..."):
        super().__init__()

        self.setPlaceholderText(placeholder)
        self.setClearButtonEnabled(True)
        self.setMinimumHeight(38)