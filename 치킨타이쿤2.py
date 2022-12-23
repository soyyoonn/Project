# menu_list = [['후라이드치킨', 18000], ['양념치킨', 19000], ['간장치킨', 19000],
#              ['후라이드순살', 17000], ['양념치킨순살', 18000], ['간장치킨순살', 18000],
#              ['마른오징어', 8000], ['과일안주', 15000], ['포테이토 후라이', 5000], ['쥐포', 7000],
#              ['모듬튀김', 12000], ['테라', 5000], ['카스', 4000], ['오비라거', 4500], ['클라우드', 4500],
#              ['콜라', 2500], ['사이다', 2000], ['쿨피스', 1000], ['오뎅탕', 4000], ['떡볶이', 7000]]

import random

def day_money():
    menu_list = [['후라이드치킨', 18000], ['양념치킨', 19000], ['간장치킨', 19000],
                 ['후라이드순살', 17000], ['양념치킨순살', 18000], ['간장치킨순살', 18000],
                 ['마른오징어', 8000], ['과일안주', 15000], ['포테이토 후라이', 5000], ['쥐포', 7000],
                 ['모듬튀김', 12000], ['테라', 5000], ['카스', 4000], ['오비라거', 4500], ['클라우드', 4500],
                 ['콜라', 2500], ['사이다', 2000], ['쿨피스', 1000], ['오뎅탕', 4000], ['떡볶이', 7000]]

    customer = random.randrange(1,101)
    print("손님 %d명" % customer)
    day_sum = 0
    bill_list = []

    for i in range(customer):
          menu = random.randrange(1, 6)
          money = 0
          customer_sum = 0
          for j in range(menu):
                 choice = random.randrange(0,20)
                 print(menu_list[choice][0])
                 print(menu_list[choice][1])
                 money = menu_list[choice][1]
                 customer_sum += money
          bill_list.append(customer_sum)
          print("%d번 손님.메뉴 %d개 주문.총 %d원." %(i+1,j+1,customer_sum))
          day_sum += customer_sum #하루 총 매출
    print(bill_list)
    return day_sum

print(day_money())
