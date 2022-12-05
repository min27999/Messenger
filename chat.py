import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("Chat.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.Send_Button.clicked.connect(self.Send_function)
        self.Login_Button.clicked.connect(self.Login_function)
        self.Search_Button.clicked.connect(self.Search_function)
        self.Join_Button.clicked.connect(self.Join_function)

    def Send_function(self):
        self.text = self.Chat_Block.toPlainText()
        print(self.Chat_Area.append(self.text))
        print(self.Chat_Area.append(""))
        self.Chat_Block.clear()

    def Login_function(self):
        NickName = open("NickName.dat")

        self.NickName_Text = self.NickName_Block.text()

        for self.i in NickName:
            self.NickName_Chart = self.i.split()

        if self.NickName_Text in self.NickName_Chart:
            if self.NickName_Text in self.NickName_Chart:
                print(self.NickName.clear())
                print(self.NickName.setText(self.NickName_Text))

    def Search_function(self):
        self.Chat_Room = open("Chat_Room.dat")
        self.chat_name = self.ChatRoom_Block.text()
        for self.i in self.Chat_Room:
            self.Chat_Chart = self.i.split()

        self.Search = open("Search.dat", "r")
        self.Search_Plus = open("Chat_Room.dat", "a")
        self.Search_Text = self.Search_Block.text()

        for self.i in self.Search:
            self.Search_Chart = self.i.split()

        if self.Search_Text in self.Chat_Chart:
                print(self.Search_Fin.setText("이미 있는 채팅방입니다."))
        else:
            if self.Search_Text in self.Search_Chart:
                self.Search_Plus.write(" ")
                self.Search_Plus.write(self.Search_Text)
                print(self.Search_Fin.setText("방이 추가되었습니다."))
                self.Search_Block.clear() #여기서 버튼을 한번 더 누르거나 해야만 Chat_Room.dat에 추가 됨 버튼만 눌러서는 추가가 되지 않음.
            else:
                print(self.Search_Fin.setText("방 제목을 다시 입력하십시오."))
    def Join_function(self):
        self.Chat_Room = open("Chat_Room.dat")
        self.chat_name = self.ChatRoom_Block.text()
        for self.i in self.Chat_Room:
            self.Chat_Chart = self.i.split()

        if self.chat_name in self.Chat_Chart:
            self.Chat_Area.clear()
            self.Chat_Name.clear()
            self.Chat_Block.clear()
            print(self.Chat_Name.setText(self.chat_name))
        else:
            self.ChatRoom_Block.clear()
            print(self.Chat_Name.setText("방 제목을 다시 입력하십시오."))

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()