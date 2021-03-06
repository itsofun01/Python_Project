# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editlimitwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import datetime
from my_service.alert import sucessShow, errorWarShow, errorCriShow
from my_service.check_limitValue import checkAddlimitValue, query_limitValue
from my_service.check_register import check_inputNormal


class editLimit_Ui(object):
    def editLimit_setupUi(self, MainWindow, user_data, back):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 120, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.currentLimit_label = QtWidgets.QLabel(self.centralwidget)
        self.currentLimit_label.setGeometry(QtCore.QRect(270, 150, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.currentLimit_label.setFont(font)
        self.currentLimit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.currentLimit_label.setObjectName("currentLimit_label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(450, 150, 51, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 280, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(230, 240, 341, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.limit_value_field = QtWidgets.QLineEdit(self.centralwidget)
        self.limit_value_field.setGeometry(QtCore.QRect(260, 330, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.limit_value_field.setFont(font)
        self.limit_value_field.setObjectName("limit_value_field")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 310, 51, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.to_summary_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_summary_btn.setGeometry(QtCore.QRect(660, 510, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.to_summary_btn.setFont(font)
        self.to_summary_btn.setObjectName("to_summary_btn")
        self.saveLimit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.saveLimit_btn.setGeometry(QtCore.QRect(330, 400, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.saveLimit_btn.setFont(font)
        self.saveLimit_btn.setObjectName("saveLimit_btn")
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
        self.thiswindow = MainWindow
        self.back = back

        self.user_data = user_data

        # btn area
        self.saveLimit_btn.clicked.connect(self.linktosavelimit)
        self.to_summary_btn.clicked.connect(self.back_MainWindow)

        query_result = query_limitValue(user_data)
        print("query ==> {}".format(query_result))
        if query_result[0] == "PASS":
            self.currentLimit_label.setText(str(query_result[1]))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "แก้ไขวงเงิน"))
        self.label_5.setText(_translate("MainWindow", "วงเงินปัจจุบัน"))
        self.currentLimit_label.setText(_translate("MainWindow", "N/A"))
        self.label_3.setText(_translate("MainWindow", "฿"))
        self.label_6.setText(_translate("MainWindow", "แก้ไขวงเงิน"))
        self.label_4.setText(_translate("MainWindow", "฿"))
        self.to_summary_btn.setText(_translate("MainWindow", "กลับไปหน้าวงเงิน"))
        self.saveLimit_btn.setText(_translate("MainWindow", "ยืนยันแก้ไขวงเงิน"))

    def linktosavelimit(self):
        print("Save limit value ==> start...")
        limit_value = self.limit_value_field.text()
        list_check = [limit_value]
        print(list_check)
        if check_inputNormal(list_check):
            limit_value_float = float(limit_value)
            today = datetime.date.today().strftime('%d-%b-%Y')

            datatoinput = {'limit_value': limit_value_float,
                           'date_create': today
                           }
            if checkAddlimitValue(datatoinput, self.user_data):
                sucessShow(self,'add limit value success','add limit value success!')
                query_result = query_limitValue(self.user_data)
                if query_result[0] == "PASS":
                    self.currentLimit_label.setText(str(query_result[1]))
                else:
                    errorCriShow(self, 'Error!!!', 'Cannot add data')
                    self.limit_value_field.clear()
        else:
            print("")
            errorWarShow(self,'Warning!!!', 'Please fill Limit value')
            self.limit_value_field.clear()

    def back_MainWindow(self):
        self.back.show()
        self.thiswindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = editLimit_Ui()
    ui.editLimit_setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
