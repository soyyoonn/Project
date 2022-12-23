# #101번
# #bool타입
#
# #102번
# #False
#
# #103번
# #True
#
# #104번
# #True
#
# #105번
# #True
#
# #106번
# # 3은 4보다 같거나 크지않다
# # => 지원하지 않는 연산자입니다.(정답)
#
# #107번
# #False(x)
# #조건을 만족하지 않기 때문에 아무 결과도 출력되지 않습니다.(정답)
#
# #108번
# print("Hi, there.")
#
# #109번
# if True:       #True이면 출력
#     print("1")
#     print("2")
# else:
#     print("3")
# print("4")
#
# #110번
# if True:
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else:
#     print("4")
# print("5")
#
# #111번
# a = input("입력: ")
# print(a*2)
#
# #112번
# a = int(input("입력: "))
# print(a+10)
#
# #113번
# a = int(input("입력: "))
# if a % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")
#
# #114번
# a = int(input("입력: "))
# num = a +20
# if num > 255:
#     print(255)
# else:
#     print(num)
#
# #115번
# a = int(input("입력: "))
# num = a - 20
# if num < 0:
#     print(0)
# elif num > 255:
#     print(255)
# else:
#     print(num)
#
# #116번
# time = (input("시간: "))
# if time[-2:] == "00":
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")

# #117번
# fruit = ["사과", "포도", "홍시"]
# a = input("좋아하는 과일은? ")
# if a in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# #118번
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# 종목 = input("종목명: ")
# if 종목 in warn_investment_list:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")

# #119번
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# season = input("제가 좋아하는 계절은: ")
# if season in fruit.keys():
#     print("정답입니다.")
# else:
#     print("오답입니다.")
#
# #120번
# 과일 = input("좋아하는 과일은: ")
# if 과일 in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# # 121번
#
# a = input("문자 입력: ")
# print(a.islower())
# if a.islower == True:
#     print(a)
# else:
#     print(a.upper())
#
# #122번
# score = int(input("점수 입력: "))
# if 81<=score<=100:
#     print("A")
# elif 61<=score<=80:
#     print("B")
# elif 41<=score<=60:
#     print("C")
# elif 21<=score<=40:
#     print("D")
# else:
#     print("E")

# #123번★
# 환율 = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}   #딕셔너리
# user = input("입력: ")
# num, currency = user.split()    #금액과 돈 단위 띄어쓰기로 구분
# print(float(num) * 환율[currency], "원")

# #124번
# a = int(input("num1: "))
# b = int(input("num2: "))
# c = int(input("num3: "))
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# elif c > a and c > b:
#     print(c)

# #125번
# 통신사 = {'011':'SKT','016':'KT','019':'LGU','010':'알수없음'}
# a = input("휴대폰 번호 입력: ")
# if a[0:3] == '011':
#     print(통신사['011'])
# elif a[0:3] == '016':
#     print(통신사['016'])
# elif a[0:3] == '019':
#     print(통신사['019'])
# elif a[0:3] == '010':
#     print(통신사['010'])

# #126번
# a = input("우편번호 입력: ")
# if a[0:3] in ['010','011','012']:
#     print("강북구")
# elif a[0:3] in ['013','014','015']:
#     print("도봉구")
# elif a[0:3] in ['016','017','018','019']:
#     print("노원구")

#127번
# a = input("주민등록번호 입력: ")
# a = a.split("-")[1]
# # print(a)
# if a[0] == "1" or a[0] == "3":
#     print("남자")
# else:
#     print("여자")

#128번
# a = input("주민등록번호 입력: ")
# a = a.split("-")[1]
# if 0<= int(a[1:3]) <= 8:
#     print("서울입니다")
# else:
#     print("서울이 아닙니다")

