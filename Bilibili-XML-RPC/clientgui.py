from PyQt5.QtWidgets import  QLabel  ,QWidget, QMainWindow,QApplication,QMessageBox
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QFileDialog,QListView  #必须导入，否则会出错 -1073740791 (0xC0000409)
from UI import Ui_MainWindow # 【UI】指的是UI文件的文件名
from os import path,listdir
from server import Node, UNHANDLED  # 向RPC Server调用方法,并接收方法的返回数据;
from client import random_string
from threading import Thread
from time import sleep
from xmlrpc.client import ServerProxy, Fault
import sys

HEAD_START = 0.1  # Seconds
SECRET_LENGTH = 100

class ListableNode(Node):  #从Node派生出子类，从而新增一个方法

    def list(self):
        return listdir(self.dirname)

class PyQtLogic(QMainWindow, Ui_MainWindow):  #构造函数，QMainWindows来自于 from
    def __init__(self):
        super(PyQtLogic,self).__init__()  # #首先找到子类（my转成QWidget的对象，然后被转化的self调用自己的init函数
        self.setupUi(self)   # #直接继承界面类，调用类的setupUi方法

    def aboutthis(self):
        QMessageBox.about(self, '关于本程序', '基于XML-RPC的p2p共享程序')
    def open(self):  #浏览 槽函数
		dirname=QFileDialog.getExistingDirectory(self,'打开文件夹','C:\\Users\\wdther\\Desktop\\XML-RPC')  #需要用到转义字符 \ 因此要用 \\双斜杠
        file1 = dirname + '\\urlfile.txt'
        self.dir.setText(file1)
        url = self.webaddress.text()
        self.tips.setText("网址已获取" + url)
		urlfile=file1
		self.node_setup(url, dirname, urlfile)
        self.update_list() #疑惑为什么调用这个函数

    def fetch(self):
        query = self.filename.text()
        print(query)
        try:
            self.server.fetch(query, self.secret)
            self.update_list()
        except Fault as f:
            if f.faultCode != UNHANDLED: raise
            print("Couldn't find the file", query)

    def node_setup(self, url, dirname, urlfile):
        self.secret = random_string(SECRET_LENGTH)
        n = ListableNode(url, dirname, self.secret)
        #n = Node(url, dirname, self.secret)
        t = Thread(target=n._start)
        t.setDaemon(1)
        t.start()
        # 让服务器先行一步：
        sleep(HEAD_START)
        self.server = ServerProxy(url)
        urlfile = path.join(dirname, urlfile)
        for line in open(urlfile):
            line = line.strip()
            self.server.hello(line)

        self.tips.setText("已经连接服务器,下一步获取文件" )

    def update_list(self):
        slm=QStringListModel()
        self.qlist=self.server.list() #数据类型为列表，而非字符串
        slm.setStringList(self.qlist)#
        self.filelistView.setModel(slm)


if __name__ == "__main__":
    app = QApplication(sys.argv)   #pyqt窗口必须在QApplication方法中使用
    window = PyQtLogic() # 实例化类
    window.show()         #windows调用show方法
    sys.exit(app.exec_())  # #消息结束的时候，结束进程，并返回0，接着调用sys.exit(0)退出程序
