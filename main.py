from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow
import sys

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    app.setStyleSheet("""
QMainWindow{
    background:#202225;
}

QWidget{
    background:#202225;
    color:white;
    font-size:11pt;
}

QListWidget{
    background:#2b2d31;
    border:none;
    padding:8px;
}

QListWidget::item{
    padding:8px;
    border-radius:6px;
}

QListWidget::item:selected{
    background:#5865F2;
}

QToolBar{
    background:#2b2d31;
    spacing:8px;
}

QPushButton{
    background:#5865F2;
    border:none;
    border-radius:6px;
    padding:8px 16px;
    color:white;
}

QPushButton:hover{
    background:#6a75ff;
}

#StatCard{
    background:#2b2d31;
    border-radius:10px;
    padding:12px;
}

#CardTitle{
    font-size:11pt;
    color:#aaaaaa;
}

#CardValue{
    font-size:22pt;
    font-weight:bold;
}
""")
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()