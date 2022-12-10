import main1
from view1 import *
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

        '''
        This function takes in two parameters and raises the first to the second's power
        
        Param x: First parameter.
        Param y: Second parameter.
        Result: Raises x to the power of y, but also accounts for if y is 0.
        '''

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
            self.labelAns.setText("Please only enter positive integers.")

        '''
        This function is called whenever the calculate button is pressed. It takes the answer given by the power
        function and creates that many ears. Since each cat has 2 ears, it divides this number by 2 to print that
        number of cats. If the answer given is odd, it prints "Ear" because half an ear is still missing but
        if another cat was printed too many ears would occur.
        
        Result: The same number of ears as the answer given from the power function.
        '''

    def clear(self):
        self.lineNum.setText("")
        self.lineExp.setText("")
        self.labelCat.setText("")
        self.labelAns.setText("")

        '''
        This function clears all text shown.
        '''




