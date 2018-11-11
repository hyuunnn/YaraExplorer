# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import yara
import os
import shutil
import csv

class Ui_Dialog(object):
    def __init__(self):
        self.match_file = []
        self.not_match_file = []

    def yara_search(self):
        self.match_file = []
        self.not_match_file = []

        path = self.lineEdit_2.text()
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
                    continue

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

    def move_files_1(self):
        path = self.lineEdit.text()

        for (rulename, filename) in self.match_file:
            shutil.move(self.lineEdit_2.text() + "\\" + filename, path)

    def move_files_2(self):
        path = self.lineEdit_3.text()

        for filename in self.not_match_file:
            shutil.move(self.lineEdit_2.text() + "\\" + filename, path)

    def make_CSV_1(self):
        f = open('result.csv', 'wb')
        wr = csv.writer(f)
        wr.writerow(["rulename", "filename"])

        for (rulename, filename) in self.match_file:
            wr.writerow([rulename, filename])

        f.close()

    def make_CSV_2(self):
        f = open('result.csv', 'wb')
        wr = csv.writer(f)
        wr.writerow(["filename"])

        for filename in self.not_match_file:
            wr.writerow([filename])

        f.close()

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
        self.plainTextEdit_2.setPlainText(self._translate("Dialog", "import \"hash\"\n"
"import \"pe\"\n"
"\n"
"rule xor_transform\n"
"{\n"
"    strings:\n"
"        /*\n"
"          AND           EBX, 0x7F8                            |81E3F8070000\n"
"          SHL           EBX, 0x14                             |C1E314\n"
"          SHR           EDX, 8                                |C1EA08\n"
"      */\n"
"      $xor_transform = {81 E? F8 07 00 00 C1 E? 14 C1 E? 08}\n"
"    condition:\n"
"        all of them\n"
"}\n"
"\n"
"rule FE_Transform\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.6\"\n"
"      date = \"2018-11-09\"\n"
"      MD5 = \"3B43E1C70A7356793C43B7C889B86A39\"\n"
"  strings:\n"
"      /*\n"
"          AND           EDI, 0x1FE                            |81E7FE010000\n"
"          XOR           BL, DL                                |32DA\n"
"          SHL           ECX, 0x18                             |C1E118\n"
"      */\n"
"      /*\n"
"          AND           ECX, 0x1FE                            |81E1FE010000\n"
"          SHL           EAX, 0x18                             |C1E018\n"
"      */\n"
"      $FE_Transform = {81 E? FE 01 00 00 [0-2] C1 E? 18}\n"
"  condition:\n"
"      all of them \n"
"}\n"
"\n"
"rule S_transform\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.4\"\n"
"      date = \"2018-09-07\"\n"
"      MD5 = \"052596A8380EDEEE8E211B504F44E133\"\n"
"  strings:\n"
"      $S_transform_50 = \"S^Ws2_32.dll\" nocase wide ascii\n"
"      $S_transform_51 = \"S^WSAStartup\" nocase wide ascii\n"
"      $S_transform_52 = \"S^inet_addr\" nocase wide ascii\n"
"      $S_transform_53 = \"S^socket\" nocase wide ascii\n"
"      $S_transform_54 = \"S^htons\" nocase wide ascii\n"
"      $S_transform_55 = \"S^ntohs\" nocase wide ascii\n"
"      $S_transform_56 = \"S^bind\" nocase wide ascii\n"
"      $S_transform_57 = \"S^WSAIoctl\" nocase wide ascii\n"
"      $S_transform_58 = \"S^setsockopt\" nocase wide ascii\n"
"      $S_transform_59 = \"S^select\" nocase wide ascii\n"
"      $S_transform_49 = \"S^UnmapViewOfFile\" nocase wide ascii\n"
"      $S_transform_48 = \"S^MapViewOfFile\" nocase wide ascii\n"
"      $S_transform_47 = \"S^MoveFileA\" nocase wide ascii\n"
"      $S_transform_46 = \"S^GetWindowsDirectoryA\" nocase wide ascii\n"
"      $S_transform_45 = \"S^TerminateThread\" nocase wide ascii\n"
"      $S_transform_44 = \"S^TerminateProcess\" nocase wide ascii\n"
"      $S_transform_43 = \"S^ReadFile\" nocase wide ascii\n"
"      $S_transform_42 = \"S^CreateProcessA\" nocase wide ascii\n"
"      $S_transform_41 = \"S^CreatePipe\" nocase wide ascii\n"
"      $S_transform_40 = \"S^CreateDirectoryA\" nocase wide ascii\n"
"      $S_transform_38 = \"S^GetSystemDirectoryA\" nocase wide ascii\n"
"      $S_transform_39 = \"S^WinExec\" nocase wide ascii\n"
"      $S_transform_32 = \"S^GetTempPathA\" nocase wide ascii\n"
"      $S_transform_33 = \"S^GetLocalTime\" nocase wide ascii\n"
"      $S_transform_30 = \"S^ReleaseSemaphore\" nocase wide ascii\n"
"      $S_transform_31 = \"S^WaitForMultipleObjects\" nocase wide ascii\n"
"      $S_transform_36 = \"S^GetFileTime\" nocase wide ascii\n"
"      $S_transform_37 = \"S^SetFileTime\" nocase wide ascii\n"
"      $S_transform_34 = \"S^WriteFile\" nocase wide ascii\n"
"      $S_transform_35 = \"S^GetFileAttributesA\" nocase wide ascii\n"
"      $S_transform_29 = \"S^DeleteCriticalSection\" nocase wide ascii\n"
"      $S_transform_28 = \"S^SetEvent\" nocase wide ascii\n"
"      $S_transform_21 = \"S^EnterCriticalSection\" nocase wide ascii\n"
"      $S_transform_20 = \"S^InitializeCriticalSection\" nocase wide ascii\n"
"      $S_transform_23 = \"S^ExitThread\" nocase wide ascii\n"
"      $S_transform_22 = \"S^LeaveCriticalSection\" nocase wide ascii\n"
"      $S_transform_25 = \"S^GetLastError\" nocase wide ascii\n"
"      $S_transform_24 = \"S^GetTickCount\" nocase wide ascii\n"
"      $S_transform_27 = \"S^CreateEventA\" nocase wide ascii\n"
"      $S_transform_26 = \"S^CreateSemaphoreA\" nocase wide ascii\n"
"      $S_transform_14 = \"S^WaitForSingleObject\" nocase wide ascii\n"
"      $S_transform_15 = \"S^ReleaseMutex\" nocase wide ascii\n"
"      $S_transform_16 = \"S^UnlockFile\" nocase wide ascii\n"
"      $S_transform_17 = \"S^CloseHandle\" nocase wide ascii\n"
"      $S_transform_10 = \"S^CreateThread\" nocase wide ascii\n"
"      $S_transform_11 = \"S^CreateFileA\" nocase wide ascii\n"
"      $S_transform_12 = \"S^GetFileSize\" nocase wide ascii\n"
"      $S_transform_13 = \"S^LockFile\" nocase wide ascii\n"
"      $S_transform_18 = \"S^OpenFileMappingA\" nocase wide ascii\n"
"      $S_transform_19 = \"S^CreateFileMappingA\" nocase wide ascii\n"
"      $S_transform_98 = \"S^InternetSetCookieA\" nocase wide ascii\n"
"      $S_transform_99 = \"S^InternetCrackUrlA\" nocase wide ascii\n"
"      $S_transform_94 = \"S^InternetOpenUrlA\" nocase wide ascii\n"
"      $S_transform_95 = \"S^InternetConnectA\" nocase wide ascii\n"
"      $S_transform_96 = \"S^HttpOpenRequestA\" nocase wide ascii\n"
"      $S_transform_97 = \"S^InternetCloseHandle\" nocase wide ascii\n"
"      $S_transform_90 = \"S^ControlService\" nocase wide ascii\n"
"      $S_transform_91 = \"S^CloseServiceHandle\" nocase wide ascii\n"
"      $S_transform_92 = \"S^wininet.dll\" nocase wide ascii\n"
"      $S_transform_93 = \"S^InternetOpenA\" nocase wide ascii\n"
"      $S_transform_89 = \"S^QueryServiceStatus\" nocase wide ascii\n"
"      $S_transform_88 = \"S^OpenServiceA\" nocase wide ascii\n"
"      $S_transform_83 = \"S^CryptCreateHash\" nocase wide ascii\n"
"      $S_transform_82 = \"S^CryptDecrypt\" nocase wide ascii\n"
"      $S_transform_81 = \"S^CryptDestroyKey\" nocase wide ascii\n"
"      $S_transform_80 = \"S^CryptEncrypt\" nocase wide ascii\n"
"      $S_transform_87 = \"S^OpenSCManagerA\" nocase wide ascii\n"
"      $S_transform_86 = \"S^CryptDeriveKey\" nocase wide ascii\n"
"      $S_transform_85 = \"S^CryptDestroyHash\" nocase wide ascii\n"
"      $S_transform_84 = \"S^CryptHashData\" nocase wide ascii\n"
"      $S_transform_76 = \"S^RegEnumValueA\" nocase wide ascii\n"
"      $S_transform_77 = \"S^CryptAcquireContextA\" nocase wide ascii\n"
"      $S_transform_74 = \"S^RegDeleteValueA\" nocase wide ascii\n"
"      $S_transform_75 = \"S^RegQueryInfoKeyA\" nocase wide ascii\n"
"      $S_transform_72 = \"S^RegCreateKeyExA\" nocase wide ascii\n"
"      $S_transform_73 = \"S^RegSetValueExA\" nocase wide ascii\n"
"      $S_transform_70 = \"S^RegQueryValueExA\" nocase wide ascii\n"
"      $S_transform_71 = \"S^RegCloseKey\" nocase wide ascii\n"
"      $S_transform_78 = \"S^CryptImportKey\" nocase wide ascii\n"
"      $S_transform_79 = \"S^CryptReleaseContext\" nocase wide ascii\n"
"      $S_transform_101 = \"S^HttpSendRequestA\" nocase wide ascii\n"
"      $S_transform_100 = \"S^InternetReadFile\" nocase wide ascii\n"
"      $S_transform_103 = \"S^HttpAddRequestHeadersA\" nocase wide ascii\n"
"      $S_transform_102 = \"S^HttpQueryInfoA\" nocase wide ascii\n"
"      $S_transform_105 = \"S^InternetWriteFile\" nocase wide ascii\n"
"      $S_transform_104 = \"S^HttpSendRequestExA\" nocase wide ascii\n"
"      $S_transform_107 = \"S^DeleteUrlCacheEntry\" nocase wide ascii\n"
"      $S_transform_106 = \"S^HttpEndRequestA\" nocase wide ascii\n"
"      $S_transform_108 = \"S^InternetGetConnectedState\" nocase wide ascii\n"
"      $S_transform_2 = \"S^GetProcessHeap\" nocase wide ascii\n"
"      $S_transform_3 = \"S^HeapDestroy\" nocase wide ascii\n"
"      $S_transform_0 = \"S^Kernel32.dll\" nocase wide ascii\n"
"      $S_transform_1 = \"S^HeapCreate\" nocase wide ascii\n"
"      $S_transform_6 = \"S^HeapFree\" nocase wide ascii\n"
"      $S_transform_7 = \"S^GetModuleFileNameA\" nocase wide ascii\n"
"      $S_transform_4 = \"S^HeapAlloc\" nocase wide ascii\n"
"      $S_transform_5 = \"S^HeapReAlloc\" nocase wide ascii\n"
"      $S_transform_8 = \"S^DeleteFileA\" nocase wide ascii\n"
"      $S_transform_9 = \"S^CreateMutexA\" nocase wide ascii\n"
"      $S_transform_65 = \"S^Iphlpapi.dll\" nocase wide ascii\n"
"      $S_transform_64 = \"S^closesocket\" nocase wide ascii\n"
"      $S_transform_67 = \"S^GetPerAdapterInfo\" nocase wide ascii\n"
"      $S_transform_66 = \"S^GetAdaptersInfo\" nocase wide ascii\n"
"      $S_transform_61 = \"S^recv\" nocase wide ascii\n"
"      $S_transform_60 = \"S^connect\" nocase wide ascii\n"
"      $S_transform_63 = \"S^sendto\" nocase wide ascii\n"
"      $S_transform_62 = \"S^send\" nocase wide ascii\n"
"      $S_transform_69 = \"S^RegOpenKeyExA\" nocase wide ascii\n"
"      $S_transform_68 = \"S^Advapi32.dll\" nocase wide ascii\n"
"  condition:\n"
"        10 of them\n"
"}\n"
"\n"
"rule joanap\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.4\"\n"
"      date = \"2018-09-07\"\n"
"      MD5 = \"7FE80CEE04003FED91C02E3A372F4B01\"\n"
"  strings:\n"
"      $joanap_2 = \"!dyp$u4MRk_Cb$uupI_1sv7Rvd23F7S\" nocase wide ascii\n"
"      $joanap_3 = \"!9jHTSr_pCZ7BW1jZB9iDAGjHQishBK\" nocase wide ascii\n"
"      $joanap_0 = \"!inIf3w25VNC8bRvXwRDapbCQMc62EtZPx9\" nocase wide ascii\n"
"      $joanap_1 = \"!YYz0X1w_GTtD7BNP69mK5XnZWzlB9bKJe1\" nocase wide ascii\n"
"      $joanap_6 = \"!xJkUIwOnZTHBmw_0uG4_48$\" nocase wide ascii\n"
"      $joanap_7 = \"!0E1mfduUaneS8YLsMZ7\" nocase wide ascii\n"
"      $joanap_4 = \"!6Y8iuaWgBu7$tK\" nocase wide ascii\n"
"      $joanap_5 = \"!n0U76nGoNe2y03lVgOd4t7VDVp1GBXW\" nocase wide ascii\n"
"      $joanap_8 = \"!TlPco4ikBlt6jNEtq1\" nocase wide ascii\n"
"      $joanap_9 = \"!ctRHFEX5m9JnZdDfpK\" nocase wide ascii\n"
"      $joanap_10 = \"!m2MBHjehQ7IK6uqIsejT\" nocase wide ascii\n"
"      $joanap_11 = \"!6ro0EYkRiqFMphgymbcTsfJ60K\" nocase wide ascii\n"
"      $joanap_12 = \"!GawD1UIQi6w8kjUgleSNGrXVwcY\" nocase wide ascii\n"
"      $joanap_13 = \"!_2FAcHI224$A_q8gS0dK\" nocase wide ascii\n"
"      $joanap_14 = \"!VWBeBxYx1nzrCkBLGQO\" nocase wide ascii\n"
"      $joanap_15 = \"!uRa9t1tCDeS197CPt7I\" nocase wide ascii\n"
"      $joanap_16 = \"!emCFgv7Xc8ItaVGN0bMf\" nocase wide ascii\n"
"      $unique = \"iamsorry!@1234567\" nocase wide ascii\n"
"  condition:\n"
"      10 of ($joanap*) and $unique\n"
"}\n"
"\n"
"rule fallchill\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.4\"\n"
"      date = \"2018-09-07\"\n"
"      MD5 = \"A119AE22A15B32C0EF9E19DDB26D6B66\"\n"
"  strings:\n"
"      $fallchill_95 = \"CsamtvSvierxvClmurt2W\" nocase wide ascii\n"
"      $fallchill_94 = \"OkvmSCMamatviW\" nocase wide ascii\n"
"      $fallchill_97 = \"DvovgvSvierxv\" nocase wide ascii\n"
"      $fallchill_96 = \"RvtDvovgvVaofvW\" nocase wide ascii\n"
"      $fallchill_91 = \"RvtSvgVaofvEcW\" nocase wide ascii\n"
"      $fallchill_90 = \"RvtColhvKvb\" nocase wide ascii\n"
"      $fallchill_93 = \"CivagvSvierxvW\" nocase wide ascii\n"
"      $fallchill_92 = \"SgaigSvierxvW\" nocase wide ascii\n"
"      $fallchill_99 = \"OkvmSvierxvW\" nocase wide ascii\n"
"      $fallchill_98 = \"RvtDvovgvKvbW\" nocase wide ascii\n"
"      $fallchill_19 = \"GvgTrxpClfmg\" nocase wide ascii\n"
"      $fallchill_18 = \"WSACovamfk\" nocase wide ascii\n"
"      $fallchill_15 = \"WSASgaigfk\" nocase wide ascii\n"
"      $fallchill_14 = \"orhgvm\" nocase wide ascii\n"
"      $fallchill_17 = \"ivxe\" nocase wide ascii\n"
"      $fallchill_16 = \"hvghlxplkg\" nocase wide ascii\n"
"      $fallchill_11 = \"tvgkvvimanv\" nocase wide ascii\n"
"      $fallchill_10 = \"axxvkg\" nocase wide ascii\n"
"      $fallchill_13 = \"hsfgwldm\" nocase wide ascii\n"
"      $fallchill_12 = \"tvgslhgybmanv\" nocase wide ascii\n"
"      $fallchill_68 = \"GvgEcrgClwvTsivaw\" nocase wide ascii\n"
"      $fallchill_69 = \"LlawLryiaibW\" nocase wide ascii\n"
"      $fallchill_60 = \"Pilxvhh32NvcgW\" nocase wide ascii\n"
"      $fallchill_61 = \"WirgvFrov\" nocase wide ascii\n"
"      $fallchill_62 = \"GvgMlwfovFrovNanvW\" nocase wide ascii\n"
"      $fallchill_63 = \"WargFliMfogrkovOyqvxgh\" nocase wide ascii\n"
"      $fallchill_64 = \"WargFliSrmtovOyqvxg\" nocase wide ascii\n"
"      $fallchill_65 = \"LlxaoFivv\" nocase wide ascii\n"
"      $fallchill_66 = \"TvinrmagvTsivaw\" nocase wide ascii\n"
"      $fallchill_67 = \"GvgFrovTrnv\" nocase wide ascii\n"
"      $fallchill_79 = \"FrmwFrihgFrovW\" nocase wide ascii\n"
"      $fallchill_78 = \"LlxaoAoolx\" nocase wide ascii\n"
"      $fallchill_73 = \"ColhvHamwov\" nocase wide ascii\n"
"      $fallchill_72 = \"GvgTvnkFrovNanvW\" nocase wide ascii\n"
"      $fallchill_71 = \"Pilxvhh32FrihgW\" nocase wide ascii\n"
"      $fallchill_70 = \"DvovgvFrovW\" nocase wide ascii\n"
"      $fallchill_77 = \"CivagvTsivaw\" nocase wide ascii\n"
"      $fallchill_76 = \"RvawFrov\" nocase wide ascii\n"
"      $fallchill_75 = \"GvgFrovSrzv\" nocase wide ascii\n"
"      $fallchill_74 = \"GvgEcrgClwvPilxvhh\" nocase wide ascii\n"
"      $fallchill_46 = \"GvgVvihrlmEcW\" nocase wide ascii\n"
"      $fallchill_47 = \"UmnakVrvdOuFrov\" nocase wide ascii\n"
"      $fallchill_44 = \"GvgLltrxaoDirevh\" nocase wide ascii\n"
"      $fallchill_45 = \"SvgFrovTrnv\" nocase wide ascii\n"
"      $fallchill_42 = \"SvgCfiivmgDrivxglibW\" nocase wide ascii\n"
"      $fallchill_43 = \"GvgCfiivmgDrivxglibW\" nocase wide ascii\n"
"      $fallchill_40 = \"CivagvFrovW\" nocase wide ascii\n"
"      $fallchill_41 = \"OkvmPilxvhh\" nocase wide ascii\n"
"      $fallchill_48 = \"GvgCfiivmgPilxvhh\" nocase wide ascii\n"
"      $fallchill_49 = \"GvgVlofnvImulinagrlmW\" nocase wide ascii\n"
"      $fallchill_108 = \"OkvmPilxvhhTlpvm\" nocase wide ascii\n"
"      $fallchill_106 = \"ClmgiloSvierxv\" nocase wide ascii\n"
"      $fallchill_107 = \"RvtOkvmKvbW\" nocase wide ascii\n"
"      $fallchill_104 = \"ColhvSvierxvHamwov\" nocase wide ascii\n"
"      $fallchill_105 = \"SvgSvierxvSgagfh\" nocase wide ascii\n"
"      $fallchill_102 = \"LllpfkPirerovtvVaofvW\" nocase wide ascii\n"
"      $fallchill_103 = \"AwqfhgTlpvmPirerovtvh\" nocase wide ascii\n"
"      $fallchill_100 = \"LllpfkAxxlfmgSrwW\" nocase wide ascii\n"
"      $fallchill_101 = \"GvgTlpvmImulinagrlm\" nocase wide ascii\n"
"      $fallchill_51 = \"GvgLlxaoTrnv\" nocase wide ascii\n"
"      $fallchill_50 = \"GvgSbhgvnDrivxglibW\" nocase wide ascii\n"
"      $fallchill_53 = \"CivagvPilxvhhW\" nocase wide ascii\n"
"      $fallchill_52 = \"GvgFrovAggiryfgvhW\" nocase wide ascii\n"
"      $fallchill_55 = \"CivagvTllosvok32Smakhslg\" nocase wide ascii\n"
"      $fallchill_54 = \"GvgTvnkPagsW\" nocase wide ascii\n"
"      $fallchill_57 = \"RvawPilxvhhMvnlib\" nocase wide ascii\n"
"      $fallchill_56 = \"SvgFrovPlrmgvi\" nocase wide ascii\n"
"      $fallchill_59 = \"Sovvk\" nocase wide ascii\n"
"      $fallchill_58 = \"MakVrvdOuFrov\" nocase wide ascii\n"
"      $fallchill_24 = \"VrigfaoAoolxEc\" nocase wide ascii\n"
"      $fallchill_25 = \"SvgLahgEiili\" nocase wide ascii\n"
"      $fallchill_26 = \"GvgLahgEiili\" nocase wide ascii\n"
"      $fallchill_27 = \"GvgDrhpFivvSkaxvEcW\" nocase wide ascii\n"
"      $fallchill_20 = \"LlxpRvhlfixv\" nocase wide ascii\n"
"      $fallchill_21 = \"LlawRvhlfixv\" nocase wide ascii\n"
"      $fallchill_22 = \"FrmwRvhlfixvW\" nocase wide ascii\n"
"      $fallchill_23 = \"CivagvRvnlgvTsivaw\" nocase wide ascii\n"
"      $fallchill_28 = \"GvgDirevTbkvW\" nocase wide ascii\n"
"      $fallchill_29 = \"VrigfaoQfvibEc\" nocase wide ascii\n"
"      $fallchill_88 = \"RvtCivagvKvbW\" nocase wide ascii\n"
"      $fallchill_89 = \"RvtrhgviSvierxvCgioHamwoviW\" nocase wide ascii\n"
"      $fallchill_82 = \"GvgPilxvhhTrnvh\" nocase wide ascii\n"
"      $fallchill_83 = \"GvgAwakgvihImul\" nocase wide ascii\n"
"      $fallchill_80 = \"WrmEcvx\" nocase wide ascii\n"
"      $fallchill_81 = \"Mlwfov32FrihgW\" nocase wide ascii\n"
"      $fallchill_86 = \"RvtQfvibVaofvEcW\" nocase wide ascii\n"
"      $fallchill_87 = \"RvtOkvmKvbEcW\" nocase wide ascii\n"
"      $fallchill_84 = \"CivagvPilxvhhAhUhviW\" nocase wide ascii\n"
"      $fallchill_85 = \"GvgUhviNanvW\" nocase wide ascii\n"
"      $fallchill_1 = \"yrmw\" nocase wide ascii\n"
"      $fallchill_0 = \"rmvg_awwi\" nocase wide ascii\n"
"      $fallchill_3 = \"hvmw\" nocase wide ascii\n"
"      $fallchill_2 = \"__WSAFDIhSvg\" nocase wide ascii\n"
"      $fallchill_5 = \"sglmh\" nocase wide ascii\n"
"      $fallchill_4 = \"hvovxg\" nocase wide ascii\n"
"      $fallchill_7 = \"xolhvhlxpvg\" nocase wide ascii\n"
"      $fallchill_6 = \"hlxpvg\" nocase wide ascii\n"
"      $fallchill_9 = \"rlxgohlxpvg\" nocase wide ascii\n"
"      $fallchill_8 = \"xlmmvxg\" nocase wide ascii\n"
"      $fallchill_37 = \"VrigfaoPilgvxgEc\" nocase wide ascii\n"
"      $fallchill_36 = \"WirgvPilxvhhMvnlib\" nocase wide ascii\n"
"      $fallchill_35 = \"GvgClnkfgviNanvW\" nocase wide ascii\n"
"      $fallchill_34 = \"FrmwNvcgFrovW\" nocase wide ascii\n"
"      $fallchill_33 = \"GvgMlwfovHamwovW\" nocase wide ascii\n"
"      $fallchill_32 = \"MlevFrovEcW\" nocase wide ascii\n"
"      $fallchill_31 = \"FrmwColhv\" nocase wide ascii\n"
"      $fallchill_30 = \"CivagvFrovMakkrmtW\" nocase wide ascii\n"
"      $fallchill_39 = \"TvinrmagvPilxvhh\" nocase wide ascii\n"
"      $fallchill_38 = \"FivvLryiaib\" nocase wide ascii\n"
"  condition:\n"
"      20 of ($fallchill*)\n"
"}\n"
"\n"
"rule rifle_sub_string : sub_string\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.4\"\n"
"      date = \"2018-09-08\"\n"
"      MD5 = \"8BD8C367DFE5C418A771CA8BDCE6AC88\"\n"
"  strings:\n"
"      $rifle_sub_string_271 = \"EP-XI9P-UP\" nocase wide ascii\n"
"      $rifle_sub_string_270 = \"LPHPUPI9TUTo-H8PoUTpl\" nocase wide ascii\n"
"      $rifle_sub_string_273 = \"kT9Uw-HcHHpoWg\" nocase wide ascii\n"
"      $rifle_sub_string_272 = \"EP-XLPvU9pG\" nocase wide ascii\n"
"      $rifle_sub_string_275 = \"FPU6pnwHPE-lnHPO\" nocase wide ascii\n"
"      $rifle_sub_string_274 = \"kT9Uw-HcHHpo\" nocase wide ascii\n"
"      $rifle_sub_string_277 = \"FPUI1Blhp\" nocase wide ascii\n"
"      $rifle_sub_string_276 = \"FPU8UnE-lnHP\" nocase wide ascii\n"
"      $rifle_sub_string_279 = \"8PU0THPCTSP\" nocase wide ascii\n"
"      $rifle_sub_string_278 = \"Bva-n8U9Tld1U9O\" nocase wide ascii\n"
"      $rifle_sub_string_363 = \"0TlnuPgU0THPO\" nocase wide ascii\n"
"      $rifle_sub_string_362 = \"IpXG0THPO\" nocase wide ascii\n"
"      $rifle_sub_string_361 = \"qPSp2PLT9PoUp9GO\" nocase wide ascii\n"
"      $rifle_sub_string_360 = \"0Tln0T9vU0THPO\" nocase wide ascii\n"
"      $rifle_sub_string_367 = \"FPU8GvUPSLT9PoUp9Gc\" nocase wide ascii\n"
"      $rifle_sub_string_366 = \"BvOpryN19poPvv\" nocase wide ascii\n"
"      $rifle_sub_string_378 = \"5WquWMKf.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_365 = \"FPUWl2T9plSPlUk-9T-jHPO\" nocase wide ascii\n"
"      $rifle_sub_string_370 = \"bXPl19poPvv\" nocase wide ascii\n"
"      $rifle_sub_string_371 = \"FPU0THP8T_PWg\" nocase wide ascii\n"
"      $rifle_sub_string_372 = \"FPU0THP8T_P\" nocase wide ascii\n"
"      $rifle_sub_string_364 = \"0TlnIHpvP\" nocase wide ascii\n"
"      $rifle_sub_string_374 = \"CP9STl-UP19poPvv\" nocase wide ascii\n"
"      $rifle_sub_string_375 = \"FPUCToRIpwlU\" nocase wide ascii\n"
"      $rifle_sub_string_376 = \"AlS-XkTPrbh0THP\" nocase wide ascii\n"
"      $rifle_sub_string_377 = \"I9P-UP0THP6-XXTldc\" nocase wide ascii\n"
"      $rifle_sub_string_204 = \"O-TU0p96wHUTXHPbjePoUv\" nocase wide ascii\n"
"      $rifle_sub_string_205 = \"FPUkP9vTplWgc\" nocase wide ascii\n"
"      $rifle_sub_string_206 = \"FPUkP9vTplWgO\" nocase wide ascii\n"
"      $rifle_sub_string_207 = \"FPUCTSPmplPBlhp9S-UTpl\" nocase wide ascii\n"
"      $rifle_sub_string_200 = \"kP9ThGkP9vTplBlhpO\" nocase wide ascii\n"
"      $rifle_sub_string_201 = \"kP98PUIplnTUTpl6-vR\" nocase wide ascii\n"
"      $rifle_sub_string_202 = \"09PPMTj9-9GclnWgTUC79P-n\" nocase wide ascii\n"
"      $rifle_sub_string_203 = \"CP9STl-UPC79P-n\" nocase wide ascii\n"
"      $rifle_sub_string_208 = \"FPUWgTUIpnPC79P-n\" nocase wide ascii\n"
"      $rifle_sub_string_209 = \"FPUIw99PlULT9PoUp9GO\" nocase wide ascii\n"
"      $rifle_sub_string_109 = \"8GvUPS1-9-SPUP9vBlhpc\" nocase wide ascii\n"
"      $rifle_sub_string_108 = \"FPU0p9Pd9pwlnOTlnpr\" nocase wide ascii\n"
"      $rifle_sub_string_107 = \"FPU8GvUPS6PU9Tov\" nocase wide ascii\n"
"      $rifle_sub_string_106 = \"FPULI\" nocase wide ascii\n"
"      $rifle_sub_string_105 = \"FPULPvRUpXOTlnpr\" nocase wide ascii\n"
"      $rifle_sub_string_104 = \"FPUOTlnprBlhp\" nocase wide ascii\n"
"      $rifle_sub_string_103 = \"qPHP-vPLI\" nocase wide ascii\n"
"      $rifle_sub_string_102 = \"rvX9TlUhO\" nocase wide ascii\n"
"      $rifle_sub_string_101 = \"FPUOTlnprC79P-n19poPvvBn\" nocase wide ascii\n"
"      $rifle_sub_string_100 = \"L9-rCPgUc\" nocase wide ascii\n"
"      $rifle_sub_string_40 = \"8U9PUo7aHU\" nocase wide ascii\n"
"      $rifle_sub_string_248 = \"FPUIplvpHP6pnP\" nocase wide ascii\n"
"      $rifle_sub_string_326 = \"O-TU0p98TldHPbjePoU\" nocase wide ascii\n"
"      $rifle_sub_string_325 = \"8PU0THPcUU9TjwUPvO\" nocase wide ascii\n"
"      $rifle_sub_string_324 = \"8PUM-vUW99p9\" nocase wide ascii\n"
"      $rifle_sub_string_323 = \"kT9Uw-HzwP9GWg\" nocase wide ascii\n"
"      $rifle_sub_string_44 = \"I9P-UPIpSX-UTjHPaTUS-X\" nocase wide ascii\n"
"      $rifle_sub_string_321 = \"6pnwHPKf0T9vUO\" nocase wide ascii\n"
"      $rifle_sub_string_320 = \"OTnPI7-9Cp6wHUTaGUP\" nocase wide ascii\n"
"      $rifle_sub_string_240 = \"8HPPX\" nocase wide ascii\n"
"      $rifle_sub_string_48 = \"8PUCPgUIpHp9\" nocase wide ascii\n"
"      $rifle_sub_string_242 = \"IHpvPE-lnHP\" nocase wide ascii\n"
"      $rifle_sub_string_243 = \"FPU6pnwHPE-lnHPc\" nocase wide ascii\n"
"      $rifle_sub_string_244 = \"6-XkTPrbh0THP\" nocase wide ascii\n"
"      $rifle_sub_string_245 = \"FPUMpo-HPBlhpc\" nocase wide ascii\n"
"      $rifle_sub_string_329 = \"FPU8GvUPS1prP98U-Uwv\" nocase wide ascii\n"
"      $rifle_sub_string_247 = \"FPU8U9TldCGXPc\" nocase wide ascii\n"
"      $rifle_sub_string_221 = \"I9P-UPC79P-n\" nocase wide ascii\n"
"      $rifle_sub_string_143 = \"8PU8P92ToP8U-Uwv\" nocase wide ascii\n"
"      $rifle_sub_string_142 = \"LwXHTo-UPCpRPlWg\" nocase wide ascii\n"
"      $rifle_sub_string_141 = \"I7-ldP8P92ToPIplhTdfc\" nocase wide ascii\n"
"      $rifle_sub_string_140 = \"bXPl8P92ToPc\" nocase wide ascii\n"
"      $rifle_sub_string_147 = \"I9P-UP19poPvvcvAvP9O\" nocase wide ascii\n"
"      $rifle_sub_string_146 = \"I9P-UP19poPvvcvAvP9c\" nocase wide ascii\n"
"      $rifle_sub_string_145 = \"qPdTvUP98P92ToPIU9HE-lnHP9c\" nocase wide ascii\n"
"      $rifle_sub_string_144 = \"qPdTvUP98P92ToPIU9HE-lnHP9O\" nocase wide ascii\n"
"      $rifle_sub_string_149 = \"qPdWlwS5PGWgO\" nocase wide ascii\n"
"      $rifle_sub_string_148 = \"Ipl2P9U8TnCp8U9Tld8Tnc\" nocase wide ascii\n"
"      $rifle_sub_string_41 = \"8PHPoUbjePoU\" nocase wide ascii\n"
"      $rifle_sub_string_249 = \"FPUIplvpHPI1\" nocase wide ascii\n"
"      $rifle_sub_string_43 = \"I9P-UP1-HPUUP\" nocase wide ascii\n"
"      $rifle_sub_string_42 = \"8PHPoU1-HPUUP\" nocase wide ascii\n"
"      $rifle_sub_string_45 = \"I9P-UPIpSX-UTjHPLI\" nocase wide ascii\n"
"      $rifle_sub_string_322 = \"6pnwHPKfuPgUO\" nocase wide ascii\n"
"      $rifle_sub_string_47 = \"8PUaRIpHp9\" nocase wide ascii\n"
"      $rifle_sub_string_46 = \"FPU8UpoRbjePoU\" nocase wide ascii\n"
"      $rifle_sub_string_49 = \"0THHqdl\" nocase wide ascii\n"
"      $rifle_sub_string_241 = \"BlTUT-HT_PI9TUTo-H8PoUTpl\" nocase wide ascii\n"
"      $rifle_sub_string_246 = \"FPU8U9TldCGXPO\" nocase wide ascii\n"
"      $rifle_sub_string_328 = \"FPUkpHwSPBlhp9S-UTplO\" nocase wide ascii\n"
"      $rifle_sub_string_288 = \"FPU8GvUPSCTSP\" nocase wide ascii\n"
"      $rifle_sub_string_289 = \"8GvUPSCTSPCp0THPCTSP\" nocase wide ascii\n"
"      $rifle_sub_string_284 = \"FPU19T2-UP19phTHP8U9TldO\" nocase wide ascii\n"
"      $rifle_sub_string_285 = \"6wHUTaGUPCpOTnPI7-9\" nocase wide ascii\n"
"      $rifle_sub_string_286 = \"FPU0THPcUU9TjwUPvO\" nocase wide ascii\n"
"      $rifle_sub_string_287 = \"HvU9oSXc\" nocase wide ascii\n"
"      $rifle_sub_string_280 = \"FPUkpHwSPBlhp9S-UTplc\" nocase wide ascii\n"
"      $rifle_sub_string_281 = \"HvU9oSXO\" nocase wide ascii\n"
"      $rifle_sub_string_282 = \"HvU9oXGc\" nocase wide ascii\n"
"      $rifle_sub_string_283 = \"HvU9o-Uc\" nocase wide ascii\n"
"      $rifle_sub_string_369 = \"FPUIw99PlU19poPvvBn\" nocase wide ascii\n"
"      $rifle_sub_string_368 = \"0Hwv70THPawhhP9v\" nocase wide ascii\n"
"      $rifle_sub_string_89 = \"OTlEUUXO9TUPL-U-\" nocase wide ascii\n"
"      $rifle_sub_string_88 = \"OTlEUUXbXPl\" nocase wide ascii\n"
"      $rifle_sub_string_85 = \"OTlEUUXFPU19pgG0p9A9H\" nocase wide ascii\n"
"      $rifle_sub_string_84 = \"OTlEUUXIpllPoU\" nocase wide ascii\n"
"      $rifle_sub_string_87 = \"OTlEUUX8PUbXUTpl\" nocase wide ascii\n"
"      $rifle_sub_string_86 = \"OTlEUUXcnnqP3wPvUEP-nP9v\" nocase wide ascii\n"
"      $rifle_sub_string_81 = \"OTlEUUXzwP9GEP-nP9v\" nocase wide ascii\n"
"      $rifle_sub_string_80 = \"OTlEUUXIHpvPE-lnHP\" nocase wide ascii\n"
"      $rifle_sub_string_83 = \"OTlEUUX8PUCTSPpwUv\" nocase wide ascii\n"
"      $rifle_sub_string_82 = \"OTlEUUXbXPlqP3wPvU\" nocase wide ascii\n"
"      $rifle_sub_string_18 = \"7Uplv\" nocase wide ascii\n"
"      $rifle_sub_string_19 = \"xxO8c0LBv8PU\" nocase wide ascii\n"
"      $rifle_sub_string_12 = \"dPU7pvUjGl-SP\" nocase wide ascii\n"
"      $rifle_sub_string_13 = \"lUp7H\" nocase wide ascii\n"
"      $rifle_sub_string_10 = \"O8cIHP-lwX\" nocase wide ascii\n"
"      $rifle_sub_string_11 = \"O8c8U-9UwX\" nocase wide ascii\n"
"      $rifle_sub_string_16 = \"TpoUHvpoRPU\" nocase wide ascii\n"
"      $rifle_sub_string_17 = \"vpoRPU\" nocase wide ascii\n"
"      $rifle_sub_string_14 = \"oHpvPvpoRPU\" nocase wide ascii\n"
"      $rifle_sub_string_15 = \"opllPoU\" nocase wide ascii\n"
"      $rifle_sub_string_217 = \"FPU0THPcUU9TjwUPvc\" nocase wide ascii\n"
"      $rifle_sub_string_216 = \"FPUCPSX1-U7O\" nocase wide ascii\n"
"      $rifle_sub_string_215 = \"FPUCPSX0THPu-SPO\" nocase wide ascii\n"
"      $rifle_sub_string_214 = \"FPU19poPvvCTSPv\" nocase wide ascii\n"
"      $rifle_sub_string_213 = \"0THPCTSPCpMpo-H0THPCTSP\" nocase wide ascii\n"
"      $rifle_sub_string_212 = \"FPUIpSXwUP9u-SPO\" nocase wide ascii\n"
"      $rifle_sub_string_211 = \"FPUIpSXwUP9u-SPc\" nocase wide ascii\n"
"      $rifle_sub_string_210 = \"8PUIw99PlULT9PoUp9GO\" nocase wide ascii\n"
"      $rifle_sub_string_219 = \"I9P-UP19poPvvO\" nocase wide ascii\n"
"      $rifle_sub_string_218 = \"FPUMpdTo-HL9T2Pv\" nocase wide ascii\n"
"      $rifle_sub_string_138 = \"CpAlTopnP\" nocase wide ascii\n"
"      $rifle_sub_string_139 = \"A8WqKf.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_373 = \"I9P-UP0THPO\" nocase wide ascii\n"
"      $rifle_sub_string_132 = \"LTvX-Uo76Pvv-dPc\" nocase wide ascii\n"
"      $rifle_sub_string_133 = \"C9-lvH-UP6Pvv-dP\" nocase wide ascii\n"
"      $rifle_sub_string_130 = \"FPU5PGu-SPCPgUO\" nocase wide ascii\n"
"      $rifle_sub_string_131 = \"Bl2-HTn-UPqPoU\" nocase wide ascii\n"
"      $rifle_sub_string_136 = \"FPUIH-vvu-SPO\" nocase wide ascii\n"
"      $rifle_sub_string_137 = \"WlwSI7THnOTlnprv\" nocase wide ascii\n"
"      $rifle_sub_string_134 = \"1PPR6Pvv-dPc\" nocase wide ascii\n"
"      $rifle_sub_string_135 = \"qPdTvUP9OTlnpr6Pvv-dPO\" nocase wide ascii\n"
"      $rifle_sub_string_350 = \"Mpo-H09PP\" nocase wide ascii\n"
"      $rifle_sub_string_312 = \"FPUMpld1-U7u-SPc\" nocase wide ascii\n"
"      $rifle_sub_string_313 = \"8PU0THPcUU9TjwUPvc\" nocase wide ascii\n"
"      $rifle_sub_string_259 = \"EP-X8T_P\" nocase wide ascii\n"
"      $rifle_sub_string_258 = \"kT9Uw-HzwP9G\" nocase wide ascii\n"
"      $rifle_sub_string_316 = \"kT9Uw-H09PPWg\" nocase wide ascii\n"
"      $rifle_sub_string_317 = \"WgX-lnWl2T9plSPlU8U9Tldvc\" nocase wide ascii\n"
"      $rifle_sub_string_314 = \"LPHPUP0THPc\" nocase wide ascii\n"
"      $rifle_sub_string_315 = \"FPU8GvUPSCTSPcv0THPCTSP\" nocase wide ascii\n"
"      $rifle_sub_string_253 = \"FPUWl2T9plSPlU8U9TldvO\" nocase wide ascii\n"
"      $rifle_sub_string_252 = \"09PPWl2T9plSPlU8U9TldvO\" nocase wide ascii\n"
"      $rifle_sub_string_318 = \"WgX-lnWl2T9plSPlU8U9TldvO\" nocase wide ascii\n"
"      $rifle_sub_string_319 = \"FPU87p9U1-U7u-SPO\" nocase wide ascii\n"
"      $rifle_sub_string_257 = \"8PUE-lnHPIpwlU\" nocase wide ascii\n"
"      $rifle_sub_string_256 = \"FPU0THPCGXP\" nocase wide ascii\n"
"      $rifle_sub_string_255 = \"FPU8U-9UwXBlhpc\" nocase wide ascii\n"
"      $rifle_sub_string_254 = \"09PPWl2T9plSPlU8U9Tldvc\" nocase wide ascii\n"
"      $rifle_sub_string_0 = \"TlAvP9cdPlU8U9Tld\" nocase wide ascii\n"
"      $rifle_sub_string_1 = \"AqM6bu.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_2 = \"BlUP9lPUI9-oRA9HO\" nocase wide ascii\n"
"      $rifle_sub_string_3 = \"BlUP9lPUI-lplTo-HT_PA9HO\" nocase wide ascii\n"
"      $rifle_sub_string_4 = \"OBuBuWC.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_5 = \"TlPUx-nn9\" nocase wide ascii\n"
"      $rifle_sub_string_6 = \"HTvUPl\" nocase wide ascii\n"
"      $rifle_sub_string_7 = \"jTln\" nocase wide ascii\n"
"      $rifle_sub_string_8 = \"-ooPXU\" nocase wide ascii\n"
"      $rifle_sub_string_9 = \"TlPUxlUp-\" nocase wide ascii\n"
"      $rifle_sub_string_23 = \"I9P-UPWl2T9plSPlUaHpoR\" nocase wide ascii\n"
"      $rifle_sub_string_22 = \"LPvU9pGWl2T9plSPlUaHpoR\" nocase wide ascii\n"
"      $rifle_sub_string_21 = \"O8fxKf.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_20 = \"vPHPoU\" nocase wide ascii\n"
"      $rifle_sub_string_27 = \"OC8c1BKf.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_26 = \"OC8WlwSP9-UP8PvvTplvO\" nocase wide ascii\n"
"      $rifle_sub_string_25 = \"OC809PP6PSp9G\" nocase wide ascii\n"
"      $rifle_sub_string_24 = \"A8WqWuk.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_29 = \"B1EM1c1B.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_28 = \"FPUcn-XUP9vBlhp\" nocase wide ascii\n"
"      $rifle_sub_string_351 = \"FPU6pnwHP0THPu-SPO\" nocase wide ascii\n"
"      $rifle_sub_string_178 = \"MppRwX19T2THPdPk-HwPc\" nocase wide ascii\n"
"      $rifle_sub_string_179 = \"bXPl19poPvvCpRPl\" nocase wide ascii\n"
"      $rifle_sub_string_176 = \"qPdbXPl5PGWgO\" nocase wide ascii\n"
"      $rifle_sub_string_177 = \"cnewvUCpRPl19T2THPdPv\" nocase wide ascii\n"
"      $rifle_sub_string_174 = \"qPdIHpvP5PG\" nocase wide ascii\n"
"      $rifle_sub_string_175 = \"qPdzwP9Gk-HwPWgO\" nocase wide ascii\n"
"      $rifle_sub_string_172 = \"Ipl2P9U8U9Tld8Pow9TUGLPvo9TXUp9Cp8Pow9TUGLPvo9TXUp9c\" nocase wide ascii\n"
"      $rifle_sub_string_173 = \"FPU8Pow9TUGLPvo9TXUp98-oH\" nocase wide ascii\n"
"      $rifle_sub_string_170 = \"BlTUT-HT_P8Pow9TUGLPvo9TXUp9\" nocase wide ascii\n"
"      $rifle_sub_string_171 = \"8PU8Pow9TUGLPvo9TXUp9L-oH\" nocase wide ascii\n"
"      $rifle_sub_string_356 = \"WgTU19poPvv\" nocase wide ascii\n"
"      $rifle_sub_string_357 = \"I9P-UP0THPc\" nocase wide ascii\n"
"      $rifle_sub_string_354 = \"FPUL9T2PCGXPc\" nocase wide ascii\n"
"      $rifle_sub_string_355 = \"FPUL9T2PCGXPO\" nocase wide ascii\n"
"      $rifle_sub_string_352 = \"FPU6pnwHP0THPu-SPc\" nocase wide ascii\n"
"      $rifle_sub_string_353 = \"qP-n0THP\" nocase wide ascii\n"
"      $rifle_sub_string_94 = \"OTlEUUXFPUBW19pgGIplhTd0p9Iw99PlUAvP9\" nocase wide ascii\n"
"      $rifle_sub_string_95 = \"OBuECC1.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_239 = \"WgTUC79P-n\" nocase wide ascii\n"
"      $rifle_sub_string_98 = \"B6cFWEM1.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_238 = \"WlUP9I9TUTo-H8PoUTpl\" nocase wide ascii\n"
"      $rifle_sub_string_92 = \"OTlEUUXqPoPT2PqPvXplvP\" nocase wide ascii\n"
"      $rifle_sub_string_93 = \"OTlEUUXqP-nL-U-\" nocase wide ascii\n"
"      $rifle_sub_string_90 = \"OTlEUUXzwP9GbXUTpl\" nocase wide ascii\n"
"      $rifle_sub_string_91 = \"OTlEUUX8PlnqP3wPvU\" nocase wide ascii\n"
"      $rifle_sub_string_96 = \"Al6-XclnMp-n\" nocase wide ascii\n"
"      $rifle_sub_string_97 = \"6-XclnMp-n\" nocase wide ascii\n"
"      $rifle_sub_string_299 = \"FPU0THPCTSP\" nocase wide ascii\n"
"      $rifle_sub_string_298 = \"FHpj-H09PP\" nocase wide ascii\n"
"      $rifle_sub_string_297 = \"Mp-nMTj9-9GWgc\" nocase wide ascii\n"
"      $rifle_sub_string_296 = \"FHpj-HcHHpo\" nocase wide ascii\n"
"      $rifle_sub_string_295 = \"LP2ToPBpIplU9pH\" nocase wide ascii\n"
"      $rifle_sub_string_294 = \"kT9Uw-H09PP\" nocase wide ascii\n"
"      $rifle_sub_string_293 = \"kT9Uw-H19pUPoUWg\" nocase wide ascii\n"
"      $rifle_sub_string_292 = \"O9TUP19poPvv6PSp9G\" nocase wide ascii\n"
"      $rifle_sub_string_291 = \"qP-n19poPvv6PSp9G\" nocase wide ascii\n"
"      $rifle_sub_string_290 = \"I9P-UPqPSpUPC79P-n\" nocase wide ascii\n"
"      $rifle_sub_string_358 = \"O9TUP0THP\" nocase wide ascii\n"
"      $rifle_sub_string_99 = \"rvX9TlUhc\" nocase wide ascii\n"
"      $rifle_sub_string_359 = \"I9P-UPLT9PoUp9GO\" nocase wide ascii\n"
"      $rifle_sub_string_231 = \"CHv09PP\" nocase wide ascii\n"
"      $rifle_sub_string_339 = \"FPU0THPBlhp9S-UTplaGE-lnHP\" nocase wide ascii\n"
"      $rifle_sub_string_194 = \"WlwS19poPvv6pnwHPv\" nocase wide ascii\n"
"      $rifle_sub_string_195 = \"FPU6pnwHP0THPu-SPWgO\" nocase wide ascii\n"
"      $rifle_sub_string_196 = \"WlwSLP2ToPL9T2P9v\" nocase wide ascii\n"
"      $rifle_sub_string_197 = \"FPULP2ToPL9T2P9a-vPu-SPO\" nocase wide ascii\n"
"      $rifle_sub_string_190 = \"qPdzwP9Gk-HwPWgc\" nocase wide ascii\n"
"      $rifle_sub_string_191 = \"qPdbXPl5PGc\" nocase wide ascii\n"
"      $rifle_sub_string_192 = \"8PU8Pow9TUGLPvo9TXUp98-oH\" nocase wide ascii\n"
"      $rifle_sub_string_193 = \"cLkc1BKf.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_198 = \"FPU6pnwHP0THPu-SPWgc\" nocase wide ascii\n"
"      $rifle_sub_string_199 = \"18c1B.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_54 = \"FLBKf.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_69 = \"STgP9IHpvP\" nocase wide ascii\n"
"      $rifle_sub_string_68 = \"STgP9FPULP2I-Xvc\" nocase wide ascii\n"
"      $rifle_sub_string_67 = \"STgP9FPUuwSLP2v\" nocase wide ascii\n"
"      $rifle_sub_string_66 = \"r-2PBlbXPl\" nocase wide ascii\n"
"      $rifle_sub_string_65 = \"STgP9bXPl\" nocase wide ascii\n"
"      $rifle_sub_string_64 = \"IqJ1CKf.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_63 = \"IP9U09PPIP9UThTo-UPIplUPgU\" nocase wide ascii\n"
"      $rifle_sub_string_62 = \"I9GXUAlX9pUPoUL-U-\" nocase wide ascii\n"
"      $rifle_sub_string_61 = \"bMWcII.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_60 = \"cooPvvTjHPI7THn9Pl\" nocase wide ascii\n"
"      $rifle_sub_string_222 = \"LPHPUP0THPO\" nocase wide ascii\n"
"      $rifle_sub_string_223 = \"FPU19poPvvEP-X\" nocase wide ascii\n"
"      $rifle_sub_string_220 = \"I9P-UP19poPvvc\" nocase wide ascii\n"
"      $rifle_sub_string_327 = \"Mp-nMTj9-9GO\" nocase wide ascii\n"
"      $rifle_sub_string_226 = \"FPUIplvpHPbwUXwUI1\" nocase wide ascii\n"
"      $rifle_sub_string_227 = \"O9TUPIplvpHPc\" nocase wide ascii\n"
"      $rifle_sub_string_224 = \"8PUWlnbh0THP\" nocase wide ascii\n"
"      $rifle_sub_string_225 = \"O9TUPIplvpHPO\" nocase wide ascii\n"
"      $rifle_sub_string_228 = \"8PU8UnE-lnHP\" nocase wide ascii\n"
"      $rifle_sub_string_229 = \"FHpj-HMpoR\" nocase wide ascii\n"
"      $rifle_sub_string_125 = \"BvOTlnpr\" nocase wide ascii\n"
"      $rifle_sub_string_124 = \"0TlnOTlnprWgO\" nocase wide ascii\n"
"      $rifle_sub_string_127 = \"bXPlIHTXjp-9n\" nocase wide ascii\n"
"      $rifle_sub_string_126 = \"WlwSOTlnprv\" nocase wide ascii\n"
"      $rifle_sub_string_121 = \"FPUOTlnprCPgUc\" nocase wide ascii\n"
"      $rifle_sub_string_120 = \"Mp-nBoplc\" nocase wide ascii\n"
"      $rifle_sub_string_123 = \"8Pln6Pvv-dPCTSPpwUO\" nocase wide ascii\n"
"      $rifle_sub_string_122 = \"FPUOTlnprCPgUO\" nocase wide ascii\n"
"      $rifle_sub_string_129 = \"IHpvPIHTXjp-9n\" nocase wide ascii\n"
"      $rifle_sub_string_128 = \"FPUIHTXjp-9nL-U-\" nocase wide ascii\n"
"      $rifle_sub_string_266 = \"q-TvPWgoPXUTpl\" nocase wide ascii\n"
"      $rifle_sub_string_267 = \"Al7-lnHPnWgoPXUTpl0THUP9\" nocase wide ascii\n"
"      $rifle_sub_string_264 = \"EP-X09PP\" nocase wide ascii\n"
"      $rifle_sub_string_265 = \"qUHAlrTln\" nocase wide ascii\n"
"      $rifle_sub_string_262 = \"EP-XqPcHHpo\" nocase wide ascii\n"
"      $rifle_sub_string_263 = \"EP-XcHHpo\" nocase wide ascii\n"
"      $rifle_sub_string_260 = \"MI6-X8U9TldO\" nocase wide ascii\n"
"      $rifle_sub_string_261 = \"MI6-X8U9Tldc\" nocase wide ascii\n"
"      $rifle_sub_string_268 = \"8PUAl7-lnHPnWgoPXUTpl0THUP9\" nocase wide ascii\n"
"      $rifle_sub_string_269 = \"FPUIw99PlUC79P-nBn\" nocase wide ascii\n"
"      $rifle_sub_string_309 = \"6p2P0THPWgc\" nocase wide ascii\n"
"      $rifle_sub_string_308 = \"6p2P0THPO\" nocase wide ascii\n"
"      $rifle_sub_string_305 = \"IpXG0THPc\" nocase wide ascii\n"
"      $rifle_sub_string_304 = \"0TlnuPgU0THPc\" nocase wide ascii\n"
"      $rifle_sub_string_307 = \"FHpj-HAlHpoR\" nocase wide ascii\n"
"      $rifle_sub_string_306 = \"bXPl0THP6-XXTldc\" nocase wide ascii\n"
"      $rifle_sub_string_301 = \"8PU0THP1pTlUP9Wg\" nocase wide ascii\n"
"      $rifle_sub_string_300 = \"BvLPjwddP919PvPlU\" nocase wide ascii\n"
"      $rifle_sub_string_303 = \"FPULTvR09PP8X-oPWgc\" nocase wide ascii\n"
"      $rifle_sub_string_302 = \"8PU0THP1pTlUP9\" nocase wide ascii\n"
"      $rifle_sub_string_30 = \"I9P-UP8U9P-SblEFHpj-H\" nocase wide ascii\n"
"      $rifle_sub_string_31 = \"bMWKf.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_32 = \"8EFPU8XPoT-H0pHnP91-U7O\" nocase wide ascii\n"
"      $rifle_sub_string_33 = \"8EWMMKf.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_34 = \"uPUcXTawhhP909PP\" nocase wide ascii\n"
"      $rifle_sub_string_35 = \"uPUAvP9FPUBlhp\" nocase wide ascii\n"
"      $rifle_sub_string_36 = \"uWCc1BKf.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_37 = \"LPHPUPLI\" nocase wide ascii\n"
"      $rifle_sub_string_38 = \"LPHPUPbjePoU\" nocase wide ascii\n"
"      $rifle_sub_string_39 = \"FPULBaTUv\" nocase wide ascii\n"
"      $rifle_sub_string_169 = \"IHpvPW2PlUMpd\" nocase wide ascii\n"
"      $rifle_sub_string_168 = \"bXPlW2PlUMpdc\" nocase wide ascii\n"
"      $rifle_sub_string_161 = \"I9P-UP8P92ToPO\" nocase wide ascii\n"
"      $rifle_sub_string_160 = \"I9P-UP8P92ToPc\" nocase wide ascii\n"
"      $rifle_sub_string_163 = \"bXPl8I6-l-dP9c\" nocase wide ascii\n"
"      $rifle_sub_string_162 = \"8U-9U8P92ToPc\" nocase wide ascii\n"
"      $rifle_sub_string_165 = \"qP-nW2PlUMpdc\" nocase wide ascii\n"
"      $rifle_sub_string_164 = \"IHpvP8P92ToPE-lnHP\" nocase wide ascii\n"
"      $rifle_sub_string_167 = \"FPUbHnPvUW2PlUMpdqPop9n\" nocase wide ascii\n"
"      $rifle_sub_string_166 = \"FPUuwSjP9bhW2PlUMpdqPop9nv\" nocase wide ascii\n"
"      $rifle_sub_string_118 = \"qPdTvUP9IH-vvWgc\" nocase wide ascii\n"
"      $rifle_sub_string_119 = \"Mp-nIw9vp9c\" nocase wide ascii\n"
"      $rifle_sub_string_114 = \"LPhOTlnpr19poc\" nocase wide ascii\n"
"      $rifle_sub_string_115 = \"AXn-UPOTlnpr\" nocase wide ascii\n"
"      $rifle_sub_string_116 = \"87prOTlnpr\" nocase wide ascii\n"
"      $rifle_sub_string_117 = \"I9P-UPOTlnprWgc\" nocase wide ascii\n"
"      $rifle_sub_string_110 = \"6Pvv-dPapgc\" nocase wide ascii\n"
"      $rifle_sub_string_111 = \"Wln1-TlU\" nocase wide ascii\n"
"      $rifle_sub_string_112 = \"FPUIHTPlUqPoU\" nocase wide ascii\n"
"      $rifle_sub_string_113 = \"aPdTl1-TlU\" nocase wide ascii\n"
"      $rifle_sub_string_341 = \"0Tln0T9vU0THPc\" nocase wide ascii\n"
"      $rifle_sub_string_340 = \"FPUWl2T9plSPlUk-9T-jHPc\" nocase wide ascii\n"
"      $rifle_sub_string_343 = \"I9P-UPCppH7PHXKf8l-Xv7pU\" nocase wide ascii\n"
"      $rifle_sub_string_342 = \"FPU19pocnn9Pvv\" nocase wide ascii\n"
"      $rifle_sub_string_345 = \"6pnwHPKf0T9vU\" nocase wide ascii\n"
"      $rifle_sub_string_344 = \"19poPvvKf0T9vU\" nocase wide ascii\n"
"      $rifle_sub_string_347 = \"19poPvvKfuPgU\" nocase wide ascii\n"
"      $rifle_sub_string_346 = \"6pnwHPKfuPgU\" nocase wide ascii\n"
"      $rifle_sub_string_349 = \"Mpo-HcHHpo\" nocase wide ascii\n"
"      $rifle_sub_string_348 = \"FPUM-vUW99p9\" nocase wide ascii\n"
"      $rifle_sub_string_55 = \"FPU0THPkP9vTplBlhpO\" nocase wide ascii\n"
"      $rifle_sub_string_187 = \"MppRwXcoopwlU8TnO\" nocase wide ascii\n"
"      $rifle_sub_string_186 = \"FPUAvP9u-SPc\" nocase wide ascii\n"
"      $rifle_sub_string_185 = \"qPdMp-n5PGO\" nocase wide ascii\n"
"      $rifle_sub_string_184 = \"qPdI9P-UP5PGO\" nocase wide ascii\n"
"      $rifle_sub_string_183 = \"qPd8PUk-HwPWgc\" nocase wide ascii\n"
"      $rifle_sub_string_182 = \"qPdAlMp-n5PGO\" nocase wide ascii\n"
"      $rifle_sub_string_181 = \"qPdbXPl5PGO\" nocase wide ascii\n"
"      $rifle_sub_string_180 = \"qPdWlwS5PGO\" nocase wide ascii\n"
"      $rifle_sub_string_189 = \"qPdzwP9GBlhp5PGc\" nocase wide ascii\n"
"      $rifle_sub_string_188 = \"qPdI9P-UP5PGc\" nocase wide ascii\n"
"      $rifle_sub_string_78 = \"8U9qI79c\" nocase wide ascii\n"
"      $rifle_sub_string_79 = \"8EMOc1B.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_74 = \"STgP9FPUIplU9pHLPU-THvc\" nocase wide ascii\n"
"      $rifle_sub_string_75 = \"STgP98PUIplU9pHLPU-THv\" nocase wide ascii\n"
"      $rifle_sub_string_76 = \"OBu66.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_77 = \"rlvX9TlUhO\" nocase wide ascii\n"
"      $rifle_sub_string_70 = \"r-2PBlqPvPU\" nocase wide ascii\n"
"      $rifle_sub_string_71 = \"r-2PBlIHpvP\" nocase wide ascii\n"
"      $rifle_sub_string_72 = \"STgP9FPUMTlPBlhpc\" nocase wide ascii\n"
"      $rifle_sub_string_73 = \"STgP9FPUMTlPIplU9pHvc\" nocase wide ascii\n"
"      $rifle_sub_string_334 = \"FPUIw99PlU19poPvv\" nocase wide ascii\n"
"      $rifle_sub_string_335 = \"09PPMTj9-9G\" nocase wide ascii\n"
"      $rifle_sub_string_336 = \"19poPvvKf0T9vUO\" nocase wide ascii\n"
"      $rifle_sub_string_337 = \"19poPvvKfuPgUO\" nocase wide ascii\n"
"      $rifle_sub_string_330 = \"FPU8GvUPSBlhp\" nocase wide ascii\n"
"      $rifle_sub_string_331 = \"FHpj-H6PSp9G8U-UwvWg\" nocase wide ascii\n"
"      $rifle_sub_string_332 = \"FPUMpo-HPBlhpO\" nocase wide ascii\n"
"      $rifle_sub_string_333 = \"FPULTvR09PP8X-oPWgO\" nocase wide ascii\n"
"      $rifle_sub_string_235 = \"FPUbW6I1\" nocase wide ascii\n"
"      $rifle_sub_string_234 = \"Bvk-HTnIpnP1-dP\" nocase wide ascii\n"
"      $rifle_sub_string_237 = \"MP-2PI9TUTo-H8PoUTpl\" nocase wide ascii\n"
"      $rifle_sub_string_236 = \"FPUcI1\" nocase wide ascii\n"
"      $rifle_sub_string_338 = \"Mp-nMTj9-9Gc\" nocase wide ascii\n"
"      $rifle_sub_string_230 = \"CHv8PUk-HwP\" nocase wide ascii\n"
"      $rifle_sub_string_233 = \"CHvFPUk-HwP\" nocase wide ascii\n"
"      $rifle_sub_string_232 = \"CHvcHHpo\" nocase wide ascii\n"
"      $rifle_sub_string_56 = \"FPU0THPkP9vTplBlhp8T_PO\" nocase wide ascii\n"
"      $rifle_sub_string_57 = \"kP9zwP9Gk-HwPO\" nocase wide ascii\n"
"      $rifle_sub_string_310 = \"FPUIpSS-lnMTlPc\" nocase wide ascii\n"
"      $rifle_sub_string_311 = \"FPUIpSS-lnMTlPO\" nocase wide ascii\n"
"      $rifle_sub_string_52 = \"8PULBaTUv\" nocase wide ascii\n"
"      $rifle_sub_string_53 = \"I9P-UPLIc\" nocase wide ascii\n"
"      $rifle_sub_string_50 = \"I9P-UP8pHTna9wv7\" nocase wide ascii\n"
"      $rifle_sub_string_51 = \"I9P-UPqPoUqdl\" nocase wide ascii\n"
"      $rifle_sub_string_150 = \"FPUAvP9u-SPO\" nocase wide ascii\n"
"      $rifle_sub_string_151 = \"qPd8PUk-HwPWgO\" nocase wide ascii\n"
"      $rifle_sub_string_152 = \"Ipl2P9U8TnCp8U9Tld8TnO\" nocase wide ascii\n"
"      $rifle_sub_string_153 = \"FPUCpRPlBlhp9S-UTpl\" nocase wide ascii\n"
"      $rifle_sub_string_154 = \"FPU8Tn8wjcwU7p9TUGIpwlU\" nocase wide ascii\n"
"      $rifle_sub_string_155 = \"FPU8Tn8wjcwU7p9TUG\" nocase wide ascii\n"
"      $rifle_sub_string_156 = \"qPdLPHPUPk-HwPc\" nocase wide ascii\n"
"      $rifle_sub_string_157 = \"qPdWlwS5PGWgc\" nocase wide ascii\n"
"      $rifle_sub_string_158 = \"qPdWlwSk-HwPc\" nocase wide ascii\n"
"      $rifle_sub_string_159 = \"qPdbXPl5PGWgc\" nocase wide ascii\n"
"      $rifle_sub_string_251 = \"zwP9G1P9hp9S-loPIpwlUP9\" nocase wide ascii\n"
"      $rifle_sub_string_250 = \"BlTUT-HT_PI9TUTo-H8PoUTplcln8XTlIpwlU\" nocase wide ascii\n"
"      $rifle_sub_string_58 = \"kWq8Bbu.LMM\" nocase wide ascii\n"
"      $rifle_sub_string_59 = \"cooPvvTjHPbjePoU09pSOTlnpr\" nocase wide ascii\n"
"      /*\n"
"        mov     [ebp+var_44], 5867637Ah\n"
"        mov     [ebp+var_40], 6B57536Ch\n"
"        mov     [ebp+var_3C], 3431336Ah\n"
"        mov     [ebp+var_38], 59617743h\n"
"        mov     [ebp+var_34], 6879764Ch\n"
"        mov     [ebp+var_30], 6F5F5530h\n"
"        mov     [ebp+var_2C], 38485A64h\n"
"        mov     [ebp+var_28], 4B65524Fh\n"
"        mov     [ebp+var_24], 72494E69h\n"
"        mov     [ebp+var_20], 324D4A2Dh\n"
"        mov     [ebp+var_1C], 41513747h\n"
"        mov     [ebp+var_18], 6D6E7078h\n"
"        mov     [ebp+var_14], 71625645h\n"
"        mov     [ebp+var_10], 75543550h\n"
"        mov     [ebp+var_C], 73443942h\n"
"        mov     [ebp+var_8], 74466636h\n"
"      */\n"
"      /*\n"
"      $sub_string_key = {C7 45 ?? 7A 63 67 58 C7 45 ?? 6C 53 57 6B C7 45 \n"
"                        ?? 6A 33 31 34 C7 45 ?? 43 77 61 59 C7 45 ?? 4C \n"
"                        76 79 68 C7 45 ?? 30 55 5F 6F C7 45 ?? 64 5A 48 \n"
"                        38 C7 45 ?? 4F 52 65 4B C7 45 ?? 69 4E 49 72 C7 \n"
"                        45 ?? 2D 4A 4D 32 C7 45 ?? 47 37 51 41 C7 45 ?? \n"
"                        78 70 6E 6D C7 45 ?? 45 56 62 71 C7 45 ?? 50 35 \n"
"                        54 75 C7 45 ?? 42 39 44 73 C7 45 ?? 36 66 46 74}\n"
"      */\n"
"  condition:\n"
"      10 of ($rifle*) /* and $sub_string_key */\n"
"}\n"
"\n"
"rule ahnlab_andarat /* ghost RAT */\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.6\"\n"
"      date = \"2018-11-09\"\n"
"      MD5 = \"1590E1EC0CE053F58BC349B4A5A9E7AD\"\n"
"  strings:\n"
"      $test_5 = \"Y Failed!\" nocase wide ascii\n"
"      $test_4 = \"X Failed!\" nocase wide ascii\n"
"      $test_3 = \"%s_%s\" nocase wide ascii\n"
"      $test_2 = \"%s\" nocase wide ascii\n"
"      $test_1 = \"Execute Success!\" nocase wide ascii\n"
"      $test_0 = \"do not Execute!\" nocase wide ascii\n"
"  condition:\n"
"      4 of them\n"
"}\n"
"\n"
"rule ahnlab_bmbot\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.6\"\n"
"      date = \"2018-11-09\"\n"
"      MD5 = \"EE5D1522845628A2F7B3A4E568F0989D\"\n"
"  strings:\n"
"      $test_7 = \"Upload:No path\" nocase wide ascii\n"
"      $test_6 = \"upload \" nocase wide ascii\n"
"      $test_5 = \"Download fail\" nocase wide ascii\n"
"      $test_4 = \"Execution fail\" nocase wide ascii\n"
"      $test_3 = \"Downloadexec success\" nocase wide ascii\n"
"      $test_2 = \"hkInit.exe\" nocase wide ascii\n"
"      $test_1 = \"DownloadExec:No URL\" nocase wide ascii\n"
"      $test_0 = \"downloadexec \" nocase wide ascii\n"
"      $test_9 = \"Upload Fail\" nocase wide ascii\n"
"      $test_8 = \"Upload Success\" nocase wide ascii\n"
"      $a = \"User-Agent:Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)\" nocase ascii wide\n"
"  condition:\n"
"      5 of them\n"
"}\n"
"\n"
"rule ahnlab_gamedoor\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.6\"\n"
"      date = \"2018-11-09\"\n"
"      MD5 = \"804539F27FC2AE9322DD57B0FE854FF8\"\n"
"  strings:\n"
"      $ahnlab_gamedoor_5 = \"hangame\\\\korean\\\\baduki.exe\" nocase wide ascii\n"
"      $ahnlab_gamedoor_4 = \"grandgameh\\\\poker\\\\poker.exe\" nocase wide ascii\n"
"      $ahnlab_gamedoor_7 = \"hangame\\\\korean\\\\highlow2.exe\" nocase wide ascii\n"
"      $ahnlab_gamedoor_6 = \"hangame\\\\korean\\\\poker7.exe\" nocase wide ascii\n"
"      $ahnlab_gamedoor_1 = \"neowiz\\\\pmang\\\\common\\\\pmlauncher.exe\" nocase wide ascii\n"
"      $ahnlab_gamedoor_0 = \"impactgame\\\\poker\\\\poker.exe\" nocase wide ascii\n"
"      $ahnlab_gamedoor_3 = \"grandgamej\\\\poker\\\\poker.exe\" nocase wide ascii\n"
"      $ahnlab_gamedoor_2 = \"grandgame\\\\poker\\\\poker.exe\" nocase wide ascii\n"
"      $ahnlab_gamedoor_9 = \"hangame\\\\korean\\\\hoola3.exe\" nocase wide ascii\n"
"      $ahnlab_gamedoor_8 = \"hangame\\\\korean\\\\laspoker.exe\" nocase wide ascii\n"
"  condition:\n"
"      3 of them\n"
"}\n"
"\n"
"rule ahnlab_phandoor : phandoor\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.6\"\n"
"      date = \"2018-11-09\"\n"
"      MD5 = \"30D48797B308CC82336A411CAC34E977\"\n"
"  strings:\n"
"      $ahnlab_phandoor_0 = \"ttt23446654\" nocase wide ascii\n"
"      $ahnlab_phandoor_1 = \"Command is [%s]\" nocase wide ascii\n"
"      $ahnlab_phandoor_2 = \"No Server !\" nocase wide ascii\n"
"      $ahnlab_phandoor_3 = \"Server found\" nocase wide ascii\n"
"      $ahnlab_phandoor_4 = \"communication is started !\" nocase wide ascii\n"
"      $ahnlab_phandoor_5 = \"Disconnected from Controller !\" nocase wide ascii\n"
"  condition:\n"
"      3 of them\n"
"}\n"
"\n"
"rule ahnlab_rifdoor_NkDoor\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.6\"\n"
"      date = \"2018-11-09\"\n"
"      MD5 = \"AA7EFE70926B114403690F1A11A6229D (rifdoor)\"\n"
"      MD5 = \"AA3FF3587F22E7E660765621185F8D8E (NkDoor)\"\n"
"  strings:\n"
"      $ahnlab_rifdoor_14 = \"_]@LJ\\\\\\\\JK/N[\" nocase wide ascii\n"
"      $ahnlab_rifdoor_9 = \"K`xac`nk/|zllj||\" nocase wide ascii\n"
"      $ahnlab_rifdoor_8 = \"K`xac`nk/infcz}j\" nocase wide ascii\n"
"      $ahnlab_rifdoor_2 = \"MzfckHZFK\" nocase wide ascii\n"
"      $ahnlab_rifdoor_1 = \"_}`kzl{Fk\" nocase wide ascii\n"
"      $ahnlab_rifdoor_0 = \"\\\\`i{xn}jSBfl}`|`i{SXfak`x|/A[SLz}}ja{Yj}|f`a\" nocase wide ascii\n"
"      $ahnlab_rifdoor_7 = \"+k`xac`nkjwjl\" nocase wide ascii\n"
"      $ahnlab_rifdoor_6 = \"Fa{j}ync/f|/|j{/{`\" nocase wide ascii\n"
"      $ahnlab_rifdoor_5 = \"+fa{j}ync\" nocase wide ascii\n"
"      $ahnlab_rifdoor_4 = \"L5Sxfak`x|S|v|{jb<=Slbk!jwj\" nocase wide ascii\n"
"      $ahnlab_rifdoor_11 = \"Jwjlz{f`a/|zllj||\" nocase wide ascii\n"
"      $ahnlab_rifdoor_10 = \"Jwjlz{f`a/infcz}j\" nocase wide ascii\n"
"      $ahnlab_rifdoor_12 = \"+jwjl\" nocase wide ascii\n"
"      $ahnlab_rifdoor_13 = \"+k`xac`nk\" nocase wide ascii\n"
"\n"
"      $ahnlab_NkDoor_1 = \"KjcnvZkn{j!jwj\" nocase wide ascii\n"
"      $ahnlab_NkDoor_2 = \"Bfl}`|`i{\" nocase wide ascii\n"
"      $ahnlab_NkDoor_3 = \"Xfak`x|/Zkn{j\" nocase wide ascii\n"
"      $ahnlab_NkDoor_4 = \"\\\\`i{xn}jSBfl}`|`i{SXfak`x|SLz}}ja{Yj}|f`aS]za\" nocase wide ascii\n"
"      $ahnlab_NkDoor_5 = \"Zkn{j/_`cflv\" nocase wide ascii\n"
"  condition:\n"
"      4 of them\n"
"}\n"
"\n"
"rule ahnlab_nctst\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.6\"\n"
"      date = \"2018-11-09\"\n"
"      MD5 = \"8E79D88915C1E8978FA4F5C6BE1C9382\"\n"
"  strings:\n"
"      $ahnlab_nctst_0 = \"Current : %d year %d month %d day\" nocase wide ascii\n"
"      $ahnlab_nctst_1 = \"Setting : %d year %d month %d day\" nocase wide ascii\n"
"  condition:\n"
"      all of them\n"
"}\n"
"\n"
"rule ahnlab_nctst_582D70C0\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.6\"\n"
"      date = \"2018-11-09\"\n"
"      MD5 = \"56472258696067B7717F011DEA5716BD\"\n"
"  strings:\n"
"      $test_5 = \"del \\\"%s\\\"\" nocase wide ascii\n"
"      $test_4 = \"attrib -h \\\"%s\\\"\" nocase wide ascii\n"
"      $test_3 = \"if exist \\\"%s\\\" goto Repeat\" nocase wide ascii\n"
"      $test_2 = \"del \\\"%s\\\"\" nocase wide ascii\n"
"      $test_1 = \"sleep 1\" nocase wide ascii\n"
"      $test_0 = \":Repeat\" nocase wide ascii\n"
"  condition:\n"
"      all of them\n"
"}\n"
"\n"
"rule ahnlab_NkDoor_Rifdoor\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.6\"\n"
"      date = \"2018-11-09\"\n"
"      MD5 = \"AA3FF3587F22E7E660765621185F8D8E\"\n"
"  strings:\n"
"      $ahnlab_NkDoor_4 = \"+fa{j}ync\" nocase wide ascii\n"
"      $ahnlab_NkDoor_5 = \"Fa{j}ync/f|/|j{/{`\" nocase wide ascii\n"
"      $ahnlab_NkDoor_6 = \"+k`xac`nkjwjl\" nocase wide ascii\n"
"      $ahnlab_NkDoor_7 = \"K`xac`nk/infcz}j\" nocase wide ascii\n"
"      $ahnlab_NkDoor_0 = \"\\\\`i{xn}jSBfl}`|`i{SXfak`x|/A[SLz}}ja{Yj}|f`a\" nocase wide ascii\n"
"      $ahnlab_NkDoor_1 = \"_}`kzl{Fk\" nocase wide ascii\n"
"      $ahnlab_NkDoor_2 = \"MzfckHZFK\" nocase wide ascii\n"
"      $ahnlab_NkDoor_3 = \"L5Sxfak`x|S|v|{jb<=Slbk!jwj\" nocase wide ascii\n"
"      $ahnlab_NkDoor_8 = \"K`xac`nk/|zllj||\" nocase wide ascii\n"
"      $ahnlab_NkDoor_9 = \"Jwjlz{f`a/infcz}j\" nocase wide ascii\n"
"      $ahnlab_NkDoor_18 = \"KjcnvZkn{j!jwj\" nocase wide ascii\n"
"      $ahnlab_NkDoor_16 = \"Bfl}`|`i{\" nocase wide ascii\n"
"      $ahnlab_NkDoor_17 = \"Xfak`x|/Zkn{j\" nocase wide ascii\n"
"      $ahnlab_NkDoor_14 = \"\\\\`i{xn}jSBfl}`|`i{SXfak`x|SLz}}ja{Yj}|f`aS]za\" nocase wide ascii\n"
"      $ahnlab_NkDoor_15 = \"Zkn{j/_`cflv\" nocase wide ascii\n"
"      $ahnlab_NkDoor_12 = \"+k`xac`nk\" nocase wide ascii\n"
"      $ahnlab_NkDoor_13 = \"_]@LJ\\\\\\\\JK/N[\" nocase wide ascii\n"
"      $ahnlab_NkDoor_10 = \"Jwjlz{f`a/|zllj||\" nocase wide ascii\n"
"      $ahnlab_NkDoor_11 = \"+jwjl\" nocase wide ascii\n"
"  condition:\n"
"      4 of them\n"
"}\n"
"\n"
"import \"hash\"\n"
"import \"pe\"\n"
"\n"
"rule ahnlab_ratankba\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.6\"\n"
"      date = \"2018-11-09\"\n"
"      MD5 = \"1F7897B041A812F96F1925138EA38C46\"\n"
"  strings:\n"
"      $ahnlab_ratankba_13 = \"%s?action=What&u=%I64u\" nocase wide ascii\n"
"      $ahnlab_rantakba_14 = \"%s?action=BaseInfo&u=%I64u\" nocase wide ascii\n"
"      /* $ahnlab_ratankba_12 = \"https://www.eye-watch.in/design/dfbox/list.jsp\" nocase wide ascii */\n"
"      $ahnlab_ratankba_11 = \"cmd.exe /c \\\"netstat -ano | find \\\"TCP\\\" >> %s\\\"\" nocase wide ascii\n"
"      $ahnlab_ratankba_10 = \"cmd.exe /c \\\"tasklist /svc >> %s\\\"\" nocase wide ascii\n"
"      $ahnlab_ratankba_9 = \"cmd.exe /c \\\"reg query \\\"HKCU\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Internet Settings\\\" >> %s\\\"\" nocase wide ascii\n"
"      $ahnlab_ratankba_8 = \"cmd.exe /c \\\"net view /domain >> %s\\\"\" nocase wide ascii\n"
"      $ahnlab_ratankba_7 = \"cmd.exe /c \\\"net view >> %s\\\"\" nocase wide ascii\n"
"      $ahnlab_ratankba_6 = \"cmd.exe /c \\\"net user >> %s\\\"\" nocase wide ascii\n"
"      $ahnlab_ratankba_5 = \"cmd.exe /c \\\"query user >> %s\\\"\" nocase wide ascii\n"
"      $ahnlab_ratankba_4 = \"cmd.exe /c \\\"ping www.google.com >> %s\\\"\" nocase wide ascii\n"
"      $ahnlab_ratankba_3 = \"cmd.exe /c \\\"ipconfig -all >> %s\\\"\" nocase wide ascii\n"
"      $ahnlab_ratankba_2 = \"cmd.exe /c \\\"ver >> %s\\\"\" nocase wide ascii\n"
"      $ahnlab_ratankba_1 = \"cmd.exe /c \\\"whoami >> %s\\\"\" nocase wide ascii\n"
"      $ahnlab_ratankba_0 = \"cmd.exe /c \\\"hostname > %s\\\"\" nocase wide ascii\n"
"  condition:\n"
"      7 of them\n"
"}\n"
"\n"
"rule ahnlab_PyAgent\n"
"{\n"
"  meta:\n"
"      tool = \"https://github.com/hy00un/Hyara\"\n"
"      version = \"1.6\"\n"
"      date = \"2018-11-09\"\n"
"      MD5 = \"A597F7B62B2F491E75DDECE06BCD8068\"\n"
"  strings:\n"
"      $ahnlab_PyAgent_28 = \"Pyeongchang2018.com\\\\pcadmin\" nocase wide ascii\n"
"      $ahnlab_PyAgent_23 = \"vudckd1qaz@WSX\" nocase wide ascii\n"
"      $ahnlab_PyAgent_22 = \"Pyeongchang2018.com\\\\pca.infradmin\" nocase wide ascii\n"
"      $ahnlab_PyAgent_21 = \"qwe123!@#\" nocase wide ascii\n"
"      $ahnlab_PyAgent_20 = \"Pyeongchang2018.com\\\\jinsik.park\" nocase wide ascii\n"
"      $ahnlab_PyAgent_27 = \"pc20181234!\" nocase wide ascii\n"
"      $ahnlab_PyAgent_26 = \"Pyeongchang2018.com\\\\PCA.OMEGAdmin\" nocase wide ascii\n"
"      $ahnlab_PyAgent_25 = \"kas!QAZ@WSX#EDC\" nocase wide ascii\n"
"      $ahnlab_PyAgent_24 = \"Pyeongchang2018.com\\\\PCA.KASAdmin\" nocase wide ascii\n"
"      $ahnlab_PyAgent_4 = \"Pyeongchang2018.com\\\\cert01\" nocase wide ascii\n"
"      $ahnlab_PyAgent_5 = \"C462!qwer\" nocase wide ascii\n"
"      $ahnlab_PyAgent_6 = \"g18.internal\\\\minadmev\" nocase wide ascii\n"
"      $ahnlab_PyAgent_7 = \"BME.2010\" nocase wide ascii\n"
"      $ahnlab_PyAgent_0 = \"Pyeongchang2018.com\\\\pcadmin\" nocase wide ascii\n"
"      $ahnlab_PyAgent_1 = \"vudckd2018!@\" nocase wide ascii\n"
"      $ahnlab_PyAgent_2 = \"Pyeongchang2018.com\\\\PCA.GMSAdmin\" nocase wide ascii\n"
"      $ahnlab_PyAgent_3 = \"gms1qaz@WSX\" nocase wide ascii\n"
"      $ahnlab_PyAgent_8 = \"g18.internal\\\\adm.adam.wollman\" nocase wide ascii\n"
"      $ahnlab_PyAgent_9 = \"Temporal.1\" nocase wide ascii\n"
"      $ahnlab_PyAgent_18 = \"Pyeongchang2018.com\\\\addc.siem\" nocase wide ascii\n"
"      $ahnlab_PyAgent_19 = \"zse!@#123\" nocase wide ascii\n"
"      $ahnlab_PyAgent_16 = \"Pyeongchang2018.com\\\\PCA.SMSAdmin\" nocase wide ascii\n"
"      $ahnlab_PyAgent_17 = \"vudckd2018!\" nocase wide ascii\n"
"      $ahnlab_PyAgent_14 = \"Pyeongchang2018.com\\\\PCA.lyncadmintest\" nocase wide ascii\n"
"      $ahnlab_PyAgent_15 = \"lync!QAZ@WSX#EDC\" nocase wide ascii\n"
"      $ahnlab_PyAgent_12 = \"Pyeongchang2018.com\\\\PCA.lyncadmin\" nocase wide ascii\n"
"      $ahnlab_PyAgent_13 = \"lync!QAZ@WSX#EDC\" nocase wide ascii\n"
"      $ahnlab_PyAgent_10 = \"g18.internal\\\\adm.vadim.antonenko\" nocase wide ascii\n"
"      $ahnlab_PyAgent_11 = \"G@h0km132\" nocase wide ascii\n"
"  condition:\n"
"      5 of them\n"
"}"))
        self.label_4.setText(self._translate("Dialog", "Path Setting"))
        self.lineEdit_2.setText(self._translate("Dialog", ""))
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
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

