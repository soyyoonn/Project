name = []
name_str = ''
name_str += '장은희 '
print(name_str)
name_str += '이소윤 '
print(name_str)
name_str += '류가미 '
print(name_str)
name_str += '김명은 '
print(name_str)
name.extend(name_str.split( ))
print(name)

tuple = (name[0],name[1],name[2],name[3])
print(tuple)

a = ('장은희',)
print(a)
a = a + ('이소윤',)
print(a)

dic ={1:'장은희',2:'이소윤',3:'류가미',4:'김명은'}
print(dic[1])
print(dic[1],dic[2])
print(dic[1],dic[2],dic[3])
print(dic[1],dic[2],dic[3],dic[4])


name_dict = dict()
num_list = []

idx = 0
idx += 1
name_dict[idx] = '고연재'
idx += 1
name_dict[idx] = '김기태'
idx += 1
name_dict[idx] = '강민영'    #딕셔너리 한명씩 추가해서 만드는 법

print(name_dict)
print(name_dict.keys())
print(name_dict.values())

# name = list(name_dict.values())
# print(name)
# name.sort()
# print(name)
#
# print(f'{name[0]}님의 출석번호는{}이고, 가입순서는{}')

#출석번호찾기
temp = list(name_dict.values())  #밸류값 이름을 리스트로 만들어서 temp 에 저장
print(temp)
temp_sort = sorted(temp)    #이름을 순서대로 정렬한 값을 temp_sort 에 저장
print(temp_sort)

idx = 0
for value in temp_sort:
    idx += 1
    print(f'{value}님의 출석번호는 {idx}이고, 가입순서는 {temp.index(value)+1}')