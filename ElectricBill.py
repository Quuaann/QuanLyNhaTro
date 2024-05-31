

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QMessageBox
from PyQt5.QtGui import QIcon
import ConnectDB,ElectricBillDB

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 600)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 10, 331, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(10, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AddButton.setFont(font)
        self.AddButton.setStyleSheet("background:rgb(1, 255, 22);\n"
"textsize: 14;\n"
"color: rgb(255, 255, 255);\n"
"")

        self.EditButton = QtWidgets.QPushButton(self.centralwidget)
        self.EditButton.setGeometry(QtCore.QRect(94, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.EditButton.setFont(font)
        self.EditButton.setStyleSheet("background: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.EditButton.setObjectName("EditButton")
        self.RemoveButton = QtWidgets.QPushButton(self.centralwidget)
        self.RemoveButton.setGeometry(QtCore.QRect(174, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RemoveButton.setFont(font)
        self.RemoveButton.setStyleSheet("background: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.RemoveButton.setObjectName("RemoveButton")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 90, 21, 16))
        self.label_2.setObjectName("label_2")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(860, 80, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SearchButton.setFont(font)
        self.SearchButton.setStyleSheet("background: rgb(170, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.SearchButton.setObjectName("SearchButton")
        self.SearchText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.SearchText.setGeometry(QtCore.QRect(710, 80, 141, 31))
        self.SearchText.setObjectName("SearchText")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 130, 920, 410))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        rows = ConnectDB.getAllElectri()
        self.showTable(rows)
        #Goi ham dua du lieu len table
        item = QtWidgets.QTableWidgetItem()

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()

        self.SearchButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton_2.setGeometry(QtCore.QRect(20, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SearchButton_2.setFont(font)
        self.SearchButton_2.setStyleSheet("border-image: url(image-Ui/arrow.png);")
        self.SearchButton_2.setText("")
        self.SearchButton_2.setFlat(True)
        self.SearchButton_2.setObjectName("SearchButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")

        self.AddButton.setObjectName("AddButton")

        self.btnRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.btnRefresh.setGeometry(QtCore.QRect(650,350 , 93, 29))

        self.btnRefresh.setObjectName("btnRefresh")

        self.txtID = QtWidgets.QTextEdit(self.centralwidget)
        self.txtID.setGeometry(QtCore.QRect(650, 150, 71, 31))
        self.txtID.setObjectName("txtID")
        self.txtRoom = QtWidgets.QTextEdit(self.centralwidget)
        self.txtRoom.setGeometry(QtCore.QRect(650, 200, 191, 31))
        self.txtRoom.setObjectName("txtRoom")
        self.txtNumber = QtWidgets.QTextEdit(self.centralwidget)
        self.txtNumber.setGeometry(QtCore.QRect(650, 250, 191, 31))
        self.txtNumber.setObjectName("txtNumber")
        self.txtSum = QtWidgets.QTextEdit(self.centralwidget)
        self.txtSum.setGeometry(QtCore.QRect(650, 300, 191, 31))
        self.txtSum.setObjectName("txtSum")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 150, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 200, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 250, 71, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 300, 71, 31))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tableWidget.itemClicked.connect(self.getData)
        self.EditButton.clicked.connect(self.update)
        self.SearchButton.clicked.connect(self.find)
        self.AddButton.clicked.connect(self.add)
        self.btnRefresh.clicked.connect(self.refresh)
        self.RemoveButton.clicked.connect(self.delete)

    def add(self):
        id = self.txtID.toPlainText()
        name = self.txtRoom.toPlainText()
        nu = self.txtNumber.toPlainText()
        sum = int(nu)*4000
        self.txtSum.setPlainText(str(sum))
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Bạn có muốn cập nhật")
        msg.setWindowTitle("Quyết định")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msg.exec()
        if returnValue == QMessageBox.Ok:
            ElectricBillDB.addElecBill(int(id),int(name),int(nu),int(sum))
            rows = ConnectDB.getAllElectri()
            self.showTable(rows)


    def refresh(self) :
        rows = ConnectDB.getAllElectri()
        self.showTable(rows)

    def getData(self) :
        id = self.tableWidget.currentRow()
        self.txtID.setPlainText(self.tableWidget.item(id,0).text())
        self.txtRoom.setPlainText(self.tableWidget.item(id,1).text())
        self.txtNumber.setPlainText(self.tableWidget.item(id,2).text())
        self.txtSum.setPlainText(self.tableWidget.item(id,3).text())

    def delete(self):
        id = self.txtID.toPlainText()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Bạn có muốn xóa hóa đơn mã "+id)
        msg.setWindowTitle("Quyết định")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msg.exec()
        if returnValue == QMessageBox.Ok:
            ElectricBillDB.delete(int(id))
            rows = ConnectDB.getAllElectri()
            self.showTable(rows)


    def find(self):
        id = self.txtID.toPlainText()
        rows = ElectricBillDB.findByid(int(id))

        if(len(rows)==0):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Không tìn thấy phòng có mã phòng là :"+self.txtID.toPlainText())
            msg.setWindowTitle("Error")
            msg.exec()

        self.showTable(rows)

    def update(self):
        id = self.txtID.toPlainText()
        name = self.txtRoom.toPlainText()
        nu = self.txtNumber.toPlainText()
        sum = int(nu)*4000
        self.txtSum.setPlainText(str(sum))
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Bạn có muốn cập nhật")
        msg.setWindowTitle("Quyết định")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msg.exec()
        if returnValue == QMessageBox.Ok:
            ElectricBillDB.updateElecBill(int(id),int(name),int(nu),int(sum))
            rows = ConnectDB.getAllElectri()
            self.showTable(rows)

    def showTable(self,rows):
        self.tableWidget.setRowCount(len(rows))
        for i in range(0,len(rows)) :
            item = QtWidgets.QTableWidgetItem(str(rows[i][0]))
            self.tableWidget.setItem(i,0,item)
            item = QtWidgets.QTableWidgetItem(str(rows[i][1]))
            self.tableWidget.setItem(i,1,item)
            item = QtWidgets.QTableWidgetItem(str(rows[i][2]))
            self.tableWidget.setItem(i,2,item)
            item = QtWidgets.QTableWidgetItem(str(rows[i][3]))
            self.tableWidget.setItem(i,3,item)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Electric bill"))
        self.AddButton.setText(_translate("MainWindow", "Add"))

        self.btnRefresh.setText(_translate("MainWindow", "Refresh"))

        self.EditButton.setText(_translate("MainWindow", "Edit"))
        self.RemoveButton.setText(_translate("MainWindow", "Remove"))
        self.label_2.setText(_translate("MainWindow", "To"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow","ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Id Phong"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Number"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tong"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))

        self.label.setText(_translate("MainWindow", "Mã hoa don :"))
        self.label_2.setText(_translate("MainWindow", "Tên phòng :"))
        self.label_3.setText(_translate("MainWindow", "So dien :"))
        self.label_4.setText(_translate("MainWindow", "Tien dien :"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
