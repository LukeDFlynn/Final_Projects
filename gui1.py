import main
from view import *
from PyQt5.QtWidgets import *

class gui(QMainWindow, Ui_MainWindow):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.setupUi(self)
        self.buttonCalc.clicked.connect(lambda: self.calculate())
        self.buttonClear.clicked.connect(lambda: self.clear())


    def power(self, x, y):
        if y == 0:
            return 1
        if y == 1:
            return x
        else:
            return x * self.power(x, y-1)

    def calculate(self):
        try:

            baseNum = int(self.lineNum.text())
            expNum = int(self.lineExp.text())
            ans = self.power(baseNum, expNum)
            if ans == 1:
                self.labelAns.setText(f"There is 1 cat ear.")
            else:
                self.labelAns.setText(f"There are {int(ans/2)} cats with {ans} ears.")

            if ans <= 32:
                if ans % 2 == 0:
                    self.labelCat.setText(int(ans/2) * "😺 ")
                else:
                    self.labelCat.setText(int(ans/2) * "😺 " + "Ear")
            else:
                self.labelAns.setText(f"Please do not make me\ncreate {ans} cat ears.")
        except:
            self.labelAns.setText("Please only enter integers.")

    def clear(self):
        self.lineNum.setText("")
        self.lineExp.setText("")
        self.labelCat.setText("")
        self.labelAns.setText("")




