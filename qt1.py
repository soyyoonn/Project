# # Ex 3-1. 창 띄우기.
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
#
# class MyApp(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('My First Application')
#         self.move(300, 300)
#         self.resize(400, 200)
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())

# # Ex 3-2. 어플리케이션 아이콘 넣기.
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtGui import QIcon
#
#
# class MyApp(QWidget):
#
#   def __init__(self):
#       super().__init__()
#       self.initUI()
#
#   def initUI(self):
#       self.setWindowTitle('Icon')
#       self.setWindowIcon(QIcon('web.png'))
#       self.setGeometry(300, 300, 300, 200)
#       self.show()
#
# if __name__ == '__main__':
#   app = QApplication(sys.argv)
#   ex = MyApp()
#   sys.exit(app.exec_())

# # Ex 3-3. 창 닫기.
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
# from PyQt5.QtCore import QCoreApplication
#
#
# class MyApp(QWidget):
#
#   def __init__(self):
#       super().__init__()
#       self.initUI()
#
#   def initUI(self):
#       btn = QPushButton('Quit', self)
#       btn.move(50, 50)
#       btn.resize(btn.sizeHint())
#       btn.clicked.connect(QCoreApplication.instance().quit)
#
#       self.setWindowTitle('Quit Button')
#       self.setGeometry(300, 300, 300, 200)
#       self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())

# # Ex 5-1. QPushButton.
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
#
#
# class MyApp(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         btn1 = QPushButton('&Button1', self)
#         btn1.setCheckable(True)
#         btn1.toggle()
#
#         btn2 = QPushButton(self)
#         btn2.setText('Button&2')
#
#         btn3 = QPushButton('Button3', self)
#         btn3.setEnabled(False)
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(btn1)
#         vbox.addWidget(btn2)
#         vbox.addWidget(btn3)
#
#         self.setLayout(vbox)
#         self.setWindowTitle('QPushButton')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())

# ## ui 파일 연걸
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
#
# #UI파일 연결
# #단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
# form_class = uic.loadUiType("test.ui")[0]
#
# #화면을 띄우는데 사용되는 Class 선언
# class WindowClass(QMainWindow, form_class) :
#     def __init__(self) :
#         super().__init__()
#         # ui 불러오기, 객체 생성
#         self.setupUi(self)
#
# if __name__ == "__main__" :
#     #QApplication : 프로그램을 실행시켜주는 클래스
#     app = QApplication(sys.argv)
#
#     #WindowClass의 인스턴스 생성
#     myWindow = WindowClass()
#
#     #프로그램 화면을 보여주는 코드
#     myWindow.show()
#
#     #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
#     app.exec_()


## stack
# import sys
# from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget, QPushButton, QLabel, QDialog, \
#     QApplication
# from PyQt5.QtGui import QPixmap
#
#
# class MainDialog(QDialog):
#     def __init__(self):
#         super().__init__()
#
#         vertical_layout = QVBoxLayout()
#
#         stack1 = QWidget()
#         stack2 = QWidget()
#
#         self.Stack = QStackedWidget()
#         self.Stack.addWidget(stack1)
#         self.Stack.addWidget(stack2)
#
#         horizontal_layout1 = QHBoxLayout()
#         label1 = QLabel()
#         label2 = QLabel()
#         horizontal_layout1.addWidget(label1)
#         horizontal_layout1.addWidget(label2)
#         pixmap = QPixmap('images.jpg')
#         pixmap2 = QPixmap('snowfox.jpg')
#         label1.setPixmap(pixmap)
#         label2.setPixmap(pixmap2)
#
#         stack1.setLayout(horizontal_layout1)
#
#         horizontal_layout2 = QHBoxLayout(self)
#         label3 = QLabel()
#         horizontal_layout2.addWidget(label3)
#         label3.setPixmap(pixmap)
#         label3.setScaledContents(True)
#         stack2.setLayout(horizontal_layout2)
#
#         vertical_layout.addWidget(self.Stack)
#
#         horizontal_layout3 = QHBoxLayout()
#         self.Button1 = QPushButton('STACK 1', self)
#         self.Button1.clicked.connect(self.show_stack1)
#         self.Button2 = QPushButton('STACK 2', self)
#         self.Button2.clicked.connect(self.show_stack2)
#         horizontal_layout3.addWidget(self.Button1)
#         horizontal_layout3.addWidget(self.Button2)
#
#         vertical_layout.addLayout(horizontal_layout3)
#
#         self.setLayout(vertical_layout)
#
#         self.Button1.setEnabled(False)
#
#     def show_stack1(self):
#         self.Stack.setCurrentIndex(0)
#         self.Button1.setEnabled(False)
#         self.Button2.setEnabled(True)
#
#     def show_stack2(self):
#         self.Stack.setCurrentIndex(1)
#         self.Button1.setEnabled(True)
#         self.Button2.setEnabled(False)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     dlg = MainDialog()
#
#     dlg.show()
#     app.exec_()


# ## stack ui 파일 연걸
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
#
# #UI파일 연결
# #단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
# form_class = uic.loadUiType("stack.ui")[0]
#
# #화면을 띄우는데 사용되는 Class 선언
# class WindowClass(QMainWindow, form_class) :
#     def __init__(self) :
#         super().__init__()
#         # ui 불러오기, 객체 생성
#         self.setupUi(self)
#         # stack의 페이지를 첫번째 페이지로 고정한다
#         self.stackedWidget.setCurrentIndex(0)
#         # 버튼의 클릭이벤트와 함수를 연결해준다
#         self.btn_nextPage.clicked.connect(self.next_stack)
#         self.btn_prePage.clicked.connect(self.pre_stack)
#
#     def next_stack(self):
#         self.stackedWidget.setCurrentIndex(1)
#
#     def pre_stack(self):
#         self.stackedWidget.setCurrentIndex(0)
#
# if __name__ == "__main__" :
#     #QApplication : 프로그램을 실행시켜주는 클래스
#     app = QApplication(sys.argv)
#
#     #WindowClass의 인스턴스 생성
#     myWindow = WindowClass()
#
#     #프로그램 화면을 보여주는 코드
#     myWindow.show()
#
#     #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
#     app.exec_()
#
# ## 로그인 ui 파일 연걸
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
#
# #UI파일 연결
# #단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
# form_class = uic.loadUiType("form.ui")[0]
#
# #화면을 띄우는데 사용되는 Class 선언
# class WindowClass(QMainWindow, form_class) :
#     def __init__(self) :
#         super().__init__()
#         # ui 불러오기, 객체 생성
#         self.setupUi(self)
#         # stack의 페이지를 첫번째 페이지로 고정한다
#         self.stackedWidget.setCurrentIndex(0)
#         # 버튼의 클릭이벤트와 함수를 연결해준다
#         self.btn_login.clicked.connect(self.main_stack)
#         self.btn_join.clicked.connect(self.next_stack)
#         self.btn_prePage.clicked.connect(self.pre_stack)
#         self.btn_prePage_2.clicked.connect(self.pre_stack)
#
#     def next_stack(self):
#         self.stackedWidget.setCurrentIndex(1)
#
#     def pre_stack(self):
#         self.stackedWidget.setCurrentIndex(0)
#
#     def main_stack(self):
#         self.stackedWidget.setCurrentIndex(2)
#
# if __name__ == "__main__" :
#     #QApplication : 프로그램을 실행시켜주는 클래스
#     app = QApplication(sys.argv)
#
#     #WindowClass의 인스턴스 생성
#     myWindow = WindowClass()
#
#     #프로그램 화면을 보여주는 코드
#     myWindow.show()
#
#     #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
#     app.exec_()
