from PyQt5 import QtWidgets
import ElectricBill, WaterBill, FaceRecognition
import Home, Login, Room, GuessPicture, Guess
import sys
import sqlite3

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def electricBill():
        global ui
        ui = ElectricBill.Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.SearchButton_2.clicked.connect(home)
        MainWindow.show()

def waterBill():
        global ui
        ui = WaterBill.Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.BackButton.clicked.connect(home)
        MainWindow.show()

def faceRecognition():
       global ui
       ui = FaceRecognition.Ui_MainWindow()
       ui.setupUi(MainWindow)
       ui.pushButton.clicked.connect(home)
       ui.cam()
       MainWindow.show()

def guess():
       global ui
       ui = Guess.Ui_MainWindow()
       ui.setupUi(MainWindow)
       ui.btn_back.clicked.connect(home)
       MainWindow.show()

def guessPicture(id):
       global ui
       ui = GuessPicture.Ui_MainWindow()
       ui.setupUi(MainWindow,id)
       ui.btn_edit.clicked.connect(login)
       MainWindow.show()
       ui.cam()

def login():
       global ui
       ui = Login.Ui_MainWindow()
       ui.setupUi(MainWindow)
       ui.pushButton.clicked.connect(lambda: loginControll(
              str(ui.username.text()),str(ui.password.text())))
       MainWindow.show()
       
def loginControll(tk,mk):
       sqliteConnection = sqlite3.connect('QLNhaTro.db')
       cursor = sqliteConnection.cursor()
       cursor.execute("SELECT * FROM Account WHERE taikhoan = ? AND pass = ?", (tk, mk))
       row = cursor.fetchone()
       if row and row[0] == 0:
              home()
       elif row and row[0] != 0: 
              guessPicture(row[0])
       else:
              print("Wrong UserName Or Password")
       sqliteConnection.close()

def room():
       global ui
       ui = Room.Ui_MainWindow()
       ui.setupUi(MainWindow)
       ui.btnThoat.clicked.connect(home)
       MainWindow.show()

def home():
       global ui
       ui = Home.Ui_MainWindow()
       ui.setupUi(MainWindow)
       ui.btn_Cashier.clicked.connect(electricBill)
       ui.btn_Employ.clicked.connect(guess)
       ui.btn_Consum.clicked.connect(faceRecognition)
       ui.btn_Static.clicked.connect(waterBill)
       ui.btn_Inven.clicked.connect(room)
       ui.btn_Logout.clicked.connect(login)
       MainWindow.show()

login()
sys.exit(app.exec())
