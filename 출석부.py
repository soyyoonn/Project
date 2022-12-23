name = ['강민영', '고연재', '김기태', '김명은', '김성일', '김연수', '김재일', '노도현', '류가미', \
       '박규환', '박성빈', '박시형', '박의용', '오송화', '이범규', '이보라', '이소윤', '이여름', \
       '이지혜', '이현도', '임성경', '임영효', '임홍선', '장은희', '정연우', '정철우', '주민석', '최지혁']

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', \
      '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', \
      '21', '22', '23', '24', '25', '26', '27', '28']

print(num[0], name[0])


#  출석부 만들기
name_list = []
num_list = []
name_str = ''

name_str += '강민영,'
name_str += '고연재,'
name_str += '김기태,'

print(name_str)  #추가된 이름 확인
name_list.extend(name_str.split(','))  #추가된 이름 리스트로 변경
name_list.pop()   #쉼표 제거
print(name_list)

print('\n')

print(f' kdt 2차반 출석부')
print(f'  번호    이름  ')
for i, name in enumerate(name_list, start=1):
    print(f'   {i}    {name}')

print('\n')

#for문이 어렵다면
idx = 0
name = name_list[0]
i = name_list.index(name)
print(f'   {i}    {name}',end='\t')
print(name_str.find(name))


