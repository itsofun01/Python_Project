# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyzewindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from my_service.check_analyze import query_analyze, findDataByDay


class Analyze_UI(object):
    def Analyze_setupUI(self, MainWindow, user_data, back):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 501, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-30, 90, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.startDate_field = QtWidgets.QDateEdit(self.centralwidget)
        self.startDate_field.setGeometry(QtCore.QRect(100, 80, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startDate_field.setFont(font)
        self.startDate_field.setObjectName("startDate_field")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 90, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.endDate_field = QtWidgets.QDateEdit(self.centralwidget)
        self.endDate_field.setGeometry(QtCore.QRect(340, 80, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.endDate_field.setFont(font)
        self.endDate_field.setObjectName("endDate_field")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 140, 711, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 380, 711, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 400, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(540, 160, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(540, 400, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.sum_pay_label = QtWidgets.QLabel(self.centralwidget)
        self.sum_pay_label.setGeometry(QtCore.QRect(530, 220, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.sum_pay_label.setFont(font)
        self.sum_pay_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sum_pay_label.setObjectName("sum_pay_label")
        self.normal_spend_label = QtWidgets.QLabel(self.centralwidget)
        self.normal_spend_label.setGeometry(QtCore.QRect(20, 210, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.normal_spend_label.setFont(font)
        self.normal_spend_label.setAlignment(QtCore.Qt.AlignCenter)
        self.normal_spend_label.setObjectName("normal_spend_label")
        self.normal_spend_pt_label = QtWidgets.QLabel(self.centralwidget)
        self.normal_spend_pt_label.setGeometry(QtCore.QRect(30, 250, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.normal_spend_pt_label.setFont(font)
        self.normal_spend_pt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.normal_spend_pt_label.setObjectName("normal_spend_pt_label")
        self.to_summary_btn = QtWidgets.QPushButton(self.centralwidget)
        self.to_summary_btn.setGeometry(QtCore.QRect(660, 510, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.to_summary_btn.setFont(font)
        self.to_summary_btn.setObjectName("to_summary_btn")
        self.all_btn = QtWidgets.QPushButton(self.centralwidget)
        self.all_btn.setGeometry(QtCore.QRect(650, 80, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.all_btn.setFont(font)
        self.all_btn.setObjectName("all_btn")
        self.find_btn = QtWidgets.QPushButton(self.centralwidget)
        self.find_btn.setGeometry(QtCore.QRect(540, 80, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.find_btn.setFont(font)
        self.find_btn.setObjectName("find_btn")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(20, 180, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.online_spend_pt_label = QtWidgets.QLabel(self.centralwidget)
        self.online_spend_pt_label.setGeometry(QtCore.QRect(180, 250, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.online_spend_pt_label.setFont(font)
        self.online_spend_pt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.online_spend_pt_label.setObjectName("online_spend_pt_label")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(170, 180, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.online_spend_label = QtWidgets.QLabel(self.centralwidget)
        self.online_spend_label.setGeometry(QtCore.QRect(170, 210, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.online_spend_label.setFont(font)
        self.online_spend_label.setAlignment(QtCore.Qt.AlignCenter)
        self.online_spend_label.setObjectName("online_spend_label")
        self.essential_spend_pt_label = QtWidgets.QLabel(self.centralwidget)
        self.essential_spend_pt_label.setGeometry(QtCore.QRect(350, 250, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.essential_spend_pt_label.setFont(font)
        self.essential_spend_pt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.essential_spend_pt_label.setObjectName("essential_spend_pt_label")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(320, 180, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.essential_spend_label = QtWidgets.QLabel(self.centralwidget)
        self.essential_spend_label.setGeometry(QtCore.QRect(340, 210, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.essential_spend_label.setFont(font)
        self.essential_spend_label.setAlignment(QtCore.Qt.AlignCenter)
        self.essential_spend_label.setObjectName("essential_spend_label")
        self.transport_spend_pt_label = QtWidgets.QLabel(self.centralwidget)
        self.transport_spend_pt_label.setGeometry(QtCore.QRect(30, 350, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.transport_spend_pt_label.setFont(font)
        self.transport_spend_pt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.transport_spend_pt_label.setObjectName("transport_spend_pt_label")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(20, 280, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.transport_spend_label = QtWidgets.QLabel(self.centralwidget)
        self.transport_spend_label.setGeometry(QtCore.QRect(20, 310, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.transport_spend_label.setFont(font)
        self.transport_spend_label.setAlignment(QtCore.Qt.AlignCenter)
        self.transport_spend_label.setObjectName("transport_spend_label")
        self.food_spend_pt_label = QtWidgets.QLabel(self.centralwidget)
        self.food_spend_pt_label.setGeometry(QtCore.QRect(180, 350, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.food_spend_pt_label.setFont(font)
        self.food_spend_pt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.food_spend_pt_label.setObjectName("food_spend_pt_label")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(170, 280, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.food_spend_label = QtWidgets.QLabel(self.centralwidget)
        self.food_spend_label.setGeometry(QtCore.QRect(170, 310, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.food_spend_label.setFont(font)
        self.food_spend_label.setAlignment(QtCore.Qt.AlignCenter)
        self.food_spend_label.setObjectName("food_spend_label")
        self.normal_income_pt_label = QtWidgets.QLabel(self.centralwidget)
        self.normal_income_pt_label.setGeometry(QtCore.QRect(30, 490, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.normal_income_pt_label.setFont(font)
        self.normal_income_pt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.normal_income_pt_label.setObjectName("normal_income_pt_label")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(20, 420, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.normal_income_label = QtWidgets.QLabel(self.centralwidget)
        self.normal_income_label.setGeometry(QtCore.QRect(20, 450, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.normal_income_label.setFont(font)
        self.normal_income_label.setAlignment(QtCore.Qt.AlignCenter)
        self.normal_income_label.setObjectName("normal_income_label")
        self.salary_income_pt_label = QtWidgets.QLabel(self.centralwidget)
        self.salary_income_pt_label.setGeometry(QtCore.QRect(180, 490, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.salary_income_pt_label.setFont(font)
        self.salary_income_pt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.salary_income_pt_label.setObjectName("salary_income_pt_label")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(170, 420, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.salary_income_label = QtWidgets.QLabel(self.centralwidget)
        self.salary_income_label.setGeometry(QtCore.QRect(170, 450, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.salary_income_label.setFont(font)
        self.salary_income_label.setAlignment(QtCore.Qt.AlignCenter)
        self.salary_income_label.setObjectName("salary_income_label")
        self.income_pay_label = QtWidgets.QLabel(self.centralwidget)
        self.income_pay_label.setGeometry(QtCore.QRect(530, 420, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.income_pay_label.setFont(font)
        self.income_pay_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.income_pay_label.setObjectName("income_pay_label")
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

        self.endDate_field.setDateTime(QtCore.QDateTime.currentDateTime())

        self.user_data = user_data

        # query
        user_query_data = query_analyze(user_data)

        # btn area
        self.find_btn.clicked.connect(self.findByDate)
        self.all_btn.clicked.connect(self.findAll)
        self.to_summary_btn.clicked.connect(self.back_MainWindow)

        self.income_pay_label.setText("{} ฿".format(str(user_query_data['income_sum'])))
        self.sum_pay_label.setText("{} ฿".format(str(user_query_data['spend_sum'])))
        self.normal_income_label.setText("{} ฿".format(user_query_data['normal_income']))
        self.salary_income_label.setText("{} ฿".format(user_query_data['salary_income']))
        self.normal_spend_label.setText("{} ฿".format(user_query_data['normal_spend']))
        self.food_spend_label.setText("{} ฿".format(user_query_data['food_spend']))
        self.transport_spend_label.setText("{} ฿".format(user_query_data['transport_spend']))
        self.online_spend_label.setText("{} ฿".format(user_query_data['online_spend']))
        self.essential_spend_label.setText("{} ฿".format(user_query_data['essential_spend']))

        self.normal_income_pt_label.setText("{} %".format(user_query_data['normal_income_pt']))
        self.salary_income_pt_label.setText("{} %".format(user_query_data['salary_income_pt']))
        self.normal_spend_pt_label.setText("{} %".format(user_query_data['normal_spend_pt']))
        self.food_spend_pt_label.setText("{} %".format(user_query_data['food_spend_pt']))
        self.transport_spend_pt_label.setText("{} %".format(user_query_data['transport_spend_pt']))
        self.online_spend_pt_label.setText("{} %".format(user_query_data['online_spend_pt']))
        self.essential_spend_pt_label.setText("{} %".format(user_query_data['essential_spend_pt']))

        if 50 < user_query_data['normal_spend_pt'] < 70:
            self.normal_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['normal_spend_pt'] >= 70:
            self.normal_spend_pt_label.setStyleSheet('color: red')
        else:
            self.normal_spend_pt_label.setStyleSheet('color: green')

        if 50 < user_query_data['food_spend_pt'] < 70:
            self.food_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['food_spend_pt'] >= 70:
            self.food_spend_pt_label.setStyleSheet('color: red')
        else:
            self.food_spend_pt_label.setStyleSheet('color: green')

        if 50 < user_query_data['transport_spend_pt'] < 70:
            self.transport_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['transport_spend_pt'] >= 70:
            self.transport_spend_pt_label.setStyleSheet('color: red')
        else:
            self.transport_spend_pt_label.setStyleSheet('color: green')

        if 50 < user_query_data['online_spend_pt'] < 70:
            self.online_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['online_spend_pt'] >= 70:
            self.online_spend_pt_label.setStyleSheet('color: red')
        else:
            self.online_spend_pt_label.setStyleSheet('color: green')

        if 50 < user_query_data['essential_spend_pt'] < 70:
            self.essential_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['essential_spend_pt'] >= 70:
            self.essential_spend_pt_label.setStyleSheet('color: red')
        else:
            self.essential_spend_pt_label.setStyleSheet('color: green')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "วิเคราะห์การใช้จ่าย"))
        self.label_2.setText(_translate("MainWindow", "วันที่ :"))
        self.startDate_field.setDisplayFormat(_translate("MainWindow", "dd-MMM-yyyy"))
        self.label_3.setText(_translate("MainWindow", "ถึง"))
        self.endDate_field.setDisplayFormat(_translate("MainWindow", "dd-MMM-yyyy"))
        self.label_4.setText(_translate("MainWindow", "รายจ่าย"))
        self.label_5.setText(_translate("MainWindow", "รายรับ"))
        self.label_6.setText(_translate("MainWindow", "รวม"))
        self.label_7.setText(_translate("MainWindow", "รวม"))
        self.sum_pay_label.setText(_translate("MainWindow", "N/A"))
        self.normal_spend_label.setText(_translate("MainWindow", "N/A ฿"))
        self.normal_spend_pt_label.setText(_translate("MainWindow", "N/A %"))
        self.to_summary_btn.setText(_translate("MainWindow", "กลับไปหน้าหลัก"))
        self.all_btn.setText(_translate("MainWindow", "ทั้งหมด"))
        self.find_btn.setText(_translate("MainWindow", "ค้นหา"))
        self.label_19.setText(_translate("MainWindow", "ค่าใช้จ่ายทั่วไป"))
        self.online_spend_pt_label.setText(_translate("MainWindow", "N/A %"))
        self.label_21.setText(_translate("MainWindow", "ค่าใช้จ่ายออนไลน์"))
        self.online_spend_label.setText(_translate("MainWindow", "N/A ฿"))
        self.essential_spend_pt_label.setText(_translate("MainWindow", "N/A %"))
        self.label_24.setText(_translate("MainWindow", "ค่าใช้จ่ายของใช้จำเป็น"))
        self.essential_spend_label.setText(_translate("MainWindow", "N/A ฿"))
        self.transport_spend_pt_label.setText(_translate("MainWindow", "N/A %"))
        self.label_27.setText(_translate("MainWindow", "ค่าเดินทาง"))
        self.transport_spend_label.setText(_translate("MainWindow", "N/A ฿"))
        self.food_spend_pt_label.setText(_translate("MainWindow", "N/A %"))
        self.label_30.setText(_translate("MainWindow", "ค่าอาหาร"))
        self.food_spend_label.setText(_translate("MainWindow", "N/A ฿"))
        self.normal_income_pt_label.setText(_translate("MainWindow", "N/A %"))
        self.label_33.setText(_translate("MainWindow", "ทั่วไป"))
        self.normal_income_label.setText(_translate("MainWindow", "N/A ฿"))
        self.salary_income_pt_label.setText(_translate("MainWindow", "N/A %"))
        self.label_36.setText(_translate("MainWindow", "เงินเดือน"))
        self.salary_income_label.setText(_translate("MainWindow", "N/A ฿"))
        self.income_pay_label.setText(_translate("MainWindow", "N/A"))

    def findByDate(self):
        start_date = self.startDate_field.text()
        end_date = self.endDate_field.text()

        user_query_data = findDataByDay(self.user_data,start_date,end_date)
        self.income_pay_label.setText("{} ฿".format(str(user_query_data['income_sum'])))
        self.sum_pay_label.setText("{} ฿".format(str(user_query_data['spend_sum'])))
        self.normal_income_label.setText("{} ฿".format(user_query_data['normal_income']))
        self.salary_income_label.setText("{} ฿".format(user_query_data['salary_income']))
        self.normal_spend_label.setText("{} ฿".format(user_query_data['normal_spend']))
        self.food_spend_label.setText("{} ฿".format(user_query_data['food_spend']))
        self.transport_spend_label.setText("{} ฿".format(user_query_data['transport_spend']))
        self.online_spend_label.setText("{} ฿".format(user_query_data['online_spend']))
        self.essential_spend_label.setText("{} ฿".format(user_query_data['essential_spend']))

        self.normal_income_pt_label.setText("{} %".format(user_query_data['normal_income_pt']))
        self.salary_income_pt_label.setText("{} %".format(user_query_data['salary_income_pt']))
        self.normal_spend_pt_label.setText("{} %".format(user_query_data['normal_spend_pt']))
        self.food_spend_pt_label.setText("{} %".format(user_query_data['food_spend_pt']))
        self.transport_spend_pt_label.setText("{} %".format(user_query_data['transport_spend_pt']))
        self.online_spend_pt_label.setText("{} %".format(user_query_data['online_spend_pt']))
        self.essential_spend_pt_label.setText("{} %".format(user_query_data['essential_spend_pt']))

        if 50 < user_query_data['normal_spend_pt'] < 70:
            self.normal_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['normal_spend_pt'] >= 70:
            self.normal_spend_pt_label.setStyleSheet('color: red')
        else:
            self.normal_spend_pt_label.setStyleSheet('color: green')

        if 50 < user_query_data['food_spend_pt'] < 70:
            self.food_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['food_spend_pt'] >= 70:
            self.food_spend_pt_label.setStyleSheet('color: red')
        else:
            self.food_spend_pt_label.setStyleSheet('color: green')

        if 50 < user_query_data['transport_spend_pt'] < 70:
            self.transport_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['transport_spend_pt'] >= 70:
            self.transport_spend_pt_label.setStyleSheet('color: red')
        else:
            self.transport_spend_pt_label.setStyleSheet('color: green')

        if 50 < user_query_data['online_spend_pt'] < 70:
            self.online_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['online_spend_pt'] >= 70:
            self.online_spend_pt_label.setStyleSheet('color: red')
        else:
            self.online_spend_pt_label.setStyleSheet('color: green')

        if 50 < user_query_data['essential_spend_pt'] < 70:
            self.essential_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['essential_spend_pt'] >= 70:
            self.essential_spend_pt_label.setStyleSheet('color: red')
        else:
            self.essential_spend_pt_label.setStyleSheet('color: green')

    def findAll(self):
        self.startDate_field.setDate(QtCore.QDate(2020, 1, 1))
        self.endDate_field.setDateTime(QtCore.QDateTime.currentDateTime())

        user_query_data = query_analyze(self.user_data)
        self.income_pay_label.setText("{} ฿".format(str(user_query_data['income_sum'])))
        self.sum_pay_label.setText("{} ฿".format(str(user_query_data['spend_sum'])))
        self.normal_income_label.setText("{} ฿".format(user_query_data['normal_income']))
        self.salary_income_label.setText("{} ฿".format(user_query_data['salary_income']))
        self.normal_spend_label.setText("{} ฿".format(user_query_data['normal_spend']))
        self.food_spend_label.setText("{} ฿".format(user_query_data['food_spend']))
        self.transport_spend_label.setText("{} ฿".format(user_query_data['transport_spend']))
        self.online_spend_label.setText("{} ฿".format(user_query_data['online_spend']))
        self.essential_spend_label.setText("{} ฿".format(user_query_data['essential_spend']))

        self.normal_income_pt_label.setText("{:.2f} %".format(user_query_data['normal_income_pt']))
        self.salary_income_pt_label.setText("{:.2f} %".format(user_query_data['salary_income_pt']))
        self.normal_spend_pt_label.setText("{:.2f} %".format(user_query_data['normal_spend_pt']))
        self.food_spend_pt_label.setText("{:.2f} %".format(user_query_data['food_spend_pt']))
        self.transport_spend_pt_label.setText("{:.2f} %".format(user_query_data['transport_spend_pt']))
        self.online_spend_pt_label.setText("{:.2f} %".format(user_query_data['online_spend_pt']))
        self.essential_spend_pt_label.setText("{:.2f} %".format(user_query_data['essential_spend_pt']))

        if 50 < user_query_data['normal_spend_pt'] < 70:
            self.normal_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['normal_spend_pt'] >= 70:
            self.normal_spend_pt_label.setStyleSheet('color: red')
        else:
            self.normal_spend_pt_label.setStyleSheet('color: green')

        if 50 < user_query_data['food_spend_pt'] < 70:
            self.food_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['food_spend_pt'] >= 70:
            self.food_spend_pt_label.setStyleSheet('color: red')
        else:
            self.food_spend_pt_label.setStyleSheet('color: green')

        if 50 < user_query_data['transport_spend_pt'] < 70:
            self.transport_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['transport_spend_pt'] >= 70:
            self.transport_spend_pt_label.setStyleSheet('color: red')
        else:
            self.transport_spend_pt_label.setStyleSheet('color: green')

        if 50 < user_query_data['online_spend_pt'] < 70:
            self.online_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['online_spend_pt'] >= 70:
            self.online_spend_pt_label.setStyleSheet('color: red')
        else:
            self.online_spend_pt_label.setStyleSheet('color: green')

        if 50 < user_query_data['essential_spend_pt'] < 70:
            self.essential_spend_pt_label.setStyleSheet('color: orange')
        elif user_query_data['essential_spend_pt'] >= 70:
            self.essential_spend_pt_label.setStyleSheet('color: red')
        else:
            self.essential_spend_pt_label.setStyleSheet('color: green')

    def back_MainWindow(self):
        self.back.show()
        self.thiswindow.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Analyze_UI()
    ui.Analyze_setupUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
