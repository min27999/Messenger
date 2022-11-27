from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout,
                             QLabel, QComboBox, QTextEdit, QLineEdit)

class GUI(QWidget):

    def __init__(self, chattings: list):
        super().__init__()
        self.chattings = chattings
        self.initUI()

    def initUI(self):
        # ID 입력
        labelID = QLabel("ID: ", self)
        inputID = QLineEdit()
        hboxID = QHBoxLayout()
        hboxID.addWidget(labelID)
        hboxID.addWidget(inputID)

        # PW 입력
        labelPW = QLabel("PW: ", self)
        inputPW = QLineEdit()
        hbowPW = QHBoxLayout()
        hbowPW.addWidget(labelPW)
        hbowPW.addWidget(inputPW)

        # 로그인 버튼
        buttonLogin = QPushButton("Login")
        buttonLogin.clicked.connect(self.login)

        vboxLogin = QVBoxLayout()
        vboxLogin.addLayout(hboxID)
        vboxLogin.addLayout(hbowPW)
        vboxLogin.addWidget(buttonLogin)
        
        # 채팅방 선택
        selectChat = QComboBox()
        selectChat.addItems(self.chattings)

        # 채팅방 선택 버튼
        buttonSelectChat = QPushButton("Select")
        buttonSelectChat.clicked.connect(self.select)

        # 채팅방 선택 위젯
        hboxSelectChat = QHBoxLayout()
        hboxSelectChat.addWidget(selectChat)
        hboxSelectChat.addWidget(buttonSelectChat)
        
        # 키워드 알림 설정
        labelNotice = QLabel("키워드 알림 설정: ", self)
        inputNotice = QLineEdit()
        buttonNotice = QPushButton("Set")
        buttonNotice.clicked.connect(self.setKeyword)
        vboxNotice = QVBoxLayout()
        hboxNotice = QHBoxLayout()
        hboxNotice.addWidget(inputNotice)
        hboxNotice.addWidget(buttonNotice)
        vboxNotice.addWidget(labelNotice)
        vboxNotice.addLayout(hboxNotice)

        # vboxSettings
        vboxSettings = QVBoxLayout()
        vboxSettings.addLayout(vboxLogin)
        vboxSettings.addLayout(hboxSelectChat)
        vboxSettings.addLayout(vboxNotice)

        # 채팅 내용
        textChattings = QTextEdit()
        textChattings.setReadOnly(True)

        # 채팅 입력
        textSend = QTextEdit()
        buttonSend = QPushButton("Send")
        buttonSend.clicked.connect(self.send)
        hboxSend = QHBoxLayout()
        hboxSend.addWidget(textSend)
        hboxSend.addWidget(buttonSend)

        vboxChattings = QVBoxLayout()
        vboxChattings.addWidget(textChattings)
        vboxChattings.addLayout(hboxSend)

        hboxDisplay = QHBoxLayout()
        hboxDisplay.addStretch(1)
        hboxDisplay.addLayout(vboxSettings)
        hboxDisplay.addLayout(vboxChattings)

        self.setLayout(hboxDisplay)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Messenger')
        self.show()

    def login(self):
        print("Login Button")

    def select(self):
        print("Select Button")

    def setKeyword(self):
        print("Set Button")

    def send(self):
        print("Send Button")
