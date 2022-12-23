# a = []
# a = input("영어 이름 입력")
# print(a[3:6])
# a_list = a
# print(a[:3]+a[6:])

count = {}
a = input("영어 이름 입력")
b = list(a.upper())
c = list(set(b))
for chr in a:
    if chr in count:
        count[chr] += 1
    else:
        count[chr] = 1
print(count)
