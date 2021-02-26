import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QDir)
from PyQt5.QtWidgets import (QTableWidgetItem, QFileDialog)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 698)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 290, 671, 240))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_excitation = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_excitation.setObjectName("checkBox_excitation")
        self.gridLayout.addWidget(self.checkBox_excitation, 4, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.checkBox_field = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_field.setObjectName("checkBox_field")
        self.gridLayout.addWidget(self.checkBox_field, 2, 3, 1, 1)
        self.checkBox_ch4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_ch4.setObjectName("checkBox_ch4")
        self.gridLayout.addWidget(self.checkBox_ch4, 3, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.checkBox_RES = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_RES.setObjectName("checkBox_RES")
        self.gridLayout.addWidget(self.checkBox_RES, 1, 3, 1, 1)
        self.checkBox_time = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_time.setObjectName("checkBox_time")
        self.gridLayout.addWidget(self.checkBox_time, 3, 3, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.checkBox_temp = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_temp.setObjectName("checkBox_temp")
        self.gridLayout.addWidget(self.checkBox_temp, 0, 3, 1, 1)
        self.checkBox_ch1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_ch1.setObjectName("checkBox_ch1")
        self.gridLayout.addWidget(self.checkBox_ch1, 0, 0, 1, 1)
        self.checkBox_ch2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_ch2.setObjectName("checkBox_ch2")
        self.gridLayout.addWidget(self.checkBox_ch2, 1, 0, 1, 1)
        self.checkBox_ch3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_ch3.setObjectName("checkBox_ch3")
        self.gridLayout.addWidget(self.checkBox_ch3, 2, 0, 1, 1)
        self.checkBox_position = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_position.setObjectName("checkBox_position")
        self.gridLayout.addWidget(self.checkBox_position, 5, 3, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(350, 550, 221, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_saveMAT = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_saveMAT.setFont(font)
        self.pushButton_saveMAT.setObjectName("pushButton_saveMAT")
        self.verticalLayout.addWidget(self.pushButton_saveMAT)
        self.pushButton_saveCSV = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_saveCSV.setFont(font)
        self.pushButton_saveCSV.setObjectName("pushButton_saveCSV")
        self.verticalLayout.addWidget(self.pushButton_saveCSV)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 951, 191))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setObjectName("tableWidget")
        self.pushButton_openFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openFile.setGeometry(QtCore.QRect(390, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_openFile.setFont(font)
        self.pushButton_openFile.setObjectName("pushButton_openFile")
        self.pushButton_openFile.clicked.connect(self.loadCsv)
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def loadCsv(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Open CSV",
        (QDir.homePath() + "/Dokumente/CSV"), "CSV (*.csv *.tsv *.txt)")
        if fileName:
            self.loadCsvOnOpen(fileName)

    def loadCsvOnOpen(self, fileName):
        if fileName:

            df = pd.read_csv(fileName, header=None, delimiter='\t', keep_default_na=False, error_bad_lines=False)
            header = df.iloc[0]

            df = df[1:]

            self.tableWidget.setColumnCount(len(df.columns))
            self.tableWidget.setRowCount(len(df.index))

            for i in range(len(df.index)):
                for j in range(len(df.columns)):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

            for j in range(len(df.columns)):
                m = QTableWidgetItem(header[j])
                self.tableWidget.setHorizontalHeaderItem(j, m)

            self.tableWidget.selectRow(0)
            self.isChanged = False



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_excitation.setText(_translate("MainWindow", "Excitation (uA)"))
        self.checkBox_field.setText(_translate("MainWindow", "Magnetic Field (T)"))
        self.checkBox_ch4.setText(_translate("MainWindow", "Channel 4"))
        self.checkBox_RES.setText(_translate("MainWindow", "Resistance (ohm)"))
        self.checkBox_time.setText(_translate("MainWindow", "Timestamp (sec)"))
        self.checkBox_temp.setText(_translate("MainWindow", "Temperature (K)"))
        self.checkBox_ch1.setText(_translate("MainWindow", "Channel 1"))
        self.checkBox_ch2.setText(_translate("MainWindow", "Channel 2"))
        self.checkBox_ch3.setText(_translate("MainWindow", "Channel 3"))
        self.checkBox_position.setText(_translate("MainWindow", "Sample position (deg)"))
        self.pushButton_saveMAT.setText(_translate("MainWindow", "Save to .MAT"))
        self.pushButton_saveCSV.setText(_translate("MainWindow", "Save to .CSV"))
        self.pushButton_openFile.setText(_translate("MainWindow", "Open File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
