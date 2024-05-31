

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image
from imgbeddings import imgbeddings
import psycopg2
import cv2
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,id):
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
        self.groupBox_2.setGeometry(QtCore.QRect(20, 270, 231, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_add = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_add.setGeometry(QtCore.QRect(10, 30, 81, 25))
        self.btn_add.setStyleSheet("background-color: rgb(38, 162, 105);")
        self.btn_add.setObjectName("btn_add")
        self.btn_edit = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_edit.setGeometry(QtCore.QRect(130, 30, 81, 25))
        self.btn_edit.setStyleSheet("background-color: rgb(246, 211, 45);")
        self.btn_edit.setObjectName("btn_edit")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(280, 70, 501, 471))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_face = QtWidgets.QLabel(self.groupBox_4)
        self.label_face.setGeometry(QtCore.QRect(10, 20, 481, 441))
        self.label_face.setObjectName("label_face")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 231, 181))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 21, 17))
        self.label_2.setObjectName("label_2")
        self.id = QtWidgets.QLineEdit(self.groupBox)
        self.id.setGeometry(QtCore.QRect(10, 60, 71, 25))
        self.id.setObjectName("id")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 111, 17))
        self.label_5.setObjectName("label_5")
        self.name = QtWidgets.QLineEdit(self.groupBox)
        self.name.setGeometry(QtCore.QRect(10, 130, 71, 25))
        self.name.setObjectName("name")
        MainWindow.setCentralWidget(self.centralwidget)

        self.btn_add.clicked.connect(self.add)
        self.btn_edit.clicked.connect(self.stop)
        self.id.setText(str(id))
        temp = 0
        for filename in os.listdir("stored-faces"):
            # Kiểm tra xem tên của tệp có bắt đầu bằng "2" không
            if filename.startswith(self.id.text()):
                temp += 1
        self.name.setText(str(temp))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def stop(self):
        self.a = 0

    def add(self):
        imgG = cv2.imread("temp/temp2.jpg",0)
        cv2.imwrite("stored-faces/" + self.id.text() + self.name.text() + ".jpg", imgG)

        # connecting to the database - replace the SERVICE URI with the service URI
        conn = psycopg2.connect("postgres://avnadmin:AVNS_C3g-_WIL48h5-ugIW0R@pg-1e534733-facemmm.d.aivencloud.com:13503/defaultdb?sslmode=require")
        img = Image.open("temp/temp2.jpg")
        # loading the `imgbeddings`
        ibed = imgbeddings()
        # calculating the embeddings
        embedding = ibed.to_embeddings(img)
        cur = conn.cursor()
        #cur.execute("DELETE FROM pictures")
        cur.execute("INSERT INTO pictures values (%s,%s)", 
                    (self.id.text() + self.name.text() + ".jpg", embedding[0].tolist()))
        print(self.id.text() + self.name.text() + ".jpg" + "Success")
        conn.commit()
        self.name.setText(str(int(self.name.text()) + 1))


    def cam(self):
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
            cv2.imwrite("temp/temp2.jpg", cropped_image)
            key = cv2.waitKey(10)
            if key == 27:
                break
        cam.release()
        cv2.destroyAllWindows() 


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Guess Picture"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Action"))
        self.btn_add.setText(_translate("MainWindow", "Take Picture"))
        self.btn_edit.setText(_translate("MainWindow", "Logout"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Face recoqnition"))
        self.label_face.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox.setTitle(_translate("MainWindow", "Guess Information"))
        self.label_2.setText(_translate("MainWindow", "ID"))
        self.label_5.setText(_translate("MainWindow", "Number Of Pictures"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.cam()
    sys.exit(app.exec_())
