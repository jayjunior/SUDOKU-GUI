import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel,QMessageBox
from PyQt5.QtCore import Qt as al , pyqtSlot
from PyQt5.QtGui import QPalette, QColor
import time
from sudokusolver import solve_sudoku


class MainWindow(QMainWindow):

    def __init__(self, sudoku):
        super(MainWindow, self).__init__()
        self.sudoku = sudoku

        self.setWindowTitle("Sudoku DEMO")
        self.create_grid(None)




    def create_grid(self,move):

        self.page = QVBoxLayout()
        self.footer = QHBoxLayout()
        solve_button = QPushButton("Solve")
        new_button = QPushButton("new Sudoku")

        self.footer.addWidget(solve_button)
        self.footer.addWidget(new_button)


        solve_button.clicked.connect(self.solve)

        solve_button.setStyleSheet("background-color:red;border:none;color:white;")
        new_button.setStyleSheet("background-color:green;border:none;color:white;")
        new_button.clicked.connect(self.generate_random_sudoku)


        grid = QGridLayout()
        grid.setSpacing(0)
        for row in range(0, 9):
            for col in range(0, 9):
                value = f"{self.sudoku[row][col]}" if self.sudoku[row][col] != 0 else " "
                if(move != None and move[0] == row and move[1] == col):
                    value = f"{move[2]}"
                field = QLabel(value)
                field.setStyleSheet(f"background-color: white;border:0.5px solid black;font-size:30px")
                field.setAlignment(al.AlignCenter)
                grid.addWidget(field, row, col)

        widget = QWidget()

        self.page.addLayout(grid)
        self.page.addLayout(self.footer)
    

        widget.setLayout(self.page)
        self.setCentralWidget(widget)
    
    def create_dialog_box(self,message):
            dlg = QMessageBox(self)
            dlg.setText(message)
            dlg.setIcon(QMessageBox.Information)
            dlg.exec()

    def generate_random_sudoku(self):
        print("clicked")
        self.sudoku = [
        [2, 5, 6, 4, 8, 0, 1, 7, 3],
        [3, 7, 4, 6, 1, 5, 9, 8, 2],
        [9, 8, 1, 7, 2, 3, 4, 5, 6],
        [5, 9, 3, 2, 7, 4, 8, 6, 1],
        [0, 1, 2, 8, 0, 6, 5, 4, 9],
        [4, 6, 8, 5, 9, 1, 3, 2, 7],
        [6, 3, 5, 1, 4, 7, 2, 0, 8],
        [1, 2, 7, 9, 5, 8, 6, 3, 4],
        [8, 4, 0, 3, 6, 2, 7, 1, 5]
                    ]  
        self.create_grid(None)

    @pyqtSlot()
    def solve(self):
        moves = solve_sudoku(self.sudoku)
        if moves == None:
            self.create_dialog_box("This have no Solutions")
            return
        elif len(moves) == 0:
            self.create_dialog_box("This have Already been solved you dumb")
            return
        for move in moves:
            self.create_grid([move[0],move[1],move[2]])
            self.sudoku[move[0]][move[1]] = move[2]

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


sudoku = [
    [2, 5, 6, 4, 8, 0, 1, 7, 3],
    [3, 7, 4, 6, 1, 5, 9, 8, 2],
    [9, 8, 1, 7, 2, 3, 4, 5, 6],
    [5, 9, 3, 2, 7, 4, 8, 6, 1],
    [0, 1, 2, 8, 0, 6, 5, 4, 9],
    [4, 6, 8, 5, 9, 1, 3, 2, 7],
    [6, 3, 5, 1, 4, 7, 2, 0, 8],
    [1, 2, 7, 9, 5, 8, 6, 3, 4],
    [8, 4, 0, 3, 6, 2, 7, 1, 5]
]


app = QApplication(sys.argv)
window = MainWindow(sudoku)
window.show()
app.exec()
app.quit()