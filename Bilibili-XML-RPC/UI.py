# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 689)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/images/cartoon3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 15, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray; \n"
"border-style: outset;")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(-1, 30, -1, -1)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray; \n"
"border-style: outset;")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.webaddress = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webaddress.sizePolicy().hasHeightForWidth())
        self.webaddress.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.webaddress.setFont(font)
        self.webaddress.setObjectName("webaddress")
        self.horizontalLayout.addWidget(self.webaddress)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.openbutton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openbutton.sizePolicy().hasHeightForWidth())
        self.openbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.openbutton.setFont(font)
        self.openbutton.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray; \n"
"border-style: outset;")
        self.openbutton.setObjectName("openbutton")
        self.horizontalLayout_4.addWidget(self.openbutton)
        self.dir = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dir.sizePolicy().hasHeightForWidth())
        self.dir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dir.setFont(font)
        self.dir.setObjectName("dir")
        self.horizontalLayout_4.addWidget(self.dir)
        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fetchbutton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fetchbutton.sizePolicy().hasHeightForWidth())
        self.fetchbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fetchbutton.setFont(font)
        self.fetchbutton.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray; \n"
"border-style: outset;")
        self.fetchbutton.setObjectName("fetchbutton")
        self.horizontalLayout_3.addWidget(self.fetchbutton)
        self.filename = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filename.sizePolicy().hasHeightForWidth())
        self.filename.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filename.setFont(font)
        self.filename.setText("")
        self.filename.setObjectName("filename")
        self.horizontalLayout_3.addWidget(self.filename)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray; \n"
"border-style: outset;")
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.tips = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tips.sizePolicy().hasHeightForWidth())
        self.tips.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tips.setFont(font)
        self.tips.setObjectName("tips")
        self.horizontalLayout_2.addWidget(self.tips)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.filelistView = QtWidgets.QListView(self.groupBox)
        self.filelistView.setObjectName("filelistView")
        self.verticalLayout.addWidget(self.filelistView)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 7)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 26))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.about = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("cute")
        self.about.setIcon(icon)
        self.about.setObjectName("about")
        self.menuEdit.addAction(self.about)
        self.menuEdit.addSeparator()
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.openbutton.clicked.connect(MainWindow.open)
        self.fetchbutton.clicked.connect(MainWindow.fetch)
        self.about.triggered.connect(MainWindow.aboutthis)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于XML-RPC文件共享"))
        self.groupBox.setTitle(_translate("MainWindow", "基本设置"))
        self.label.setText(_translate("MainWindow", "节点地址"))
        self.webaddress.setText(_translate("MainWindow", "http://127.0.0.1:8001"))
        self.openbutton.setText(_translate("MainWindow", "浏览"))
        self.dir.setPlaceholderText(_translate("MainWindow", "将显示您所选择的文件夹..."))
        self.fetchbutton.setText(_translate("MainWindow", "获取文件"))
        self.filename.setPlaceholderText(_translate("MainWindow", "请输入文件名..."))
        self.label_2.setText(_translate("MainWindow", "提示："))
        self.tips.setPlaceholderText(_translate("MainWindow", "将显示提示..."))
        self.label_3.setText(_translate("MainWindow", " 文件列表"))
        self.menuEdit.setTitle(_translate("MainWindow", "帮助"))
        self.about.setText(_translate("MainWindow", "关于"))
import apprcc2_rc
