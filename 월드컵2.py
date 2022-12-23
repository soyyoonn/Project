seedA = ['네덜란드', '잉글랜드', '아르헨티나', '프랑스', '스페인', '벨기에', '브라질', '포르투갈']
seedB = ['세네갈', '웨일스', '멕시코', '튀니지', '독일', '크로아티아', '세르비아', '우루과이']
seedC = ['에콰도르', '미국', '폴란드', '덴마크', '일본', '모로코', '카메룬', '가나']
seedD = ['카타르', '이란', '사우디', '호주', '코스타리카', '캐나다', '스위스', '대한민국']

A = ['네덜란드', '세네갈', '에콰도르', '카타르']
B = ['잉글랜드', '웨일스', '미국', '이란']
C = ['아르헨티나', '멕시코', '폴란드', '사우디']
D = ['프랑스', '튀니지', '덴마크', '호주']
E = ['스페인', '독일', '일본', '코스타리카']
F = ['벨기에', '크로아티아', '모로코', '캐나다']
G = ['브라질', '세르비아', '카메룬', '스위스']
H = ['포르투갈', '우루과이', '가나', '대한민국']

import random

score = 0
team = 0
wr = 0
game = 0
point = 0

def preround_func(team1):
    for i in range(1,4,1):
        game = random.randint(1, 3)
        point = 0
        point1 = 0
        print(team1[0]+ " vs " +team1[i])
        if game == 1:
            print(team1[0]+ " 승리")
            point += 3
        elif game == 2:
            print(team1[i]+ " 승리")
            point1 += 3
        else:
            print("무승부")
            point += 1
            point1 += 1

        print(team1[0]+ " %d점" %point)
        print(team1[i]+ " %d점" %point1)

preround_func(A)

def winrate_func(seed):
    a = random.randint(1,10)
    if a % 7 == 0:
        return seedA
    elif a % 6 == 0:
        return seedB
    elif a % 4 == 0:
        return seedC
    elif a % 2 == 0:
        return seedD
    print(a)
winrate_func()

# seedA = ['네덜란드', '잉글랜드', '아르헨티나', '프랑스', '스페인', '벨기에', '브라질', '포르투갈']
# seedB = ['세네갈', '웨일스', '멕시코', '튀니지', '독일', '크로아티아', '세르비아', '우루과이']
# seedC = ['에콰도르', '미국', '폴란드', '덴마크', '일본', '모로코', '카메룬', '가나']
# seedD = ['카타르', '이란', '사우디', '호주', '코스타리카', '캐나다', '스위스', '대한민국']

