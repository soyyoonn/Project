import random

second = 1
bang = 0    #방송
si = 0      #시청자
tsi = 0     #총시청자
sub = 0     #구독자
tsub = 0    #총구독자


a = (input("유튜브 채널 이름: "))

b = (input("오늘의 콘텐츠: "))

while bang < 20:

    print("방송 시작\n")
    bang += 1

    for second in range(11):
        si = random.randint(1,2451)+50
        print("시청자 %d명 증가\n" %si)
        tsi += si
        print("현재 총 시청자 수는 %d명\n" %tsi)

    sub = tsi / random.randint(1,5)+1
    tsub += sub
    print("%d회 방송. 현재 총 구독자 수는 %d명\n" %(bang, tsub))

if tsub >= 100000:

    print("10만 구독자 달성.실버버튼!!\n")

elif tsub < 100000:

    print("채널 폭파\n")

