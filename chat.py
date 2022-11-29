import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("chat.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.Send_Button.clicked.connect(self.Send_function)
        self.Login_Button.clicked.connect(self.Login_function)
        self.Search_Button.clicked.connect(self.Search_function)
        self.Join_Button.clicked.connect(self.Join_function)
        self.Chat_Chart.currentIndexChanged.connect(self.ChatChart_function)

    def Send_function(self):
        self.text = self.Chat_Block.toPlainText()
        print(self.Chat_Area.append(self.text))
        print(self.Chat_Area.append(""))

    def Login_function(self):
        ID = open("ID.dat")
        PW = open("pw.dat")
        self.ID_text = self.ID_Block.toPlainText()
        self.PW_text = self.PW_Block.toPlainText()
        for self.i in ID:
            self.ID_Chart = self.i.split()
        for self.j in PW:
            self.PW_Chart = self.j.split()

        if self.ID_text in self.ID_Chart:
            if self.PW_text in self.PW_Chart:
                print(self.NickName.clear())
                print(self.NickName.append(self.ID_text))

    def chat_search(self):                      #수정 필요
        self.search = open("search.dat")
        for line in self.search():
            self.chart = line.split()

    def Search_function(self):
        print("검색 완료")

    def Join_function(self):
        print("가입 완료")

    def ChatChart_function(self):
        self.Chat_Area.clear()
        self.Chat_Name.clear()
        self.Chat_Block.clear()
        self.chat_name = self.Chat_Chart.currentText()
        print(self.Chat_Name.append(self.chat_name))

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()