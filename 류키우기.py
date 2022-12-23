import random

t = 1  #턴

g = 2  #금붕어

total = 0

b = 0    #태어난 금붕어

d = 0    #죽은 금붕어

print("류의 애칭: 홍\n")
print("류 짝꿍의 애칭: 복\n")

b = random.randrange(10)+1
g += b
print("%d턴.%d마리 태어남.총%d마리\n" %(t, b, g))

while(g <= 1000):
    t += 1
    total = g//2

    i = 0
    b2 = 0   #새로 태어난 금붕어
    while(i < total):
        b = random.randrange(5)+1 * 2
        g += b
        b2 += b
        i += 1

        if (g >= 1000):
            break
    print("%d턴.%d마리 태어남.총%d마리\n" % (t, b2,g))

    if (g >= 1000):
        print("%d턴.총%d마리\n" % (t, g))
        break

    d = random.randrange(5) + 1 * 2
    g -= d
    print("%d턴.%d마리 죽음.총%d마리\n" % (t, d, g))
    print("%d턴.총%d마리\n" % (t, g))
    if (g < 2):
        print("전멸\n")
        break
