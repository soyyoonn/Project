import sys
import time

import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from datetime import datetime,timedelta
from PyQt5.QtCore import QTime,QDate
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import threading

form_class = uic.loadUiType("bcon.ui")[0]

class Check_attendance(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.log_check = False
        # self.manage_mode = False
        self.btn_home1.clicked.connect(self.move_main)   # 메인 페이지로 이동
        self.btn_home2.clicked.connect(self.move_main)
        self.btn_home3.clicked.connect(self.move_main)
        self.btn_home4.clicked.connect(self.move_main)
        self.btn_home5.clicked.connect(self.move_main)
        self.btn_home6.clicked.connect(self.move_main)
        self.btn_login.clicked.connect(self.move_login)    # 메인 페이지 로그인 버튼 누르면 로그인 페이지로
        self.btn_check.clicked.connect(self.move_check)    # 메인 페이지 출결 버튼 누르면 출결 페이지로
        self.btn_cal.clicked.connect(self.move_calendar)   # 메인 페이지 일정 버튼 누르면 일정 페이지로
        self.calendarWidget.clicked.connect(self.schedule)   # 캘린더 위젯 누르면 schedule 메서드 실행
        self.btn_add.clicked.connect(self.schedule_add)      # 일정 추가 버튼 누르면 schedule_add 메서드 실행
        self.btn_message.clicked.connect(self.move_message)   # 메인 페이지 메시지 버튼 누르면 메시지 페이지로
        self.btn_login2.clicked.connect(self.login)          # 로그인 페이지 로그인 버튼 누르면 login 메서드 실행
        self.pw.returnPressed.connect(self.login)
        self.message.returnPressed.connect(self.send_message)
        self.btn_logout.clicked.connect(self.logout)        # 학생 출결 페이지 로그아웃 버튼 눌러서 로그아웃 됨
        self.btn_tlogout.clicked.connect(self.logout)       # 관리자 출결 페이지 로그아웃 버튼 눌러서 로그아웃 됨
        self.btn_send.clicked.connect(self.send_message)    # 메시지 전송 버튼 누르면 send_message 메서드 실행
        self.btn_in.clicked.connect(self.checkintime)       # 입실 버튼 누르면 checkintime 메서드 실행
        self.btn_out.clicked.connect(self.checkouttime)     # 퇴실 버튼 누르면 checkouttime 메서드 실행
        self.btn_go.clicked.connect(self.checkgotime)       # 외출 버튼 누르면 checkgotime 메서드 실행
        self.btn_back.clicked.connect(self.checkbacktime)   # 복귀 버튼 누르면 checkbacktime 메서드 실행
        self.okbutton.clicked.connect(self.check_condition)  # 확인 버튼 누르면 check_condition 메서드 실행(출결 조건 확인 후 카운트)
        self.okbutton2.clicked.connect(self.student_check)
        self.studentlist.currentTextChanged.connect(self.messagelist) # 콤보박스에서 학생 이름 선택하면 메시지 내용이 뜬다
        self.latenotice = ''

    def move_main(self):
        self.stackedWidget.setCurrentIndex(0)
        if self.log_check == True:
            # 퇴실 시간 됐을 시 알림------------------------------------------
            time = QTime.currentTime()
            time = time.toString('hhmmss')
            outtime = time
            if 170001 <= int(outtime) < 170100:
                QMessageBox.information(self, '알림', f'퇴실 시간입니다')

    def move_login(self):
        self.stackedWidget.setCurrentIndex(1)
        self.clear_check()
        if self.log_check == True:
            self.logout()

    def clear_check(self):
        self.id.clear()
        self.pw.clear()

    def move_check(self):
        if self.log_check == False:
            QMessageBox.information(self, '알림', '로그인을 해주세요')
            self.stackedWidget.setCurrentIndex(1)
            self.clear_check()

        elif self.log[0][4] == '교수':
            self.stackedWidget.setCurrentIndex(3)
            self.backalarm()
            self.latealarm()

        elif self.log_check == True:
            conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                                   charset='utf8')
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM check_data WHERE 이름='{self.log[0][3]}'")
            self.attendance_count = cursor.fetchall()
            conn.close()
            self.attendancecount.setText(str(self.attendance_count[0][9]))
            self.latecount.setText(str(self.attendance_count[0][10]))
            self.leavecount.setText(str(self.attendance_count[0][11]))
            self.goingoutcount.setText(str(self.attendance_count[0][12]))
            self.absentcount.setText(str(self.attendance_count[0][13]))
            self.stackedWidget.setCurrentIndex(2)

    def move_calendar(self):
        if self.log_check == False:
            QMessageBox.information(self, '알림', '로그인을 해주세요')
            self.stackedWidget.setCurrentIndex(1)
            self.clear_check()
        elif self.log_check == True:
            self.stackedWidget.setCurrentIndex(4)

    def move_message(self):
        if self.log_check == False:
            QMessageBox.information(self, '알림', '로그인을 해주세요')
            self.stackedWidget.setCurrentIndex(1)
            self.clear_check()
        elif self.log[0][4] == '교수':
            self.stackedWidget.setCurrentIndex(6)
            self.newmessagealarm()
        elif self.log_check == True:
            self.stackedWidget.setCurrentIndex(5)

    # def manage(self):      # 관리자 모드 설정
    #     # if self.log[0][4] != '교수':
    #     #     self.manage_mode = False
    #     #     QMessageBox.critical(self, '알림', '관리자가 아닙니다')
    #     #     return
    #     if self.log[0][4] == '교수':
    #         self.manage_mode = True

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
            self.log_check = True
            self.log2_btn()
            self.move_main()
            # 입실 시간 됐을 시 알림------------------------------------------
            time = QTime.currentTime()
            time = time.toString('hhmmss')
            intime = time
            if 90001 <= int(intime) < 90100:
                QMessageBox.information(self, '알림', f'입실 시간입니다')


        elif self.log[0][1] == id and self.log[0][4] == '교수':
            QMessageBox.information(self, '알림', f'{self.log[0][3]}님 로그인 되었습니다')
            self.log_check = True
            # self.manage_mode = True
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
        self.log_check = False
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
        s = cursor.fetchall()
        print(s)
        for i in range(len(s)):
            add = s[i][0] + ' ' + s[i][1]
            self.schedulespace.addItem(add)
            # self.schedulespace.addItem((b[i][0]))
            # self.schedulespace.addItem((b[i][1]))

    def schedule_add(self):    # 일정 추가
        scheduleadd = self.scheduleadd.text()
        print(scheduleadd)
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO schedule (이름, 일정, 날짜) VALUES('{self.log[0][3]}','{scheduleadd}','{int(self.date_add)}')")
        conn.commit()
        conn.close()
        self.schedule()
        self.scheduleadd.clear()
        QMessageBox.information(self, '알림', '일정이 추가됐습니다')

    def send_message(self):  # 학생이 관리자에게 메시지 전송
        self.messagespace.clear()
        teacherlist = self.teacherlist.currentText()
        print(teacherlist)
        message = self.message.text()
        print(message)
        if message == '':
            QMessageBox.information(self, '알림', '메시지를 입력해주세요')
            return
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO message (보낸사람, 메시지, 받는사람) VALUES('{self.log[0][3]}','{message}','{teacherlist}')")
        conn.commit()
        cursor.execute(f"SELECT * FROM message WHERE 보낸사람='{self.log[0][3]}'")
        m = cursor.fetchall()
        conn.close()
        self.message.clear()
        print(m)
        for i in range(len(m)):
            self.messagespace.addItem(m[i][0] + ' : '+ m[i][1])

    def messagelist(self):    # 학생이 보낸 메시지 확인
        self.messagespace2.clear()
        self.studentlist = self.studentlist.currentText()
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM message WHERE 받는사람='{self.log[0][3]}' and 보낸사람='{self.studentlist}'")
        checkmessage = cursor.fetchall()
        conn.close()
        for i in range(len(checkmessage)):
            self.messagespace2.addItem(checkmessage[i][0] + ' : ' + checkmessage[i][1])
        self.newmessagealarm()


    def newmessagealarm(self):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM message WHERE 받는사람='{self.log[0][3]}' and 알림=1")
        self.messagenotice = cursor.fetchall()
        print(self.messagenotice)
        if self.messagenotice != ():
            self.messagelabel.setText(f'{self.messagenotice[0][0]}님에게 새로운 메시지가 도착했습니다.')
            self.messagelabel.show()
        cursor.execute(f"UPDATE message SET 알림=0")
        if self.messagenotice == ():
            self.messagelabel.hide()
        conn.commit()
        conn.close()

    def student_check(self):  # 관리자 모드 학생 출결현황 출력
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM check_data WHERE 번호 < 28")
        self.attendance_check = cursor.fetchall()
        print(self.attendance_check)
        conn.close()

        Row = 0
        self.tableWidget.setRowCount(len(self.attendance_check))
        for i in self.attendance_check:
            self.tableWidget.setItem(Row, 0, QTableWidgetItem(i[3]))  # 이름
            self.tableWidget.setItem(Row, 1, QTableWidgetItem(i[5]))  # 입실시간
            self.tableWidget.setItem(Row, 2, QTableWidgetItem(i[7]))  # 외출시간
            self.tableWidget.setItem(Row, 3, QTableWidgetItem(i[6]))  # 복귀시간
            self.tableWidget.setItem(Row, 4, QTableWidgetItem(i[8]))  # 퇴실시간
            self.tableWidget.setItem(Row, 5, QTableWidgetItem(str(i[9])))  # 출석횟수
            self.tableWidget.setItem(Row, 6, QTableWidgetItem(str(i[10])))  # 지각횟수
            self.tableWidget.setItem(Row, 7, QTableWidgetItem(str(i[11])))  # 조퇴횟수
            self.tableWidget.setItem(Row, 8, QTableWidgetItem(str(i[12])))  # 외출횟수
            self.tableWidget.setItem(Row, 9, QTableWidgetItem(str(i[13])))  # 결석횟수
            Row += 1


    def check_condition(self):  # 출결 조건 설정
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM check_data WHERE 이름='{self.log[0][3]}'")
        self.attendance_count = cursor.fetchall()
        conn.close()
        if  self.attendance_count[0][8] == None:
            self.absent_plus()
        elif int(self.intime) < 92100 and int(self.outtime) >= 170100 and self.attendance_count[0][7] == None:
            self.attendance_plus()
        elif int(self.intime) >= 92100 and int(self.outtime) >= 170100:
            self.late_plus()
        elif int(self.intime) < 92100 and 130100 <= int(self.outtime) < 170000:
            self.leave_plus()
        elif int(self.intime) > 130100 and int(self.outtime) >= 170100:
            self.absent_plus()
        elif 92100 < int(self.gotime) < 130100 and 130100 <= int(self.backtime) <= 170000:
            self.goingout_plus()
        elif 92100 < int(self.gotime) < 130100 and 92100 < int(self.backtime) < 130100:
            self.goingout_plus()
        elif 130100 < int(self.gotime) < 170000 and 130100 <= int(self.backtime) <= 170000:
            self.goingout_plus()

    def checkintime(self):    # 입실 찍을 때
        checkin = self.checkin.text()
        now = datetime.now()
        # self.checkintime = now.strftime('%H%M%S')
        # print(self.checkintime)
        intime = now.strftime('%Y-%m-%d %H:%M:%S')
        # -------------------------------
        time = QTime.currentTime()
        time = time.toString('hhmmss')
        self.intime = time
        # ------------------------------------
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE check_data SET 입실='{intime}', 퇴실=NULL WHERE 이름='{self.log[0][3]}'")
        if int(self.intime) > 92100:
            cursor.execute(
                f"UPDATE check_data SET 입실='{intime}', 입실체크 = 1 WHERE 이름='{self.log[0][3]}'")
        conn.commit()
        conn.close()
        QMessageBox.information(self, '알림', f'{intime}\n {self.log[0][3]}님 입실')
        self.checkin.setText(intime)




    def checkouttime(self):   # 퇴실 찍을 때
        checkout = self.checkout.text()
        now = datetime.now()
        outtime = now.strftime('%Y-%m-%d %H:%M:%S')
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE check_data SET 퇴실='{outtime}' WHERE 이름='{self.log[0][3]}'")
        conn.commit()
        conn.close()
        QMessageBox.information(self, '알림', f'{outtime}\n {self.log[0][3]}님 퇴실')
        self.checkout.setText(outtime)
        time = QTime.currentTime()
        time = time.toString('hhmmss')
        self.outtime = time


    def checkgotime(self):     # 외출 찍을 때
        checkgo = self.checkgo.text()
        now = datetime.now()
        gotime = now.strftime('%Y-%m-%d %H:%M:%S')
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE check_data SET 외출='{gotime}' WHERE 이름='{self.log[0][3]}'")
        conn.commit()
        conn.close()
        QMessageBox.information(self, '알림', f'{gotime}\n {self.log[0][3]}님 외출')
        self.checkgo.setText(gotime)
        time = QTime.currentTime()
        time = time.toString('hhmmss')
        self.gotime = time


    def checkbacktime(self):      # 복귀 찍을 때
        checkback = self.checkback.text()
        now = datetime.now()
        backtime = now.strftime('%Y-%m-%d %H:%M:%S')
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE check_data SET 복귀='{backtime}', 복귀체크=1  WHERE 이름='{self.log[0][3]}'")
        conn.commit()
        conn.close()
        QMessageBox.information(self, '알림', f'{backtime}\n {self.log[0][3]}님 복귀')
        self.checkback.setText(backtime)
        time = QTime.currentTime()
        time = time.toString('hhmmss')
        self.backtime = time


    def backalarm(self):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM check_data WHERE 복귀체크=1")
        self.backnotice = cursor.fetchall()
        print(self.backnotice)
        if self.backnotice != ():
            self.studentlabel.setText(f'{self.backnotice[0][3]}님이\n'
                                      f'외출 후 복귀했습니다.')
            self.studentlabel.show()
            cursor.execute(f"UPDATE check_data SET 복귀체크=0 WHERE '{self.backnotice[0][3]}'")
        if self.backnotice == ():
            self.studentlabel.hide()
        conn.commit()
        conn.close()

    def latealarm(self):
        self.th = thread_one(self)
        self.th.start()


        # conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
        #                        charset='utf8')
        # cursor = conn.cursor()
        # cursor.execute(f"SELECT * FROM check_data WHERE 입실체크=1")
        # self.latenotice = cursor.fetchall()
        # print(self.latenotice)
        # if self.latenotice != ():
        #     self.studentlabel.setText(f'지각자 {self.latenotice[0][3]}님이\n'
        #                               f'입실했습니다.')
        #     self.studentlabel.show()
        #     cursor.execute(f"UPDATE check_data SET 입실체크=0 WHERE 이름='{self.latenotice[0][3]}'")
        # if self.latenotice == ():
        #     self.studentlabel.hide()
        # conn.commit()
        # conn.close()

    def attendance_plus(self):  # 출석 카운트 +1
        attendacecount = self.attendancecount.text()
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE check_data SET 출석횟수='{int(self.log[0][9])+1}' WHERE 이름='{self.log[0][3]}'")
        cursor.execute(f"SELECT * FROM check_data WHERE 출석횟수='{int(self.log[0][9])+1}' and 이름='{self.log[0][3]}'")
        self.attendance_count = cursor.fetchall()
        # print(self.log[0][9])
        # print(self.attendance_count)
        # print(self.attendance_count[0][9])
        conn.commit()
        conn.close()
        self.attendancecount.setText(str(self.attendance_count[0][9]))


    def late_plus(self):  # 지각 카운트 +1
        latecount = self.latecount.text()
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE check_data SET 지각횟수='{int(self.log[0][10]) + 1}' WHERE 이름='{self.log[0][3]}'")
        cursor.execute(f"SELECT * FROM check_data WHERE 이름='{self.log[0][3]}'")
        self.late_count = cursor.fetchall()
        # print(self.late_count[0][10])
        conn.commit()
        conn.close()
        self.latecount.setText(str(self.late_count[0][10]))


    def leave_plus(self):  # 조퇴 카운트 +1
        leavecount = self.leavecount.text()
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE check_data SET 조퇴횟수='{int(self.log[0][11]) + 1}' WHERE 이름='{self.log[0][3]}'")
        cursor.execute(f"SELECT * FROM check_data WHERE 이름='{self.log[0][3]}'")
        self.leave_count = cursor.fetchall()
        conn.commit()
        conn.close()
        self.leavecount.setText(str(self.leave_count[0][11]))


    def goingout_plus(self):  # 외출 카운트 +1
        goingoutcount = self.goingoutcount.text()
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE check_data SET 외출횟수='{int(self.log[0][12]) + 1}' WHERE 이름='{self.log[0][3]}'")
        cursor.execute(f"SELECT * FROM check_data WHERE 이름='{self.log[0][3]}'")
        self.goingout_count = cursor.fetchall()
        conn.commit()
        conn.close()
        self.goingoutcount.setText(str(self.goingout_count[0][12]))


    def absent_plus(self):  # 결석 카운트 +1
        absentcount = self.absentcount.text()
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE check_data SET 결석횟수='{int(self.log[0][13]) + 1}' WHERE 이름='{self.log[0][3]}'")
        cursor.execute(f"SELECT * FROM check_data WHERE 이름='{self.log[0][3]}'")
        self.absent_count = cursor.fetchall()
        conn.commit()
        conn.close()
        self.absentcount.setText(str(self.absent_count[0][13]))

class thread_one(threading.Thread):
    def __init__(self, check):
        super().__init__()
        self.check = check

    def run(self):
        while True:
            time.sleep(1)
            conn = pymysql.connect(host='localhost', port=3306, user='root', password='00000000', db='sy',
                                   charset='utf8')
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM check_data WHERE 입실체크=1")
            self.check.latenotice = cursor.fetchone()
            # print(self.check.latenotice)
            if self.check.latenotice != None:
                self.check.studentlabel.setText(f'지각자 {self.check.latenotice[3]}님이\n'
                                          f'입실했습니다.')
                self.check.studentlabel.show()
                time.sleep(5)
                cursor.execute(f"UPDATE check_data SET 입실체크=0 WHERE 이름='{self.check.latenotice[3]}'")
            if self.check.latenotice == None:
                self.check.studentlabel.hide()
            conn.commit()
            conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = Check_attendance()

    myWindow.show()

    app.exec_()
