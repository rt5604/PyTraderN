# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Project\stock\PyTrader\pytrader.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1675, 1000)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Project\\stock\\PyTrader\\pytrader.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(356, 426))
        self.groupBox.setMaximumSize(QtCore.QSize(356, 426))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setContentsMargins(-1, 18, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.accountComboBox = QtWidgets.QComboBox(self.groupBox)
        self.accountComboBox.setObjectName("accountComboBox")
        self.horizontalLayout.addWidget(self.accountComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.orderTypeComboBox = QtWidgets.QComboBox(self.groupBox)
        self.orderTypeComboBox.setObjectName("orderTypeComboBox")
        self.orderTypeComboBox.addItem("")
        self.orderTypeComboBox.addItem("")
        self.orderTypeComboBox.addItem("")
        self.orderTypeComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.orderTypeComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.codeLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.codeLineEdit.setObjectName("codeLineEdit")
        self.verticalLayout.addWidget(self.codeLineEdit)
        self.codeNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.codeNameLineEdit.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.codeNameLineEdit.setObjectName("codeNameLineEdit")
        self.verticalLayout.addWidget(self.codeNameLineEdit)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.hogaTypeComboBox = QtWidgets.QComboBox(self.groupBox)
        self.hogaTypeComboBox.setObjectName("hogaTypeComboBox")
        self.hogaTypeComboBox.addItem("")
        self.hogaTypeComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.hogaTypeComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.qtySpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.qtySpinBox.setMaximum(1000000)
        self.qtySpinBox.setObjectName("qtySpinBox")
        self.horizontalLayout_4.addWidget(self.qtySpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.priceSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.priceSpinBox.setMaximum(1000000)
        self.priceSpinBox.setSingleStep(50)
        self.priceSpinBox.setObjectName("priceSpinBox")
        self.horizontalLayout_5.addWidget(self.priceSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.orderBtn = QtWidgets.QPushButton(self.groupBox)
        self.orderBtn.setObjectName("orderBtn")
        self.verticalLayout_2.addWidget(self.orderBtn)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setMaximumSize(QtCore.QSize(356, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.logTextEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.logTextEdit.setObjectName("logTextEdit")
        self.horizontalLayout_7.addWidget(self.logTextEdit)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.horizontalLayout_9.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(1289, 700))
        self.groupBox_2.setMaximumSize(QtCore.QSize(1289, 876))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.accountEvaluationTable = QtWidgets.QTableWidget(self.groupBox_2)
        self.accountEvaluationTable.setMinimumSize(QtCore.QSize(1251, 111))
        self.accountEvaluationTable.setMaximumSize(QtCore.QSize(1251, 111))
        self.accountEvaluationTable.setRowCount(1)
        self.accountEvaluationTable.setObjectName("accountEvaluationTable")
        self.accountEvaluationTable.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.accountEvaluationTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.accountEvaluationTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.accountEvaluationTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.accountEvaluationTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.accountEvaluationTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.accountEvaluationTable.setHorizontalHeaderItem(5, item)
        self.verticalLayout_3.addWidget(self.accountEvaluationTable)
        self.stocksTable = QtWidgets.QTableWidget(self.groupBox_2)
        self.stocksTable.setMinimumSize(QtCore.QSize(1251, 500))
        self.stocksTable.setMaximumSize(QtCore.QSize(1251, 600))
        self.stocksTable.setObjectName("stocksTable")
        self.stocksTable.setColumnCount(6)
        self.stocksTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.stocksTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stocksTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stocksTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.stocksTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.stocksTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.stocksTable.setHorizontalHeaderItem(5, item)
        self.verticalLayout_3.addWidget(self.stocksTable)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(920, -1, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.realtimeCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.realtimeCheckBox.setEnabled(True)
        self.realtimeCheckBox.setMaximumSize(QtCore.QSize(170, 28))
        self.realtimeCheckBox.setObjectName("realtimeCheckBox")
        self.horizontalLayout_8.addWidget(self.realtimeCheckBox)
        self.inquiryBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.inquiryBtn.setMaximumSize(QtCore.QSize(150, 46))
        self.inquiryBtn.setObjectName("inquiryBtn")
        self.horizontalLayout_8.addWidget(self.inquiryBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.automatedStocksTable = QtWidgets.QTableWidget(self.groupBox_3)
        self.automatedStocksTable.setObjectName("automatedStocksTable")
        self.automatedStocksTable.setColumnCount(6)
        self.automatedStocksTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.automatedStocksTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.automatedStocksTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.automatedStocksTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.automatedStocksTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.automatedStocksTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.automatedStocksTable.setHorizontalHeaderItem(5, item)
        self.verticalLayout_5.addWidget(self.automatedStocksTable)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1675, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label.setBuddy(self.accountComboBox)
        self.label_2.setBuddy(self.orderTypeComboBox)
        self.label_3.setBuddy(self.codeLineEdit)
        self.label_4.setBuddy(self.hogaTypeComboBox)
        self.label_5.setBuddy(self.qtySpinBox)
        self.label_6.setBuddy(self.priceSpinBox)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.accountComboBox, self.orderTypeComboBox)
        MainWindow.setTabOrder(self.orderTypeComboBox, self.codeLineEdit)
        MainWindow.setTabOrder(self.codeLineEdit, self.hogaTypeComboBox)
        MainWindow.setTabOrder(self.hogaTypeComboBox, self.qtySpinBox)
        MainWindow.setTabOrder(self.qtySpinBox, self.priceSpinBox)
        MainWindow.setTabOrder(self.priceSpinBox, self.orderBtn)
        MainWindow.setTabOrder(self.orderBtn, self.codeNameLineEdit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyTrader v0.4"))
        self.groupBox.setTitle(_translate("MainWindow", "수동주문"))
        self.label.setText(_translate("MainWindow", "계좌"))
        self.label_2.setText(_translate("MainWindow", "주문"))
        self.orderTypeComboBox.setItemText(0, _translate("MainWindow", "신규매수"))
        self.orderTypeComboBox.setItemText(1, _translate("MainWindow", "신규매도"))
        self.orderTypeComboBox.setItemText(2, _translate("MainWindow", "매수취소"))
        self.orderTypeComboBox.setItemText(3, _translate("MainWindow", "매도취소"))
        self.label_3.setText(_translate("MainWindow", "종목"))
        self.label_4.setText(_translate("MainWindow", "종류"))
        self.hogaTypeComboBox.setItemText(0, _translate("MainWindow", "지정가"))
        self.hogaTypeComboBox.setItemText(1, _translate("MainWindow", "시장가"))
        self.label_5.setText(_translate("MainWindow", "수량"))
        self.label_6.setText(_translate("MainWindow", "가격"))
        self.orderBtn.setText(_translate("MainWindow", "현금주문"))
        self.groupBox_4.setTitle(_translate("MainWindow", "로그"))
        self.groupBox_2.setTitle(_translate("MainWindow", "잔고 및 보유종목 현황"))
        item = self.accountEvaluationTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "예수금 (d+2)"))
        item = self.accountEvaluationTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "총매입"))
        item = self.accountEvaluationTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "총평가"))
        item = self.accountEvaluationTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "총손익"))
        item = self.accountEvaluationTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "총수익률 (%)"))
        item = self.accountEvaluationTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "추정자산"))
        item = self.stocksTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "종목명"))
        item = self.stocksTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "보유량"))
        item = self.stocksTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "매입가"))
        item = self.stocksTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "현재가"))
        item = self.stocksTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "평가손익"))
        item = self.stocksTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "수익률 (%)"))
        self.realtimeCheckBox.setText(_translate("MainWindow", "실시간 조회"))
        self.inquiryBtn.setText(_translate("MainWindow", "조회"))
        self.groupBox_3.setTitle(_translate("MainWindow", "자동 선정 종목 리스트"))
        item = self.automatedStocksTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "주문유형"))
        item = self.automatedStocksTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "종목명"))
        item = self.automatedStocksTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "호가구분"))
        item = self.automatedStocksTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "수량"))
        item = self.automatedStocksTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "가격"))
        item = self.automatedStocksTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "상태"))