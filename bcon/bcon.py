import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

form_class = uic.loadUiType("bcon.ui")[0]

class Check_attendance(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.a = False
        self.btn_home1.clicked.connect(self.move_main)   # 메인 페이지로 이동
        self.btn_home2.clicked.connect(self.move_main)
        self.btn_home3.clicked.connect(self.move_main)
        self.btn_home4.clicked.connect(self.move_main)
        self.btn_home5.clicked.connect(self.move_main)
        self.btn_home6.clicked.connect(self.move_main)
        self.btn_home7.clicked.connect(self.move_main)
        self.btn_login.clicked.connect(self.move_login)    # 메인 페이지 로그인 버튼 누르면 로그인 페이지로
        self.btn_check.clicked.connect(self.move_check)    # 메인 페이지 출결 버튼 누르면 출결 페이지로
        self.btn_cal.clicked.connect(self.move_calendar)   # 메인 페이지 일정 버튼 누르면 일정 페이지로
        self.calendarWidget.clicked.connect(self.schedule)   # 캘린더 위젯 누르면 schedule 메서드 실행
        self.btn_add.clicked.connect(self.schedule_add)      # 일정 추가 버튼 누르면 schedule_add 메서드 실행
        self.btn_message.clicked.connect(self.move_message)   # 메인 페이지 메시지 버튼 누르면 메시지 페이지로
        self.btn_login2.clicked.connect(self.login)         # 로그인 완료 버튼 누르면 login 메서드 실행
        self.btn_tcheck.clicked.connect(self.move_tcheck)   # 관리자 출결 페이지로 이동
        self.btn_logout.clicked.connect(self.logout)        # 학생 출결 페이지 로그아웃 버튼 눌러서 로그아웃 됨
        self.btn_tlogout.clicked.connect(self.logout)       # 관리자 출결 페이지 로그아웃 버튼 눌러서 로그아웃 됨
        self.btn_tcal.clicked.connect(self.move_tcalendar)
        self.btn_tmessage.clicked.connect(self.move_tmessage)

    def move_main(self):
        self.stackedWidget.setCurrentIndex(0)

    def move_login(self):
        self.stackedWidget.setCurrentIndex(1)
        self.clear_check()
        if self.a == True:
            self.logout()

    def clear_check(self):
        self.id.clear()
        self.pw.clear()

    def move_check(self):
        if self.a == False:
            QMessageBox.information(self, '알림', '로그인을 해주세요')
            self.stackedWidget.setCurrentIndex(1)
            self.clear_check()
        elif self.a == True:
            self.stackedWidget.setCurrentIndex(2)

    def move_tcheck(self):
        self.stackedWidget.setCurrentIndex(3)

    def move_calendar(self):
        if self.a == False:
            QMessageBox.information(self, '알림', '로그인을 해주세요')
            self.stackedWidget.setCurrentIndex(1)
            self.clear_check()
        elif self.a == True:
            self.stackedWidget.setCurrentIndex(4)

    def move_tcalendar(self):
        self.stackedWidget.setCurrentIndex(5)

    def move_message(self):
        if self.a == False:
            QMessageBox.information(self, '알림', '로그인을 해주세요')
            self.stackedWidget.setCurrentIndex(1)
            self.clear_check()
        elif self.a == True:
            self.stackedWidget.setCurrentIndex(6)

    def move_tmessage(self):
        self.stackedWidget.setCurrentIndex(7)

    def login(self):
        id = self.id.text()
        pw = self.pw.text()
        if id == '' or pw == '':
            QMessageBox.information(self, '알림', '모두 입력해주세요')
            return
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * FROM check_data WHERE ID='{id}' AND 비밀번호='{pw}'")
        print(id)
        print(pw)
        self.log = cursor.fetchall()
        print(self.log)

        if bool(self.log) == False:  # 아이디나 비밀번호가 맞지 않을 때
            print('1234')
            QMessageBox.information(self, '알림', '아이디 또는 비밀번호를 확인해주세요')

        elif self.log[0][1] == id:
            QMessageBox.information(self, '알림', f'{self.log[0][3]}님 로그인 되었습니다')
            self.a = True
            self.log2_btn()
            self.move_main()


    def logout(self):
        # conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
        #                        charset='utf8')
        # cursor = conn.cursor()
        # cursor.execute(
        #     f"UPDATE check_data SET 로그인여부= CONCAT ('0')")
        # conn.commit()
        # conn.close()
        QMessageBox.information(self, '알림', f'{self.log[0][3]}님 로그아웃 되었습니다')
        self.a = False
        self.log_btn()
        self.move_main()

    def log_btn(self):   # 로그아웃 후 로그아웃 버튼 로그인 버튼으로 변경
        self.btn_login.setText('로그인')
        self.btn_logout.setText('로그인')
        self.btn_tlogout.setText('로그인')

    def log2_btn(self):     # 로그인 후 로그인 버튼 로그아웃 버튼으로 변경
        self.btn_login.setText('로그아웃')
        self.btn_logout.setText('로그아웃')
        self.btn_tlogout.setText('로그아웃')

    def schedule(self):
        self.schedulespace.clear()
        self.date = self.calendarWidget.selectedDate()
        print(self.date)
        self.date_add = self.date.toString("yyyyMMdd")
        print(self.date_add)
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM schedule WHERE 날짜='{int(self.date_add)}'")
        b = cursor.fetchall()
        print(b)
        for i in range(len(b)):
            self.schedulespace.addItem((b[i][0]))
            self.schedulespace.addItem((b[i][1]))

    def schedule_add(self):    # 일정 추가
        scheduleadd = self.scheduleadd.text()
        print(scheduleadd)
        # self.schedulespace.append(scheduleadd)
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO schedule (이름, 일정, 날짜) VALUES('{self.log[0][3]}','{scheduleadd}','{int(self.date_add)}')")
        conn.commit()
        self.schedule()
        # conn.close()
        self.scheduleadd.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = Check_attendance()

    myWindow.show()

    app.exec_()
