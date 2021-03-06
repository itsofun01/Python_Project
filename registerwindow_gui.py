# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from my_service.alert import errorWarShow, sucessShow, errorCriShow
from my_service.check_register import checkRegis, insertRegister_to_Db, check_inputNormal


class RegisterUi(object):
    def setupRegisterUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Fname_field = QtWidgets.QLineEdit(self.centralwidget)
        self.Fname_field.setGeometry(QtCore.QRect(260, 160, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Fname_field.setFont(font)
        self.Fname_field.setObjectName("Fname_field")
        self.Lname_field = QtWidgets.QLineEdit(self.centralwidget)
        self.Lname_field.setGeometry(QtCore.QRect(530, 160, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Lname_field.setFont(font)
        self.Lname_field.setObjectName("Lname_field")
        self.Regis_Username_field = QtWidgets.QLineEdit(self.centralwidget)
        self.Regis_Username_field.setGeometry(QtCore.QRect(260, 290, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Regis_Username_field.setFont(font)
        self.Regis_Username_field.setObjectName("Regis_Username_field")
        self.Regis_Password_field = QtWidgets.QLineEdit(self.centralwidget)
        self.Regis_Password_field.setGeometry(QtCore.QRect(260, 350, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Regis_Password_field.setFont(font)
        self.Regis_Password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Regis_Password_field.setObjectName("Regis_Password_field")
        self.Regis_ConPassword_field = QtWidgets.QLineEdit(self.centralwidget)
        self.Regis_ConPassword_field.setGeometry(QtCore.QRect(260, 410, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Regis_ConPassword_field.setFont(font)
        self.Regis_ConPassword_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Regis_ConPassword_field.setObjectName("Regis_ConPassword_field")
        self.Date_field = QtWidgets.QDateEdit(self.centralwidget)
        self.Date_field.setGeometry(QtCore.QRect(260, 220, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Date_field.setFont(font)
        self.Date_field.setObjectName("Date_field")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 170, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 170, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 230, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 300, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 360, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 420, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.Regis_Register_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Regis_Register_btn.setGeometry(QtCore.QRect(260, 460, 75, 23))
        self.Regis_Register_btn.setObjectName("Regis_Register_btn")
        self.Regis_Reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Regis_Reset_btn.setGeometry(QtCore.QRect(350, 460, 75, 23))
        self.Regis_Reset_btn.setObjectName("Regis_Reset_btn")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 70, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Regis_Register_btn.clicked.connect(self.regisprocess)
        self.Regis_Reset_btn.clicked.connect(self.reset_form_btn)
        self.thiswindow = MainWindow
        #self.prewindow = prewindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Date_field.setDisplayFormat(_translate("MainWindow", "dd-MMM-yyyy"))
        self.label.setText(_translate("MainWindow", "ชื่อ"))
        self.label_2.setText(_translate("MainWindow", "นามสกุล"))
        self.label_3.setText(_translate("MainWindow", "ว/ด/ป เกิด"))
        self.label_4.setText(_translate("MainWindow", "Username"))
        self.label_5.setText(_translate("MainWindow", "Password"))
        self.label_6.setText(_translate("MainWindow", "Confirm password"))
        self.Regis_Register_btn.setText(_translate("MainWindow", "Register"))
        self.Regis_Reset_btn.setText(_translate("MainWindow", "Reset"))
        self.label_7.setText(_translate("MainWindow", "โปรแกรมบันทึกรายรับรายจ่าย"))

    def reset_form_btn(self):
        self.Fname_field.clear()
        self.Lname_field.clear()
        self.Regis_Username_field.clear()
        self.Regis_Password_field.clear()
        self.Regis_ConPassword_field.clear()
        self.Date_field.date()

    def linktologin(self):
        self.thiswindow.hide()
        #self.prewindow.show()

    def regisprocess(self):
        Fname = self.Fname_field.text()
        Lname = self.Lname_field.text()
        username = self.Regis_Username_field.text()
        password = self.Regis_Password_field.text()
        confirm_password = self.Regis_ConPassword_field.text()
        birthday = self.Date_field.text()
        list_check = [Fname,Lname,username,password,confirm_password,birthday] #List for send to check null value function

        if check_inputNormal(list_check):
            if(password == confirm_password):
                if checkRegis(username):
                    errorWarShow(self,'Error!!!', 'Duplicate Data\nPlease input other username to register')
                    self.Regis_Username_field.clear()
                    self.Regis_Password_field.clear()
                    self.Regis_ConPassword_field.clear()
                else:
                    datatoinput = {"username": username,
                                   "password": password,
                                   "Fname": Fname,
                                   "Lname": Lname,
                                   "birthday": birthday,
                                   }
                    if insertRegister_to_Db(datatoinput):
                        sucessShow(self,'Sucessful!!!', 'User has been created')
                        self.Fname_field.clear()
                        self.Lname_field.clear()
                        self.Regis_Username_field.clear()
                        self.Regis_Password_field.clear()
                        self.Regis_ConPassword_field.clear()
                        self.Date_field.clear()
                    else:
                        errorCriShow(self,'Error!!!', 'User Create Fail')
                        self.Fname_field.clear()
                        self.Lname_field.clear()
                        self.Regis_Username_field.clear()
                        self.Regis_Password_field.clear()
                        self.Regis_ConPassword_field.clear()
                        self.Date_field.clear()
            else:
                errorWarShow(self,'Error!!!', 'Password not same Re-Password')
                self.Regis_Password_field.clear()
                self.Regis_ConPassword_field.clear()
        else:
            errorWarShow(self,'Error!!!', 'Please fill all information')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisFormuser = QtWidgets.QMainWindow()
    ui = RegisterUi()
    ui.setupRegisterUi(RegisFormuser)
    RegisFormuser.show()
    sys.exit(app.exec_())
