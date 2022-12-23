# import random
#
# def change(student):
#     num = random.randint(0, len(student)-1)
#     return student.pop(num)
#
# student=['강민영','김성일','박규환','이보라','이현도','김기태','김명은','박성빈','이지혜','임영효','김연수','김재일','고연재','류가미','박의용','노도현','박시형','주민석','이여름','임성경','이범규','장은희','정연우','최지혁','이소윤','임홍선','오송화','정철우']
#
# print("분리수거 %s %s  " %(change(student), change(student)))
# print("쓸기 %s  " %change(student))
# print("닦기 %s  " %change(student))

import random

student = ['강민영','김성일','박규환','이보라','이현도','김기태','김명은','박성빈','이지혜','임영효','김연수','김재일','고연재','류가미','박의용','노도현','박시형','주민석','이여름','임성경','이범규','장은희','정연우','최지혁','이소윤','임홍선','오송화','정철우']

random.shuffle(student)

print("분리수거 ", student.pop(0),student.pop(0))
print("닦기 ", student.pop(0))
print("쓸기 ", student.pop(0))



