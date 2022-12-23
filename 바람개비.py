n = int(input("밑변 길이: "))

for i in range(0,n):
    for k in range(i+1):
        print('*', end=" ")
    for j in range((n-1)-i):
        print(' ', end=" ")
    for k in range(n-i):
        print('*', end=" ")
    print(' ')
for i in range(0,n):
    for j in range((n-1)-i):
        print(' ', end=" ")
    for k in range(i+1):
        print('*', end=" ")
    for j in range(i):
        print(' ', end=" ")
    for k in range(n-i):
        print('*', end=" ")
    print(' ')