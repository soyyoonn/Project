import random
import keyboard
import time


# 몬스터 기본 리스트(기태?)
def battle(bt_choco):
    # 좀비 - 등장확률: 48%, 공격력: 100, HP: 300~500
    bt_zombie = ['🧟좀비🧟', 48, [100], [300, 500]]

    # 구울 - 등장활률 30%, 공격력: 180, HP: 450~700
    bt_ghoul = ['🧟구울🧟', 30, [180], [450, 700]]

    # 해골 - 등장확률: 12% 공격력: 220, HP: 480~800
    bt_skull = ['☠해골☠', 12, [220], [480, 800]]

    # 버그베어 - 등장확률: 5%, 공격력: 350, HP: 550~900
    bt_bugbear = ['🐻버그베어🐻', 5, [350], [550, 900]]

    # 동혀니 - 등장확률: 2%, 공격력 1000 ~ 3000, HP 3000~8000
    bt_donghyeon = ['🧛‍동혀니🧛', 2, [1000, 3000], [3000, 8000]]

    # 홍거리 - 등장확률 2%, 공격력 1000 ~ 3000, HP 3000~8000
    bt_honggeol = ['🧙‍홍거리🧙', 2, [1000, 3000], [3000, 8000]]

    # 디아복로 - 등장확률 1%, 공격력 2500 ~ 8000, HP 5000~15000
    bt_diaboklo = ['😈디아복로😈', 1, [2500, 8000], [5000, 15000]]

    # 몬스터 2중 리스트 index 0 = 좀비, 1 = 구울, 2 = 해골, 3 = 버그베어, 4 = 동혀니, 5 = 홍거리, 6 = 디아복로
    bt_monster_list = [bt_zombie, bt_ghoul, bt_skull, bt_bugbear, bt_donghyeon, bt_honggeol, bt_diaboklo]

    # 어떤 몬스터(리스트)가 랜덤 출현
    bt_monster = monster_appear(bt_monster_list)
    # 랜덤으로 나온 몬스터 현재, 최대 Hp 리스트로 담아주기
    bt_monster_Hp = list(monster_Hp(bt_monster))

    # 전투 화면 함수 호출(매개변수: 몬스터 등장 리턴값)
    fight_screen(bt_monster, bt_monster_Hp, bt_choco)
    # 전투 함수 호출
    fight(bt_monster, bt_monster_Hp, bt_choco, bt_monster_list)


# 전투 함수 (성일, 소윤)
def fight(fi_monster, fi_monster_Hp, fi_choco, fi_monster_list):
    # 초코의용 엘릭서 턴 초기화
    elixir_turn = 0

    while True:
        # 무슨 행동을 할껀지 사용자에게 입력받기
        fi_action = input(f"{'무엇을 할까?':>20}\n"
                          f"{'[1.공격🥊]　[2.도망🏃‍]':>25}\n"
                          f"{'[3.포션🍖(':>12}{fi_choco[3]})] [4.엘릭서🍭({fi_choco[4]})]\n"
                          f"{'─' * 38}\n"
                          f"숫자를 입력해주세요: ")
        # 공격 선택
        if fi_action == '1':
            # 초코의용 공격력
            fi_choco_power = random.randint(fi_choco[1][0], fi_choco[1][1])
            # 초코의용 공격 데미지 출력
            print(f"초코의용의 공격!\n"
                  f"{fi_monster[0]}에게 {fi_choco_power}의 데미지를 입혔습니다.")
            # 몬스터 현재 체력에서 초코의용이 공격한 데미지만큼 빼줌
            fi_monster_Hp[0] -= fi_choco_power

            # 전투 화면 출력 함수 호출
            fight_screen(fi_monster, fi_monster_Hp, fi_choco)

            # 몬스터 체력이 0과 같거나 작을 때 -> 몬스터 잡음
            if fi_monster_Hp[0] <= 0:
                # 몬스터 처치 출력문
                print(f"🎉{fi_monster[0]}을(를) 처치했습니다.🎉")
                # 몬스터를 잡으면 초코의용 성장
                fi_choco = reward(fi_choco)
                # 처치한 몬스터가 디아복로면 엔딩
                if fi_monster[0] == fi_monster_list[6][0]:
                    peace_ending()
                break
        # 도망 선택
        elif fi_action == '2':
            # 도망시도 출력물
            print("빤스런을 시도합니다.")
            time.sleep(1.5)     # 1.5초 딜레이
            # 도망 확률: 80%
            si_pantierun_rate = random.randint(1, 100)
            # 도망 성공
            if si_pantierun_rate in range(1, 81):
                print("빤스런에 성공했습니다. 🏃💨")
                break
            # 도망 실패
            else:
                print("빤스런에 실패 하였습니다. 😭")
        # 포션 선택
        elif fi_action == '3':
            # 현재체력이 최대일 때
            if fi_choco[2][0] == fi_choco[2][1]:
                print("체력이 꽉 차있습니다. 💦")
                # 전투화면 출력
                fight_screen(fi_monster, fi_monster_Hp, fi_choco)
            # 포션이 없을 때
            elif fi_choco[3] == 0:
                print("포션이 없습니다. 💦")
                # 전투화면 출력
                fight_screen(fi_monster, fi_monster_Hp, fi_choco)
            # 포션 사용
            else:
                # 포션사용 함수 호출
                potion(fi_choco)
                # 포션사용후 전투화면 출력
                fight_screen(fi_monster, fi_monster_Hp, fi_choco)
            continue
        # 엘릭서 선택
        elif fi_action == '4':
            # 엘릭서가 없을 경우
            if fi_choco[4] == 0:
                print("엘릭서가 없습니다. 💦\n다시 입력해주세요.")
                # 전투화면 출력
                fight_screen(fi_monster, fi_monster_Hp, fi_choco)
                continue
            # 엘릭서 턴에 엘릭서 사용함수의 리턴값 담아주기, (엘릭서 효과 남은 턴)
            elixir_turn = elixir(fi_choco)
            # 엘릭서 사용 후 전투화면 출력
            # fight_screen(fi_monster, fi_monster_Hp, fi_choco)
        # 범위 밖을 입력했을 경우
        else:
            print("다시 입력해주세요.")
            print('─' * 38)
            continue

        # 엘릭서 턴이 없을 경우(무적 효과가 없을때) 공격 받음
        if elixir_turn == 0:
            time.sleep(1.5)     # 1.5초 딜레이
            # 몬스터가 좀비, 구울, 해골, 버그베어일 경우
            if fi_monster in fi_monster_list[0:4]:
                # 몬스터 공격력
                fi_monster_power = fi_monster[2][0]
            # 몬스터가 동혀니, 홍거리, 디아복로일 경우
            else:
                # 몬스터 공격력
                fi_monster_power = random.randint(fi_monster[2][0], fi_monster[2][1])

            # 몬스터 공격 출력문
            print(f"{fi_monster[0]}이(가) 공격합니다.\n"
                  f"{fi_monster[0]}에게 {fi_monster_power}의 데미지를 입었습니다.")

            # 초코의용의 현재 체력에서 몬스터의 공격력 빼주기
            if fi_choco[2][0] <= fi_monster_power:      # 현재 체력보다 더 씨게 맞으면 체력 0으로(죽음)
                fi_choco[2][0] = 0
                # 차감된 체력확인 하기 위한 전투화면 출력
                fight_screen(fi_monster, fi_monster_Hp, fi_choco)
                # 초코의용 사망, 엔딩 출력
                die_ending()
            else:
                fi_choco[2][0] -= fi_monster_power
                # 차감된 체력확인 하기 위한 전투화면 출력
                fight_screen(fi_monster, fi_monster_Hp, fi_choco)

        # 엘릭서 턴이 있을 경우(무적 효과 받고 있을 때) 공격 방어
        else:
            elixir_turn -= 1    # 엘릭서 턴 차감
            time.sleep(1.5)     # 1.5초 딜레이
            # 몬스터가 좀비, 구울, 해골, 버그베어일 경우
            if fi_monster in fi_monster_list[0:4]:
                # 몬스터 공격력
                fi_monster_power = fi_monster[2][0]
            # 몬스터가 동혀니, 홍거리, 디아복로일 경우
            else:
                # 몬스터 공격력
                fi_monster_power = random.randint(fi_monster[2][0], fi_monster[2][1])
            # 몬스터 공격 출력문 + 엘릭서 효과 출력
            print(f"{fi_monster[0]}이(가) 공격합니다.\n"
                  f"🎇엘릭서의 효과로 데미지를 입지 않습니다.🎇\n"
                  f"🎇{fi_monster_power}의 데미지를 방어했습니다.🎇\n"
                  f"엘릭서 효과 남은 턴: {elixir_turn}")
            # 차감되지 않은 체력확인을 위한 전투화면 출력
            fight_screen(fi_monster, fi_monster_Hp, fi_choco)


# 몬스터 등장 함수 (성일)
def monster_appear(ma_monster_list):
    # 랜덤값 담아줄 변수
    ma_monster_rate = random.randint(1, 100)
    # 딜레이 1초
    time.sleep(1)

    # 좀비: 48% 확률 출현
    if ma_monster_rate in range(1, 49):
        # "좀비가 나타났다" 출력
        print(f"{ma_monster_list[0][0]:>14}가 나타났다!")
        time.sleep(1.5)  # 딜레이 1.5초
        zombie_AA()      # 좀비 ascii art 출력
        time.sleep(1.5)  # 딜레이 1.5초
        # 좀비 리스트 반환 ma_monster_list[0] = bt_zombie = ['🧟좀비🧟', 48, [100], [300, 500]]
        return ma_monster_list[0]
    # 구울: 30% 확률 출현
    elif ma_monster_rate in range(49, 79):
        # "구울이 나타났다" 출력
        print(f"{ma_monster_list[1][0]:>14}이 나타났다!")
        time.sleep(1.5)  # 딜레이 1.5초
        ghoul_AA()       # 구울 ascii art 출력
        time.sleep(1.5)  # 딜레이 1.5초
        # 구울 리스트 반환 ma_monster_list[1] = si_ghoul = ['🧟구울🧟', 30, [180], [450, 700]]
        return ma_monster_list[1]
    # 해골: 12% 확률 출현
    elif ma_monster_rate in range(79, 91):
        # "해골이 나타났다" 출력
        print(f"{ma_monster_list[2][0]:>14}이 나타났다!")
        time.sleep(1.5)  # 딜레이 1.5초
        skull_AA()      # 해골 ascii art 출력
        time.sleep(1.5)  # 딜레이 1.5초
        # 해골 리스트 반환 ma_monster_list[2] = si_skull = ['☠해골☠', 12, [220], [480, 800]]
        return ma_monster_list[2]
    # 버그베어: 5% 확률 출현
    elif ma_monster_rate in range(91, 96):
        # "버그베어가 나타났다" 출력
        print(f"{ma_monster_list[3][0]:>14}가 나타났다!")
        time.sleep(1.5)  # 딜레이 1.5초
        bugbear_AA()     # 버그베어 ascii art 출력
        time.sleep(1.5)  # 딜레이 1.5초
        # 버그베어 리스트 반환 ma_monster_list[3] = si_bugbear = ['🐻버그베어🐻', 5, [350], [550, 900]]
        return ma_monster_list[3]
    # 동혀니: 2% 확률 출현
    elif ma_monster_rate in range(96, 98):
        # "동혀니가 나타났다" 출력
        print(f"{ma_monster_list[4][0]:>14}가 나타났다!")
        time.sleep(1.5)  # 딜레이 1.5초
        donghyeon_AA()   # 동혀니 ascii art 출력
        time.sleep(1.5)  # 딜레이 1.5초
        # 동혀니 리스트 반환 ma_monster_list[4] = si_donghyeon = ['🧛‍동혀니🧛', 2, [1000, 3000], [3000, 8000]]
        return ma_monster_list[4]
    # 홍거리: 2% 확률 출현
    elif ma_monster_rate in range(98, 100):
        # "홍거리가 나타났다" 출력
        print(f"{ma_monster_list[5][0]:>14}이가 나타났다!")
        time.sleep(1.5)  # 딜레이 1.5초
        honggeol_AA()    # 홍거리 ascii art 출력
        time.sleep(1.5)  # 딜레이 1.5초
        # 홍거리 리스트 반환 ma_monster_list[5] = si_honggeol = ['🧙‍홍거리🧙', 2, [1000, 3000], [3000, 8000]]
        return ma_monster_list[5]
    # 디아복로일 경우
    elif ma_monster_rate in range(100, 101):
        # 디아복로가 나타났다 출력
        print(f"{ma_monster_list[6][0]:>14}가 나타났다!")
        time.sleep(1.5)  # 딜레이 1.5초
        diaboklo_AA()    # 디아복로 ascii art 출력
        time.sleep(1.5)  # 딜레이 1.5초
        # 디아복로 리스트 반환 ma_monster_list[6] = si_diaboklo = ['😈디아복로😈', 1, [2500, 8000], [5000, 15000]]
        return ma_monster_list[6]


# 몬스터 체력 설정 함수 (성일)
def monster_Hp(mH_monster):
    # 몬스터 최대 체력 랜덤값 받기
    mH_maxHp = random.randint(mH_monster[3][0], mH_monster[3][1])
    # 몬스터 현재 체력 = 최대 체력
    mH_nowHp = mH_maxHp
    return mH_nowHp, mH_maxHp


# 전투 화면 출력 함수 (성일), 랜덤 몬스터 리스트, 현재 체력&최대 체력 리스트, 초코의용 정보리스트 받음
def fight_screen(fs_monster, fs_monster_Hp, fs_choco):
    print('─' * 38)
    # 몬스터 이름. 현재 체력/최대 체력 출력
    print(f"{fs_monster[0]}  HP: {fs_monster_Hp[0]}/{fs_monster_Hp[1]}")
    print('\n' * 5)
    # 초코의용군 이름. 현재 체력/최대 체력 포션, 엘릭서 출력
    print(f"{fs_choco[0]:>21}  HP: {fs_choco[2][0]}/{fs_choco[2][1]}")
    print(f"{'🍖(':>28}{fs_choco[3]}) 🍭({fs_choco[4]})")
    print('─' * 38)


# 포션 사용 함수, 포션 사용 선택시(소윤)
def potion(po_choco):
    print("포션을 사용합니다  🍖-1")
    po_choco[2][0] = po_choco[2][1]
    # 현재 hp => 최대 hp
    print("✨HP가 회복됩니다✨")
    print(f"{po_choco[0]:>22} HP: {po_choco[2][0]}/{po_choco[2][1]}")
    # 포션 개수 차감
    po_choco[3] -= 1


# 전투 후 승리시 보상 함수(소윤)
def reward(rw_choco):
    time.sleep(1)
    print("🎉전투에서 승리했습니다🎉")
    print("💪공격력과 HP가 5%씩 상승합니다💪")
    # 최소 공격력 5% 상승
    rw_choco[1][0] += round(rw_choco[1][0] * 0.05)
    # 최대 공격력 5% 상승
    rw_choco[1][1] += round(rw_choco[1][1] * 0.05)
    # 현재 HP 5% 상승
    rw_choco[2][0] += round(rw_choco[2][0] * 0.05)
    # 최대 HP 5% 상승
    rw_choco[2][1] += round(rw_choco[2][1] * 0.05)

    # 포션 랜덤 50% 획득
    rw_potion = random.randint(1, 2)
    # 엘릭서는 포션 획득 시 랜덤 0.5% 획득
    rw_elixir = random.randint(1, 1000)
    # 포션 획득 할 경우
    if rw_potion == 1 and rw_elixir > 5:
        print("포션을 획득했습니다 +🍖")
        rw_choco[3] += 1
    # 포션 얻은 후 엘릭서 획득 할 경우
    elif rw_potion == 1 and rw_elixir <= 5:
        print("엘릭서를 획득했습니다 +🍭")
        rw_choco[4] += 1
    # 포션 획득하지 못 할 경우
    else:
        print("포션을 획득하지 못했습니다")
    return rw_choco


# 엘릭서 사용 함수 (소윤)
def elixir(el_choco):
    print("엘릭서를 사용합니다 -🍭")
    el_elixir = 10  # 엘릭서 턴은 10번
    print("🎇10턴동안 무적🎇")
    # 현재 hp => 최대 hp
    el_choco[2][0] = el_choco[2][1]
    print("✨HP가 회복됩니다✨")
    # 엘릭서 개수 차감
    el_choco[4] -= 1
    return el_elixir


# -------------------------------------------- 엔딩 함수 ----------------------------------------------------------------


#해피엔딩
def peace_ending():
    print("🎊디아복로를 처치하였습니다.🎊")
    print('세상에 평화가 찾아옵니다...')
    exit()


# 배드엔딩
def die_ending():
    print('''
     @@@@@                                        @@@@@
    @@@@@@@                                      @@@@@@@
    @@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
     @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
         @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
           @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
             @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
                @@@@@@@    @@@@@@    @@@@@@
                @@@@@@      @@@@      @@@@@
                @@@@@@      @@@@      @@@@@
                 @@@@@@    @@@@@@    @@@@@
                  @@@@@@@@@@　  @@@@@@@@@@
                   @@@@@@@@@@  @@@@@@@@@
                @@@   @@@@@@@@@@@@@@@    @@
               @@@@  @@@@ @ @ @ @ @@@@  @@@@
              @@@@@   @@@ @ @ @ @ @@@   @@@@@
            @@@@@      @@@@@@@@@@@@@      @@@@@
          @@@@          @@@@@@@@@@@          @@@@
       @@@@@              @@@@@@@              @@@@@
      @@@@@@@                                 @@@@@@@
       @@@@@                                   @@@@@
    ''')
    print(f"{'💀 초코의용이 사망했습니다. 💀':>35}\n")
    Game_over_AA()
    exit()


# -------------------------------------------- ascii art ---------------------------------------------------------------


# 디아복로 AA 출력 함수
def diaboklo_AA():
    print("""
                  .                                                      .
            .n                   .                 .                  n.
      .   .dP                  dP                   9b                 9b.    .
     4    qXb         .       dX                     Xb       .        dXp     t
    dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
    9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
     9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
      `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
        `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
            ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                            )b.  .dbo.dP'`v'`9b.odb.  .dX(
                          ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                         dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                        dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                        9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                         `'      9XXXXXX(   )XXXXXXP      `'
                                  XXXX X.`v'.X XXXX
                                  XP^X'`b   d'`X^XX
                                  X. 9  `   '  P )X
                                  `b  `       '  d'
                                   `             '
    """)


# 구울 AA 출력 함수
def ghoul_AA():
    print("""
          ▄██████████▄
        ▄█▒▒▒▒▒▒▒▒▒▒▒▒█▄
        █▒▒▐█▌▒▒▒▒▒▐█▌▒█▄
        █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▄
        █▒██████████████▒█▄
        █▒█▄─█─█─█─█─▄██▒▒█
        █▒▒████████████▒▒▒█
        █▒▒▒█▄─█──█─▄█▒▒▒▒█
        █▒▒▒▒████████▒▒▒▒▒█
       ▄█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀
       █▒▒▒▀▀▄▄▄▄▄▄▀▀▒▒▒█▀
      ▄█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
    ▄█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▄
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▄
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▄
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒█
    ▀█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒█
     ▀█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒█
      ▀█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒█▒▒█
       ██▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█▒▒▒▒▒▒█▒▒▒█
       █▒█▒▒▒▒▒▒▒▒▒▒█▒▒▒▒█▒▒▒▒▒▒█▒▒▒▒█
       █▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒█▒▒▒▒▒███▒▒▒▒█
       ▀█▒▒██████████▒▒▒██████▀ █▒▒▒▒█
        ▀█▒▒█▄      █▒▒▒█ █▒▒█  █▒▒▒▒█
         ▀█▒▒█▄     █▒▒▒█ █▒▒█  █▒▒▒█▀
          ▀█▒▒█     █▒▒█▀ █▒▒█  █▒▒█▀
           ▀█▒█     █▒█▀  █▒▒█  █▒█▀
            ▀██     ██▀   ▀██▀  ██▀⠀⠀
    """)


# 좀비 AA 출력 함수
def zombie_AA():
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠾⠛⠉⠉⠀⠀⠀⠀⠀⠀⢀⡤⠊⠉⠉⠛⠳⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢮⡀⠀⠀⠀⠀   ⠀⠀⠙⢷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⡡⢤⠀⠀⠀⢰⣛⣉⣉⣓⠢⣄⠀⠀⠀⠈⢉⡁⠐⠒⠒⠂⠉⠉⠉⠛⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠁⣘⡒⠁⢀⠀⠀⠀⣀⣀⣀⣈⣹⣾⣕⠀⢠⡎⠁⡹⠀⣠⠄⠀⠀⠀⠀ ⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢀⣎⡩⠃⢠⣏⡴⠞⠛⠉⠉⠀⠀⠀⠀⠹⡏⠀⠉⠉⣠⣾⠖⠋⠉⠻⣅⠀⣠⠖⢲⠌⢻⡄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣿⡠⠔⢿⠀⢀⡟⠉⠀⠀⠀⣀⣤⣤⡀⠀⠀⠀⣿⠀⠀⠀⡼⠉⠉⠒⢦⣀⠘⠷⡛⠒⡿⣄ ⠈⣷⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⣠⠏⠀⢸⠀⠀⠀⠀⢰⣿⣿⣿⡇⠀⠀⢀⡿⠀⠀⣸⠃⠀⠀⣀⣄⡙⢷⣄⡇⠘⠀⢸⡆ ⢹⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢸⣧⠞⠁⠀⠀⢸⡆⠀⠀⠀⠸⣿⣿⡿⠃⠀⢀⣼⠃⠀⠀⣿⣆⠀⠀⣿⣿⡟⠀⠙⣧⠳⡤⠞⠀⢸⡇⠀⠀⠀⠀
    ⠀⢀⣠⠤⠤⢄⡀⠈⣧⢈⣧⠀⠀⢸⣿⣄⣀⣀⣠⣬⣥⠴⠶⢚⣿⠋⠀⠀⠀⢻⣿⣦⣄⠈⠁⠀⠀⣰⠟⠆⠀⠀⠀⢸⣡⠴⠖⠶⣦
    ⢠⠏⠀⠀⠀⢀⠈⠓⢿⡄⢳⠀⠀⠀⢳⣌⠻⠯⣤⣀⣀⣀⣴⣿⠏⢀⣶⢰⣦⠈⢿⣿⣿⣷⣀⣠⡼⠋⠀⢀⡀⠀⢀⣿⠥⢄⠀⠀⣿
    ⣏⠀⠀⠀⡟⢉⡽⣦⡈⢻⣼⠄⠀⠀⠀⠉⠓⠦⠤⠬⣏⣡⠾⠃⢀⣾⣿⢸⣿⣇⠈⠻⡯⠽⢯⡽⠁⠠⣴⠝⠃⢀⣾⢋⣁⠈⢀⡾⠃
    ⠘⠶⠲⢦⣷⠸⣤⣸⡇⠀⢻⣦⡀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠘⠛⠋⠘⠋⠋⠀⠀⠑⠚⠉⠀⠀⠀⠈⣠⣠⡾⠳⠤⣿⡀⣾⠁⠀
    ⠀⠀⠀⠀⠸⢧⠉⠉⠀⢀⡾⠀⠉⠻⣦⠀⠀⠀⠈⢟⡽⠄⠀⠀⢀⣀⣤⣤⣤⣄⣀⠀⠀⠀⢀⡀⠀⠀⣴⡿⠛⠻⢶⣤⣿⡿⠋⠀⠀
    ⠀⠀⠀⠀⠀⠙⠒⠒⠚⠋⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠁⠀⣠⣾⡿⢿⠀⠀⢀⣮⣙⡻⣦⡈⠙⠿⠀⣸⠏⠀⠀⠀⠀⢀⣿⣇⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡆⠀⠀⠀⠀⣼⣿⣿⣇⣸⣷⣶⣾⡀⣯⣻⣿⣿⡄⠀⠀⡿⠀⠀⠀⠀⠀⢻⣾⡛⡇⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⡇⠀⠀⠀⠀⠀⠀⠛⠟⠁⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⡀⠀⢸⣿⣿⡟⢻⡿⠿⣇⣿⢸⠿⣿⣿⣿⡏⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠐⡇⠀⠸⣯⠉⠙⠒⣃⣀⣈⣭⣭⣤⣀⣩⡟⠁⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠃⠀⣀⣽⠷⠞⠛⠉⠉⠁⠀⣠⠤⠤⢤⣉⠙⠢⠤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠘⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⠀⠹⠂⠀  ⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠶⢦⣤⣀⣀⠀⠀⠀⠀⢀⣈⣛⣥⣤⠴⠾⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀
    """)


#Game over 출력 함수
def Game_over_AA():
    print("""
     @@@@@     @    @     @ @@@@@@@        @@@@@  @     @ @@@@@@@ @@@@@@ 
    @     @   @ @   @@   @@ @             @     @ @     @ @       @     @  
    @        @   @  @ @ @ @ @             @     @ @     @ @       @     @ 
    @  @@@@ @     @ @  @  @ @@@@@         @     @ @     @ @@@@@   @@@@@@
    @     @ @@@@@@@ @     @ @             @     @  @   @  @       @   @  
    @     @ @     @ @     @ @             @     @   @ @   @       @    @  
     @@@@@  @     @ @     @ @@@@@@@        @@@@@     @    @@@@@@@ @     @
        """)


#해골 AA 출력 함수
def skull_AA():
    print("""
                         .@@@@@@@@@@'.
                      .@@@@@@@@@@@@@@@@@@.
                    .X@@@@@@@@@@@@@@@@@@@@@@:.
                   :@@@@@@@@@@@@@@@@@@@@@@@@@@:
                  !@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
                 :!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!
                 ~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!
                   !@@@@@@@@@@@@@@@@@@@@@@@@@@@@!
                   ~?WuxiW*`   `@@@@@@@@@@@@@@@!
                 :@@@@$$$$       `"@@@@@@@@@@@@!
                :%@@@~@$$$m:        @@@@@@@@@@@
              :!`@@@@@@@@@@@@@x.  .x@@@@~""@@*"
    .....   -~@@&lt;@@@@@@@@@@@@@@@W@*?$    /`
    @@@@@@@@@.!~~@!!@@@@@.@@@@@@!   `@@:    :
    @@@@@@@@@@@@  !H:@@@!WM$$$$Ti.: .@@@@@!`
    :@@@@@@@@X~@@@ ?H@@@@@@@@@@@@@@@@@@@@M~
    .@@@@@@@@@@-@@  ?@@@@@@@@@@@@@@@$! `
    @@@@@@@@@@@@ @ : ?@@@B@Wu("**$RM!
    $R@i@@@@@@@@@@@@  ~@@@@@@@@@@:``
    @@@@@@@@@@@@@@@@@  ~"...@@@..~
    """)


# 동혀니 AA 출력 함수
def donghyeon_AA():
    print("""
           ▄▀▀▀▀▀▀▀▀▀▀▄▄
        ▄▀▀             ▀▄
      ▄▀                  ▀▄
      █                     ▀▄
     ▐▌        ▄▄▄▄▄▄▄       ▐▌
     █           ▄▄▄▄  ▀▀▀▀▀  █
    ▐▌       ▀▀▀▀     ▀▀▀▀▀   ▐▌
    █         ▄▄▀▀▀▀▀    ▀▀▀▀▄ █
    █                ▀   ▐     ▐▌
    ▐▌         ▐▀▀██▄      ▄▄▄ ▐▌
     █           ▀▀▀      ▀▀██  █
     ▐▌    ▄             ▌      █
      ▐▌  ▐              ▀▄     █
       █   ▌        ▐▀    ▄▀   ▐▌
       ▐▌  ▀▄        ▀ ▀ ▀▀   ▄▀
       ▐▌  ▐▀▄                █
       ▐▌   ▌ ▀▄    ▀▀▀▀▀▀   █
       █   ▀    ▀▄          ▄▀
      ▐▌          ▀▄      ▄▀
     ▄▀   ▄▀        ▀▀▀▀█▀
    ▀   ▄▀          ▀   ▀▀▀▀▄▄▄▄▄    
    """)


# 홍거리 AA 출력 함수
def honggeol_AA():
    print("""
    　　　　　　▄████████████████▄
    　　　　　████████████████████▄
    　　　　███████████████████████▄
    　　　██████████▀　　　　　　　　　▀▄
    　　　██████████　　　　　　　　　　　▀▄
    　　 ██████████ ▄████▄　　　　 ▄███▄█
    　　 █████████  ██▀▀███▄   ▄██▀▀███
    　　 ████████   ██ ▀ ███   ███ ▀ ██
    　　 ██▀ █ ▀█   ▀████▀    ▀██████▀
    　　█▒     ▀            ▄█       █
    　 ▄█▒         ▓▓            ▓▓  █
    　▄█▒▒           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓  █
     ▄█▒▒▒             ▓▓▓▓▓▓▓▓    ▄█
    ▄█▒▒▒▒                         ▄▀
    █▒▒▒▒▒▒                     ▄▄▀
    █▒▒▒▒▒▒▒▒              ▄▄▄▀▀
    █▒▒▒▒▒▒▒▒▒▒      ▄▄▄▀▀▀▀
    █▒▒▒▒▒▒▒▒▒▒▒  ▄▄▀▀
    ███████████████
    ▓██▓▓▓▓█████▓███
    ▓▓██▓▓▓▓███▓▓█▓██
    ▓▓▓██▓▓▓███▓▓█▓▓██
    ▓▓▓▓██████████▓▓▓██
    ▓▓▓▓▓▓██████▓▓▓▓▓▓██
    """)


# 포탈 AA 출력 함수
def portal_AA():
    print("""
    88888888888888888888888888888888888888888888888888888888888888888888888
    88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
    88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
    88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
    88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
    88   |``"..__ |    |`";.| i|_|`- |    | -`|_|'| _!-|   |   _|..-|'   88
    88   |      |``--..|_ | `;!|l| _!|●   | !_|1|.'j   |_..!-'|     |    88
    88   |      |    |   |`-,!_|_|..-|____|-..|_||.!-;'  |    |     |    88
    88___|______|____!.,.!,.!,!|d| | /    \ | |p|,!,.!.,.!..__|_____|____88
    88      |     |    |  |  | |_| / ██████ \||_|| |   |   |    |      | 88 
    88      |     |    |..!-;'i|r| !/      \  |r| |`-..|   |    |      | 88
    88      |    _!.-j'  | _!,"|_|/ ████████ \|_||!._|  `i-!.._ |      | 88
    88     _!.-'|    | _."|  !;|1|!/        \ |l|`.| `-._|    |``-.._  | 88
    88..-i'     |  _.''|  !-| !|_| ██████████ |_|.|`-. | ``._ |     |``".88
    88   |      |.|    |.|  !| |u|/          \|n||`. |`!   | `".    |    88
    88   |  _.-'  |  .'  |.' |/|_|████████████|_|! |`!  `,.|    |-._|    88
    88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMMM[@] \|  `. | `._  |   `-._ 88
    88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
    88      |_.'|   .' | .' |/                   \  \ |  `.  | `._-Lee|  88
    88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
    88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
    88888888888888888888888888888888888888888888888888888888888888888888888
    """)


# 버그베어 AA 출력 함수
def bugbear_AA():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡖⠲⡄⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠃⠀⠉⠉         ⠉⠓⠞⠉⢣⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠈⠳⡄⠀⠀⠀
⠀⠀⠀⠀⣰⠉⠀⠀⠀⠀⠀●⠀⠀⠀⠀⠀⠀●⠀⠀⠀⠀       ⠀⠙⡆⠀⠀
⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⢿⢯⡭⣉⣷⣖⠀⠀⠀⠀⠀⠀⠀     ⠀⢹⠀⠀
⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⠀⢸⠀⠀
⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ⢸⠀⠀
⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀     ⣀⡎⠀⠀
⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀   ⢀⡴⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⢀⡠⠖⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠑⠒⠒⠶⠶⠶⠶⠖⠒⠛⠉⠀⠀⠀⠀⠀
    """)


# -------------------------------------------- 아래부터 던전 함수 ---------------------------------------------------------


# 던전 만드는 함수, 변수들 앞에 이니셜 mm 붙임
def make_maze(mm_border = 1):      # make_maze함수의 매개변수 border의 기본값 1로 해줌
    # 10 x 10(임의)로 행렬 크기 설정
    cols = 15
    rows = 15
    # cols, rows 행변수, 열변수의 값만큼 행렬 크기를 설정한 값을 maze 변수에 넣음
    mm_maze = [["X" for j in range(cols)] for i in range(rows)]

    # 던전 좌표마다 랜덤 값 부여
    for mm_x in range(len(mm_maze)):
        for mm_y in range(len(mm_maze)):
            # 0은 아무 이벤트 없음, 1은 몬스터 출현, 2는 포션
            mm_event = random.randint(0, 2)
            if mm_event == 0:
                mm_maze[mm_x][mm_y] = '⬜'
            elif mm_event == 1:
                mm_maze[mm_x][mm_y] = '😈'
            elif mm_event == 2:
                mm_maze[mm_x][mm_y] = '🍖'

    # 테두리 함수 사용해서 테두리 지정 (12.09 연수)
    mm_maze = bord(mm_maze, mm_border)

    return mm_maze


# 테두리 함수 (12.09 연수)
def bord(bo_maze, bo_border = 1):
    bo_line = ''

    if bo_border == 1:
        bo_line = '🏔'
    elif bo_border == 2:
        bo_line = '🌈'
    elif bo_border == 3:
        bo_line = '🌋'

    # 10x10의 테두리 bd_line 변수값으로 지정
    for bo_x in range(len(bo_maze)):  # 상단 테두리
        bo_maze[bo_x][0] = bo_line
    for bo_x in range(len(bo_maze)):  # 좌측 테두리
        bo_maze[0][bo_x] = bo_line
    for bo_x in range(len(bo_maze)):  # 우측 테두리
        bo_maze[len(bo_maze) - 1][bo_x] = bo_line
    for bo_x in range(len(bo_maze)):  # 아래 테두리
        bo_maze[bo_x][len(bo_maze) - 1] = bo_line

    # 테두리 수정한 던전, 테두리 이모지 변수 반환
    return bo_maze


# 던전 출력 함수
def print_map(pm_maze, si_choco):
    # 현재 상태 창
    print('─' * 38)
    print(f"{'😊':>13}{si_choco[0]}😊")
    print(f"HP: {si_choco[2][0]}/{si_choco[2][1]}  🥊공격력🥊: {si_choco[1][0]}~{si_choco[1][1]}")
    print(f"🍖({si_choco[3]}) 🍭({si_choco[4]})")
    print('─' * 38)
    # 10 x 10(임의)로 행렬 크기 설정
    cols = 15
    rows = 15

    # 랜덤으로 뽑은 a, b를 인덱스 값으로 지정해서 포탈을 생성해 줍니다
    potal_a = 2#random.randrange(1, len(pm_maze))
    potal_b = 2#random.randrange(1, len(pm_maze))
    pm_maze[potal_a][potal_b] = '🚪'

    # (1, 1)자리에 스폰
    mx = 1
    my = 1
    pm_maze[mx][my] = "😊"

    # 그림자를 씌울 shadow_maze 변수
    shadow_maze = [["X" for j in range(cols)] for i in range(rows)]
    for x in range(len(shadow_maze)):
        for y in range(len(shadow_maze)):
            shadow_maze[x][y] = ('\033[100m' + '⬛' + '\033[0m')

    # 던전을 3개 만들었습니다.
    maze1 = make_maze(1)
    maze2 = make_maze(2)
    maze3 = make_maze(3)

    # maze1 = 🏔던전, maze2 = 🌈던전, maze3 = 🌋던전
    map_list = [maze1, maze2, maze3]

    # 맵 출력
    for i in range(len(pm_maze)):
        for j in range(len(pm_maze)):
            # 주인공 주변 3x3만 보이게 출력
            if (i == (mx - 1) and j == (my - 1)) or (i == mx and j == (my - 1)) or (i == (mx + 1) and j == (my - 1)) \
                    or (i == (mx - 1) and j == my) or (i == mx and j == my) or (i == (mx + 1) and j == my) \
                    or (i == (mx - 1) and j == (my + 1)) or (i == mx and j == (my + 1)) or (
                    i == (mx + 1) and j == (my + 1)):
                print('\033[103m' + pm_maze[i][j] + '\033[0m', end='')
            # 주인공 주변 3x3이 아니면 그림자 출력
            else:
                print(shadow_maze[i][j], end='')
        print()
    print('─' * 38)

    cnt = 0

    while 1:
        print()
        pm_border = pm_maze[0][0]
        # 키보드 입력
        while 1:
            if keyboard.is_pressed('Up'):
                key = 'up'
                time.sleep(0.1)
                break
            elif keyboard.is_pressed('Down'):
                key = 'down'
                time.sleep(0.1)
                break
            elif keyboard.is_pressed('Left'):
                key = 'left'
                time.sleep(0.1)
                break
            elif keyboard.is_pressed('Right'):
                key = 'right'
                time.sleep(0.1)
                break

        # 위로 이동
        if key == "up" and pm_maze[mx - 1][my] != pm_maze[0][0]:    # 테두리값 = pm_maze[0][0]으로 바꿈(12.09 연수)
            # 기존 주인공 자리 0으로 초기화
            pm_maze[mx][my] = '⬜'
            print(f'{"<위로 전진!>":^33}')
            # 이동하는 곳의 값이 1이면 몬스터 이벤트 발생
            if pm_maze[mx - 1][my] == '😈':
                battle(si_choco)
            # 이동하는 곳의 값이 P이면 포탈 이벤트 발생
            elif pm_maze[mx - 1][my] == '🚪':
                print(f'{"<다음 던전으로 이동합니다...>":^33}')
                # 딜레이 1초
                time.sleep(1)
                # 포탈 이동 화면
                portal_AA()
                time.sleep(1)
                # 다음 던전으로 랜덤 이동 수정 (12.10  기태)
                if pm_border == '🏔':
                    #rv는 maplist[rv]로 포탈 이동시 같은 맵 처음으로 이동하지 않게함.
                    rv = random.randint(1,2)
                elif pm_border == '🌈':
                    # 0과 2중 하나만 고르고 싶었는데 리스트를 따로 만들지않고 02 라는 문자열에서 한 글자만 가져온뒤
                    rv = random.choice('02')
                    #rv 를 int 형으로 바꿔줌
                    rv = int(rv)
                elif pm_border == '🌋':
                    rv = random.randint(0,1)
                a = map_list[rv]
                # 던전 들어가는 곳에 따라서 출력 문구 맞춤 - 수정 (12.09 연수)
                if map_list.index(a) == 0:
                    print(f'{"<산맥 던전에 입장했습니다>":^33}')
                elif map_list.index(a) == 1:
                    print(f'{"<무지개 던전에 입장했습니다>":^33}')
                elif map_list.index(a) == 2:
                    print(f'{"<마그마 던전에 입장했습니다>":^33}')
                return print_map(a, si_choco)
            # 이동하는 곳의 값이 2면 포션 획득
            elif pm_maze[mx - 1][my] == '🍖':
                print(f'{"<포션을 획득했습니다!>":^33}')
                si_choco[3] += 1
            mx -= 1
            cnt += 1
        # 왼쪽 이동
        elif key == "left" and pm_maze[mx][my - 1] !=  pm_maze[0][0]:
            # 기존 주인공 자리 0으로 초기화
            pm_maze[mx][my] = '⬜'
            print(f'{"<왼쪽으로 전진!>":^33}')
            # 이동하는 곳의 값이 1이면 몬스터 이벤트 발생
            if pm_maze[mx][my - 1] == '😈':
                battle(si_choco)
            # 이동하는 곳의 값이 P이면 포탈 이벤트 발생
            elif pm_maze[mx][my - 1] == '🚪':
                print(f'{"<다음 던전으로 이동합니다...>":^33}')
                # 딜레이 1초
                time.sleep(1)
                # 포탈 이동 화면
                portal_AA()
                time.sleep(1)
                # 다음 던전으로 랜덤 이동 수정 (12.10  기태)
                if pm_border == '🏔':
                    #rv는 maplist[rv]로 포탈 이동시 같은 맵 처음으로 이동하지 않게함.
                    rv = random.randint(1,2)
                elif pm_border == '🌈':
                    # 0과 2중 하나만 고르고 싶었는데 리스트를 따로 만들지않고 02 라는 문자열에서 한 글자만 가져온뒤
                    rv = random.choice('02')
                    #rv 를 int 형으로 바꿔줌
                    rv = int(rv)
                elif pm_border == '🌋':
                    rv = random.randint(0,1)
                a = map_list[rv]
                # 던전 들어가는 곳에 따라서 출력 문구 맞춤 - 수정 (12.09 연수)
                if map_list.index(a) == 0:
                    print(f'{"<산맥 던전에 입장했습니다>":^33}')
                elif map_list.index(a) == 1:
                    print(f'{"<무지개 던전에 입장했습니다>":^33}')
                elif map_list.index(a) == 2:
                    print(f'{"<마그마 던전에 입장했습니다>":^33}')
                return print_map(a, si_choco)
            # 이동하는 곳의 값이 2면 포션 획득
            elif pm_maze[mx][my - 1] == '🍖':
                print(f'{"<포션을 획득했습니다!>":^33}')
                si_choco[3] += 1
            my -= 1
            cnt += 1
        # 아래 이동
        elif key == "down" and pm_maze[mx + 1][my] !=  pm_maze[0][0]:
            # 기존 주인공 자리 0으로 초기화
            pm_maze[mx][my] = '⬜'
            print(f'{"<아래로 전진!>":^33}')
            # 이동하는 곳의 값이 1이면 몬스터 이벤트 발생
            if pm_maze[mx + 1][my] == '😈':
                battle(si_choco)
            # 이동하는 곳의 값이 P이면 포탈 이벤트 발생
            elif pm_maze[mx + 1][my] == '🚪':
                print(f'{"<다음 던전으로 이동합니다...>":^33}')
                # 딜레이 1초
                time.sleep(1)
                # 포탈 이동 화면
                portal_AA()
                time.sleep(1)
                # 다음 던전으로 랜덤 이동 수정 (12.10  기태)
                if pm_border == '🏔':
                    #rv는 maplist[rv]로 포탈 이동시 같은 맵 처음으로 이동하지 않게함.
                    rv = random.randint(1,2)
                elif pm_border == '🌈':
                    # 0과 2중 하나만 고르고 싶었는데 리스트를 따로 만들지않고 02 라는 문자열에서 한 글자만 가져온뒤
                    rv = random.choice('02')
                    #rv 를 int 형으로 바꿔줌
                    rv = int(rv)
                elif pm_border == '🌋':
                    rv = random.randint(0,1)
                a = map_list[rv]
                # 던전 들어가는 곳에 따라서 출력 문구 맞춤 - 수정 (12.09 연수)
                if map_list.index(a) == 0:
                    print(f'{"<산맥 던전에 입장했습니다>":^33}')
                elif map_list.index(a) == 1:
                    print(f'{"<무지개 던전에 입장했습니다>":^33}')
                elif map_list.index(a) == 2:
                    print(f'{"<마그마 던전에 입장했습니다>":^33}')
                return print_map(a, si_choco)
            # 이동하는 곳의 값이 2면 포션 획득
            elif pm_maze[mx + 1][my] == '🍖':
                print(f'{"<포션을 획득했습니다!>":^33}')
                si_choco[3] += 1
            mx += 1
            cnt += 1
        # 오른쪽 이동
        elif key == "right" and pm_maze[mx][my + 1] != pm_maze[0][0]:
            # 기존 주인공 자리 0으로 초기화
            pm_maze[mx][my] = '⬜'
            print(f'{"<오른쪽으로 전진!>":^33}')
            # 이동하는 곳의 값이 1이면 이벤트 발생
            if pm_maze[mx][my + 1] == '😈':
                battle(si_choco)
            # 이동하는 곳의 값이 P이면 포탈 이벤트 발생
            elif pm_maze[mx][my + 1] == '🚪':
                print(f'{"<다음 던전으로 이동합니다...>":^33}')
                # 딜레이 1초
                time.sleep(1)
                # 포탈 이동 화면
                portal_AA()
                time.sleep(1)
                # 다음 던전으로 랜덤 이동 수정 (12.10  기태)
                if pm_border == '🏔':
                    #rv는 maplist[rv]로 포탈 이동시 같은 맵 처음으로 이동하지 않게함.
                    rv = random.randint(1,2)
                elif pm_border == '🌈':
                    # 0과 2중 하나만 고르고 싶었는데 리스트를 따로 만들지않고 02 라는 문자열에서 한 글자만 가져온뒤
                    rv = random.choice('02')
                    #rv 를 int 형으로 바꿔줌
                    rv = int(rv)
                elif pm_border == '🌋':
                    rv = random.randint(0,1)
                a = map_list[rv]
                # 던전 들어가는 곳에 따라서 출력 문구 맞춤 - 수정 (12.09 연수)
                if map_list.index(a) == 0:
                    print(f'{"<산맥 던전에 입장했습니다>":^33}')
                elif map_list.index(a) == 1:
                    print(f'{"<무지개 던전에 입장했습니다>":^33}')
                elif map_list.index(a) == 2:
                    print(f'{"<마그마 던전에 입장했습니다>":^33}')
                return print_map(a, si_choco)
            # 이동하는 곳의 값이 2면 포션 획득
            elif pm_maze[mx][my + 1] == '🍖':
                print(f'{"<포션을 획득했습니다!>":^33}')
                si_choco[3] += 1
            my += 1
            cnt += 1
        # 이동 불가
        else:
            print(f'{"그 쪽으론 갈 수 없습니다.":^33}')

        if cnt == 3:
            pm_border = pm_maze[0][0]   # 테두리 기존 던전 테두리로 고정 (연수)
            pm_maze = make_maze()
            pm_maze[potal_a][potal_b] = '🚪'
            # 다시 테두리 덮어씀 (연수)
            for pm_x in range(len(pm_maze)):  # 상단 테두리
                pm_maze[pm_x][0] = pm_border
            for pm_x in range(len(pm_maze)):  # 좌측 테두리
                pm_maze[0][pm_x] = pm_border
            for pm_x in range(len(pm_maze)):  # 우측 테두리
                pm_maze[len(pm_maze) - 1][pm_x] = pm_border
            for pm_x in range(len(pm_maze)):  # 아래 테두리
                pm_maze[pm_x][len(pm_maze) - 1] = pm_border
            cnt = 0
            print(f'{"던전의 모양이 바꼈습니다!":^33}')

        pm_maze[mx][my] = "😊"
        # 현재 상태 창
        print('─' * 38)
        print(f"{'😊':>13}{si_choco[0]}😊")
        print(f"HP: {si_choco[2][0]}/{si_choco[2][1]}  🥊공격력🥊: {si_choco[1][0]}~{si_choco[1][1]}")
        print(f"🍖({si_choco[3]}) 🍭({si_choco[4]})")
        print('─' * 38)
        # 이동한 맵 출력
        for i in range(len(pm_maze)):
            for j in range(len(pm_maze)):
                if (i == (mx - 1) and j == (my - 1)) or (i == mx and j == (my - 1)) or (i == (mx + 1) and j == (my - 1)) \
                        or (i == (mx - 1) and j == my) or (i == mx and j == my) or (i == (mx + 1) and j == my) \
                        or (i == (mx - 1) and j == (my + 1)) or (i == mx and j == (my + 1)) or (
                        i == (mx + 1) and j == (my + 1)):
                    print('\033[103m' + pm_maze[i][j] + '\033[0m', end='')
                else:
                    print(shadow_maze[i][j], end='')
            print()
        print('─' * 38)


def main():
    print(f'{"<초코의용군의 대모험!>":^33}')
    maze = make_maze()
    si_choco = ['초코의용군', [0, 1], [500, 500], 0, 1]
    print(f'{"던전에 입장합니다...":^33}')
    print_map(maze, si_choco)


main()
