import random
bill_list = []
total_Money = 0

def day_money(alba): #이소윤
    menu_list = [['후라이드치킨', 18000], ['양념치킨', 19000], ['간장치킨', 19000],
                 ['후라이드순살', 17000], ['양념치킨순살', 18000], ['간장치킨순살', 18000],
                 ['마른오징어', 8000], ['과일안주', 15000], ['포테이토 후라이', 5000], ['쥐포', 7000],
                 ['모듬튀김', 12000], ['테라', 5000], ['카스', 4000], ['오비라거', 4500], ['클라우드', 4500],
                 ['콜라', 2500], ['사이다', 2000], ['쿨피스', 1000], ['오뎅탕', 4000], ['떡볶이', 7000]]

    customer = random.randrange(1,101)
    if alba >= 1:
        customer *= alba
    print("손님 %d명" % customer)
    day_sum = 0

    for i in range(customer):
        menu = random.randrange(1, 6)
        money = 0
        customer_sum = 0
        for j in range(menu):
            choice = random.randrange(0,20)
            # print(menu_list[choice][0])
            # print(menu_list[choice][1])
            money = menu_list[choice][1]
            customer_sum += money
        bill_list.append(customer_sum)
        # print("%d번 손님.메뉴 %d개 주문.총 %d원." %(i+1,j+1,customer_sum))
        day_sum += customer_sum
    day_sum -= claim(customer)
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
            return alba

def sevendaySale(): #이범규
    total_Money = 0
    alba = 0
    for i in range (0,4):
        if i>=1:
            alba=alba_employment(total_Money)
            for j in range(0, 7):
                total_Money += day_money(alba)

        else:
            for j in range (0,7):
                total_Money+=day_money(alba)

        print('{}주차 매출은 {}입니다'.format(i + 1, total_Money))
    return total_Money

total_Money = sevendaySale()
if total_Money>500000000:
    print('프랜차이즈로 가즈아')
else:
    print('폐업 ㅠㅠ')



