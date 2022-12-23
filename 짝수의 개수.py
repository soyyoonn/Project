# a = input("영어 입력")
# b = int(input("숫자 입력"))
# c = ord(a) * b
# print(str(c).zfill(8))


# a = input("영어 입력")
# print(hex(ord(a)))

#짝수의 개수
even = 0
while True:
    num = int(input("숫자를 입력하세요: "))

    if num == 0:
        break
    else:
        if num % 2 == 0:
            even += 1

print(f"짝수는 {even}개")