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
    background:#2B2D31;
    border:none;
    spacing:12px;
    padding:8px;
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
                      
QProgressBar{
    border:none;
    background:#1B1D20;
    border-radius:10px;
    height:28px;
}

QProgressBar::chunk{
    background:#4CAF50;
    border-radius:10px;
}

#StatCard:hover{
    background:#36393F;
}
QTableWidget{
    background:#2B2D31;
    border:none;
    gridline-color:#3A3D44;
    border-radius:10px;
}

QHeaderView::section{
    background:#202225;
    color:white;
    padding:10px;
    border:none;
    font-weight:bold;
}

QLineEdit{
    background:#2B2D31;
    border:1px solid #444;
    border-radius:8px;
    padding:8px;
    color:white;
}

QLineEdit:focus{
    border:1px solid #5865F2;
}
""")
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()