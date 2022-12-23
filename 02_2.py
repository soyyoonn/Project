a = 'Hobby'
b = list("Hobby")     # b = ["H","o","b","b","y"]
a.find('H'),a.find('o'),a.find('b'),a.find('y')
a.index('H'),a.index('o'),a.index('b'),a.index('y')
a.count('H'),a.count('o'),a.count('b'),a.count('y')
a.upper()
a.lower()

print(a.find('H'),a.index('H'),a.count('H'))
print(a.find('o'),a.index('o'),a.count('o'))
print(a.find('b'),a.index('b'),a.count('b'))
print(a.find('y'),a.index('y'),a.count('y'))
print(a.upper(),a.lower())

print(b[0],b[1],b[2],b[3],b[4])

a = "Hobby"

cnt = a.lower().count('h')    # cnt = a.count(a[0])
idx = a.lower().index('h')    # idx = a.index(a[0])
print(a[0],f'count:{cnt} index:{idx}')    # print(a[0], "count:", cnt, "index:", idx)



# str = "Hobby"
# str_list = list(str)
#
# print(str_list)
# print(f"배열의 길이: {len(str_list)}")
#
# for i in str_list:
#     print(f"{i}의 위치: {str_list.index(i)}", end=" ")
#     print(f"{i}의 갯수: {str_list.count(i)}")
#     if str_list.count(i) > 1:
#         str_list[str_list.index(i)] = 0



