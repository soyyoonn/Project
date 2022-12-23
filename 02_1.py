
print("hello world")
print('python is fun')
print("""life is too short,you need python""")
print('''life is too short,you need python''')

food="python's favorite food is perl"
print(food)

say='"python is very easy." he says.'
print(say)

food='python\'s favorite food is perl'
say="\"python is very easy.\" he says."
print(food)
print(say)


multiline="life is too short\nyou need python."  #줄을바꾸는 이스케이프 코드 \n
print(multiline)

multiline='''
life is too short
you need python
'''
print(multiline)

multiline="""
life is too short
you need python
"""
print(multiline)

head="python"
tail=" is fun"
print(head+tail)

a='python'
print(a*2)

a="life is too short"
print(len(a))     #문자열 길이 구하기

a="life is too short, you need python"
print(a[0],a[12],a[-1])    #문자열 인덱싱. -1은 뒤에서부터 첫번째 문자

a="life is too short, you need python"
print(a[0:4])  #문자열 슬라이싱
print(a[5:7])
print(a[12:17])
print(a[19:])
print(a[:17])
print(a[:]) #문자열의 처음부터 끝까지

a="20010331rainy"
year=a[0:4]
day=a[4:8]
weather=a[8:]
print(year,day,weather)

a="pithon"
print(a[:1]+'y'+a[2:])