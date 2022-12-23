#71번
my_variable =()
print(my_variable)

#72번
movie_rank = ('닥터스트레인지','스플릿','럭키')
print(movie_rank)

#73번
num = (1,)
print(num)
print(type(num))

#74번
# 튜플은 요소값을 변경할 수 없다

#75번
t = 1, 2, 3, 4
print(type(t))  #튜플은 괄호 생략 가능

#76번
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)

#77번
interest = ('삼성전자', 'LG전자', 'SK Hynix')
a = list(interest)
print(a)

#78번
interest = ['삼성전자', 'LG전자', 'SK Hynix']
tuple1 = tuple(interest)
print(tuple1)

#79번
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

#80번
a = tuple(range(2, 100, 2))
print(a)

#81번
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(valid_score)

#82번
a, b, *valid_score = scores
print(valid_score)

#83번
a, *valid_score, b = scores
print(valid_score)

#84번
temp = { }
print(temp)

#85번
icecream = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(icecream)

#86번
icecream['죠스바'] = 1200
icecream['월드콘'] = 1500
print(icecream)

#87번
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print("메로나 가격: ", ice['메로나'])

#88번
ice['메로나'] = 1300
print(ice)

#89번
del ice['메로나']
print(ice)

#90번
#딕셔너리에 누가바가 없다

#91번
inventory ={'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}
print(inventory)

#92번
print(inventory['메로나'][0],"원")

#93번
print(inventory['메로나'][1],"개")

#94번
inventory['월드콘'] = [500,7]
print(inventory)

#95번
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
keys = list(icecream.keys())
print(keys)

#96번
values = list(icecream.values())
print(values)

#97번
print(sum(values))

#98번
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream['팥빙수'] = 2700
icecream['아맛나'] = 1000
print(icecream)
icecream.update(new_product)
print(icecream)

#99번
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

#100번
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)