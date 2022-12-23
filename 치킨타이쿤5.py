import random
bill_list = []
total_Money = 0

def day_money(alba,ad): #이소윤
    menu_list = [['후라이드치킨', 18000], ['양념치킨', 19000], ['간장치킨', 19000],
                 ['후라이드순살', 17000], ['양념치킨순살', 18000], ['간장치킨순살', 18000],
                 ['마른오징어', 8000], ['과일안주', 15000], ['포테이토 후라이', 5000], ['쥐포', 7000],
                 ['모듬튀김', 12000], ['테라', 5000], ['카스', 4000], ['오비라거', 4500], ['클라우드', 4500],
                 ['콜라', 2500], ['사이다', 2000], ['쿨피스', 1000], ['오뎅탕', 4000], ['떡볶이', 7000]]
    nego = random.randrange(0,999)  #네고왕이벤트 변수 이범규
    customer = random.randrange(1,101)

    if alba >= 1:
       customer *= alba
       customer += ad
    else:
       customer += ad



    print("손님 %d명" % customer)
    day_sum = 0
    count = 0
    bonus_price = 0
    if nego==7:
        print('네고왕 이벤트!! 금일 모든메뉴 반값')
    for i in range(customer):
        menu = random.randrange(1, 6)
        money = 0
        customer_sum = 0
        for j in range(menu):
            choice = random.randrange(0,20)
            # print(menu_list[choice][0])
            # print(menu_list[choice][1])
            if nego == 7:
                money = int(menu_list[choice][1] * 0.5)
            else:
                money = menu_list[choice][1]
            customer_sum += money
        bill_list.append(customer_sum)
        count += 1
        bonus_price += bonus(count)
        # print("%d번 손님.메뉴 %d개 주문.총 %d원." %(i+1,j+1,customer_sum))
        day_sum += customer_sum
    day_sum -= claim(customer)
    day_sum -= bonus_price
    print('금일매출 {}원'.format(day_sum))

    return day_sum



def claim(customer): #최지혁
    refund = 0
    for i in range(0, int(customer * 0.15)):
        b = random.choice(bill_list)
        refund += 2 * b
        bill_list.remove(b)
    bill_list.clear() #추가
    print('금일 환불금액 {}원'.format(refund))
    return refund

def bonus(count):
    if count % 700 == 0:
        print(count,"번째 손님 당첨")
        print("☆★후라이드 치킨 서비스★☆")
        return 18000
    else:
        return 0

def alba_employment(total): #오송화
    if total>1500000:

        while True:
            max_alba=total//1500000
            print('한주차가지났습니다')
            alba=int(input("알바를 몇명 고용하시겠습니까?, 최대 %d명 뽑을 수 있습니다"%max_alba))#수정
            if alba>max_alba:
                print("최대 고용인원을 초과했습니다")
                continue
            total=total-(1500000*alba)
            # print("알바 수: ",alba)
            # print("알바비 뺀 매출: ",total)
            return alba,total

def advertisement (total):    #광고 이벤트
    benefit = 0
    while total>10000000:
        print(f"현재 잔고 : {total:,}")
        print("광고를 할 수 있어요!, TV 1번 유튜브 2번 인스타 3번")
        if total > 100000000:
            choice=int(input("TV, 유튜브, 인스타 광고를 할 수 있습니다., 종료는 0"))
            if choice == 1:
                total -= 100000000
                benefit += 8000
                continue
            elif choice == 2:
                total -= 50000000
                benefit += 4000
                continue
            elif choice == 3:
                total -= 10000000
                benefit += 1000
                continue
            else:
                break

        elif total > 50000000:
            choice=int(input("유튜브와 인스타 광고를 할 수 있습니다. 종료는 0"))
            if choice == 2:
                total -= 50000000
                benefit += 4000
                continue
            elif choice == 3:
                total -= 10000000
                benefit += 1000
                continue
            else:
                break
        elif total > 10000000:
            choice=int(input("인스타 광고를 할 수 있습니다. 종료는 0"))
            if choice ==3:
                total -= 10000000
                benefit += 1000
                continue
            else:
                break
        else:
            break
    return benefit, total

def sevendaySale(): #이범규
    total_Money = 0
    alba = 0
    ad = 0
    for i in range (0,4):
        if i>=1:
            alba , total_Money = alba_employment(total_Money)
            ad , total_Money = advertisement(total_Money)

            for j in range(0, 7):
                total_Money += day_money(alba,ad)

        else:
            for j in range (0,7):
                total_Money+=day_money(alba,ad)

        print('{}주차 매출은 {}입니다'.format(i + 1, total_Money))
    return total_Money



total_Money = sevendaySale()
if total_Money>500000000:
    print('프랜차이즈로 가즈아')
else:
    print('폐업 ㅠㅠ')