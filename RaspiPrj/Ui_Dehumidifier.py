# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/TestCode/Dehumidifier-main-thread/Dehumidifier.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(629, 478)
        Dialog.setSizeGripEnabled(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(495, 440, 91, 30))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 621, 161))
        self.groupBox.setObjectName("groupBox")
        self.BtnSearch = QtWidgets.QPushButton(self.groupBox)
        self.BtnSearch.setEnabled(True)
        self.BtnSearch.setGeometry(QtCore.QRect(10, 50, 99, 30))
        self.BtnSearch.setObjectName("BtnSearch")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 100, 401, 32))
        self.comboBox.setObjectName("comboBox")
        self.LabelStatus = QtWidgets.QLabel(self.groupBox)
        self.LabelStatus.setGeometry(QtCore.QRect(130, 60, 451, 22))
        self.LabelStatus.setObjectName("LabelStatus")
        self.BtnConnect = QtWidgets.QPushButton(self.groupBox)
        self.BtnConnect.setGeometry(QtCore.QRect(440, 100, 71, 30))
        self.BtnConnect.setObjectName("BtnConnect")
        self.BtnDisconnect = QtWidgets.QPushButton(self.groupBox)
        self.BtnDisconnect.setGeometry(QtCore.QRect(530, 100, 71, 30))
        self.BtnDisconnect.setObjectName("BtnDisconnect")
        self.groupOP = QtWidgets.QGroupBox(Dialog)
        self.groupOP.setGeometry(QtCore.QRect(10, 200, 621, 231))
        self.groupOP.setObjectName("groupOP")
        self.BtnPwr = QtWidgets.QPushButton(self.groupOP)
        self.BtnPwr.setGeometry(QtCore.QRect(480, 130, 99, 30))
        self.BtnPwr.setObjectName("BtnPwr")
        self.LedM1 = QtWidgets.QLabel(self.groupOP)
        self.LedM1.setGeometry(QtCore.QRect(310, 80, 31, 22))
        self.LedM1.setObjectName("LedM1")
        self.label_7 = QtWidgets.QLabel(self.groupOP)
        self.label_7.setGeometry(QtCore.QRect(140, 40, 41, 22))
        self.label_7.setObjectName("label_7")
        self.LedPwr = QtWidgets.QLabel(self.groupOP)
        self.LedPwr.setGeometry(QtCore.QRect(510, 80, 31, 22))
        self.LedPwr.setObjectName("LedPwr")
        self.BtnMode = QtWidgets.QPushButton(self.groupOP)
        self.BtnMode.setGeometry(QtCore.QRect(310, 130, 99, 30))
        self.BtnMode.setObjectName("BtnMode")
        self.label_9 = QtWidgets.QLabel(self.groupOP)
        self.label_9.setGeometry(QtCore.QRect(30, 200, 41, 22))
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(self.groupOP)
        self.label.setGeometry(QtCore.QRect(300, 40, 41, 22))
        self.label.setObjectName("label")
        self.BtnHumidity = QtWidgets.QPushButton(self.groupOP)
        self.BtnHumidity.setGeometry(QtCore.QRect(60, 130, 99, 30))
        self.BtnHumidity.setObjectName("BtnHumidity")
        self.LedFull = QtWidgets.QLabel(self.groupOP)
        self.LedFull.setGeometry(QtCore.QRect(80, 200, 31, 22))
        self.LedFull.setObjectName("LedFull")
        self.label_6 = QtWidgets.QLabel(self.groupOP)
        self.label_6.setGeometry(QtCore.QRect(80, 40, 41, 22))
        self.label_6.setObjectName("label_6")
        self.LedH1 = QtWidgets.QLabel(self.groupOP)
        self.LedH1.setGeometry(QtCore.QRect(30, 80, 31, 22))
        self.LedH1.setObjectName("LedH1")
        self.label_5 = QtWidgets.QLabel(self.groupOP)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 41, 22))
        self.label_5.setObjectName("label_5")
        self.LedH2 = QtWidgets.QLabel(self.groupOP)
        self.LedH2.setGeometry(QtCore.QRect(80, 80, 31, 22))
        self.LedH2.setObjectName("LedH2")
        self.label_2 = QtWidgets.QLabel(self.groupOP)
        self.label_2.setGeometry(QtCore.QRect(350, 40, 41, 22))
        self.label_2.setObjectName("label_2")
        self.LedH4 = QtWidgets.QLabel(self.groupOP)
        self.LedH4.setGeometry(QtCore.QRect(190, 80, 31, 22))
        self.LedH4.setObjectName("LedH4")
        self.LedH3 = QtWidgets.QLabel(self.groupOP)
        self.LedH3.setGeometry(QtCore.QRect(140, 80, 31, 22))
        self.LedH3.setObjectName("LedH3")
        self.label_3 = QtWidgets.QLabel(self.groupOP)
        self.label_3.setGeometry(QtCore.QRect(400, 40, 41, 22))
        self.label_3.setObjectName("label_3")
        self.LedM2 = QtWidgets.QLabel(self.groupOP)
        self.LedM2.setGeometry(QtCore.QRect(360, 80, 31, 22))
        self.LedM2.setObjectName("LedM2")
        self.label_8 = QtWidgets.QLabel(self.groupOP)
        self.label_8.setGeometry(QtCore.QRect(190, 40, 41, 22))
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.groupOP)
        self.label_4.setGeometry(QtCore.QRect(500, 40, 41, 22))
        self.label_4.setObjectName("label_4")
        self.LedM3 = QtWidgets.QLabel(self.groupOP)
        self.LedM3.setGeometry(QtCore.QRect(410, 80, 31, 22))
        self.LedM3.setObjectName("LedM3")

        self.retranslateUi(Dialog)
        self.buttonBox.clicked['QAbstractButton*'].connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "抽湿机"))
        self.groupBox.setTitle(_translate("Dialog", "设备信息"))
        self.BtnSearch.setText(_translate("Dialog", "搜索"))
        self.LabelStatus.setText(_translate("Dialog", "TextLabel"))
        self.BtnConnect.setText(_translate("Dialog", "连接"))
        self.BtnDisconnect.setText(_translate("Dialog", "断开"))
        self.groupOP.setTitle(_translate("Dialog", "操作控制"))
        self.BtnPwr.setText(_translate("Dialog", "电源"))
        self.LedM1.setText(_translate("Dialog", "H1"))
        self.label_7.setText(_translate("Dialog", "60%"))
        self.LedPwr.setText(_translate("Dialog", "H1"))
        self.BtnMode.setText(_translate("Dialog", "模式"))
        self.label_9.setText(_translate("Dialog", "水满"))
        self.label.setText(_translate("Dialog", "除湿"))
        self.BtnHumidity.setText(_translate("Dialog", "湿度"))
        self.LedFull.setText(_translate("Dialog", "H1"))
        self.label_6.setText(_translate("Dialog", "50%"))
        self.LedH1.setText(_translate("Dialog", "H1"))
        self.label_5.setText(_translate("Dialog", "连续"))
        self.LedH2.setText(_translate("Dialog", "H1"))
        self.label_2.setText(_translate("Dialog", "干衣"))
        self.LedH4.setText(_translate("Dialog", "H1"))
        self.LedH3.setText(_translate("Dialog", "H1"))
        self.label_3.setText(_translate("Dialog", "静音"))
        self.LedM2.setText(_translate("Dialog", "H1"))
        self.label_8.setText(_translate("Dialog", "70%"))
        self.label_4.setText(_translate("Dialog", "电源"))
        self.LedM3.setText(_translate("Dialog", "H1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
