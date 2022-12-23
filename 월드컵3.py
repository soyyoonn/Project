A = ['네덜란드', '세네갈', '에콰도르', '카타르']
B = ['잉글랜드', '웨일스', '미국', '이란']
C = ['아르헨티나', '멕시코', '폴란드', '사우디']
D = ['프랑스', '튀니지', '덴마크', '호주']
E = ['스페인', '독일', '일본', '코스타리카']
F = ['벨기에', '크로아티아', '모로코', '캐나다']
G = ['브라질', '세르비아', '카메룬', '스위스']
H = ['포르투갈', '우루과이', '가나', '대한민국']

seedA = ['네덜란드', '잉글랜드', '아르헨티나', '프랑스', '스페인', '벨기에', '브라질', '포르투갈']
seedB = ['세네갈', '웨일스', '멕시코', '튀니지', '독일', '크로아티아', '세르비아', '우루과이']
seedC = ['에콰도르', '미국', '폴란드', '덴마크', '일본', '모로코', '카메룬', '가나']
seedD = ['카타르', '이란', '사우디', '호주', '코스타리카', '캐나다', '스위스', '대한민국']

import random

score = 0
team = 0
wr = 0
game = 0

a1 = a2 = a3 = a4 = 0
b1 = b2 = b3 = b4 = 0
c1 = c2 = c3 = c4 = 0
d1 = d2 = d3 = d4 = 0
e1 = e2 = e3 = e4 = 0
f1 = f2 = f3 = f4 = 0
g1 = g2 = g3 = g4 = 0
h1 = h2 = h3 = h4 = 0

seedA = random.randint(1,10)
seedB = random.randint(1,10)
seedC = random.randint(1,10)
seedD = random.randint(1,10)

print("A조 예선")

print("네덜란드 vs 세네갈")
if seedA < 8 and seedB >= 7:
    print("네덜란드 승리")
    a1 += 3
elif seedA >=8 and seedB < 7:
    print("세네갈 승리")
    a2 += 3
elif seedA >= 8 and seedB >= 7:
    print("무승부")
    a1 += 1
    a2 += 1
elif seedA < 8 and seedB < 7:
    print("무승부")
    a1 += 1
    a2 += 1

print("네덜란드 %d점" %a1)
print("세네갈 %d점" %a2)

print("="*30)

print("네덜란드 vs 에콰도르")
if seedA < 8 and seedC >= 5:
    print("네덜란드 승리")
    a1 += 3
elif seedA >=8 and seedC < 5:
    print("에콰도르 승리")
    a3 += 3
elif seedA >= 8 and seedC >= 5:
    print("무승부")
    a1 += 1
    a3 += 1
elif seedA < 8 and seedC < 5:
    print("무승부")
    a1 += 1
    a3 += 1

print("네덜란드 %d점" %a1)
print("에콰도르 %d점" %a3)

print("="*30)

print("네덜란드 vs 카타르")
if seedA < 8 and seedD >= 3:
    print("네덜란드 승리")
    a1 += 3
elif seedA >=8 and seedD < 3:
    print("카타르 승리")
    a4 += 3
elif seedA >= 8 and seedD >= 3:
    print("무승부")
    a1 += 1
    a4 += 1
elif seedA < 8 and seedD < 3:
    print("무승부")
    a1 += 1
    a4 += 1

print("네덜란드 %d점" %a1)
print("카타르 %d점" %a4)

print("="*30)

print("세네갈 vs 에콰도르")
if seedB < 7 and seedC >= 5:
    print("세네갈 승리")
    a2 += 3
elif seedB >=7 and seedC < 5:
    print("에콰도르 승리")
    a3 += 3
elif seedB >= 7 and seedC >= 5:
    print("무승부")
    a2 += 1
    a3 += 1
elif seedB < 7 and seedC < 5:
    print("무승부")
    a2 += 1
    a3 += 1

print("세네갈 %d점" %a2)
print("에콰도르 %d점" %a3)

print("="*30)

print("세네갈 vs 카타르")
if seedB < 7 and seedD >= 3:
    print("세네갈 승리")
    a2 += 3
elif seedB >=7 and seedD < 3:
    print("카타르 승리")
    a4 += 3
elif seedB >= 7 and seedD >= 3:
    print("무승부")
    a2 += 1
    a4 += 1
elif seedB < 7 and seedD < 3:
    print("무승부")
    a2 += 1
    a4 += 1

print("세네갈 %d점" %a2)
print("카타르 %d점" %a4)

print("="*30)

print("에콰도르 vs 카타르")
if seedC < 5 and seedD >= 3:
    print("에콰도르 승리")
    a3 += 3
elif seedC >=5 and seedD < 3:
    print("카타르 승리")
    a4 += 3
elif seedC >= 5 and seedD >= 3:
    print("무승부")
    a3 += 1
    a4 += 1

print("에콰도르 %d점" %a3)
print("카타르 %d점" %a4)

print("="*30)

print(f'{A[0]}:{a1} ' f'{A[1]}:{a2} ' f'{A[2]}: {a3} ' f'{A[3]}: {a4} ')
A = {'네덜란드':a1,'세네갈':a2,'에콰도르':a3,'카타르':a4}
# A1 = sorted(A.items(),key=operator.itemgetter(1),reverse=True)
print("16강 진출 :",max(A,key=A.get))
maxA = max(A,key=A.get)
del A[max(A,key=A.get)]
maxA2 = max(A,key=A.get)
print("16강 진출:",max(A,key=A.get))

print("="*30)

seedA = random.randint(1,10)
seedB = random.randint(1,10)
seedC = random.randint(1,10)
seedD = random.randint(1,10)

print("B조 예선")

print("잉글랜드 vs 웨일스")
if seedA < 8 and seedB >= 7:
    print("잉글랜드 승리")
    b1 += 3
elif seedA >=8 and seedB < 7:
    print("웨일스 승리")
    b2 += 3
elif seedA >= 8 and seedB >= 7:
    print("무승부")
    b1 += 1
    b2 += 1
elif seedA < 8 and seedB < 7:
    print("무승부")
    b1 += 1
    b2 += 1

print("잉글랜드 %d점" %b1)
print("웨일스 %d점" %b2)

print("="*30)

print("잉글랜드 vs 미국")
if seedA < 8 and seedC >= 5:
    print("잉글랜드 승리")
    b1 += 3
elif seedA >=8 and seedC < 5:
    print("미국 승리")
    b3 += 3
elif seedA >= 8 and seedC >= 5:
    print("무승부")
    b1 += 1
    b3 += 1
elif seedA < 8 and seedC < 5:
    print("무승부")
    b1 += 1
    b3 += 1

print("잉글랜드 %d점" %b1)
print("미국 %d점" %b3)

print("="*30)

print("잉글랜드 vs 이란")
if seedA < 8 and seedD >= 3:
    print("잉글랜드 승리")
    b1 += 3
elif seedA >=8 and seedD < 3:
    print("이란 승리")
    b4 += 3
elif seedA >= 8 and seedD >= 3:
    print("무승부")
    b1 += 1
    b4 += 1
elif seedA < 8 and seedD < 3:
    print("무승부")
    b1 += 1
    b4 += 1

print("잉글랜드 %d점" %b1)
print("이란 %d점" %b4)

print("="*30)

print("웨일스 vs 미국")
if seedB < 7 and seedC >= 5:
    print("웨일스 승리")
    b2 += 3
elif seedB >=7 and seedC < 5:
    print("미국 승리")
    b3 += 3
elif seedB >= 7 and seedC >= 5:
    print("무승부")
    b2 += 1
    b3 += 1
elif seedB < 7 and seedC < 5:
    print("무승부")
    b2 += 1
    b3 += 1

print("웨일스 %d점" %b2)
print("미국 %d점" %b3)

print("="*30)

print("웨일스 vs 이란")
if seedB < 7 and seedD >= 3:
    print("웨일스 승리")
    b2 += 3
elif seedB >=7 and seedD < 3:
    print("이란 승리")
    b4 += 3
elif seedB >= 7 and seedD >= 3:
    print("무승부")
    b2 += 1
    b4 += 1
elif seedB < 7 and seedD < 3:
    print("무승부")
    b2 += 1
    b4 += 1

print("웨일스 %d점" %b2)
print("이란 %d점" %b4)

print("="*30)

print("미국 vs 이란")
if seedC < 5 and seedD >= 3:
    print("미국 승리")
    b3 += 3
elif seedC >=5 and seedD < 3:
    print("이란 승리")
    b4 += 3
elif seedC >= 5 and seedD >= 3:
    print("무승부")
    b3 += 1
    b4 += 1
elif seedC < 5 and seedD < 3:
    print("무승부")
    b3 += 1
    b4 += 1

print("미국 %d점" %b3)
print("이란 %d점" %b4)

print("="*30)

print(f'{B[0]}:{b1} ' f'{B[1]}:{b2} ' f'{B[2]}: {b3} ' f'{B[3]}: {b4} ')
B = {'잉글랜드':b1, '웨일스':b2, '미국':b3, '이란':b4}
print("16강 진출 :",max(B,key=B.get))
maxB = max(B,key=B.get)
del B[max(B,key=B.get)]
print("16강 진출 :",max(B,key=B.get))
maxB2 = max(B,key=B.get)

print("="*30)

seedA = random.randint(1,10)
seedB = random.randint(1,10)
seedC = random.randint(1,10)
seedD = random.randint(1,10)

print("C조 예선")

print("아르헨티나 vs 멕시코")
if seedA < 8 and seedB >= 7:
    print("아르헨티나 승리")
    c1 += 3
elif seedA >=8 and seedB < 7:
    print("멕시코 승리")
    c2 += 3
elif seedA >= 8 and seedB >= 7:
    print("무승부")
    c1 += 1
    c2 += 1
elif seedA < 8 and seedB < 7:
    print("무승부")
    c1 += 1
    c2 += 1

print("아르헨티나 %d점" %c1)
print("멕시코 %d점" %c2)

print("="*30)

print("아르헨티나 vs 폴란드")
if seedA < 8 and seedC >= 5:
    print("아르헨티나 승리")
    c1 += 3
elif seedA >=8 and seedC < 5:
    print("폴란드 승리")
    c3 += 3
elif seedA >= 8 and seedC >= 5:
    print("무승부")
    c1 += 1
    c3 += 1
elif seedA < 8 and seedC < 5:
    print("무승부")
    c1 += 1
    c3 += 1

print("아르헨티나 %d점" %c1)
print("폴란드 %d점" %c3)

print("="*30)

print("아르헨티나 vs 사우디")
if seedA < 8 and seedD >= 3:
    print("아르헨티나 승리")
    c1 += 3
elif seedA >=8 and seedD < 3:
    print("사우디 승리")
    c4 += 3
elif seedA >= 8 and seedD >= 3:
    print("무승부")
    c1 += 1
    c4 += 1
elif seedA < 8 and seedD < 3:
    print("무승부")
    c1 += 1
    c4 += 1

print("아르헨티나 %d점" %c1)
print("사우디 %d점" %c4)

print("="*30)

print("멕시코 vs 폴란드")
if seedB < 7 and seedC >= 5:
    print("멕시코 승리")
    c2 += 3
elif seedB >=7 and seedC < 5:
    print("폴란드 승리")
    c3 += 3
elif seedB >= 7 and seedC >= 5:
    print("무승부")
    c2 += 1
    c3 += 1
elif seedB < 7 and seedC < 5:
    print("무승부")
    c2 += 1
    c3 += 1

print("멕시코 %d점" %c2)
print("폴란드 %d점" %c3)

print("="*30)

print("멕시코 vs 사우디")
if seedB < 7 and seedD >= 3:
    print("멕시코 승리")
    c2 += 3
elif seedB >= 7 and seedD < 3:
    print("사우디 승리")
    c4 += 3
elif seedB >= 7 and seedD >= 3:
    print("무승부")
    c2 += 1
    c4 += 1
elif seedB < 7 and seedD < 3:
    print("무승부")
    c2 += 1
    c4 += 1

print("멕시코 %d점" % c2)
print("사우디 %d점" % c4)

print("="*30)

print("폴란드 vs 사우디")
if seedC < 5 and seedD >= 3:
    print("폴란드 승리")
    c3 += 3
elif seedC >=5 and seedD < 3:
    print("사우디 승리")
    c4 += 3
elif seedC >= 5 and seedD >= 3:
    print("무승부")
    c3 += 1
    c4 += 1
elif seedC < 5 and seedD < 3:
    print("무승부")
    c3 += 1
    c4 += 1

print("폴란드 %d점" %c3)
print("사우디 %d점" %c4)

print("="*30)

print(f'{C[0]}:{c1} ' f'{C[1]}:{c2} ' f'{C[2]}: {c3} ' f'{C[3]}: {c4} ')
C = {'아르헨티나':c1, '멕시코':c2, '폴란드':c3, '사우디':c4}
print("16강 진출 :",max(C,key=C.get))
maxC = max(C,key=C.get)
del C[max(C,key=C.get)]
print("16강 진출 :",max(C,key=C.get))
maxC2 = max(C,key=C.get)

print("="*30)

seedA = random.randint(1,10)
seedB = random.randint(1,10)
seedC = random.randint(1,10)
seedD = random.randint(1,10)

print("D조 예선")

print("프랑스 vs 튀니지")
if seedA < 8 and seedB >= 7:
    print("프랑스 승리")
    d1 += 3
elif seedA >=8 and seedB < 7:
    print("튀니지 승리")
    d2 += 3
elif seedA >= 8 and seedB >= 7:
    print("무승부")
    d1 += 1
    d2 += 1
elif seedA < 8 and seedB < 7:
    print("무승부")
    d1 += 1
    d2 += 1

print("프랑스 %d점" %d1)
print("튀니지 %d점" %d2)

print("="*30)

print("프랑스 vs 덴마크")
if seedA < 8 and seedC >= 5:
    print("프랑스 승리")
    d1 += 3
elif seedA >=8 and seedC < 5:
    print("덴마크 승리")
    d3 += 3
elif seedA >= 8 and seedC >= 5:
    print("무승부")
    d1 += 1
    d3 += 1
elif seedA < 8 and seedC < 5:
    print("무승부")
    d1 += 1
    d3 += 1

print("프랑스 %d점" %d1)
print("덴마크 %d점" %d3)

print("="*30)

print("프랑스 vs 호주")
if seedA < 8 and seedD >= 3:
    print("프랑스 승리")
    d1 += 3
elif seedA >=8 and seedD < 3:
    print("호주 승리")
    d4 += 3
elif seedA >= 8 and seedD >= 3:
    print("무승부")
    d1 += 1
    d4 += 1
elif seedA < 8 and seedD < 3:
    print("무승부")
    d1 += 1
    d4 += 1

print("프랑스 %d점" %d1)
print("호주 %d점" %d4)

print("="*30)

print("튀니지 vs 덴마크")
if seedB < 7 and seedC >= 5:
    print("튀니지 승리")
    d2 += 3
elif seedB >=7 and seedC < 5:
    print("덴마크 승리")
    d3 += 3
elif seedB >= 7 and seedC >= 5:
    print("무승부")
    d2 += 1
    d3 += 1
elif seedB < 7 and seedC < 5:
    print("무승부")
    d2 += 1
    d3 += 1

print("튀니지 %d점" %d2)
print("덴마크 %d점" %d3)

print("="*30)

print("튀니지 vs 호주")
if seedB < 7 and seedD >= 3:
    print("튀니지 승리")
    d2 += 3
elif seedB >= 7 and seedD < 3:
    print("호주 승리")
    d4 += 3
elif seedB >= 7 and seedD >= 3:
    print("무승부")
    d2 += 1
    d4 += 1
elif seedB < 7 and seedD < 3:
    print("무승부")
    d2 += 1
    d4 += 1

print("튀니지 %d점" % d2)
print("호주 %d점" % d4)

print("="*30)

print("덴마크 vs 호주")
if seedC < 5 and seedD >= 3:
    print("덴마크 승리")
    d3 += 3
elif seedC >=5 and seedD < 3:
    print("호주 승리")
    d4 += 3
elif seedC >= 5 and seedD >= 3:
    print("무승부")
    d3 += 1
    d4 += 1
elif seedC < 5 and seedD < 3:
    print("무승부")
    d3 += 1
    d4 += 1

print("덴마크 %d점" % d3)
print("호주 %d점" % d4)

print("="*30)

print(f'{D[0]}:{d1} ' f'{D[1]}:{d2} ' f'{D[2]}: {d3} ' f'{D[3]}: {d4} ')
D = {'프랑스':d1, '튀니지':d2, '덴마크':d3, '호주':d4}
print("16강 진출 :",max(D,key=D.get))
maxD = max(D,key=D.get)
del D[max(D,key=D.get)]
print("16강 진출 :",max(D,key=D.get))
maxD2 = max(D,key=D.get)

print("="*30)

seedA = random.randint(1,10)
seedB = random.randint(1,10)
seedC = random.randint(1,10)
seedD = random.randint(1,10)

print("E조 예선")

print("스페인 vs 독일")
if seedA < 8 and seedB >= 7:
    print("스페인 승리")
    e1 += 3
elif seedA >= 8 and seedB < 7:
    print("독일 승리")
    e2 += 3
elif seedA >= 8 and seedB >= 7:
    print("무승부")
    e1 += 1
    e2 += 1
elif seedA < 8 and seedB < 7:
    print("무승부")
    e1 += 1
    e2 += 1

print("스페인 %d점" % e1)
print("독일 %d점" % e2)

print("="*30)

print("스페인 vs 일본")
if seedA < 8 and seedC >= 5:
    print("스페인 승리")
    e1 += 3
elif seedA >=8 and seedC < 5:
    print("일본 승리")
    e3 += 3
elif seedA >= 8 and seedC >= 5:
    print("무승부")
    e1 += 1
    e3 += 1
elif seedA < 8 and seedC < 5:
    print("무승부")
    e1 += 1
    e3 += 1

print("스페인 %d점" % e1)
print("일본 %d점" % e3)

print("="*30)

print("스페인 vs 코스타리카")
if seedA < 8 and seedD >= 3:
    print("스페인 승리")
    e1 += 3
elif seedA >=8 and seedD < 3:
    print("코스타리카 승리")
    e4 += 3
elif seedA >= 8 and seedD >= 3:
    print("무승부")
    e1 += 1
    e4 += 1
elif seedA < 8 and seedD < 3:
    print("무승부")
    e1 += 1
    e4 += 1

print("스페인 %d점" % e1)
print("코스타리카 %d점" % e4)

print("="*30)

print("독일 vs 일본")
if seedB < 7 and seedC >= 5:
    print("독일 승리")
    e2 += 3
elif seedB >=7 and seedC < 5:
    print("일본 승리")
    e3 += 3
elif seedB >= 7 and seedC >= 5:
    print("무승부")
    e2 += 1
    e3 += 1
elif seedB < 7 and seedC < 5:
    print("무승부")
    e2 += 1
    e3 += 1

print("독일 %d점" % e2)
print("일본 %d점" % e3)

print("="*30)

print("독일 vs 코스타리카")
if seedB < 7 and seedD >= 3:
    print("독일 승리")
    e2 += 3
elif seedB >= 7 and seedD < 3:
    print("코스타리카 승리")
    e4 += 3
elif seedB >= 7 and seedD >= 3:
    print("무승부")
    e2 += 1
    e4 += 1
elif seedB < 7 and seedD < 3:
    print("무승부")
    e2 += 1
    e4 += 1

print("독일 %d점" % e2)
print("코스타리카 %d점" % e4)

print("="*30)

print("일본 vs 코스타리카")
if seedC < 5 and seedD >= 3:
    print("일본 승리")
    e3 += 3
elif seedC >=5 and seedD < 3:
    print("코스타리카 승리")
    e4 += 3
elif seedC >= 5 and seedD >= 3:
    print("무승부")
    e3 += 1
    e4 += 1
elif seedC < 5 and seedD < 3:
    print("무승부")
    e3 += 1
    e4 += 1

print("일본 %d점" % e3)
print("코스타리카 %d점" % e4)

print("="*30)

print(f'{E[0]}:{e1} ' f'{E[1]}:{e2} ' f'{E[2]}: {e3} ' f'{E[3]}: {e4} ')
E = {'스페인':e1, '독일':e2, '일본':e3, '코스타리카':e4}
print("16강 진출 :",max(E,key=E.get))
maxE = max(E,key=E.get)
del E[max(E,key=E.get)]
print("16강 진출 :",max(E,key=E.get))
maxE2 = max(E,key=E.get)

print("="*30)

seedA = random.randint(1,10)
seedB = random.randint(1,10)
seedC = random.randint(1,10)
seedD = random.randint(1,10)

print("F조 예선")

print("벨기에 vs 크로아티아")
if seedA < 8 and seedB >= 7:
    print("벨기에 승리")
    f1 += 3
elif seedA >= 8 and seedB < 7:
    print("크로아티아 승리")
    f2 += 3
elif seedA >= 8 and seedB >= 7:
    print("무승부")
    f1 += 1
    f2 += 1
elif seedA < 8 and seedB < 7:
    print("무승부")
    f1 += 1
    f2 += 1

print("벨기에 %d점" % f1)
print("크로아티아 %d점" % f2)

print("="*30)

print("벨기에 vs 모로코")
if seedA < 8 and seedC >= 5:
    print("벨기에 승리")
    f1 += 3
elif seedA >=8 and seedC < 5:
    print("모로코 승리")
    f3 += 3
elif seedA >= 8 and seedC >= 5:
    print("무승부")
    f1 += 1
    f3 += 1
elif seedA < 8 and seedC < 5:
    print("무승부")
    f1 += 1
    f3 += 1

print("벨기에 %d점" % f1)
print("모로코 %d점" % f3)

print("="*30)

print("벨기에 vs 캐나다")
if seedA < 8 and seedD >= 3:
    print("벨기에 승리")
    f1 += 3
elif seedA >=8 and seedD < 3:
    print("캐나다 승리")
    f4 += 3
elif seedA >= 8 and seedD >= 3:
    print("무승부")
    f1 += 1
    f4 += 1
elif seedA < 8 and seedD < 3:
    print("무승부")
    f1 += 1
    f4 += 1

print("벨기에 %d점" % f1)
print("캐나다 %d점" % f4)

print("="*30)

print("크로아티아 vs 모로코")
if seedB < 7 and seedC >= 5:
    print("크로아티아 승리")
    f2 += 3
elif seedB >=7 and seedC < 5:
    print("모로코 승리")
    f3 += 3
elif seedB >= 7 and seedC >= 5:
    print("무승부")
    f2 += 1
    f3 += 1
elif seedB < 7 and seedC < 5:
    print("무승부")
    f2 += 1
    f3 += 1

print("크로아티아 %d점" % f2)
print("모로코 %d점" % f3)

print("="*30)

print("크로아티아 vs 캐나다")
if seedB < 7 and seedD >= 3:
    print("크로아티아 승리")
    f2 += 3
elif seedB >= 7 and seedD < 3:
    print("캐나다 승리")
    f4 += 3
elif seedB >= 7 and seedD >= 3:
    print("무승부")
    f2 += 1
    f4 += 1
elif seedB < 7 and seedD < 3:
    print("무승부")
    f2 += 1
    f4 += 1

print("크로아티아 %d점" % f2)
print("캐나다 %d점" % f4)

print("="*30)

print("모로코 vs 캐나다")
if seedC < 5 and seedD >= 3:
    print("모로코 승리")
    f3 += 3
elif seedC >=5 and seedD < 3:
    print("캐나다 승리")
    f4 += 3
elif seedC >= 5 and seedD >= 3:
    print("무승부")
    f3 += 1
    f4 += 1
elif seedC < 5 and seedD < 3:
    print("무승부")
    f3 += 1
    f4 += 1

print("모로코 %d점" % f3)
print("캐나다 %d점" % f4)

print("="*30)

print(f'{F[0]}:{f1} ' f'{F[1]}:{f2} ' f'{F[2]}: {f3} ' f'{F[3]}: {f4} ')
F = {'벨기에':f1, '크로아티아':f2, '모로코':f3, '캐나다':f4}
print("16강 진출 :",max(F,key=F.get))
maxF = max(F,key=F.get)
del F[max(F,key=F.get)]
print("16강 진출 :",max(F,key=F.get))
maxF2 = max(F,key=F.get)

print("="*30)

seedA = random.randint(1,10)
seedB = random.randint(1,10)
seedC = random.randint(1,10)
seedD = random.randint(1,10)

print("G조 예선")

print("브라질 vs 세르비아")
if seedA < 8 and seedB >= 7:
    print("브라질 승리")
    g1 += 3
elif seedA >= 8 and seedB < 7:
    print("세르비아 승리")
    g2 += 3
elif seedA >= 8 and seedB >= 7:
    print("무승부")
    g1 += 1
    g2 += 1
elif seedA < 8 and seedB < 7:
    print("무승부")
    g1 += 1
    g2 += 1

print("브라질 %d점" % g1)
print("세르비아 %d점" % g2)

print("="*30)

print("브라질 vs 카메룬")
if seedA < 8 and seedC >= 5:
    print("브라질 승리")
    g1 += 3
elif seedA >=8 and seedC < 5:
    print("카메룬 승리")
    g3 += 3
elif seedA >= 8 and seedC >= 5:
    print("무승부")
    g1 += 1
    g3 += 1
elif seedA < 8 and seedC < 5:
    print("무승부")
    g1 += 1
    g3 += 1

print("브라질 %d점" % g1)
print("카메룬 %d점" % g3)

print("="*30)

print("브라질 vs 스위스")
if seedA < 8 and seedD >= 3:
    print("브라질 승리")
    g1 += 3
elif seedA >=8 and seedD < 3:
    print("스위스 승리")
    g4 += 3
elif seedA >= 8 and seedD >= 3:
    print("무승부")
    g1 += 1
    g4 += 1
elif seedA < 8 and seedD < 3:
    print("무승부")
    g1 += 1
    g4 += 1

print("브라질 %d점" % g1)
print("스위스 %d점" % g4)

print("="*30)

print("세르비아 vs 카메룬")
if seedB < 7 and seedC >= 5:
    print("세르비아 승리")
    g2 += 3
elif seedB >=7 and seedC < 5:
    print("카메룬 승리")
    g3 += 3
elif seedB >= 7 and seedC >= 5:
    print("무승부")
    g2 += 1
    g3 += 1
elif seedB < 7 and seedC < 5:
    print("무승부")
    g2 += 1
    g3 += 1

print("세르비아 %d점" % g2)
print("카메룬 %d점" % g3)

print("="*30)

print("세르비아 vs 스위스")
if seedB < 7 and seedD >= 3:
    print("세르비아 승리")
    g2 += 3
elif seedB >= 7 and seedD < 3:
    print("스위스 승리")
    g4 += 3
elif seedB >= 7 and seedD >= 3:
    print("무승부")
    g2 += 1
    g4 += 1
elif seedB < 7 and seedD < 3:
    print("무승부")
    g2 += 1
    g4 += 1

print("세르비아 %d점" % g2)
print("스위스 %d점" % g4)

print("="*30)

print("카메룬 vs 스위스")
if seedC < 5 and seedD >= 3:
    print("카메룬 승리")
    g3 += 3
elif seedC >=5 and seedD < 3:
    print("스위스 승리")
    g4 += 3
elif seedC >= 5 and seedD >= 3:
    print("무승부")
    g3 += 1
    g4 += 1
elif seedC < 5 and seedD < 3:
    print("무승부")
    g3 += 1
    g4 += 1

print("카메룬 %d점" % g3)
print("스위스 %d점" % g4)

print("="*30)

print(f'{G[0]}:{g1} ' f'{G[1]}:{g2} ' f'{G[2]}: {g3} ' f'{G[3]}: {g4} ')
G = {'브라질':g1, '세르비아':g2, '카메룬':g3, '스위스':g4}
print("16강 진출 :",max(G,key=G.get))
maxG = max(G,key=G.get)
del G[max(G,key=G.get)]
print("16강 진출 :",max(G,key=G.get))
maxG2 = max(G,key=G.get)

print("="*30)

seedA = random.randint(1,10)
seedB = random.randint(1,10)
seedC = random.randint(1,10)
seedD = random.randint(1,10)

print("H조 예선")

print("포르투갈 vs 우루과이")
if seedA < 8 and seedB >= 7:
    print("포르투갈 승리")
    h1 += 3
elif seedA >= 8 and seedB < 7:
    print("우루과이 승리")
    h2 += 3
elif seedA >= 8 and seedB >= 7:
    print("무승부")
    h1 += 1
    h2 += 1
elif seedA < 8 and seedB < 7:
    print("무승부")
    h1 += 1
    h2 += 1

print("포르투갈 %d점" % h1)
print("우루과이 %d점" % h2)

print("="*30)

print("포르투갈 vs 가나")
if seedA < 8 and seedC >= 5:
    print("포르투갈 승리")
    h1 += 3
elif seedA >=8 and seedC < 5:
    print("가나 승리")
    h3 += 3
elif seedA >= 8 and seedC >= 5:
    print("무승부")
    h1 += 1
    h3 += 1
elif seedA < 8 and seedC < 5:
    print("무승부")
    h1 += 1
    h3 += 1

print("포르투갈 %d점" % h1)
print("가나 %d점" % h3)

print("="*30)

print("포르투갈 vs 대한민국")
if seedA < 8 and seedD >= 3:
    print("포르투갈 승리")
    h1 += 3
elif seedA >=8 and seedD < 3:
    print("대한민국 승리")
    h4 += 3
elif seedA >= 8 and seedD >= 3:
    print("무승부")
    h1 += 1
    h4 += 1
elif seedA < 8 and seedD < 3:
    print("무승부")
    h1 += 1
    h4 += 1

print("포르투갈 %d점" % h1)
print("대한민국 %d점" % h4)

print("="*30)

print("우루과이 vs 가나")
if seedB < 7 and seedC >= 5:
    print("우루과이 승리")
    h2 += 3
elif seedB >=7 and seedC < 5:
    print("가나 승리")
    h3 += 3
elif seedB >= 7 and seedC >= 5:
    print("무승부")
    h2 += 1
    h3 += 1
elif seedB < 7 and seedC < 5:
    print("무승부")
    h2 += 1
    h3 += 1

print("우루과이 %d점" % h2)
print("가나 %d점" % h3)

print("="*30)

print("우루과이 vs 대한민국")
if seedB < 7 and seedD >= 3:
    print("우루과이 승리")
    h2 += 3
elif seedB >= 7 and seedD < 3:
    print("대한민국 승리")
    h4 += 3
elif seedB >= 7 and seedD >= 3:
    print("무승부")
    h2 += 1
    h4 += 1
elif seedB < 7 and seedD < 3:
    print("무승부")
    h2 += 1
    h4 += 1

print("우루과이 %d점" % h2)
print("대한민국 %d점" % h4)

print("="*30)

print("가나 vs 대한민국")
if seedC < 5 and seedD >= 3:
    print("가나 승리")
    h3 += 3
elif seedC >=5 and seedD < 3:
    print("대한민국 승리")
    h4 += 3
elif seedC >= 5 and seedD >= 3:
    print("무승부")
    h3 += 1
    h4 += 1
elif seedC < 5 and seedD < 3:
    print("무승부")
    h3 += 1
    h4 += 1

print("가나 %d점" % h3)
print("대한민국 %d점" % h4)

print("="*30)

print(f'{H[0]}:{h1} ' f'{H[1]}:{h2} ' f'{H[2]}: {h3} ' f'{H[3]}: {h4} ')
H = {'포르투갈':h1, '우루과이':h2, '가나':h3, '대한민국':h4}
print("16강 진출 :",max(H,key=H.get))
maxH = max(H,key=H.get)
del H[max(H,key=H.get)]
print("16강 진출 :",max(H,key=H.get))
maxH2 = max(H,key=H.get)

print("="*30)

round16 = [maxA, maxA2, maxB, maxB2, maxC, maxC2, maxD, maxD2, maxE, maxE2, maxF, maxF2, maxG, maxG2, maxH, maxH2]
print("16강 진출 : ",round16[:])
round16_random = random.sample(round16,16)
#print(round16_random)
round8 = []
print("="*30)

for i in range(0,16,2):
    print(round16_random[i]+"vs"+round16_random[i+1])
    seedA = random.randint(1, 10)
    seedB = random.randint(1, 10)
    if seedA > seedB:
        round8.append(round16_random[i])
        print("%s 승리" %round16_random[i])
        print("=" * 30)
    elif seedA < seedB:
        round8.append(round16_random[i+1])
        print("%s 승리" %round16_random[i+1])
        print("=" * 30)
    else:
        while True:
            seedA = random.randint(1, 10)
            seedB = random.randint(1, 10)
            if seedA > seedB:
                round8.append(round16_random[i])
                print("%s 승리" % round16_random[i])
                print("=" * 30)
                break
            elif seedA < seedB:
                round8.append(round16_random[i+1])
                print("%s 승리" % round16_random[i + 1])
                print("=" * 30)
                break
print("8강 진출 : ",round8)
round8_random = random.sample(round8,8)
round4 = []
print("=" * 30)

for i in range(0,8,2):
    print(round8_random[i]+"vs"+round8_random[i+1])
    seedA = random.randint(1, 10)
    seedB = random.randint(1, 10)
    if seedA > seedB:
        round4.append(round8_random[i])
        print("%s 승리" %round8_random[i])
        print("=" * 30)
    elif seedA < seedB:
        round4.append(round8_random[i+1])
        print("%s 승리" %round8_random[i+1])
        print("=" * 30)
    else:
        while True:
            seedA = random.randint(1, 10)
            seedB = random.randint(1, 10)
            if seedA > seedB:
                round4.append(round8_random[i])
                print("%s 승리" % round8_random[i])
                print("=" * 30)
                break
            elif seedA < seedB:
                round4.append(round8_random[i+1])
                print("%s 승리" % round8_random[i + 1])
                print("=" * 30)
                break
print("4강 진출 : ",round4)
round4_random = random.sample(round4,4)
round2 = []
print("=" * 30)

for i in range(0,4,2):
    print(round4_random[i]+"vs"+round4_random[i+1])
    seedA = random.randint(1, 10)
    seedB = random.randint(1, 10)
    if seedA > seedB:
        round2.append(round4_random[i])
        print("%s 승리" %round4_random[i])
        print("=" * 30)
    elif seedA < seedB:
        round2.append(round4_random[i+1])
        print("%s 승리" %round4_random[i+1])
        print("=" * 30)
    else:
        while True:
            seedA = random.randint(1, 10)
            seedB = random.randint(1, 10)
            if seedA > seedB:
                round2.append(round4_random[i])
                print("%s 승리" % round4_random[i])
                print("=" * 30)
                break
            elif seedA < seedB:
                round2.append(round4_random[i+1])
                print("%s 승리" % round4_random[i + 1])
                print("=" * 30)
                break
print("결승 진출 : ",round2[0],round2[1])

print(round2[0]+"vs"+round2[1])
seedA = random.randint(1, 10)
seedB = random.randint(1, 10)
if seedA > seedB:
    print("%s 우승" % round2[0])
elif seedA < seedB:
    print("%s 우승" % round2[1])
else:
    while True:
        seedA = random.randint(1, 10)
        seedB = random.randint(1, 10)
        if seedA > seedB:
            print("%s 우승" % round2[0])
            break
        elif seedA < seedB:
            print("%s 우승" % round2[1])
            break







