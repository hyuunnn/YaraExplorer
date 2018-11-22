# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import expanduser

import yara
import os
import shutil
import csv
import qdarkgraystyle

class Ui_Dialog(object):
    def __init__(self):
        self.match_file = []
        self.not_match_file = []

    def yara_search(self):
        self.match_file = []
        self.not_match_file = []

        path = self.lineEdit_2.text()

        try:
            rules = yara.compile(source=self.plainTextEdit_2.toPlainText())

            for (path, dir, files) in os.walk(path):
                for filename in files:
                    try:
                        f = open(path + "\\" + filename, "rb")
                        matches = rules.match(data=f.read())
                        f.close()

                        if matches:
                            rulename = [match.rule for match in matches]
                            self.match_file.append([', '.join(rulename), filename])

                        else:
                            self.not_match_file.append(filename)

                    except IOError: # Permission denied
                        print("[*] Permission denied : " + filename)
                        continue

            self.tableWidget.setSortingEnabled(False)
            self.tableWidget_2.setSortingEnabled(False)

            self.tableWidget.setRowCount(len(self.match_file))
            self.tableWidget.setColumnCount(2)

            for idx, (rulename, filename) in enumerate(self.match_file):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(idx, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(idx, 0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(idx, 1, item)
                item = self.tableWidget.verticalHeaderItem(idx)
                item.setText(self._translate("Dialog", str(idx+1)))
                item = self.tableWidget.item(idx, 0)
                item.setText(self._translate("Dialog", rulename))
                item = self.tableWidget.item(idx, 1)
                item.setText(self._translate("Dialog", filename))

            self.tableWidget_2.setRowCount(len(self.not_match_file))
            self.tableWidget_2.setColumnCount(1)

            for idx, filename in enumerate(self.not_match_file):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setVerticalHeaderItem(idx, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setItem(idx, 0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget_2.setItem(idx, 1, item)
                item = self.tableWidget_2.verticalHeaderItem(idx)
                item.setText(self._translate("Dialog", str(idx+1)))
                item = self.tableWidget_2.item(idx, 0)
                item.setText(self._translate("Dialog", filename))

            self.tableWidget.setSortingEnabled(True)
            self.tableWidget_2.setSortingEnabled(True)

            print("[*] Yara Search Complete!!")
        except yara.SyntaxError as e:
            print("[*] yara.SyntaxError -> {}".format(e))

    def move_files_1(self):
        path = self.lineEdit.text()

        if not os.path.isdir(path):
            os.mkdir(path)
            print("[*] mkdir : " + path)

        for (rulename, filename) in self.match_file:
            shutil.move(self.lineEdit_2.text() + "\\" + filename, path)
        print("[*] Move Files Complete!!")

    def move_files_2(self):
        path = self.lineEdit_3.text()

        if not os.path.isdir(path):
            os.mkdir(path)
            print("[*] mkdir : " + path)

        for filename in self.not_match_file:
            shutil.move(self.lineEdit_2.text() + "\\" + filename, path)
        print("[*] Move Files Complete!!")

    def make_CSV_1(self):
        f = open('result.csv', 'wb')
        wr = csv.writer(f)
        wr.writerow(["rulename", "filename"])

        for (rulename, filename) in self.match_file:
            wr.writerow([rulename, filename])

        f.close()
        print("[*] Make CSV Complete!!")

    def make_CSV_2(self):
        f = open('result.csv', 'wb')
        wr = csv.writer(f)
        wr.writerow(["filename"])

        for filename in self.not_match_file:
            wr.writerow([filename])

        f.close()
        print("[*] Make CSV Complete!!")

    def select_rule(self):
        path = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "Open a Yara File",
            expanduser("~"),
            "Yara Rule Files(*.yar *.yara)")
        try:
            f = open(path[0],"r")
            data = f.read()
            f.close()
            self.plainTextEdit_2.clear()
            self.plainTextEdit_2.insertPlainText(data)
        except FileNotFoundError:
            print("[*] FileNotFoundError (select_rule)")

    def select_path(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            "Open a folder",
            expanduser("~"),
            QtWidgets.QFileDialog.ShowDirsOnly)
        self.lineEdit_2.setText(path)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(954, 736)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.Main = QtWidgets.QWidget()
        self.Main.setObjectName("Main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Main)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.Main)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕 Light")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.Main)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout.addWidget(self.plainTextEdit_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.Main)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.select_rule)
        self.verticalLayout.addWidget(self.pushButton_5)
        self.label_4 = QtWidgets.QLabel(self.Main)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕 Light")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Main)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton_7 = QtWidgets.QPushButton(self.Main)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.select_path)
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton = QtWidgets.QPushButton(self.Main)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.yara_search)
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.Main, "")
        self.YaraExplorer = QtWidgets.QWidget()
        self.YaraExplorer.setObjectName("YaraExplorer")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.YaraExplorer)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.YaraExplorer)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕 Light")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(self.YaraExplorer)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕 Light")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 3)
        self.tableWidget = QtWidgets.QTableWidget(self.YaraExplorer)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(self.match_file))

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.YaraExplorer)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(len(self.not_match_file))
        self.tableWidget_2.setHorizontalHeaderItem(0, item)

        self.gridLayout.addWidget(self.tableWidget_2, 1, 3, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.YaraExplorer)
        font = QtGui.QFont()
        font.setFamily("나눔고딕 Light")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.YaraExplorer)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.YaraExplorer)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.move_files_1)
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.YaraExplorer)
        font = QtGui.QFont()
        font.setFamily("나눔고딕 Light")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 3, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.YaraExplorer)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 4, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.YaraExplorer)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.move_files_2)
        self.gridLayout.addWidget(self.pushButton_3, 2, 5, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.YaraExplorer)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.make_CSV_1)
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 3)
        self.pushButton_6 = QtWidgets.QPushButton(self.YaraExplorer)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.make_CSV_2)
        self.gridLayout.addWidget(self.pushButton_6, 3, 3, 1, 3)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.YaraExplorer, "")
        self.verticalLayout_3.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self._translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(self._translate("Dialog", "Dialog"))
        self.label_2.setText(self._translate("Dialog", "Yara Rule"))
        self.plainTextEdit_2.setPlainText(self._translate("Dialog", "// \"http://virustotal.github.io/yara/\"\nrule silent_banker : banker\n{\n    meta:\n        description = \"This is just an example\"\n        thread_level = 3\n        in_the_wild = true\n    strings:\n        $a = {6A 40 68 00 30 00 00 6A 14 8D 91}\n        $b = {8D 4D B0 2B C1 83 C0 27 99 6A 4E 59 F7 F9}\n        $c = \"UVODFRYSIHLNWPEJXQZAKCBGMT\"\n    condition:\n        $a or $b or $c\n}"))
        self.pushButton_5.setText(self._translate("Dialog", "Select Rule File"))
        self.label_4.setText(self._translate("Dialog", "Path Setting"))
        self.lineEdit_2.setText(self._translate("Dialog", ""))
        self.pushButton_7.setText(self._translate("Dialog", "Select Path"))
        self.pushButton.setText(self._translate("Dialog", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main), self._translate("Dialog", "Main"))
        self.label.setText(self._translate("Dialog", "Detected File"))
        self.label_6.setText(self._translate("Dialog", "Not Detected File"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(self._translate("Dialog", "rulename"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(self._translate("Dialog", "filename"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(self._translate("Dialog", "filename"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)

        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(self._translate("Dialog", "Move File"))
        self.lineEdit.setText(self._translate("Dialog", ""))
        self.pushButton_2.setText(self._translate("Dialog", "Move"))
        self.label_5.setText(self._translate("Dialog", "Move File"))
        self.lineEdit_3.setText(self._translate("Dialog", ""))
        self.pushButton_3.setText(self._translate("Dialog", "Move"))
        self.pushButton_4.setText(self._translate("Dialog", "Save CSV"))
        self.pushButton_6.setText(self._translate("Dialog", "Save CSV"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.YaraExplorer), self._translate("Dialog", "YaraExplorer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

