# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generated/ui/counter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(10, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.count_num = QtWidgets.QLineEdit(self.centralwidget)
        self.count_num.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.count_num.setFont(font)
        self.count_num.setAlignment(QtCore.Qt.AlignCenter)
        self.count_num.setReadOnly(True)
        self.count_num.setObjectName("count_num")
        self.horizontalLayout.addWidget(self.count_num)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.count_btn = QtWidgets.QPushButton(self.centralwidget)
        self.count_btn.setMinimumSize(QtCore.QSize(0, 100))
        self.count_btn.setObjectName("count_btn")
        self.horizontalLayout_2.addWidget(self.count_btn)
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setMinimumSize(QtCore.QSize(0, 100))
        self.reset_btn.setObjectName("reset_btn")
        self.horizontalLayout_2.addWidget(self.reset_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "计数器"))
        self.label.setText(_translate("MainWindow", "当前计数"))
        self.count_num.setText(_translate("MainWindow", "0"))
        self.count_btn.setText(_translate("MainWindow", "计数 + 1 (Space)"))
        self.reset_btn.setText(_translate("MainWindow", "重置(&C)"))