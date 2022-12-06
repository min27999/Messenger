import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from client import Client

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("chat.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class MainWindow(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.outputChat.setReadOnly(True)
        self.nameChannel.setReadOnly(True)

        self.buttonSend.clicked.connect(self.send)
        self.buttonLogin.clicked.connect(self.login)
        self.buttonSearch.clicked.connect(self.search)
        self.buttonJoin.clicked.connect(self.join)

        self.setWindowTitle("Messenger")

        self.show()

    def send(self):
        inputMsg = self.inputChat.toPlainText().strip()
        chat = self.outputChat.toPlainText() + f"<{self.nickname}> {inputMsg}"
        self.inputChat.clear()
        self.outputChat.setText(chat + '\n')
        self.client.send_message_to_channel(inputMsg)

    def login(self):
        self.nickname = self.inputNickname.text()

    def search(self):
        print("search button")

    def join(self):
        self.channel = self.inputChannel.text()
        self.nameChannel.setText(f"Channel: {self.channel}")
        self.client = Client(self, self.nickname, self.channel)
        self.client.start()
        self.client.chattingChanged.connect(self.updateOutputChat)

    @pyqtSlot(str)
    def updateOutputChat(self, chat):
        chat = self.outputChat.toPlainText() + chat + '\n'
        self.outputChat.setText(chat)
