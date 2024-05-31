

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QMessageBox
from PyQt5.QtGui import QIcon
import ConnectDB
import Home

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 474)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 100, 411, 171))
        self.tableWidget.setMaximumSize(QtCore.QSize(801, 271))
        self.tableWidget.setObjectName("tableWidget")

        #Lấy dữ liệu 
        rows = ConnectDB.getAll()
        self.tableWidget.setColumnCount(3)
        #self.tableWidget.setRowCount(len(rows))
        self.showTable(rows)#Goi ham dua du lieu len table
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
        self.btnLoc = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoc.setGeometry(QtCore.QRect(30, 310, 93, 29))
        self.btnLoc.setObjectName("btnLoc")
        self.cbbPhong = QtWidgets.QComboBox(self.centralwidget)
        self.cbbPhong.setGeometry(QtCore.QRect(570, 200, 91, 24))
        self.cbbPhong.setObjectName("cbbPhong")
        self.cbbPhong.addItem("")
        self.cbbPhong.addItem("")
        self.txtID = QtWidgets.QTextEdit(self.centralwidget)
        self.txtID.setGeometry(QtCore.QRect(570, 90, 71, 31))
        self.txtID.setObjectName("txtID")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 100, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 160, 81, 20))
        self.label_2.setObjectName("label_2")
        self.txtName = QtWidgets.QTextEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(570, 150, 191, 31))
        self.txtName.setObjectName("txtName")
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(640, 250, 93, 29))
        self.btnUpdate.setObjectName("btnUpdate")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 30, 301, 41))
        self.btnRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.btnRefresh.setGeometry(QtCore.QRect(200, 310, 93, 29))
        self.btnRefresh.setObjectName("btnRefresh")
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(470, 250, 93, 29))
        self.btnSearch.setObjectName("btnSearch")

        self.btnThoat = QtWidgets.QPushButton(self.centralwidget)
        self.btnThoat.setGeometry(QtCore.QRect(10, 10, 93, 29))
        self.btnThoat.setObjectName("btnThoat")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.btnUpdate.clicked.connect(self.update)
        self.btnSearch.clicked.connect(self.find)
        self.btnLoc.clicked.connect(self.findStatus)
        self.tableWidget.itemClicked.connect(self.getData)
        self.btnRefresh.clicked.connect(self.refresh)

    def refresh(self) :
        rows = ConnectDB.getAll()
        self.showTable(rows)

    def getData(self) :
        id = self.tableWidget.currentRow()
        self.txtID.setPlainText(self.tableWidget.item(id,0).text())
        self.txtName.setPlainText(self.tableWidget.item(id,1).text())
        str = self.tableWidget.item(id,2).text()

        if(str=="Chưa thuê") :
            self.cbbPhong.setItemText(0,"Chưa thuê")
            self.cbbPhong.setItemText(1,"Đã thuê")
        else :
            self.cbbPhong.setItemText(1,"Chưa thuê")
            self.cbbPhong.setItemText(0,"Đã thuê")

    def findStatus(self):
        status = self.cbbPhong.currentText()
        rows = ConnectDB.findAllStatus(status)
        self.showTable(rows)

    def find(self):
        id = self.txtID.toPlainText()
        rows = ConnectDB.findByid(int(id))

        if(len(rows)==0):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Không tìn thấy phòng có mã phòng là :"+self.txtID.toPlainText())
            msg.setWindowTitle("Error")
            msg.exec()

        self.showTable(rows)

    def update(self):
        id = self.txtID.toPlainText()
        name = self.txtName.toPlainText()
        status = self.cbbPhong.currentText()
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Bạn có muốn cập nhật")
        msg.setWindowTitle("Quyết định")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msg.exec()
        if returnValue == QMessageBox.Ok:
            ConnectDB.updateRoom(int(id),name,status)
            rows = ConnectDB.getAll()
            self.showTable(rows)
    
    def showTable(self,rows):
        self.tableWidget.setRowCount(len(rows))
        for i in range(0,len(rows)) :
            item = QtWidgets.QTableWidgetItem(str(rows[i][0]))
            self.tableWidget.setItem(i,0,item)
            item = QtWidgets.QTableWidgetItem(rows[i][1])
            self.tableWidget.setItem(i,1,item)
            item = QtWidgets.QTableWidgetItem(rows[i][2])
            self.tableWidget.setItem(i,2,item)

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã Phòng"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên Phòng"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Trạng thái"))
        self.btnLoc.setText(_translate("MainWindow", "Lọc"))
        self.btnRefresh.setText(_translate("MainWindow", "Refresh"))
        self.cbbPhong.setItemText(0, _translate("MainWindow", "Đã thuê"))
        self.cbbPhong.setItemText(1, _translate("MainWindow", "Chưa thuê"))
        self.label.setText(_translate("MainWindow", "Mã phòng :"))
        self.label_2.setText(_translate("MainWindow", "Tên phòng :"))
        self.btnThoat.setText(_translate("MainWindow", "Thoat"))
        self.btnUpdate.setText(_translate("MainWindow", "Thay đổi"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body ><p><span style=\" font-size:16pt;\">QUẢN LÝ PHÒNG TRỌ</span></p></body></html>"))
        self.btnSearch.setText(_translate("MainWindow", "Tìm kiếm"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
