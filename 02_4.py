if 4 in [1, 2, 3, 4]: print("4가 있습니다\n")

#simple.py
languages = ['python', 'perl', 'c', 'java']
for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" %lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")

a = 3
if a > 1:
    print("a is greater than 1\n")

def add(a,b):
    return a + b
print(add(3, 4))

a = 4.24E10
print(a)
b = 4.24e-10
print("%.12f" %4.24e-10)

a = 0o177   #8진수
print(a)

b = 0x8ff  #16진수
print(b)



