A조 = {1:'네덜란드', 2:'세네갈', 3:'에콰도르', 4:'카타르'}
B조 = {1:'잉글랜드', 2:'웨일스', 3:'미국', 4:'이란'}
C조 = {1:'아르헨티나', 2:'멕시코', 3:'폴란드', 4:'사우디'}
D조 = {1:'프랑스', 2:'튀니지', 3:'덴마크', 4:'호주'}
E조 = {1:'스페인', 2:'독일', 3:'일본', 4:'코스타리카'}
F조 = {1:'벨기에', 2:'크로아티아', 3:'모로코', 4:'캐나다'}
G조 = {1:'브라질', 2:'세르비아', 3:'카메룬', 4:'스위스'}
H조 = {1:'포르투갈', 2:'우루과이', 3:'가나', 4:'대한민국'}

seedA = ['네덜란드', '잉글랜드', '아르헨티나', '프랑스', '스페인', '벨기에', '브라질', '포르투갈']
seedB = ['세네갈', '웨일스', '멕시코', '튀니지', '독일', '크로아티아', '세르비아', '우루과이']
seedC = ['에콰도르', '미국', '폴란드', '덴마크', '일본', '모로코', '카메룬', '가나']
seedD = ['카타르', '이란', '사우디', '호주', '코스타리카', '캐나다', '스위스', '대한민국']

import random

score = 0
team = 0
wr = 0
game = 0

A1 = A2 = A3 = A4 = 0
B1 = B2 = B3 = B4 = 0
C1 = C2 = C3 = C4 = 0
D1 = D2 = D3 = D4 = 0
E1 = E2 = E3 = E4 = 0
F1 = F2 = F3 = F4 = 0
G1 = G2 = G3 = G4 = 0
H1 = H2 = H3 = H4 = 0

game = random.randint(1,3)

print("A조 예선")

print("네덜란드 vs 세네갈")
if game == 1:
    print("네덜란드 승리")
    A1 += 3
elif game == 2:
    print("세네갈 승리")
    A2 += 3
else:
    print("무승부")
    A1 += 1
    A2 += 1

print("네덜란드 %d점" %A1)
print("세네갈 %d점" %A2)

print("="*30)

print("네덜란드 vs 에콰도르")
if game == 1:
    print("네덜란드 승리")
    A1 += 3
elif game == 2:
    print("에콰도르 승리")
    A3 += 3
else:
    print("무승부")
    A1 += 1
    A3 += 1

print("네덜란드 %d점" %A1)
print("에콰도르 %d점" %A3)

print("="*30)

print("네덜란드 vs 카타르")
if game == 1:
    print("네덜란드 승리")
    A1 += 3
elif game == 2:
    print("카타르 승리")
    A4 += 3
else:
    print("무승부")
    A1 += 1
    A4 += 1

print("네덜란드 %d점" %A1)
print("카타르 %d점" %A4)

print("="*30)

print("세네갈 vs 에콰도르")
if game == 1:
    print("세네갈 승리")
    A2 += 3
elif game == 2:
    print("에콰도르 승리")
    A3 += 3
else:
    print("무승부")
    A2 += 1
    A3 += 1

print("세네갈 %d점" %A2)
print("에콰도르 %d점" %A3)

print("="*30)

print("세네갈 vs 카타르")
if game == 1:
    print("세네갈 승리")
    A2 += 3
elif game == 2:
    print("카타르 승리")
    A4 += 3
else:
    print("무승부")
    A2 += 1
    A4 += 1

print("세네갈 %d점" %A2)
print("카타르 %d점" %A4)

print("="*30)

print("에콰도르 vs 카타르")
if game == 1:
    print("에콰도르 승리")
    A3 += 3
elif game == 2:
    print("카타르 승리")
    A4 += 3
else:
    print("무승부")
    A3 += 1
    A4 += 1

print("에콰도르 %d점" %A3)
print("카타르 %d점" %A4)

print("="*30)

print(f'{A조[1][0]}:{A1} ' f'{A조[2][0]}:{A2} ' f'{A조[3][0]}: {A3} ' f'{A조[4][0]}: {A4} ')

# A조 = {1:'네덜란드', 2:'세네갈', 3:'에콰도르', 4:'카타르'}
a = [A1 , A2, A3, A4]
max(a)
A조[1][0] = A1
list = sorted(a)
list.reverse()
print(list[0],list[1])
print("16강 진출: ")
#점수 높은 팀 구해서 16강 진출 /점수 같으면 승부다시
print("="*30)

print("B조 예선")

print("잉글랜드 vs 웨일스")
if game == 1:
    print("잉글랜드 승리")
    B1 += 3
elif game == 2:
    print("웨일스 승리")
    B2 += 3
else:
    print("무승부")
    B1 += 1
    B2 += 1

print("잉글랜드 %d점" %B1)
print("웨일스 %d점" %B2)

print("="*30)

print("잉글랜드 vs 미국")
if game == 1:
    print("잉글랜드 승리")
    B1 += 3
elif game == 2:
    print("미국 승리")
    B3 += 3
else:
    print("무승부")
    B1 += 1
    B3 += 1

print("잉글랜드 %d점" %B1)
print("미국 %d점" %B3)

print("="*30)

print("잉글랜드 vs 이란")
if game == 1:
    print("잉글랜드 승리")
    B1 += 3
elif game == 2:
    print("이란 승리")
    B4 += 3
else:
    print("무승부")
    B1 += 1
    B4 += 1

print("잉글랜드 %d점" %B1)
print("이란 %d점" %B4)

print("="*30)

print("웨일스 vs 미국")
if game == 1:
    print("웨일스 승리")
    B2 += 3
elif game == 2:
    print("미국 승리")
    B3 += 3
else:
    print("무승부")
    B2 += 1
    B3 += 1

print("웨일스 %d점" %B2)
print("미국 %d점" %B3)

print("="*30)

print("웨일스 vs 이란")
if game == 1:
    print("웨일스 승리")
    B2 += 3
elif game == 2:
    print("이란 승리")
    B4 += 3
else:
    print("무승부")
    B2 += 1
    B4 += 1

print("웨일스 %d점" %B2)
print("이란 %d점" %B4)

print("="*30)

print("미국 vs 이란")
if game == 1:
    print("미국 승리")
    B3 += 3
elif game == 2:
    print("이란 승리")
    B4 += 3
else:
    print("무승부")
    B3 += 1
    B4 += 1

print("미국 %d점" %B3)
print("이란 %d점" %B4)

print("="*30)

print(f'{B조[1][0]}:{B1} ' f'{B조[2][0]}:{B2} ' f'{B조[3][0]}: {B3} ' f'{B조[4][0]}: {B4} ')

print("="*30)

print("C조 예선")

print("아르헨티나 vs 멕시코")
if game == 1:
    print("아르헨티나 승리")
    C1 += 3
elif game == 2:
    print("멕시코 승리")
    C2 += 3
else:
    print("무승부")
    C1 += 1
    C2 += 1

print("아르헨티나 %d점" %C1)
print("멕시코 %d점" %C2)

print("="*30)

print("아르헨티나 vs 폴란드")
if game == 1:
    print("아르헨티나 승리")
    C1 += 3
elif game == 2:
    print("폴란드 승리")
    C3 += 3
else:
    print("무승부")
    C1 += 1
    C3 += 1

print("아르헨티나 %d점" %C1)
print("폴란드 %d점" %C3)

print("="*30)

print("아르헨티나 vs 사우디")
if game == 1:
    print("아르헨티나 승리")
    C1 += 3
elif game == 2:
    print("사우디 승리")
    C4 += 3
else:
    print("무승부")
    C1 += 1
    C4 += 1

print("아르헨티나 %d점" %C1)
print("사우디 %d점" %C4)

print("="*30)

print("멕시코 vs 폴란드")
if game == 1:
    print("멕시코 승리")
    C2 += 3
elif game == 2:
    print("폴란드 승리")
    C3 += 3
else:
    print("무승부")
    C2 += 1
    C3 += 1

print("멕시코 %d점" %C2)
print("폴란드 %d점" %C3)

print("="*30)

print("멕시코 vs 사우디")
if game == 1:
    print("멕시코 승리")
    C2 += 3
elif game == 2:
    print("사우디 승리")
    C4 += 3
else:
    print("무승부")
    C2 += 1
    C4 += 1

print("멕시코 %d점" %C2)
print("사우디 %d점" %C4)

print("="*30)

print("폴란드 vs 사우디")
if game == 1:
    print("폴란드 승리")
    C3 += 3
elif game == 2:
    print("사우디 승리")
    C4 += 3
else:
    print("무승부")
    C3 += 1
    C4 += 1

print("폴란드 %d점" %C3)
print("사우디 %d점" %C4)

print("="*30)

print(f'{C조[1][0]}:{C1} ' f'{C조[2][0]}:{C2} ' f'{C조[3][0]}: {C3} ' f'{C조[4][0]}: {C4} ')

print("="*30)

print("D조 예선")

print("프랑스 vs 튀니지")
if game == 1:
    print("프랑스 승리")
    D1 += 3
elif game == 2:
    print("튀니지 승리")
    D2 += 3
else:
    print("무승부")
    D1 += 1
    D2 += 1

print("프랑스 %d점" %D1)
print("튀니지 %d점" %D2)

print("="*30)

print("프랑스 vs 덴마크")
if game == 1:
    print("프랑스 승리")
    D1 += 3
elif game == 2:
    print("덴마크 승리")
    D3 += 3
else:
    print("무승부")
    D1 += 1
    D3 += 1

print("프랑스 %d점" %D1)
print("튀니지 %d점" %D3)

print("="*30)

print("프랑스 vs 호주")
if game == 1:
    print("프랑스 승리")
    D1 += 3
elif game == 2:
    print("호주 승리")
    D4 += 3
else:
    print("무승부")
    D1 += 1
    D4 += 1

print("프랑스 %d점" %D1)
print("호주 %d점" %D4)

print("="*30)

print("튀니지 vs 덴마크")
if game == 1:
    print("튀니지 승리")
    D2 += 3
elif game == 2:
    print("덴마크 승리")
    D3 += 3
else:
    print("무승부")
    D2 += 1
    D3 += 1

print("튀니지 %d점" %D2)
print("덴마크 %d점" %D3)

print("="*30)

print("튀니지 vs 호주")
if game == 1:
    print("튀니지 승리")
    D2 += 3
elif game == 2:
    print("호주 승리")
    D4 += 3
else:
    print("무승부")
    D2 += 1
    D4 += 1

print("튀니지 %d점" %D2)
print("호주 %d점" %D4)

print("="*30)

print("덴마크 vs 호주")
if game == 1:
    print("덴마크 승리")
    D3 += 3
elif game == 2:
    print("호주 승리")
    D4 += 3
else:
    print("무승부")
    D3 += 1
    D4 += 1

print("덴마크 %d점" %D3)
print("호주 %d점" %D4)

print("="*30)

print(f'{D조[1][0]}:{D1} ' f'{D조[2][0]}:{D2} ' f'{D조[3][0]}: {D3} ' f'{D조[4][0]}: {D4} ')

print("="*30)

print("E조 예선")

print("스페인 vs 독일")
if game == 1:
    print("스페인 승리")
    E1 += 3
elif game == 2:
    print("독일 승리")
    E2 += 3
else:
    print("무승부")
    E1 += 1
    E2 += 1

print("스페인 %d점" %E1)
print("독일 %d점" %E2)

print("="*30)

print("스페인 vs 일본")
if game == 1:
    print("스페인 승리")
    E1 += 3
elif game == 2:
    print("일본 승리")
    E3 += 3
else:
    print("무승부")
    E1 += 1
    E3 += 1

print("스페인 %d점" %E1)
print("일본 %d점" %E3)

print("="*30)

print("스페인 vs 코스타리카")
if game == 1:
    print("스페인 승리")
    E1 += 3
elif game == 2:
    print("코스타리카 승리")
    E4 += 3
else:
    print("무승부")
    E1 += 1
    E4 += 1

print("스페인 %d점" %E1)
print("코스타리카 %d점" %E4)

print("="*30)

print("독일 vs 일본")
if game == 1:
    print("독일 승리")
    E2 += 3
elif game == 2:
    print("일본 승리")
    E3 += 3
else:
    print("무승부")
    E2 += 1
    E3 += 1

print("독일 %d점" %E2)
print("일본 %d점" %E3)

print("="*30)

print("독일 vs 코스타리카")
if game == 1:
    print("독일 승리")
    E2 += 3
elif game == 2:
    print("코스타리카 승리")
    E4 += 3
else:
    print("무승부")
    E2 += 1
    E4 += 1

print("독일 %d점" %E2)
print("코스타리카 %d점" %E4)

print("="*30)

print("일본 vs 코스타리카")
if game == 1:
    print("일본 승리")
    E3 += 3
elif game == 2:
    print("코스타리카 승리")
    E4 += 3
else:
    print("무승부")
    E3 += 1
    E4 += 1

print("일본 %d점" %E3)
print("코스타리카 %d점" %E4)

print("="*30)

print(f'{E조[1][0]}:{E1} ' f'{E조[2][0]}:{E2} ' f'{E조[3][0]}: {E3} ' f'{E조[4][0]}: {E4} ')

print("="*30)

print("F조 예선")

print("벨기에 vs 크로아티아")
if game == 1:
    print("벨기에 승리")
    F1 += 3
elif game == 2:
    print("크로아티아 승리")
    F2 += 3
else:
    print("무승부")
    F1 += 1
    F2 += 1

print("벨기에 %d점" %F1)
print("크로아티아 %d점" %F2)

print("="*30)

print("벨기에 vs 모로코")
if game == 1:
    print("벨기에 승리")
    F1 += 3
elif game == 2:
    print("모로코 승리")
    F3 += 3
else:
    print("무승부")
    F1 += 1
    F3 += 1

print("벨기에 %d점" %F1)
print("모로코 %d점" %F3)

print("="*30)

print("벨기에 vs 캐나다")
if game == 1:
    print("벨기에 승리")
    F1 += 3
elif game == 2:
    print("캐나다 승리")
    F4 += 3
else:
    print("무승부")
    F1 += 1
    F4 += 1

print("벨기에 %d점" %F1)
print("캐나다 %d점" %F4)

print("="*30)

print("크로아티아 vs 모로코")
if game == 1:
    print("크로아티아 승리")
    F2 += 3
elif game == 2:
    print("모로코 승리")
    F3 += 3
else:
    print("무승부")
    F2 += 1
    F3 += 1

print("크로아티아 %d점" %F2)
print("모로코 %d점" %F3)

print("="*30)

print("크로아티아 vs 캐나다")
if game == 1:
    print("크로아티아 승리")
    F2 += 3
elif game == 2:
    print("캐나다 승리")
    F4 += 3
else:
    print("무승부")
    F2 += 1
    F4 += 1

print("크로아티아 %d점" %F2)
print("캐나다 %d점" %F4)

print("="*30)

print("모로코 vs 캐나다")
if game == 1:
    print("모로코 승리")
    F3 += 3
elif game == 2:
    print("캐나다 승리")
    F4 += 3
else:
    print("무승부")
    F3 += 1
    F4 += 1

print("모로코 %d점" %F3)
print("캐나다 %d점" %F4)

print("="*30)

print(f'{F조[1][0]}:{F1} ' f'{F조[2][0]}:{F2} ' f'{F조[3][0]}: {F3} ' f'{F조[4][0]}: {F4} ')

print("="*30)

print("G조 예선")

print("브라질 vs 세르비아")
if game == 1:
    print("브라질 승리")
    G1 += 3
elif game == 2:
    print("세르비아 승리")
    G2 += 3
else:
    print("무승부")
    G1 += 1
    G2 += 1

print("브라질 %d점" %G1)
print("세르비아 %d점" %G2)

print("="*30)

print("브라질 vs 카메룬")
if game == 1:
    print("브라질 승리")
    G1 += 3
elif game == 2:
    print("카메룬 승리")
    G3 += 3
else:
    print("무승부")
    G1 += 1
    G3 += 1

print("브라질 %d점" %G1)
print("카메룬 %d점" %G3)

print("="*30)

print("브라질 vs 스위스")
if game == 1:
    print("브라질 승리")
    G1 += 3
elif game == 2:
    print("스위스 승리")
    G4 += 3
else:
    print("무승부")
    G1 += 1
    G4 += 1

print("브라질 %d점" %G1)
print("스위스 %d점" %G4)

print("="*30)

print("세르비아 vs 카메룬")
if game == 1:
    print("세르비아 승리")
    G2 += 3
elif game == 2:
    print("카메룬 승리")
    G3 += 3
else:
    print("무승부")
    G2 += 1
    G3 += 1

print("세르비아 %d점" %G2)
print("카메룬 %d점" %G3)

print("="*30)

print("세르비아 vs 스위스")
if game == 1:
    print("세르비아 승리")
    G2 += 3
elif game == 2:
    print("스위스 승리")
    G4 += 3
else:
    print("무승부")
    G2 += 1
    G4 += 1

print("세르비아 %d점" %G2)
print("스위스 %d점" %G4)

print("="*30)

print("카메룬 vs 스위스")
if game == 1:
    print("카메룬 승리")
    G3 += 3
elif game == 2:
    print("스위스 승리")
    G4 += 3
else:
    print("무승부")
    G3 += 1
    G4 += 1

print("카메룬 %d점" %G3)
print("스위스 %d점" %G4)

print("="*30)

print(f'{G조[1][0]}:{G1} ' f'{G조[2][0]}:{G2} ' f'{G조[3][0]}:{G3} ' f'{G조[4][0]}:{G4} ')

print("="*30)

print("H조 예선")

print("포르투갈 vs 우루과이")
if game == 1:
    print("포르투갈 승리")
    H1 += 3
elif game == 2:
    print("우루과이 승리")
    H2 += 3
else:
    print("무승부")
    H1 += 1
    H2 += 1

print("포르투갈 %d점" %H1)
print("우루과이 %d점" %H2)

print("="*30)

print("포르투갈 vs 가나")
if game == 1:
    print("포르투갈 승리")
    H1 += 3
elif game == 2:
    print("가나 승리")
    H3 += 3
else:
    print("무승부")
    H1 += 1
    H3 += 1

print("포르투갈 %d점" %H1)
print("가나 %d점" %H3)

print("="*30)

print("포르투갈 vs 대한민국")
if game == 1:
    print("포르투갈 승리")
    H1 += 3
elif game == 2:
    print("대한민국 승리")
    H4 += 3
else:
    print("무승부")
    H1 += 1
    H4 += 1

print("포르투갈 %d점" %H1)
print("대한민국 %d점" %H4)

print("="*30)

print("우루과이 vs 가나")
if game == 1:
    print("우루과이 승리")
    H2 += 3
elif game == 2:
    print("가나 승리")
    H3 += 3
else:
    print("무승부")
    H2 += 1
    H3 += 1

print("우루과이 %d점" %H2)
print("가나 %d점" %H3)

print("="*30)

print("우루과이 vs 대한민국")
if game == 1:
    print("우루과이 승리")
    H2 += 3
elif game == 2:
    print("대한민국 승리")
    H4 += 3
else:
    print("무승부")
    H2 += 1
    H4 += 1

print("우루과이 %d점" %H2)
print("대한민국 %d점" %H4)

print("="*30)

print("가나 vs 대한민국")
if game == 1:
    print("가나 승리")
    H3 += 3
elif game == 2:
    print("대한민국 승리")
    H4 += 3
else:
    print("무승부")
    H3 += 1
    H4 += 1

print("가나 %d점" %H3)
print("대한민국 %d점" %H4)

print("="*30)

print(f'{H조[1][0]}:{H1} ' f'{H조[2][0]}:{H2} ' f'{H조[3][0]}:{H3} ' f'{H조[4][0]}:{H4} ')

print("="*30)