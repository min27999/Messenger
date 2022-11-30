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
        self.Chat_Chart.currentIndexChanged.connect(self.ChatChart_function)
        self.Chat_Object.currentIndexChanged.connect(self.ChartObject_function)

    def Send_function(self):
        self.text = self.Chat_Block.toPlainText()
        print(self.Chat_Area.append(self.text))
        print(self.Chat_Area.append(""))

    def Login_function(self):
        NickName = open("NickName.dat")

        self.NickName_Text = self.NickName_Block.text()

        for self.i in NickName:
            self.NickName_Chart = self.i.split()

        if self.NickName_Text in self.NickName_Chart:
            if self.NickName_Text in self.NickName_Chart:
                print(self.NickName.clear())
                print(self.NickName.setText(self.NickName_Text))

    def ChatChart_function(self):
        self.Chat_Area.clear()
        self.Chat_Name.clear()
        self.Chat_Block.clear()
        self.chat_name = self.Chat_Chart.currentText()
        print(self.Chat_Name.setText(self.chat_name))

    def Search_function(self):
        Search = open("Search.dat")
        self.Search_Text = self.Search_Block.text()
        self.Search_Chart = []
        self.Search_index = []

        for self.i in Search:
            self.Search_Chart.append(self.i.split(", "))
            # print(self.Search_Chart)

            for self.Word in self.Search_Chart:
                if self.Search_Text in self.Word:
                    self.Search_index.append(self.Search_Chart.index(self.Word))
                    # print(self.Search_index)

        for self.j in self.Search_index:
            # print(self.j)
            self.Chat_Object.addItem(self.Search_Chart[self.j])


    def ChartObject_function(self):
        return

    def Join_function(self):
        print("가입 완료")

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()