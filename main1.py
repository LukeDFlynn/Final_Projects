from gui import *

def power(x, y):
    if y == 1:
        return x
    else:
        return x * power(x, y-1)

def main():
    app = QApplication([])
    window = gui()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
