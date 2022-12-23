# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를 %d번 찍었습니다" % treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다")
#
# for i in range(10):
#     treeHit = i + 1
#     print("나무를 %d번 찍었습니다" % treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다")

# coffee = 10
# money = 0
# # money = int(input("돈을 넣어주세요"))
# while True:
#     money = int(input("돈을 넣어주세요"))
#     if money == 300:
#         print("돈을 받았습니다")
#         print("커피 한 잔")
#         coffee = coffee - 1
#     elif money > 300:
#         print("돈을 받았습니다")
#         print("커피 한 잔")
#         coffee = coffee - 1
#         print("거스름돈 %d원" % (money - 300))
#     else:
#         print("돈이 부족합니다")
#         break
#     if coffee ==0:
#         print("커피가 부족합니다")
#         break

# tea = 1200
# cocoa = 300
# coffee = 500
# money = 10000
# count = 0
#
# for i in range(21):
#     for j in range(34):
#         for k in range(9):
#             if(i*500)+(j*300)+(k*1200) <= money:
#                 print(i,j,k)
#                 count += 1
#
# print(count)

tea = 1200
coffee = 500
cocoa = 300
sum = 0

# menu = {1:1200,2:500,3:300,4:'s',5:'x'}

money = int(input("돈을 넣어 주세요."))

while sum <= money:
    choice = int(input("메뉴를 골라주세요. 1:'유자차' 2:'커피' 3:'코코아' 4:'계산' 5:'종료'"))
    if choice == 1:
        print("유자차 선택")
        sum += tea
    elif choice == 2:
        print("커피 선택")
        sum += coffee
    elif choice == 3:
        print("코코아 선택")
        sum += cocoa
    elif choice == 4:
        print("총 %d원 계산하기" %sum)
        change = money - sum
        print("잔돈 %d원" %change)
    else:
        break

print("금액초과")