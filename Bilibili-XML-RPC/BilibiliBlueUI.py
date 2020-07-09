# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BilibiliBlueUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 980)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("CN_bilibili-蓝色.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 230, 501, 601))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.groupBox.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.groupBox.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray; \n"
"border-style: outset;\n"
"\n"
"background-color: rgba(255,255,255,0.6);\n"
"\n"
"")
        self.groupBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(-1, 30, -1, -1)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nodelabel = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodelabel.sizePolicy().hasHeightForWidth())
        self.nodelabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nodelabel.setFont(font)
        self.nodelabel.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray; \n"
"border-style: outset;")
        self.nodelabel.setFrameShape(QtWidgets.QFrame.Box)
        self.nodelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nodelabel.setIndent(-1)
        self.nodelabel.setObjectName("nodelabel")
        self.horizontalLayout.addWidget(self.nodelabel)
        self.webaddress = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webaddress.sizePolicy().hasHeightForWidth())
        self.webaddress.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.webaddress.setFont(font)
        self.webaddress.setMouseTracking(False)
        self.webaddress.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.webaddress.setStyleSheet("")
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
        self.dir.setStyleSheet("")
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
        self.filename.setStyleSheet("")
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
        self.tips.setStyleSheet("")
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
        self.filelistView.setStyleSheet("\n"
"background-color: rgba(255, 255, 255,0.3);")
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -10, 541, 941))
        self.label.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label.setStyleSheet("border-radius: 10px;  \n"
"border-style: outset;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("CN_bilibili-蓝色.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 580, 341, 281))
        self.label_4.setText("")
        #self.label_4.setPixmap(QtGui.QPixmap("小电视跳动.gif"))
        self.gif=QtGui.QMovie("小电视跳动.gif")

        self.label_4.setMovie(self.gif)
        self.gif.start()
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label.raise_()
        self.groupBox.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.about = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("cute")
        self.about.setIcon(icon)
        self.about.setObjectName("about")
        self.closeui = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("关  闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeui.setIcon(icon1)
        self.closeui.setObjectName("closeui")
        self.ontop = QtWidgets.QAction(MainWindow)
        self.ontop.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("固定.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ontop.setIcon(icon2)
        self.ontop.setObjectName("ontop")

        self.retranslateUi(MainWindow)
        self.openbutton.clicked.connect(MainWindow.open)
        self.fetchbutton.clicked.connect(MainWindow.fetch)
        self.about.triggered.connect(MainWindow.aboutthis)
        self.closeui.triggered['bool'].connect(MainWindow.close)
        self.ontop.triggered['bool'].connect(MainWindow.WinOnTop)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基于XML-RPC文件共享"))
        self.groupBox.setTitle(_translate("MainWindow", "基本设置"))
        self.nodelabel.setText(_translate("MainWindow", "节点地址"))
        self.webaddress.setText(_translate("MainWindow", "http://127.0.0.1:8001"))
        self.openbutton.setText(_translate("MainWindow", "浏览"))
        self.dir.setPlaceholderText(_translate("MainWindow", "将显示您所选择的文件夹..."))
        self.fetchbutton.setText(_translate("MainWindow", "获取文件"))
        self.filename.setPlaceholderText(_translate("MainWindow", "请输入文件名..."))
        self.label_2.setText(_translate("MainWindow", "提示："))
        self.tips.setPlaceholderText(_translate("MainWindow", "将显示提示..."))
        self.label_3.setText(_translate("MainWindow", " 文件列表"))
        self.about.setText(_translate("MainWindow", "关于"))
        self.closeui.setText(_translate("MainWindow", "关闭"))
        self.ontop.setText(_translate("MainWindow", "置顶"))
import apprcc2_rc
