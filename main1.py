from gui1 import *

def power(x, y):
    if y == 1:
        return x
    else:
        return x * power(x, y-1)
    '''
    This function takes in two parameters and raises the first value to the second value's power.
    
    param x: The first parameter.
    param y: The second parameter.
    return: x raised to the y power.
    '''

def main():
    app = QApplication([])
    window = gui()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
