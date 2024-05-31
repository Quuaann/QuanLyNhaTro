

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableGuess = QtWidgets.QTableWidget(self.centralwidget)
        self.tableGuess.setGeometry(QtCore.QRect(270, 170, 511, 311))
        self.tableGuess.setObjectName("tableGuess")
        self.tableGuess.setColumnCount(5)
        self.tableGuess.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableGuess.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableGuess.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableGuess.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableGuess.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableGuess.setHorizontalHeaderItem(4, item)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 90, 221, 391))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 21, 17))
        self.label_2.setObjectName("label_2")
        self.id = QtWidgets.QLineEdit(self.groupBox)
        self.id.setGeometry(QtCore.QRect(10, 60, 71, 25))
        self.id.setObjectName("id")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 31, 17))
        self.label_3.setObjectName("label_3")
        self.Phong = QtWidgets.QLineEdit(self.groupBox)
        self.Phong.setGeometry(QtCore.QRect(10, 200, 111, 25))
        self.Phong.setObjectName("Phong")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 320, 31, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 67, 17))
        self.label_5.setObjectName("label_5")
        self.name = QtWidgets.QLineEdit(self.groupBox)
        self.name.setGeometry(QtCore.QRect(10, 130, 201, 25))
        self.name.setObjectName("name")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 67, 17))
        self.label_6.setObjectName("label_6")
        self.phone = QtWidgets.QLineEdit(self.groupBox)
        self.phone.setGeometry(QtCore.QRect(10, 270, 201, 25))
        self.phone.setObjectName("phone")
        self.CMND = QtWidgets.QLineEdit(self.groupBox)
        self.CMND.setGeometry(QtCore.QRect(10, 340, 201, 25))
        self.CMND.setObjectName("CMND")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 500, 251, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_add = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_add.setGeometry(QtCore.QRect(10, 30, 71, 25))
        self.btn_add.setStyleSheet("background-color: rgb(51, 209, 122);")
        self.btn_add.setObjectName("btn_add")
        self.btn_edit = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_edit.setGeometry(QtCore.QRect(90, 30, 71, 25))
        self.btn_edit.setStyleSheet("background-color: rgb(249, 240, 107);")
        self.btn_edit.setObjectName("btn_edit")
        self.btn_delete = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_delete.setGeometry(QtCore.QRect(170, 30, 71, 25))
        self.btn_delete.setStyleSheet("background-color: rgb(237, 51, 59);")
        self.btn_delete.setObjectName("btn_delete")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(270, 90, 511, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox_type = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_type.setGeometry(QtCore.QRect(10, 30, 101, 25))
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.searchGuess = QtWidgets.QLineEdit(self.groupBox_3)
        self.searchGuess.setGeometry(QtCore.QRect(130, 30, 280, 25))
        self.searchGuess.setObjectName("searchGuess")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(694, 119, 73, 25))
        self.btn_search.setStyleSheet("background-color: rgb(51, 209, 122);")
        self.btn_search.setText("Search")
        self.btn_search.setObjectName("btn_search")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.btn_back.setStyleSheet("border-image: url(image-Ui/arrow.png);")
        self.btn_back.setText("")
        self.btn_back.setObjectName("btn_back")
        MainWindow.setCentralWidget(self.centralwidget)

        self.tableGuess.cellClicked.connect(self.cell_clicked)  # Kết nối sự kiện cellClicked
        self.btn_add.clicked.connect(self.add)
        self.btn_edit.clicked.connect(self.edit)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_search.clicked.connect(self.search)
        self.load()    

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def cell_clicked(self):
            self.id.setText(self.tableGuess.item(self.tableGuess.currentRow(), 0).text())
            self.name.setText(self.tableGuess.item(self.tableGuess.currentRow(), 1).text())
            self.Phong.setText(self.tableGuess.item(self.tableGuess.currentRow(), 2).text())
            self.phone.setText(self.tableGuess.item(self.tableGuess.currentRow(), 3).text())
            self.CMND.setText(self.tableGuess.item(self.tableGuess.currentRow(), 4).text())

    def add(self):
        sqliteConnection = sqlite3.connect('QLNhaTro.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("INSERT INTO cus (ID, name, id_phong, SDT, CMND) VALUES (?, ?, ?, ?, ?)", 
                       (int(self.id.text()), self.name.text(), 
                        int(self.Phong.text()), self.phone.text(), self.CMND.text()))
        sqliteConnection.commit()
        sqliteConnection.close()
        self.load()

    def edit(self):
        if self.id.text() != '':
            row = int(self.id.text())
            sqliteConnection = sqlite3.connect('QLNhaTro.db')
            cursor = sqliteConnection.cursor()
            cursor.execute("UPDATE cus SET ID = ?, name = ?, id_phong = ?, SDT = ?, CMND = ? WHERE ID = ?", 
                        (int(self.id.text()), self.name.text(), 
                         int(self.Phong.text()), self.phone.text(), self.CMND.text(), row))
            sqliteConnection.commit()
            sqliteConnection.close()
            self.load()
            print("Success")
        else: 
            print("Chọn hàng cần sửa")

    def delete(self):
        if self.id.text()!= '':
            row = int(self.id.text())
            sqliteConnection = sqlite3.connect('QLNhaTro.db')
            cursor = sqliteConnection.cursor()
            cursor.execute("DELETE FROM cus WHERE ID =?", (row,))
            sqliteConnection.commit()
            sqliteConnection.close()
            self.load()
            print("Success")
        else: 
            print("Chọn hàng cần xóa")

    def search(self):
        if self.searchGuess.text()!= '':
            type = self.comboBox_type.currentText()
            keyword = self.searchGuess.text()
            sqliteConnection = sqlite3.connect('QLNhaTro.db')
            cursor = sqliteConnection.cursor()
            if type == "Room":
                type = "id_phong"
            if type == 'Phone':
                type = "SDT"
            cursor.execute("SELECT * FROM cus WHERE " + type + " LIKE ?", ('%' + keyword + '%',))
            result = cursor.fetchall()
            self.tableGuess.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableGuess.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableGuess.setItem(row_number, column_number, 
                                            QtWidgets.QTableWidgetItem(str(data)))
        else:   self.load()


    def load(self):
        sqliteConnection = sqlite3.connect('QLNhaTro.db')
        cursor = sqliteConnection.cursor()
        query = 'select* from cus'
        result = cursor.execute(query)
        self.tableGuess.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableGuess.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableGuess.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Guest management"))
        item = self.tableGuess.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableGuess.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.tableGuess.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ROOM"))
        item = self.tableGuess.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PHONE"))
        item = self.tableGuess.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "CMND"))
        self.groupBox.setTitle(_translate("MainWindow", "Guess Information"))
        self.label_2.setText(_translate("MainWindow", "ID"))
        self.label_3.setText(_translate("MainWindow", "Room"))
        self.label_4.setText(_translate("MainWindow", "CMND"))
        self.label_5.setText(_translate("MainWindow", "Name"))
        self.label_6.setText(_translate("MainWindow", "Phone"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Action"))
        self.btn_add.setText(_translate("MainWindow", "Add"))
        self.btn_edit.setText(_translate("MainWindow", "Edit"))
        self.btn_delete.setText(_translate("MainWindow", "Delete"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Search"))
        self.comboBox_type.setItemText(0, _translate("MainWindow", "ID"))
        self.comboBox_type.setItemText(1, _translate("MainWindow", "Name"))
        self.comboBox_type.setItemText(2, _translate("MainWindow", "Room"))
        self.comboBox_type.setItemText(3, _translate("MainWindow", "Phone"))
        self.comboBox_type.setItemText(4, _translate("MainWindow", "CMND"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
