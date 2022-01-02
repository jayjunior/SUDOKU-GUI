import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel,QMessageBox
from PyQt5.QtCore import Qt as al , pyqtSlot
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

        # Shoot out to @https://stackoverflow.com/users/5237560/alain-t for this awesome generator !!

        base  = 3
        side  = base*base
        
        # pattern for a baseline valid solution
        def pattern(r,c): return (base*(r%base)+r//base+c)%side
        
        # randomize rows, columns and numbers (of valid base pattern)
        from random import sample
        def shuffle(s): return sample(s,len(s)) 

        rBase = range(base) 
        rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
        cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
        nums  = shuffle(range(1,base*base+1))
        
        # produce board using randomized baseline pattern
        self.sudoku = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
        squares = side*side
        empties = squares * 3//4
        for p in sample(range(squares),empties):
            self.sudoku[p//side][p%side] = 0

        self.create_grid(None)


    @pyqtSlot()
    def solve(self):
        moves = solve_sudoku(self.sudoku)
        if len(moves) == 0:
            self.create_dialog_box("This have Already been solved you dumb")
            return
        for move in moves:
            self.create_grid([move[0],move[1],move[2]])
            self.sudoku[move[0]][move[1]] = move[2]


initial_sudoku = [
    [0,0,2,0,3,0,0,0,8],
    [0,0,0,0,0,8,0,0,0],
    [0,3,1,0,2,0,0,0,0],
    [0,6,0,0,5,0,2,7,0],
    [0,1,0,0,0,0,0,5,0],
    [2,0,4,0,6,0,0,3,1],
    [0,0,0,0,8,0,6,0,5],
    [0,0,0,0,0,0,0,1,3],
    [0,0,5,3,1,0,4,0,0]
]


app = QApplication(sys.argv)
window = MainWindow(initial_sudoku)
window.show()
app.exec()
app.quit()