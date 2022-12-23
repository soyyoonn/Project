import random
import time

# 초기 초코의용 리스트: 공격력 최소: 100, 최대: 150, 최대 HP: 500hp, 현재 HP: 500hp, 포션: 0개, 엘릭서: 0개
si_choco=['초코의용군', [100, 150], [500, 500], 3, 3]
# 좀비 - 등장확률: 48%, 공격력: 100, HP: 300~500
si_zombie=['좀비', 48, [100], [300, 500]]
# 구울 - 등장활률 30%, 공격력: 180, HP: 450~700
si_ghoul=['구울', 30, [180], [450, 700]]
# 해골 - 등장확률: 12% 공격력: 220, HP: 480~800
si_skull=['해골', 12, [220], [480, 800]]
# 버그베어 - 등장확률: 5%, 공격력: 350, HP: 550~900
si_bugbear=['버그베어', 5, [350], [550, 900]]
# 동혀니 - 등장확률: 2%, 공격력 1000 ~ 3000, HP 3000~8000
si_donghyeon=['동혀니', 2, [1000, 3000], [3000, 8000]]
# 홍거리 - 등장확률 2%, 공격력 1000 ~ 3000, HP 3000~8000
si_honggeol=['홍거리', 2, [1000, 3000], [3000, 8000]]
# 디아복로 - 등장확률 1%, 공격력 2500 ~ 8000, HP 5000~15000
si_diaboklo=['디아복로', 1, [2500, 8000], [5000, 15000]]
#몬스터 리스트 0= 좀비, 1= 구울, 2= 해골, 3= 버그베어, 4= 동혀니, 5= 홍거리, 6= 디아복로
si_monster_list=[si_zombie, si_ghoul, si_skull, si_bugbear, si_donghyeon, si_honggeol, si_diaboklo]
si_monster_Hp=[]


def si_fight_screen(monster,si_monster_nowHp, si_monster_maxHp):
    # 전투화면 함수 선언(몬스터)
    print('ㅡ'*20)
    print(f"{monster[0]} {si_monster_nowHp}/{si_monster_maxHp}")
    print('\n'*5)
    print(f"{si_choco[0]:>20} {si_choco[2][0]}/{si_choco[2][1]}")
    print('ㅡ'*20)
    print(f"포션　: {si_choco[3]:>2}{'공격　도망':>18}\n엘릭서: {si_choco[4]:>2}")
    print('ㅡ'*20)


def sy_potion(si_choco):
    # 포션 사용 함수
    # y 포션 사용 선택시
    print("포션을 사용합니다")
    si_choco[2][0] = si_choco[2][1]
    # 현재 hp = 최대 hp
    print(f"{si_choco[0]:>20} {si_choco[2][0]}/{si_choco[2][1]}")
    si_choco[3] -= 1
    # 포션 개수 차감

def si_event_appear():
    # 이벤트 발생 함수
    print("!" * 33)
    print("!" * 33)
    print("!" * 33)
    print("!" * 33)
    print("!!!!!!!!!!!!!!몬스터!!!!!!!!!!!!!!")
    print("!" * 33)
    print("!" * 33)
    print("!" * 33)
    print("!" * 33)

def si_monster_appear():
    # 몬스터 등장 함수
    si_monster_rate=random.randint(1,100)
    # 랜덤값 담아줄 변수
    si_event_appear()
    # 몬스터 출현 함수호출
    time.sleep(1)
    # 딜레이 1초
    if si_monster_rate in range(1, 49):
        # 좀비일 경우
        print(f"{si_monster_list[0][0]}가 나타났다")
        # 좀비가 나타났다 출력
        return si_monster_list[0]
        # '좀비' 반환
    if si_monster_rate in range(49, 79):
        # 구울일 경우
        print(f"{si_monster_list[1][0]}이 나타났다")
        # 구울이 나타났다 출력
        return si_monster_list[1]
        # '구울' 반환
    if si_monster_rate in range(79, 91):
        # 해골일 경우
        print(f"{si_monster_list[2][0]}이 나타났다")
        # 해골이 나타났다 출력
        return si_monster_list[2]
        # '해골' 반환
    if si_monster_rate in range(91, 96):
        # 버그베어일 경우
        print(f"{si_monster_list[3][0]}가 나타났다")
        # 버그베어가 나타났다 출력
        return si_monster_list[3]
        # '버그베어' 반환
    if si_monster_rate in range(96, 98):
        # 동혀니일 경우
        print(f"{si_monster_list[4][0]}가 나타났다")
        # 동혀니가 나타났다 출력
        return si_monster_list[4]
        # '동혀니' 반환
    if si_monster_rate in range(98, 100):
        # 홍거리일 경우
        print(f"{si_monster_list[5][0]}이가 나타났다")
        # 홍거리가 나타났다 출력
        return si_monster_list[5]
        # '홍거리' 반환
    if si_monster_rate in range(100, 101):
        # 디아복로일 경우
        print(f"{si_monster_list[6][0]}가 나타났다")
        # 디아복로가 나타났다 출력
        return si_monster_list[6]
        # '디아복로' 반환

def sy_elixir(si_choco,elixir):
    #엘릭서 사용 함수
    print("엘릭서를 사용합니다")
    elixir = 10
    print("10턴동안 무적")
    si_choco[2][0] = si_choco[2][1]
    # 현재 hp = 최대 hp
    si_choco[4] -= 1
    # 엘릭서 개수 차감
    return elixir

#전투 후 승리시 보상 함수
def sy_reward(si_choco):
    print("전투에서 승리했습니다")
    print("공격력과 HP가 5%씩 상승합니다")
    # 최소 공격력 5% 상승
    si_choco[1][0] += round(si_choco[1][0] * 0.05)
    # 최대 공격력 5% 상승
    si_choco[1][1] += round(si_choco[1][1] * 0.05)
    # 현재 HP 5% 상승
    si_choco[2][0] += round(si_choco[2][0] * 0.05)
    # 최대 HP 5% 상승
    si_choco[2][1] += round(si_choco[2][1] * 0.05)

    # 포션 랜덤 50% 획득
    potion = random.randint(1, 2)
    # 엘릭서는 포션 획득 시 랜덤 0.5% 획득
    elixir = random.randint(1, 1000)
    # 포션 획득 할 경우
    if potion == 1 and elixir > 5:
        print("포션을 획득했습니다")
        si_choco[3] += 1
    # 포션 얻은 후 엘릭서 획득 할 경우
    elif potion == 1 and elixir <= 5:
        print("엘릭서를 획득했습니다")
        si_choco[4] += 1
    # 포션 획득하지 못 할 경우
    else:
        print("포션을 획득하지 못했습니다")

    return si_choco

def si_Monster_Hp(si_who_monster):
    si_monster_maxHp = random.randint(si_who_monster[3][0], si_who_monster[3][1])
    # 몬스터 최대체력 랜덤값 받기
    si_monster_nowHp = si_monster_maxHp
    # 몬스터 현재체력
    return si_monster_nowHp,si_monster_maxHp

def si_fight(si_who_monster,si_monster_nowHp,elixir):
    si_monster_maxHp= si_monster_nowHp
    si_choco_power = random.randint(si_choco[1][0], si_choco[1][1])
    # 초코의용 공격력
    sy_elixir_turn = 0
    # 초코의용 엘릭서 턴 초기화
    if si_who_monster in si_monster_list[0:4]:
        # 몬스터가 좀비, 구울, 해골, 버그베어일 경우
        si_monster_power = si_who_monster[2][0]
        # 몬스터 공격력
    else:
        # 몬스터가 동혀니, 홍거리, 디아복로일 경우
        si_monster_power = random.randint(si_who_monster[2][0], si_who_monster[2][1])
        # 몬스터 공격력
    while True:
        si_action= int(input("1. 공격 2. 도망 3. 포션 사용 4. 엘릭서 사용\n"))
        # 무슨 행동을 할껀지 사용자에게 입력받기
        if si_action not in range(1,5):
            print("다시 입력해주세요.")
            continue
        if si_action==1:
            si_pantierun_fail=0
            print(f"초코의용이 공격합니다.\n{si_who_monster[0]}에게 {si_choco_power}의 데미지를 입혔습니다.")
            # 공격 데미지 출력
            si_monster_nowHp-=si_choco_power
            # 몬스터 현재체력에 초코의용의 공격력만큼 빼줌
            si_fight_screen(si_who_monster,si_monster_nowHp,si_monster_maxHp)
            # 전투화면 함수 호출
            if si_monster_nowHp<=0:
                # 몬스터 체력이 0과 같거나 작을 때
                print(f"{si_who_monster[0]}을(를) 처치했습니다.")
                # 몬스터 처치 출력문
                break
        elif si_action == 2 :
            # 도망을 선택한 경우
            print("빤스런을 시도합니다.")
            # 도망시도 출력물
            time.sleep(1.5)
            #1.5초 딜레이
            si_pantierun_rate=random.randint(1,100)
            # 도망 확률은 80%
            if si_pantierun_rate in range(1,81):
                # 도망 성공
                print("빤스런에 성공했습니다.")
                break
            else:
                # 도망 실패
                print("빤스런에 실패 하였습니다.")
        elif si_action == 3:
            # 포션사용
            sy_potion(si_choco)
            # 포션사용 함수 호출
            si_fight_screen(si_who_monster,si_monster_nowHp,si_monster_maxHp)
            # 포션사용후 전투화면 출력
            continue

        else:
            sy_elixir_turn=sy_elixir(si_choco,sy_elixir_turn)
            # 엘릭서 턴에 엘릭서 사용함수의 리턴값 담아주기
            si_fight_screen(si_who_monster, si_monster_nowHp, si_monster_maxHp)
            # 엘릭서 사용 후 전투화면 출력
        if sy_elixir_turn==0:
            # 엘릭서 턴이 없을 경우 공격받게
            time.sleep(1.5)
            # 1.5초 딜레이
            print(f"{si_who_monster[0]}이(가) 공격합니다.\n{si_who_monster[0]}에게 {si_monster_power}의 데미지를 입었습니다.")
            # 몬스터 공격 출력문
            si_choco[2][0] -= si_monster_power
            # 초코의용의 현재 체력에서 몬스터의 공격력 빼주기
            si_fight_screen(si_who_monster, si_monster_nowHp, si_monster_maxHp)
            # 차감된 체력확인 하기 위한 전투화면 출력
            if si_choco[2][0] <= 0:
                # 초코의용의 체력이 0과 같거나 작을 경우
                print("초코의용이 사망했습니다.\nGame Over")
                # 초코의용 사망, 엔딩 출력
                break
        else:
            sy_elixir_turn -= 1
            # 엘릭서 턴 차감
            time.sleep(1.5)
            # 1.5초 딜레이
            print(f"{si_who_monster[0]}이(가) 공격합니다.\n엘릭서의 효과로 데미지를 입지 않습니다.\n{si_monster_power}의 데미지를 방어했습니다.\n남은 엘릭서 효과: {sy_elixir_turn}")
            # 엘릭서 효과 출력
            si_fight_screen(si_who_monster, si_monster_nowHp, si_monster_maxHp)
            # 차감되지 않은 체력확인을 위한 전투화면 출력

def battle() :
    si_who_monster=si_monster_appear()
    # 어떤 몬스터가 출현했는지 리턴값 저장하기
    si_monster_Hp=list(si_Monster_Hp(si_who_monster))
    #몬스터 Hp 담아주기
    si_fight_screen(si_who_monster,si_monster_Hp[0],si_monster_Hp[1])
    # 전투 화면 함수 호출(매개변수: 몬스터 등장 리턴값)
    si_fight(si_who_monster,si_monster_Hp[0],sy_elixir)
    # 전투 함수 호출
battle()