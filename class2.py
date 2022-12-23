# result1 = 0
# result2 = 0
#
# def add1(num):
#     global result1
#     result1 += num
#     return result1
#
# def add2(num):
#     global result2
#     result2 += num
#     return result2
#
# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))

# #클래스
# class calculator:
#     def __init__(self):
#         self.result = 0
#
#     def add(self, num):
#         self.result += num
#         return self.result
#
#     def sub(self,num):
#         self.result -= num
#         return self.result
#
# #객체
# cal1 = calculator()
# cal2 = calculator()
#
# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))


# class Fourcal:
#     #메서드의 매개변수
#     def setdata(self, first, second):
#         #메서드의 수행문
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result
#
# a = Fourcal()
# b = Fourcal()
# a.setdata(4, 2)
# b.setdata(3, 8)
# print(a.add())

class FamilyNameBak:        # class 사용
	lastname = '박'

	def __init__(self, name):       # __init__(생성자) 사용
		self.fullname = self.lastname + name

	def travel(self, where):
		print(f'{self.fullname}, {where}여행을 가다')

	def love(self, other):
		print(f'{self.fullname}, {other.fullname} 사랑에 빠졌네')

	def __add__(self, other):       # 연산자 오버라이딩
		print(f'{self.fullname}, {other.fullname} 결혼했네')

	def fight(self, other):
		print(f'{self.fullname}, {other.fullname} 싸우네')

	def __sub__(self, other):       # 연산자 오버라이딩
		print(f'{self.fullname}, {other.fullname} 이혼했네')


class FamilyNameKim(FamilyNameBak):     # 상속
	lastname = '김'

	def travel(self, where, day):       # 메소드 오버라이딩
		print(f'{self.fullname}, {where}여행 {day}일 가네')


a = FamilyNameBak("응용")     # FamilyNameBak의 인스턴스, 객체 a
b = FamilyNameKim("줄리엣")    # FamilyNameKim의 인스턴스, 객체 b

a.travel("부산")
b.travel("부산", 3)

a.love(b)

a + b   # 연산자 오버라이딩

a.fight(b)

a - b   # 연산자 오버라이딩
