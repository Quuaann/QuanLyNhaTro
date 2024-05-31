

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from imgbeddings import imgbeddings
from PIL import Image
import numpy as np
import psycopg2
import cv2
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 0, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 480, 231, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_add = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_add.setGeometry(QtCore.QRect(10, 30, 81, 25))
        self.btn_add.setStyleSheet("background-color: rgb(38, 162, 105);")
        self.btn_add.setObjectName("btn_add")
        self.btn_edit = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_edit.setGeometry(QtCore.QRect(130, 30, 81, 25))
        self.btn_edit.setStyleSheet("background-color: rgb(246, 211, 45);")
        self.btn_edit.setObjectName("btn_edit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.pushButton.setStyleSheet("border-image: url(image-Ui/arrow.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(280, 70, 501, 471))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_face = QtWidgets.QLabel(self.groupBox_4)
        self.label_face.setGeometry(QtCore.QRect(10, 20, 481, 441))
        self.label_face.setObjectName("label_face")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 231, 391))
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
        self.room = QtWidgets.QLineEdit(self.groupBox)
        self.room.setGeometry(QtCore.QRect(10, 200, 111, 25))
        self.room.setObjectName("room")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.btn_add.clicked.connect(self.recognition)
        self.btn_edit.clicked.connect(self.cam)
        self.pushButton.clicked.connect(self.stop)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def cam(self):
        self.id.setText("")
        self.name.setText("")
        self.room.setText("")
        self.phone.setText("")
        self.CMND.setText("")

        # loading the haar case algorithm file into alg variable
        alg = "haarcascade_frontalface_default.xml"
        # passing the algorithm to OpenCV
        haar_cascade = cv2.CascadeClassifier(alg)
        # capturing the video feed from the camera
        cam = cv2.VideoCapture(0)
        self.a = 1
        while self.a == 1:
            _, img = cam.read()
            cropped_image = img
            text = "Face not detected"
            # convert each frame from BGR to Grayscale
            grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # detect faces using Haar Cascade 
            face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)
            # draw a rectangle around the face and update the text to Face Detected
            for (x, y, w, h) in face:
                    text = "Face Detected"
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cropped_image = grayImg[y : y + h, x : x + w]

            image = cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 
                                (255, 0, 0), 2, cv2.LINE_AA)
            h, w, c = image.shape
            qImg = QImage(image.data, w, h, w * c, QImage.Format_BGR888)
            pixmap = QPixmap.fromImage(qImg)
            self.label_face.setPixmap(pixmap)
            cv2.imwrite("temp/temp.jpg", cropped_image)
            key = cv2.waitKey(10)
            if key == 27:
                break
        cam.release()
        cv2.destroyAllWindows() 

    def stop(self):
        self.a = 0

    def recognition(self):
        self.stop()
        conn = psycopg2.connect("postgres://avnadmin:AVNS_C3g-_WIL48h5-ugIW0R@pg-1e534733-facemmm.d.aivencloud.com:13503/defaultdb?sslmode=require")
        img2 = Image.open("temp/temp.jpg")
        # loading the `imgbeddings`
        ibed = imgbeddings()
        # calculating the embeddings
        embedding = ibed.to_embeddings(img2)

        cur = conn.cursor()
        string_representation = "["+ ",".join(str(x) for x in embedding[0].tolist()) +"]"
        cur.execute("SELECT * FROM pictures ORDER BY embedding <-> %s LIMIT 1;", 
                    (string_representation,))
        rows = cur.fetchall()
        for row in rows:
            print(row[0])
            s = row[0] 

        img3 = Image.open("stored-faces/" + row[0])
        embedding2 = ibed.to_embeddings(img3)
        euclidean_distance = np.linalg.norm(embedding - embedding2)
        print(euclidean_distance)

        sqliteConnection = sqlite3.connect('QLNhaTro.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("SELECT * FROM cus WHERE ID = ?", (s[0],))      
        print("Success: Guess " + s[0])      
        rowsql = cursor.fetchone()
        if euclidean_distance > 10:
            self.id.setText("Unknown")
            self.name.setText("Unknown")
            self.room.setText("Unknown")
            self.phone.setText("Unknown")
            self.CMND.setText("Unknown")
        elif rowsql is not None:
            self.id.setText(str(rowsql[0]))
            self.name.setText(rowsql[1])
            self.room.setText(str(rowsql[2]))
            self.phone.setText(rowsql[3])
            self.CMND.setText(rowsql[4])
        sqliteConnection.close()
        cur.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Face Recoqnition"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Action"))
        self.btn_add.setText(_translate("MainWindow", "Recognite"))
        self.btn_edit.setText(_translate("MainWindow", "Reset"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Face recoqnition"))
        self.label_face.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox.setTitle(_translate("MainWindow", "Guess Information"))
        self.label_2.setText(_translate("MainWindow", "ID"))
        self.label_3.setText(_translate("MainWindow", "Room"))
        self.label_4.setText(_translate("MainWindow", "CMND"))
        self.label_5.setText(_translate("MainWindow", "Name"))
        self.label_6.setText(_translate("MainWindow", "Phone"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.a = 1
    MainWindow.show()
    ui.cam()
    sys.exit(app.exec_())
