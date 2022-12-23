menu = {1:1200, 2:1900, 3:1200, 4:1100, 5:900, 6:1100, 7:1800, 8:1900, 9:1600, 10:2100, 11:1700, 12:900, 13:900, 14:1700}
money = 0
total = 0
choice = 0

money = int(input("돈을 넣어 주세요.\n"))
print("\n")

while total <= money:
    choice = int(input("메뉴를 골라주세요. 1:'콜라' 2:'우주맛콜라' 3:'제로콜라' 4:'스프라이트' 5:'환타' 6:'닥터페퍼' 7:'몬스터' 8:'파워에이드' 9:'네스티' 10:'비타민워터' 11:'미닛메이드' 12:'조지아' 13:'암바사' 14:'마테차'\n"))
    for i in menu:
        if i == choice:
            total += menu[i]
            print("%d원 중 %d원 사용.\n" %(money, total))

            if (money - total > 0):
                print("잔액 %d원.\n" % (money - total))
            # if i == 15:
            #     break
            #     print("종료.")

    if total > money:
        print("금액 초과.\n")