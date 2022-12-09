from PyQt5.QtWidgets import *
from view import *
import main

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.setupUi(self)
        self.buttonExcel.clicked.connect(lambda: self.excel)
        self.buttonCSV.clicked.connect(lambda:self.csv)
        self.radMovie.setChecked(True)
        self.radMovie.clicked.connect(lambda: self.on_radMovie_clicked(self))
        self.radBook.clicked.connect(lambda: self.on_radBook_clicked())

    def on_radMovie_clicked(self, scrapeMovie):
        main.scrapeMovie()

    def on_radBook_clicked(self):
        main.scrapeBook()

    def excel(self):
        if self.radMovie.isClicked():
            self.movie_list.to_excel("List of top 1000 Movies by IMDb.xlsx")
            print("Movies exported to Excel!")
        if self.radBook.isClicked():
            self.books.to_excel("Books.xlsx")
            print("Books exported to Excel!")
    def csv(self):
        if self.radMovie.isClicked():
            print("Movies exported to CSV!")
            self.movie_list.to_csv("List of top 1000 Movies by IMDb.csv")

        if self.radBook.isClicked():
            print("Books exported to CSV!")
            self.books.to_excel("Books.xlsx")


