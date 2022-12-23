n = 2
a = int(input("정수 입력: "))

for i in range(2, a):
    if a % i == 0:
        break
    n = n + 1

if n == a:
    print("소수.\n")

else:

    print("소수 아님.\n")