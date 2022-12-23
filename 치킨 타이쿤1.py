menu_list =[['후라이드치킨',18000],['양념치킨',19000],['간장치킨',19000],
       ['후라이드순살',17000],['양념치킨순살',18000],['간장치킨순살',18000],
       ['마른오징어',8000],['과일안주',15000],['포테이토 후라이',5000],['쥐포',7000],
       ['모듬튀김',12000],['테라',5000],['카스',4000],['오비라거',4500],['클라우드',4500],
       ['콜라',2500],['사이다',2000],['쿨피스',1000],['오뎅탕',4000],['떡볶이',7000]]

customer = 0
albamon = 0
refund = 0
claim = 0
money = 0
customer_sum = 0 #손님 총 주문 금액
day_sum = 0 #하루 총 매출
refund_sum = 0  #일주일 환불 금액
week_money = 0
total = 0 #총 매출
bill_list = []
max = 0

import random

print("치킨825 치킨치킨타이쿤!!!")

for week in range(1,5):#1주차 ~4주차반복
       print(week,"주차")
       if week_money > 1500000: #1주차 정산이 150만원 넘으면 알바 고용
              total += week_money
              max = week_money // 1500000
              albamon = int(input("알바 %d명 까지 고용 가능" % max))
              print(albamon, "명 고용")
              total = total - (1500000 * albamon)
       elif albamon > max:
              continue

       for day in range(7):
              day += 1
              print("%d일" %day)
              customer = random.randrange(1,101)
              if albamon > 1:
                     customer *= albamon
              print("손님 %d명" % customer)
              claim = int(customer * 0.15)
              # print("클레임: %d건" %claim)
              day_sum = 0
              # day_refund = 0   #하루 환불 금액
              print("=" * 30)

              for i in range(customer):
                     menu = random.randrange(1, 6)
                     money = 0
                     customer_sum = 0
                     refund = 0
                     for j in range(menu):
                            choice = random.randrange(0,20)
                            # print(menu_list[choice][0])
                            # print(menu_list[choice][1])
                            money = menu_list[choice][1]
                            customer_sum += money
                     bill_list.append(customer_sum)
                     # print("%d번 손님.메뉴 %d개 주문.총 %d원." %(i+1,j+1,customer_sum))
                     # print("=" * 30)
                     day_sum += customer_sum
              print("하루 총 매출: %d" %day_sum)
              # print(bill_list)
              # print("=" * 30)
              for k in range(claim):
                     a = random.choice(bill_list)
                     refund += (a * 2)
                     # day_refund += refund
              # print("환불 금액: %d" % refund)
              # bill_list.clear()
              print("=" * 30)
              # refund_sum += refund
       # print("일주일 총 환불: %s" % refund)
       # print("일주일 총 매출: %s" %(sum(bill_list) - refund))
       # print("="*30)

       week_money = (sum(bill_list) - refund) #일주일 매출
       total += week_money

print("한달 매출:%d" %total)
if total > 500000000:
       print("프랜차이즈~~~")
elif total < 500000000:
       print("게임오버")











