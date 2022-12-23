import random
import keyboard
import time


# 던전 클래스 (이벤트만 있는)
class Dungeon:
    def __init__(self, cols, rows, border):  # 던전의 크기를 정하는 메서드
        self.cols = cols  # 열
        self.rows = rows  # 행
        self.border = border  # 테두리

        # 행과 열의 길이만큼 행렬 크기 맞춤제작
        self.maze = [["X" for j in range(self.cols)] for i in range(self.rows)]  # 던전

        potal_x = random.randrange(2, len(self.maze) - 1)
        potal_y = random.randrange(2, len(self.maze) - 1)
        self.potal_x = potal_x  # 포탈 위치
        self.potal_y = potal_y

    # 이벤트들로 던전을 채우는 메서드
    def make_maze(self):
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                # 0은 아무 이벤트 없음, 1은 몬스터 출현, 2는 포션
                event = random.randint(0, 2)
                if event == 0:
                    self.maze[x][y] = '⬜'
                elif event == 1:
                    self.maze[x][y] = '😈'
                elif event == 2:
                    self.maze[x][y] = '🍖'

    # 테두리를 지정 테마로 바꿔주는 메서드
    def theme(self):
        for x in range(len(self.maze)):  # 상단 테두리
            self.maze[x][0] = self.border
        for x in range(len(self.maze)):  # 좌측 테두리
            self.maze[0][x] = self.border
        for x in range(len(self.maze)):  # 우측 테두리
            self.maze[len(self.maze) - 1][x] = self.border
        for x in range(len(self.maze)):  # 아래 테두리
            self.maze[x][len(self.maze) - 1] = self.border

    # 포탈 메서드
    def potal(self):
        # 던전의 포탈 위치 랜덤생성
        self.maze[self.potal_x][self.potal_y] = '🚪'


# 몬스터의 정보를 나타내는 클래스
class Monster:
    cannot_att = 0  # 0이면 몬스터 공격 가능 1이상이면 공격 불가(보우연재의 디버프)

    def __init__(self, name, att, hp):  # 생성자 메서드
        self.name = name  # 몬스터 이름
        self.att = att  # 공격력(랜덤하게 들어감)
        self.maxHp = hp  # 최대 체력
        self.nowHp = hp  # 현재 체력(남은 체력)

    # 몬스터 조우시 출력하는 메서드
    def monster_stat(self):
        print(f'{"[":>28}{self.name}]\n'
              f'{"[HP]":>27} {self.nowHp}/{self.maxHp}')


# 파티원 정보 클래스
class Party:
    att = [10000, 15000]  # 공격력 클래스 변수로 넣어줌(전부 공격력 계수는 같으니까)

    potion = 0
    elixir = 1
    ramen = 0
    cook_ramen = 0
    boiled_ramen = 0
    confu = 0
    confu_save = 0
    ricecake = 0
    ricecake_save = 0
    cigarette = 0
    cigarette_save = 0

    def __init__(self, name, hp, mp):
        self.name = name
        self.nowHp = hp
        self.maxHp = hp
        self.nowMp = mp
        self.maxMp = mp
        self.invincibility = 0  # 무적변수
        self.confu = 0  # 범규약 콘푸로스트 효과를 받는 턴 수
        self.ricecake = 0  # 범규약 떡하나 효과를 받는 턴 수
        self.rand_Hp = random.randint((self.nowHp * 0.3), (self.nowHp * 0.8))  # 랜덤 Hp
        self.rand_Mp = random.randint((self.nowHp * 0.3), (self.nowHp * 0.8))  # 랜덤 Mp

    # 파티원 HP 출력 메서드
    def party_hp(self):
        print(f"{'[HP]':>6} {self.nowHp}/{self.maxHp}", end='')

    # 파티원 MP 출력 메서드
    def party_mp(self):
        print(f"{'[MP]':>6} {self.nowMp}/{self.maxMp}", end='')

    # (보라) 포션 메서드 아래부터
    def potion_mt(self):  # 포션
        if self.nowHp == self.maxHp:
            print('풀피로 마실수 없습니다')
            return 0

        if Party.potion >= 1:  # 포션개수가 1개이상
            print()
            print('포션 사용')
            print(f'{self.name}의 [HP {self.rand_Hp}] [MP {self.rand_Mp}] 회복되었습니다')
            self.nowHp += self.rand_Hp  # 현재 체력에 랜덤체력 더해주기
            self.nowMp += self.rand_Mp  # 현재 마나에 랜덤마나 더해주기
            Party.potion -= 1  # 포션 차감
            if self.rand_Hp > self.maxHp:  # 더해진 체력이 max를 넘어갈경우
                self.nowMp = self.maxHp
            if self.rand_Mp > self.maxMp:  # 더해진 마나가 max를 넘어갈경우
                self.nowMp = self.maxHp
            return 1

        else:  # 포션이 없는경우
            print()
            print('포션이 없습니다.')
            print('전투복귀')
            return 0

    def elixir_mt(self):  # 엘릭서
        if Party.elixir >= 1:  # 엘릭서개수가 1개이상
            print()
            print('엘릭서 사용')
            self.invincibility += 10  # 무적변수 턴차감
            print(f'{self.name} {self.invincibility}턴 무적상태로 변신')
            Party.elixir -= 1  # 엘릭서 차감
            return 1
        else:  # 엘릭서가 없는 경우
            print()
            print('엘릭서가 없습니다.')
            print('전투복귀')
            return 0

    def ramen_mt(self,party_list):  # 라면
        # 라면을 끓일지 / 라면을 먹을지
        while True:
            choice_ramen = input("1. 라면 끓이기 2. 라면 먹기 3. 취소하기")
            if choice_ramen == '1' :  # 1. 라면 끓이기
                if Party.ramen > 0:     #라면 있을 떄
                    print()
                    print('당신과함께라면 끓이기시작')
                    print('다음턴으로 넘어갑니다')
                    Party.ramen -= 1  # 생라면 1개 차감
                    Party.cook_ramen += 1  # 라면끓이는 중 1개 추가
                    return 1
                if Party.ramen <= 0:        #라면 없을 때
                    print()
                    print('라면이 없습니다. 전투를 하고 라면을 얻어보세요.')
                    continue

            elif choice_ramen == '2':  # 2. 라면 먹기
                if Party.boiled_ramen == 0:    # 라면 없을 때
                    print("라면이 없습니다. 먼저 라면을 끓여주세요")
                    continue
                elif Party.boiled_ramen >= 1:       # 라면 있을 때
                    print()
                    print('당신과함께라면 냠냠')
                    ramen_hp = party_list[0].maxHp * 0.5    # 초코의용의 maxHp만큼 전원 회복시킬 변수
                    ramen_mp = party_list[0].maxMp * 0.5    # 초코의용의 maxMp만큼 전원 회복시킬 변수

                    for i in range (4):     # party_list의 인원만큼 반복
                        if party_list[i].nowHp == 0:        # 죽은 사람은 제외
                            pass
                        else:
                            party_list[i].nowHp += ramen_hp     # 초코의용의 maxHp만큼 전원 회복
                            party_list[i].nowMp += ramen_mp     # 초코의용의 maxMp만큼 전원 회복

                            if party_list[i].nowHp > party_list[i].maxHp:       # maxHp 보다 커질 경우
                                party_list[i].nowHp = party_list[i].maxHp

                            if party_list[i].nowMp > party_list[i].maxMp:       # maxMp 보다 커질 경우
                                party_list[i].nowMp = party_list[i].maxMp

                        print(f"{party_list[i].name}의 상태 {party_list[i].nowHp}, {party_list[i].nowMp}") #회복된 것 확인
                    Party.boiled_ramen -= 1  # 라면 차감
                    return 1
            elif choice_ramen == '3':   # 3.취소하기
                print("취소하기를 선택했습니다")
                print("이전 선택창으로 돌아갑니다")
                print()
                return 0
            else:               # 잘못 눌렀을 경우
                print("잘못 눌렀습니다")
                continue

    def bum_medicine_mt(self):  # 범규약
        md_choice = input('[1번 콘푸라이트] [2번 떡하나] [3번 담배] [4번 취소]')
        while True:
            if md_choice == '1':  # 콘푸라이트를 선택한 경우
                if Party. confu_save >= 1:  # 콘푸라이트 1개이상 사용가능
                    print()
                    print('─' * 60, '\n')
                    # 약범규 죽으면 회복 불가능
                    if self.nowHp == 0:
                        print("회복할 수 없습니다")
                        break
                    # hp가 최대 hp면 회복 스킵
                    elif self.nowHp == self.maxHp:
                        print("현재 최대 체력입니다")
                        break
                    # 현재 hp가 최대 hp 보다 5% 아래면 둘 다 회복
                    elif self.nowHp + round(self.maxHp * 0.05) <= self.maxHp:
                        self.nowHp += round(self.maxHp * 0.05)
                        print(f'{"호랑이 기운이 솟아나요":>33}')
                        # 체력 5% 회복
                        print(f'{f"{self.name} 체력 5% 회복!":>33}\n')
                    # 현재 hp를 5% 회복 했을 때 hp가 최대 hp 보다 많으면, 현재 hp = 최대 hp 로 설정
                    elif self.nowHp + round(self.maxHp * 0.05) > self.maxHp:
                        self.nowHp = self.maxHp
                        print(f'{"호랑이 기운이 솟아나요":>33}')
                        # 체력 5% 회복
                        print(f'{f"{self.name} 체력 5% 회복!":>33}\n')
                    Party.confu -= 1  # 콘푸라이트 차감
                    return 1
                else:  # 범규약 없는 경우
                    print()
                    print('콘푸라이트가 없습니다')
                    break      # 이전 선택지로 돌아감

            if md_choice == '2':  # 떡하나를 선택한 경우
                if Party.ricecake_save >= 1:  # 떡 개수 1개이상 사용가능
                    print()
                    # 약범규 죽으면 회복 불가능
                    if self.nowHp == 0:
                        print("회복할 수 없습니다")
                        break
                    # hp가 최대 hp면 회복 스킵
                    elif self.nowHp == self.maxHp:
                        print("현재 최대 체력입니다")
                        break
                    # 현재 hp가 최대 hp 보다 20% 아래면 둘 다 회복
                    elif self.nowHp + round(self.maxHp * 0.2) <= self.maxHp:
                        self.nowHp += round(self.maxHp * 0.2)
                        print(f'{"떡하나주면 안잡아먹지":>33}\n')
                        # 체력 20% 회복
                        print(f'{f"{self.name} 체력 20% 회복!":>33}\n')
                    # 현재 hp를 20% 회복 했을 때 hp가 최대 hp 보다 많으면, 현재 hp = 최대 hp 로 설정
                    elif self.nowHp + round(self.maxHp * 0.2) > self.maxHp:
                        self.nowHp = self.maxHp
                        print(f'{"떡하나주면 안잡아먹지":>33}\n')
                        # 체력 20% 회복
                        print(f'{f"{self.name} 체력 20% 회복!":>33}\n')
                    Party.ricecake -= 1  # 떡 차감
                    return 1
                else:  # 떡 없는 경우
                    print()
                    print('떡이 없습니다')
                    break     # 이전 선택지로 돌아감

            if md_choice == '3':  # 담배를 선택한 경우
                if Party.cigarette_save >= 1:  # 담배 개수 1개이상 사용가능
                    print()
                    Party.cigarette -= 1  # 담배 차감
                    # 약범규 죽으면 회복 불가능
                    if self.nowHp == 0:
                        print("회복할 수 없습니다")
                        break
                    # hp가 최대 hp면 회복 스킵
                    elif self.nowHp == self.maxHp:
                        print("현재 최대 체력입니다")
                        break
                    # 현재 hp가 최대 hp 보다 50% 아래면 둘 다 회복
                    elif self.nowHp + round(self.maxHp * 0.5) <= self.maxHp:
                        self.nowHp += round(self.maxHp * 0.5)
                        print(f'{"뻐~끔 ! 뻐~끔 !":>33}\n')
                        # 체력 50% 회복
                        print(f'{f"{self.name} 체력 50% 회복!":>33}\n')
                    # 현재 hp를 50% 회복 했을 때 hp가 최대 hp 보다 많으면, 현재 hp = 최대 hp 로 설정
                    elif self.nowHp + round(self.maxHp * 0.5) > self.maxHp:
                        self.nowHp = self.maxHp
                        print(f'{"뻐~끔 ! 뻐~끔 !":>33}\n')
                        # 체력 50% 회복
                        print(f'{f"{self.name} 체력 50% 회복!":>33}\n')
                    Party.cigarette -= 1  # 담배 차감
                    return 1
                else:  # 담배없는 경우
                    print()
                    print('담배가 없습니다')
                    break        # 이전 선택지로 돌아감

            elif md_choice == '4':  # 취소하기
                print("취소하기를 선택했습니다")
                print("이전 선택창으로 돌아갑니다")
                print()
                return 0
            else:  # 잘못눌렀을 경우
                print("잘못 눌렀습니다. 다시 선택해주세요.")
                print()
                continue

    def choose_item(self, party_list):  # 아이템 선택하는 메서드
        while True:
            print("아이템을 골라주세요")
            item_choice = input("1. 포션 2. 엘릭서 3. 라면 4. 약범규의 약 5. 취소하기")  # 선택지 출력
            if item_choice == '1':  # 포션
                cancel = self.potion_mt()
            elif item_choice == '2':  # 엘릭서
                cancel = self.elixir_mt()
            elif item_choice == '3':  # 라면
                cancel = self.ramen_mt(party_list)
            elif item_choice == '4':  # 약범규의 약
                cancel = self.bum_medicine_mt()
            elif item_choice == '5':  # 취소하기
                print("취소하기를 선택했습니다")
                print("이전 선택창으로 돌아갑니다")
                print()
                return 0
            else:  # 잘못눌렀을 경우
                print("잘못 눌렀습니다. 다시 선택해주세요.")
                print()
                continue
            if cancel == 1:
                return 1
            else:
                continue


# 초코의용(완료)
class Choco(Party):  # Party 클래스 상속받은 Choco 클래스
    # Choco 클래스의 skill 메서드
    def skill(self, monster):
        while True:
            print('─' * 60, '\n')
            # 스킬 선택문
            choice = input(f'{"[":>6}{self.name}]\n'
                           f'{"[HP]":>7} {self.nowHp}/{self.maxHp} {"[1.":>13} 꺾이지 않는 마음] [2. 용사의 의지]\n'
                           f'{"[MP]":>7} {self.nowMp}/{self.maxMp} {"[3.":>18} 트리플 어택] [4. 취소]\n'
                           f'{"번호를 입력해주세요: ":>30}')

            # 초코의용 스킬 3가지
            # 1. 꺾이지 않는 마음
            if choice == '1':
                if self.nowMp <= (self.maxMp * 0.5):  # mp 부족하면 실행 안됨
                    print('─' * 60, '\n')
                    print(f'{"마나가 부족합니다.":>31}\n')
                    continue  # 선택창으로 되돌아감
                else:
                    print('─' * 60, '\n')
                    print(f'{"<":>18}{self.name}의 꺾이지 않는 마음!>\n')
                    # 1회 개인 무적(방어)
                    self.invincibility += 1
                    self.nowMp -= int(self.maxMp * 0.5)
                    print(f'{self.name:>22}은 {self.invincibility}턴 무적이 됩니다.\n')
                    return 1
            # 2. 용사의 의지
            elif choice == '2':
                if self.nowMp < (self.maxMp * 0.3):  # mp -30% 보다 부족하면 실행 안됨
                    print('─' * 60, '\n')
                    print(f'{"마나가 부족합니다.":>31}\n')
                    continue  # 선택창으로 되돌아감
                else:
                    print('─' * 60, '\n')
                    print(f'{"<":>18}{self.name}의 용사의 의지!>\n')
                    skill_att = random.randint(self.att[0] * 2, self.att[1] * 2)
                    print(f"{monster.name:>15}에게 {skill_att}의 데미지를 입혔습니다!\n")
                    monster.nowHp -= skill_att  # 몬스터 체력 차감
                    self.nowMp -= round(self.maxMp * 0.3)  # mp -30%
                    return 1
            # 3. 트리플 어택
            elif choice == '3':
                if self.nowMp < (self.maxMp * 0.4):  # mp -30% 보다 부족하면 실행 안됨
                    print('─' * 60, '\n')
                    print(f'{"마나가 부족합니다.":>31}\n')
                    continue  # 선택창으로 되돌아감
                else:
                    print('─' * 60, '\n')
                    print(f'{"<":>18}{self.name}의 트리플 어택!>\n')
                    # 3번 공격(기본 공격력의 절반 데미지로)
                    for i in range(3):
                        skill_att = random.randint(int(self.att[0] * 0.5), int(self.att[1] * 0.5))
                        print(f"{monster.name:>13}에게 {skill_att}의 데미지를 입혔습니다! {i + 1}번 공격")
                        monster.nowHp -= skill_att  # 몬스터 체력 차감
                        time.sleep(0.5)
                    print(f'{"3번 공격했습니다!":>31}\n')  # 총 몇 번 공격했는지 출력
                    self.nowMp -= round(self.maxMp * 0.4)  # mp -40%
                    return 1
            # 4. 취소
            elif choice == '4':
                print('─' * 60, '\n')
                print(f"{'<취소하기를 선택했습니다>':>33}")
                print(f"{'<이전 선택창으로 돌아갑니다>':>34}\n")
                return 0
            else:
                print('─' * 60, '\n')
                print(f"{'<잘못 눌렀습니다. 다시 선택해주세요.>':>37}\n")
                continue


# 킹기태
class King(Party):  # Party 클래스 상속받은 King 클래스
    # King 클래스의 skill 메서드
    def skill(self, monster, party_list):
        while True:
            print('─' * 60, '\n')
            # 스킬 선택문
            choice = input(f'{"[":>6}{self.name}]\n'
                           f'{"[HP]":>7} {self.nowHp}/{self.maxHp} {"[1.":>18} 음이탈] [2. 시나리오]\n'
                           f'{"[MP]":>7} {self.nowMp}/{self.maxMp} {"[3.":>21} 기도] [4. 취소]\n'
                           f'{"번호를 입력해주세요: ":>30}')
            # 킹기태 스킬 3가지
            # 1. 음이탈
            if choice == '1':
                if self.nowMp < (self.maxMp * 0.1):  # mp -10%보다 부족하면 실행 안됨
                    print('─' * 60, '\n')
                    print(f'{"<마나가 부족합니다.>":>32}\n')
                    continue  # 선택창으로 되돌아감
                else:
                    print('─' * 60, '\n')
                    print(f'{"<":>22}{self.name}의 음이탈!>\n')
                    # 몬스터 공격력 5% 감소
                    monster.att -= round(monster.att * 0.05)
                    print(f"{'몬스터의 공격력이 감소합니다':>34}\n")
                    # mp -10%
                    self.nowMp -= round(self.maxMp * 0.1)
                    return 1
            # 2. 시나리오
            elif choice == '2':
                if self.nowMp < (self.maxMp * 0.4):  # mp -40%보다 부족하면 실행 안됨
                    print('─' * 60, '\n')
                    print(f'{"<마나가 부족합니다.>":>32}\n')
                    continue  # 선택창으로 되돌아감
                else:
                    print('─' * 60, '\n')
                    print(f'{"<":>22}{self.name}의 시나리오!>\n')
                    # 아군의 hp, mp 10% 회복
                    for i in range(len(party_list)):
                        # 죽은 사람은 힐 불가능
                        if party_list[i].nowHp == 0:
                            continue
                        # hp, mp 모두 풀로 차있으면 회복 스킵
                        elif (party_list[i].nowHp == party_list[i].maxHp) and \
                                (party_list[i].nowMp == party_list[i].maxMp):
                            continue
                        # 현재 hp, mp 둘 다 최대 hp, mp 보다 10% 아래면 둘 다 회복
                        elif ((party_list[i].nowHp + round(party_list[i].maxHp * 0.1)) <= party_list[i].maxHp) and \
                                ((party_list[i].nowMp + round(party_list[i].maxMp * 0.1)) <= party_list[i].maxMp):
                            party_list[i].nowHp += round(party_list[i].maxHp * 0.1)
                            party_list[i].nowMp += round(party_list[i].maxMp * 0.1)
                        # 현재 hp를 +10% 회복했을 때 hp가 최대 hp 보다 많으면, 현재 hp = 최대 hp 로 설정
                        elif (party_list[i].nowHp + round(party_list[i].maxHp * 0.1)) > party_list[i].maxHp:
                            party_list[i].nowHp = party_list[i].maxHp
                            party_list[i].nowMp += round(party_list[i].maxMp * 0.1)
                        # 현재 mp를 +10% 회복했을 때 mp가 최대 mp보다 많으면, 현재 mp = 최대 mp 로 설정
                        elif (party_list[i].nowMp + round(party_list[i].maxMp * 0.1)) > party_list[i].maxMp:
                            party_list[i].nowHp += round(party_list[i].maxHp * 0.1)
                            party_list[i].nowMp = party_list[i].maxMp
                    print(f"{'모든 파티원의 HP / MP 10 % 상승!':>40}\n")
                    # mp -40%
                    self.nowMp -= round(self.maxMp * 0.4)
                    return 1
                    # 3. 기도
            elif choice == '3':
                print('─' * 60, '\n')
                print(f'{"<":>25}{self.name}의 기도!>\n')
                if self.nowMp < (self.maxMp * 0.9):  # mp -90%보다 부족하면 실행 안됨
                    print(f'{"<마나가 부족합니다.>":>32}\n')
                    continue  # 선택창으로 되돌아감
                else:
                    cnt = 0
                    for i in range(len(party_list)):
                        if party_list[i].nowHp == 0:
                            print(f'{party_list[i].name} 부활')
                            party_list[i].nowHp += party_list[i].maxHp
                            party_list[i].nowMp += (party_list[i].maxMp - party_list[i].nowMp)
                            cnt += 1
                    if cnt == 0:
                        print(f"{'사망한 파티원 없음.이전으로 돌아감.':>36}\n")
                        return 0
                    else:
                        print("기도 완료")
                        # mp -90%
                        self.nowMp -= round(self.maxMp * 0.9)
                        return 1
            # 4. 취소
            elif choice == '4':
                print('─' * 60, '\n')
                print(f"{'<취소하기를 선택했습니다>':>33}")
                print(f"{'<이전 선택창으로 돌아갑니다>':>34}\n")
                return 0
            else:
                print('─' * 60, '\n')
                print(f"{'<잘못 눌렀습니다. 다시 선택해주세요.>':>37}\n")
                continue


# 보우연재 (완료)
class Bow(Party):  # Party 클래스 상속받은 Bow 클래스
    # Bow 클래스의 skill 메서드
    def skill(self, monster):
        while 1:
            print('─' * 60, '\n')
            # 스킬 선택문
            choice = input(f'{"[":>6}{self.name}]{"[1. 흩날리는 앞머리]":>36}\n'
                           f'{"[HP]":>7} {self.nowHp}/{self.maxHp} {"[2. latte는 말이야]":>35}\n'
                           f'{"[MP]":>7} {self.nowMp}/{self.maxMp} {"[3. 집중의 황금안경]":>30} [4. 취소]\n'
                           f'{"번호를 입력해주세요: ":>30}')
            # 보우연재 스킬 3가지
            # 1. 앞머리
            if choice == '1':
                if self.nowMp < (self.maxMp * 0.2):  # mp -20% 보다 부족하면 실행 x
                    print('─' * 60, '\n')
                    print(f'{"마나가 부족합니다.":>31}')
                    continue  # 선택창으로 되돌아감
                else:
                    print('─' * 60, '\n')
                    print(f'{"<":>21}{self.name}의 흩날리는 앞머리!>\n')
                    # 1~3번 랜덤 공격(기본 공격력의 절반 데미지로)
                    cnt = random.randint(1, 3)
                    for i in range(cnt):
                        skill_att = random.randint(int(self.att[0] * 0.5), int(self.att[1] * 0.5))
                        print(f"{monster.name:>15}에게 {skill_att}의 데미지를 입혔습니다. {i + 1}번 공격")
                        monster.nowHp -= skill_att  # 몬스터 체력 차감
                        time.sleep(0.5)
                    print(f"{cnt:>27}번 공격했다!\n")  # 총 몇 번 공격했는지 출력
                    self.nowMp -= round(self.maxMp * 0.2)  # mp -20%
                    return 1
            # 2. 라떼
            elif choice == '2':
                # 보우연재의 공격력 수치의 2배로 공격(크리티컬)
                if self.nowMp < (self.maxMp * 0.3):  # mp -30% 보다 부족하면 실행 x
                    print('─' * 60, '\n')
                    print(f'{"마나가 부족합니다.":>31}')
                    continue  # 선택창으로 되돌아감
                else:
                    print('─' * 60, '\n')
                    print(f'{"<":>20}{self.name}의 latte는 말이야!>\n')
                    skill_att = random.randint(self.att[0] * 2, self.att[1] * 2)
                    print(f"{monster.name:>18}에게 {skill_att}의 데미지를 입혔습니다.\n")
                    monster.nowHp -= skill_att  # 몬스터 체력 차감
                    self.nowMp -= round(self.maxMp * 0.3)  # mp -30%
                    return 1
            # 3. 안경
            elif choice == '3':
                if self.nowMp < (self.maxMp * 0.5):  # mp -50% 보다 부족하면 실행 x
                    print('─' * 60, '\n')
                    print(f'{"마나가 부족합니다.":>31}')
                    continue  # 선택창으로 되돌아감
                # 몬스터가 1턴 공격 불가하게 만듬
                else:
                    print('─' * 60, '\n')
                    print(f'{"<":>20}{self.name}의 집중의 황금안경!>\n')
                    print(f'{monster.name:>15}(이)가 1턴 공격불가 상태가 되었습니다.\n')
                    self.nowMp -= round(self.maxMp * 0.5)  # mp -50% << 너무 사기여서 50%, 1턴으로 바꿈(연수)
                    Monster.cannot_att += 1  # 몬스터 클래스 변수의 공격불가 횟수를 3으로 만들어줌 턴이 지날때마다 줄어듬
                    return 1
            # 4. 취소
            elif choice == '4':
                print('─' * 60, '\n')
                print(f"{'<취소하기를 선택했습니다>':>33}")
                print(f"{'<이전 선택창으로 돌아갑니다>':>34}\n")
                return 0
            # 그 외의 값을 입력하면 다시 선택
            else:
                print('─' * 60, '\n')
                print(f"{'<잘못 눌렀습니다. 다시 선택해주세요.>':>37}\n")
                continue


# 약범규
class Tiger(Party):  # Party 클래스 상속받은 Tiger 클래스
    # Tiger 클래스의 skill 메서드, 약제조 스킬
    def skill(self, monster):
        while 1:
            print('─' * 60, '\n')
            choice = input(f'{"[1. 약제조]":>20}  [2. 격투스킬]  [3. 취소]\n'
                           f'{"번호를 입력해주세요: ":>30}')
            # 약제조 선택
            if choice == '1':
                while 1:
                    # 약범규 약제조 스킬 3가지
                    print('─' * 60, '\n')
                    mk_md = input(f'{"어떤 약을 만들까?":>31}\n\n'
                                  f'{"[":>6}{self.name}]\n'
                                  f'{"[HP]":>7} {self.nowHp}/{self.maxHp}{"[1. 콘푸로스트]":>28}  [2. 떡하나]\n'
                                  f'{"[MP]":>7} {self.nowMp}/{self.maxMp}{"[3. 담배피던 시절] ":>30} [4. 취소]\n'
                                  f'{"번호를 입력해주세요: ":>30}')
                    # 콘푸로스트 제작
                    if mk_md == '1':
                        if self.nowMp < (self.maxMp * 0.1):
                            print('─' * 60, '\n')
                            print(f'{"마나가 부족합니다.":>31}\n')
                            continue
                        else:
                            print('─' * 60, '\n')
                            print(f"{self.name:>20}가 콘푸로스트를 만들기 시작!\n")
                            Party.confu_save += 1
                            self.nowMp -= round(self.maxMp * 0.1)  # mp -10%
                            return 1
                    # 떡 제작
                    elif mk_md == '2':
                        if self.nowMp < (self.maxMp * 0.1):
                            print('─' * 60, '\n')
                            print(f'{"마나가 부족합니다.":>31}\n')
                            continue
                        else:
                            # 떡 1-3턴 동안 먹기
                            print('─' * 60, '\n')
                            print(f"{self.name:>20}가 떡을 만들기 시작!\n")
                            Party.ricecake_save += 1
                            self.nowMp -= round(self.maxMp * 0.2)  # mp -20%
                            return 1
                    # 담배 제작
                    elif mk_md == '3':
                        if self.nowMp < (self.maxMp * 0.3):
                            print('─' * 60, '\n')
                            print(f'{"마나가 부족합니다.":>31}\n')
                            continue
                        else:
                            print('─' * 60, '\n')
                            print(f"{self.name:>20}가 담배를 만들기 시작!\n")
                            Party.cigarette_save += 1
                            self.nowMp -= round(self.maxMp * 0.3)  # mp -30%
                            return 1
                    # 취소
                    elif mk_md == '4':
                        print('─' * 60, '\n')
                        print(f"{'<취소하기를 선택했습니다>':>33}")
                        print(f"{'<이전 선택창으로 돌아갑니다>':>34}\n")
                        break
                    # 그 외의 값을 입력하면 다시 선택
                    else:
                        print('─' * 60, '\n')
                        print(f"{'<잘못 눌렀습니다. 다시 선택해주세요.>':>37}\n")
                        continue
            # 격투 선택
            elif choice == '2':
                while 1:
                    # 약범규 격투스킬 3가지
                    print('─' * 60, '\n')
                    fi_att = input(f'어떤 스킬을 쓸까?\n\n'
                                   f'{"[":>6}{self.name}]\n'
                                   f'{"[HP]":>7} {self.nowHp}/{self.maxHp}{"[1. 범소리]":>28}  [2. 약사세요]\n'
                                   f'{"[MP]":>7} {self.nowMp}/{self.maxMp}{"[3. 호랑이 냥냥펀치] ":>30} [4. 취소]\n'
                                   f'{"번호를 입력해주세요: ":>30}')
                    # 범소리
                    if fi_att == '1':
                        if self.nowMp < (self.maxMp * 0.2):
                            print('─' * 60, '\n')
                            print(f'{"마나가 부족합니다.":>31}\n')
                            continue
                        else:
                            print('─' * 60, '\n')
                            print(f'{self.name:>26}의 범소리!')
                            # 50% 확률로 몬서터 공격 실패? 랜덤..
                            rand_att1 = random.randrange(2)  # 50% 확률(0이 나오면 몬스터 공격 못함)
                            # mp -20%
                            self.nowMp -= round(self.maxMp * 0.2)
                            if rand_att1 == 0:
                                print(f'{"실패했습니다.몬스터는 쫄지 않아":>33}\n')
                            else:
                                print(f'{"몬스터가 약범규의 호통에 기가 눌렸습니다.":>36}\n')
                                Monster.cannot_att += 1
                            return 1
                    # 약팔이
                    elif fi_att == '2':
                        if self.nowMp < (self.maxMp * 0.4):
                            print('─' * 60, '\n')
                            print(f'{"마나가 부족합니다.":>31}\n')
                            continue
                        else:
                            print('─' * 60, '\n')
                            print(f'{"약범규가 영업하는척 기습을 시도합니다":>35}')
                            # 몬스터에게 약팔다가 기습공격 성공활률 40% 기존 공격력의 2배로 때림
                            rand__att2 = random.randrange(10)
                            if rand__att2 <= 4:
                                time.sleep(0.6)
                                print(f'{"기습 성공!":^60}')
                                skill_att = random.randint(self.att[0] * 2, self.att[1] * 2)  # 공격력 2배
                                monster.nowHp -= skill_att  # 몬스터 체력 차감
                                print(f'{monster.name:>18}에게 {skill_att}의 데미지를 입혔습니다.\n')
                                return 1
                            else:
                                time.sleep(0.6)
                                print(f'{"실패...몬스터가 약을 뺏어 먹습니다.":>36}\n')
                                # 실패시 몬스터 체력 10% 회복
                                if (monster.nowHp + (monster.nowHp * 0.1)) >= monster.maxHp:
                                    monster.nowHp = monster.maxHp
                                else:
                                    monster.nowHp += (monster.nowHp * 0.1)
                            # mp -40%
                            self.nowMp -= round(self.maxMp * 0.4)
                            return 1
                    # 냥냥펀치
                    elif fi_att == '3':
                        if self.nowMp < (self.maxMp * 0.2):
                            print('─' * 60, '\n')
                            print(f'{"마나가 부족합니다.":>31}\n')
                            continue
                        else:
                            print('─' * 60, '\n')
                            print(f"{'<호랑이 냥냥펀치!>':>31}")
                            # 기본 공격력의 120% 딜로 때림
                            skill_att = random.randint(int(self.att[0] * 1.2), int(self.att[1] * 1.2))
                            monster.nowHp -= skill_att  # 몬스터 체력 차감
                            print(f"{monster.name:>18}에게 {skill_att}의 데미지를 입혔습니다.\n")
                            # mp -20%
                            self.nowMp -= round(self.maxMp * 0.2)
                            return 1
                    # 4. 취소
                    elif fi_att == '4':
                        print('─' * 60, '\n')
                        print(f"{'<취소하기를 선택했습니다>':>33}")
                        print(f"{'<이전 선택창으로 돌아갑니다>':>34}\n")
                        break
                    # 그 외의 값을 입력하면 다시 선택
                    else:
                        print('─' * 60, '\n')
                        print(f"{'<잘못 눌렀습니다. 다시 선택해주세요.>':>37}\n")
                        continue
            # 4. 취소
            elif choice == '3':
                print('─' * 60, '\n')
                print(f"{'<취소하기를 선택했습니다>':>33}")
                print(f"{'<이전 선택창으로 돌아갑니다>':>34}\n")
                return 0
            # 그 외의 값을 입력하면 다시 선택
            else:
                print('─' * 60, '\n')
                print(f"{'<잘못 눌렀습니다. 다시 선택해주세요.>':>37}\n")
                continue


# ------------------ 함수 ------------------------
# 몬스터마다 등장확률 준 함수
def monster_appear(nomal_monster, boss_monster):
    rand = random.uniform(94, 100)  # 확률 범위 0~100
    # 일반 몬스터
    if rand < 46.5:
        return nomal_monster[0]  # 좀비
    elif (rand >= 46.5) and (rand < 76.5):
        return nomal_monster[1]  # 구울
    elif (rand >= 76.5) and (rand < 88.5):
        return nomal_monster[2]  # 해골
    elif (rand >= 88.5) and (rand < 93.5):
        return nomal_monster[3]  # 버그베어
    else:
        random.shuffle(boss_monster)    # 보스 몬스터
        return boss_monster.pop()


# 몬스터 객체 리스트 만드는 함수
def nomal_monster_fc():
    # zombie 객체는 Monster클래스의 인스턴스
    zombie = Monster("좀비", 100, random.randrange(300, 501))
    # ghoul 객체는 Monster클래스의 인스턴스
    ghoul = Monster("구울", 180, random.randrange(400, 701))
    # skull 객체는 Monster클래스의 인스턴스
    sukll = Monster("해골", 220, random.randrange(480, 801))
    # bugbear 객체는 Monster클래스의 인스턴스
    bugbear = Monster("버그베어", 350, random.randrange(550, 901))

    # Monster클래스의 인스턴스를 리스트화
    nomal_monster = [zombie, ghoul, sukll, bugbear]

    return nomal_monster


# 보스 몬스터 리스트 만드는 함수
def boss_monster_fc():
    # arhendo 객체는 Monster클래스의 인스턴스
    arhendo = Monster("아르헨도", random.randrange(1000, 3001), random.randrange(5000, 10001))
    # cheolmom 객체는 Monster클래스의 인스턴스
    cheolmom = Monster("철몸", random.randrange(1000, 3001), random.randrange(5000, 10001))
    # gyubeom 객체는 Monster클래스의 인스턴스
    gyubeom = Monster("규범이", random.randrange(1000, 3001), random.randrange(5000, 10001))
    # minjuseok 객체는 Monster클래스의 인스턴스
    minjuseok = Monster("민주석", random.randrange(1000, 3001), random.randrange(5000, 10001))
    # ilsung 객체는 Monster클래스의 인스턴스
    ilsung = Monster("일성김", random.randrange(1000, 3001), random.randrange(5000, 10001))
    # uyeoni 객체는 Monster클래스의 인스턴스
    uyeoni = Monster("우연이", random.randrange(1000, 3001), random.randrange(5000, 10001))
    # diaboglo 객체는 Monster클래스의 인스턴스 6.5
    diaboglo = Monster("디아복로", random.randrange(2500, 8001), random.randrange(10000, 20001))

    boss_monster = [arhendo, cheolmom, gyubeom, minjuseok, ilsung, uyeoni, diaboglo]

    return boss_monster


# 파티원 객체 리스트 만드는 함수
def party_list_fc():
    yong = Choco('초코의용', 50000, 30000)  # yong 객체. Choco의 인스턴스
    tae = King('킹기태', 50000, 30000)  # tae 객체. King의 인스턴스
    jae = Bow('보우연재', 50000, 30000)  # jae 객체. Bow의 인스턴스
    beom = Tiger('약범규', 50000, 30000)  # beom 객체. beom은 Tiger의 인스턴스

    return [yong, tae, jae, beom]  # 파티원 객체 리스트 return


# 전투 후 승리시 보상 함수
def reward(person):
    # 최소 공격력 2~5% 상승
    person.att[0] += round(person.att[0] * round(random.uniform(0.02, 0.051), 2))
    # 최대 공격력 2~5% 상승
    person.att[1] += round(person.att[1] * round(random.uniform(0.02, 0.051), 2))
    # 현재 HP 최대 HP 2~5% 상승
    hp = round(person.nowHp * round(random.uniform(0.02, 0.051), 2))
    person.nowHp += hp
    person.maxHp += hp
    # 현재 MP 최대 MP 2~5% 상승
    mp = round(person.nowMp * round(random.uniform(0.02, 0.051), 2))
    person.nowMp += mp
    person.maxMp += mp


def reward_item(Party):
    rand_reward_item1 = random.randrange(10)   # 포션얻을 확률 범위
    rand_reward_item2 = random.uniform(0,100)     # 나머지 얻을 확률 범위
    if rand_reward_item1 <= 3:      # 포션 획득확률 30%
        print("포션을 획득했습니다.")
        Party.potion += 1       # 포션 추가
        if rand_reward_item2 <= 0.5:        # 엘릭서 얻을 확률 0.5%
            print("엘릭서를 획득했습니다.")
            Party.elixir += 1       #엘릭서 추가
        elif rand_reward_item2 >0.5 and rand_reward_item2 <=30.5:       # 생라면 얻을 확률 30%
            print("생라면을 획득했습니다")
            Party.ramen += 1        # 생라면 추가
        else:       #포션만 얻었을 떼(엘릭서, 라면 얻지 못했을 때)
            pass
    print(f"포션 : {Party.potion}개 "
          f"엘릭서 : {Party.elixir}개"
          f"생라면 : {Party.ramen} 개")


# 전투 함수
def fight(party_list, boss_monster_list):  # (이름, 등장확률, 1타공격력, HP, 현재HP)
    print('─' * 60)
    nomal_monster_list = nomal_monster_fc()  # 모든 몬스터 객체의 리스트를 함수로 불러와주고 monster_list 변수에 넣어줌

    # Monster_appear 함수의 return값(일반 몬스터, 보스몬스터)을 monster 변수에 넣어줌
    monster = monster_appear(nomal_monster_list, boss_monster_list)
    print(f"\n{'<':>20}{monster.name}(이)가 나타났다!!!!>\n")

    while True:
        i = 0
        if Party.cook_ramen >= 1:
            Party.boiled_ramen += 1
            Party.cook_ramen -= 1
        if Party.confu_save >= 1:
            Party.confu += 1
        if Party.ricecake_save >= 1:
            Party.ricecake += 1
        if Party.cigarette_save >= 1:
            Party.cigarette += 1

        # ----------------------- 파티원 액션 -----------------------
        while i < 4:
            cancel = 1
            if party_list[i].nowHp == 0:
                pass
            else:
                # 몬스터와 초코의용군의 상태 창 출력
                print('─' * 60, '\n')
                monster.monster_stat()
                print(f"\n\n\n\n")

                # 파티원 이름 출력
                print(f"{'[':>6}{party_list[0].name}]{'[':>7}{party_list[1].name}]"
                      f"{'[':>7}{party_list[2].name}]{'[':>7}{party_list[3].name}]")

                # 파티원 HP 출력
                for j in range(len(party_list)):
                    party_list[j].party_hp()
                print()

                # 파티원 MP 출력
                for j in range(len(party_list)):
                    party_list[j].party_mp()
                print('\n')

                print(f'{"포션":>15}🍖 ({Party.potion})  엘릭서🍭 ({Party.elixir})  라면🍜 ({Party.ramen})\n'
                      f'{"콘푸로스트":>15}🐯🥛({Party.confu})  떡하나🍡({Party.ricecake})  담배🚬({Party.cigarette})\n')

                # 파티원 턴마다 상태 출력
                print('─' * 60)
                print(f'\n{"<":>25}{party_list[i].name}의 턴!>')
                print(f'{"<":>20}{party_list[i].name}(은)는 무엇을 할까?>\n\n'
                      f'{"[":>6}{party_list[i].name}]{"[":>35}{monster.name}]\n'
                      f'{"[HP]":>6} {party_list[i].nowHp}/{party_list[i].maxHp}'
                      f'{"[HP]":>34} {monster.nowHp}/{monster.maxHp}\n'
                      f'{"[MP]":>6} {party_list[i].nowMp}/{party_list[i].maxMp}\n')
                print('─' * 60, '\n')

                choice = input(f"{'[1. 공격]':>15}  [2. 스킬]  [3. 아이템]  [4. 도망]\n"
                               f"{'번호를 입력해주세요: ':>30}")  # 선택지 출력

                if choice == '1':  # 공격
                    nomal_att = random.randint(party_list[i].att[0], party_list[i].att[1])
                    print('─' * 60, '\n')
                    print(f"{party_list[i].name:>25}의 공격!\n"
                          f"{monster.name:>18}에게 {nomal_att}의 데미지를 입혔습니다.\n")
                    monster.nowHp -= nomal_att  # 몬스터 체력 차감
                    # 전투에서 이김
                    if monster.nowHp <= 0:
                        monster.nowHp = 0
                        print('─' * 60, '\n')
                        time.sleep(0.7)
                        print(f"🎉{monster.name}을(를) 처치했습니다.🎉")

                        # 보스몹을 잡으면 ->
                        if monster in boss_monster_list:  # 리스트 인덱싱으로 보스몹인지 확인
                            idx = boss_monster_list.index(monster)
                            boss_monster_list.pop(idx)
                            print(f'{monster.name}(을)를 영원히 소멸시켰습니다.')

                        # 보스몹을 모두 잡으면 엔딩
                        if not boss_monster_list[:]:
                            print('보스들을 모두 잡았습니다 세상에 평화가 찾아옵니다.')
                            exit()
                        else:
                            print(f'남은 보스몹들:', end='')  # 보스몹이 남아있으면 출력
                            for z in range(len(boss_monster_list)):
                                print(boss_monster_list[z].name, end=' ')

                        # 파티원 성장
                        print("\n🎉전투에서 승리했습니다🎉")
                        print("💪파티원의 공격력과 HP, MP가 2~5%씩 상승합니다💪")
                        # 파티원 한 명 한 명 reward 함수로 성장
                        for j in range(len(party_list)):
                            reward(party_list[j])

                        # 성장한 정보 출력 파티원 이름 출력
                        print(f"{'[':>6}{party_list[0].name}]{'[':>7}{party_list[1].name}]"
                              f"{'[':>7}{party_list[2].name}]{'[':>7}{party_list[3].name}]")

                        # 파티원 HP 출력
                        for j in range(len(party_list)):
                            party_list[j].party_hp()
                        print()

                        # 파티원 MP 출력
                        for j in range(len(party_list)):
                            party_list[j].party_mp()
                        print()

                        return party_list, boss_monster_list  # 전투 종료
                    else:
                        pass
                elif choice == '2':  # 스킬
                    # cancel = party_list[i].skill(monster)
                    if i == 1:
                        cancel = party_list[i].skill(monster, party_list)
                    else:
                        cancel = party_list[i].skill(monster)
                    # 전투에서 이김
                    if monster.nowHp <= 0:
                        monster.nowHp = 0
                        print('─' * 60, '\n')
                        time.sleep(0.7)
                        print(f"🎉{monster.name}을(를) 처치했습니다.🎉")

                        # 보스몹을 잡으면 ->
                        if monster in boss_monster_list:  # 리스트 인덱싱으로 보스몹인지 확인
                            idx = boss_monster_list.index(monster)
                            boss_monster_list.pop(idx)
                            print(f'{monster.name}(을)를 영원히 소멸시켰습니다.')

                        # 보스몹을 모두 잡으면 엔딩
                        if not boss_monster_list[:]:
                            print('보스들을 모두 잡았습니다 세상에 평화가 찾아옵니다.')
                            exit()
                        else:
                            print(f'남은 보스몹들:', end='')  # 보스몹이 남아있으면 출력
                            for z in range(len(boss_monster_list)):
                                print(boss_monster_list[z].name, end=' ')

                        # 파티원 성장
                        print("\n🎉전투에서 승리했습니다🎉")
                        print("💪파티원의 공격력과 HP, MP가 2 ~ 5%씩 상승합니다💪")
                        # 파티원 한 명 한 명 reward 함수로 성장
                        for j in range(len(party_list)):
                            reward(party_list[j])

                        # 성장한 정보 출력 파티원 이름 출력
                        print(f"{'[':>6}{party_list[0].name}]{'[':>7}{party_list[1].name}]"
                              f"{'[':>7}{party_list[2].name}]{'[':>7}{party_list[3].name}]")

                        # 파티원 HP 출력
                        for j in range(len(party_list)):
                            party_list[j].party_hp()
                        print()

                        # 파티원 MP 출력
                        for j in range(len(party_list)):
                            party_list[j].party_mp()
                        print()

                        return party_list, boss_monster_list  # 전투 종료
                    else:
                        pass
                elif choice == '3':  # 아이템
                    cancel = party_list[i].choose_item(party_list)
                elif choice == '4':  # 도망
                    print("도망가기를 선택했습니다")
                    rand_run = random.randrange(10)  # 도망 확률 10%
                    if rand_run == 1:  # 도망 성공
                        print("도망 성공!!")
                        return party_list, boss_monster_list  # 전투 종료
                    else:  # 도망 실패
                        print("도망실패 ㅠㅠ")
                        print("전투로 복귀합니다")
                else:  # 잘못눌렀을 경우
                    print("잘못 눌렀습니다. 다시 선택해 주세요.")
                    continue
            if cancel == 1:  # 일반적으로 진행 하면 다음 턴으로 넘어감
                i += 1
            elif cancel == 0:  # 취소하기 하면 다음 턴으로 안넘어가게 함
                pass

        # ----------------------- 몬스터 공격할 수 없는 상태 (디버프 걸려있으면) -----------------------
        if Monster.cannot_att > 0:
            print(f'{monster.name}(은)는 공격할 수 없다!')
            Monster.cannot_att -= 1
        # 몬스터 공격
        else:
            while 1:
                atted_psn = random.randrange(4)  # 초코의용군 파티원 중 하나 랜덤으로 공격받음 party_list[atted_psn]
                # 몬스터 공격 출력문
                if party_list[atted_psn].nowHp == 0:
                    continue
                else:
                    print('─' * 60)
                    time.sleep(0.7)
                    print(f"{monster.name}(이)가 {party_list[atted_psn].name}(을)를 공격합니다.\n"
                          f"{party_list[atted_psn].name}에게 {monster.att}의 데미지!")
                    break

            # ----------------------- 파티원의 현재 체력에서 몬스터의 공격력 빼주기 -----------------------
            # 무적 효과가 적용된 팀원일 경우 데미지 입지 않음
            if party_list[atted_psn].invincibility > 0:
                print(f'{party_list[atted_psn].name}(은)는 무적상태입니다.')
                party_list[atted_psn].invincibility -= 1
            # 현재 체력보다 더 씨게 맞으면 체력 0으로(죽음)
            elif party_list[atted_psn].nowHp <= monster.att:
                party_list[atted_psn].nowHp = 0
                # 죽은 파티원 출력(~가 죽었습니다)
                print(f"{party_list[atted_psn].name} : {party_list[atted_psn].nowHp}/{party_list[atted_psn].maxHp}\n"
                      f"{party_list[atted_psn].name}(이)가 죽었습니다")

                if (party_list[0].nowHp == 0) and (party_list[1].nowHp == 0) and (party_list[2].nowHp == 0) \
                        and (party_list[3].nowHp == 0):
                    print("모든 파티가 사망했습니다")
                    print("!!GAME OVER!!")
                    exit()  # dead 엔딩. 게임 끝
            else:
                # 파티원 현재 체력, 몬스터 공격 받고 깎임
                party_list[atted_psn].nowHp -= monster.att
                # 차감된 체력확인 하기 위한 파티원들 정보창 출력
                # 파티원 이름 출력
                print(f"{'[':>6}{party_list[0].name}]{'[':>7}{party_list[1].name}]"
                      f"{'[':>7}{party_list[2].name}]{'[':>7}{party_list[3].name}]")

                # 파티원 HP 출력
                for j in range(len(party_list)):
                    party_list[j].party_hp()
                print()

                # 파티원 MP 출력
                for j in range(len(party_list)):
                    party_list[j].party_mp()
                print()

            for i in range(len(party_list)):
                party_list[i].invincibility -= 1


# 함수의 매개변수에 객체를 받음, 모험시작 함수
def start(dungeon=Dungeon(15, 15, '🍰')):
    # dungeon 객체는 Dungeon 클래스의 인스턴스. 행, 열, 테두리 값 지정. start 함수에 객체 넣어줌
    dungeon2 = Dungeon(15, 15, '🍀')
    dungeon3 = Dungeon(15, 15, '🧊')
    dungeon4 = Dungeon(15, 15, '🍞')
    dungeon5 = Dungeon(15, 15, '🍱')
    party_list = party_list_fc()  # 파티원 객체의 리스트를 함수로 불러와주고 party_list 변수에 넣어줌
    boss_monster_list = boss_monster_fc()

    # Dungeon 클래스의 메서드들 하나하나 실행하면서 던전 제작
    dungeon.make_maze()
    dungeon.theme()
    if dungeon.maze[0][0] == '🍱':
        pass
    else:
        dungeon.potal()

    # 의용파티 초반 스폰 장소 (1, 1), Party 클래스에 넣으면 좋을듯?
    mx = 1
    my = 1
    dungeon.maze[mx][my] = '😊'

    # 던전이 잘 만들어졌는지 출력하는 코드
    print(f'{"─" * 60}\n\n{"<초코의용군 파티 모험 시작!>":>34}')
    print(f'{"<방향키를 눌러 이동해주세요>":>33}\n')
    for i in range(len(dungeon.maze)):
        print(f'{"":>12}', end='')
        for j in range(len(dungeon.maze)):
            if (i == (mx - 1) and j == (my - 1)) or (i == mx and j == (my - 1)) or (i == (mx + 1) and j == (my - 1)) \
                    or (i == (mx - 1) and j == my) or (i == mx and j == my) or (i == (mx + 1) and j == my) \
                    or (i == (mx - 1) and j == (my + 1)) or (i == mx and j == (my + 1)) or (
                    i == (mx + 1) and j == (my + 1)):
                print('\033[103m' + dungeon.maze[i][j] + '\033[0m', end='')
            # 주인공 주변 3x3이 아니면 그림자 출력
            else:
                print('\033[100m' + '⬛' + '\033[0m', end='')
        print()
    print(f'\n\n{"─" * 60}\n')

    # 파티원 이름 출력
    print(f"{'[':>6}{party_list[0].name}]{'[':>7}{party_list[1].name}]"
          f"{'[':>7}{party_list[2].name}]{'[':>7}{party_list[3].name}]")

    # 파티원 HP 출력
    for j in range(len(party_list)):
        party_list[j].party_hp()
    print()

    # 파티원 MP 출력
    for j in range(len(party_list)):
        party_list[j].party_mp()
    print('\n')

    print(f'{"포션":>15}🍖 ({Party.potion})  엘릭서🍭 ({Party.elixir})  라면🍜 ({Party.ramen})\n'
          f'{"콘푸로스트":>15}🐯🥛({Party.confu})  떡하나🍡({Party.ricecake})  담배🚬({Party.cigarette})\n')

    print(f'{"─" * 60}\n')

    cnt = 0  # cnt가 3이 되면 던전 초기화
    fgt = 0  # fgt가 10이 되면 던전 초기화

    while 1:
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
        if key == "up" and dungeon.maze[mx - 1][my] != dungeon.maze[0][0]:  # 테두리값 = maze[0][0]
            # 기존 주인공 자리 ⬜으로 초기화
            dungeon.maze[mx][my] = '⬜'
            print(f'{"<위로 전진!>":>33}\n')
            # 이동하는 곳의 값이 😈이면 몬스터 이벤트 발생
            if dungeon.maze[mx - 1][my] == '😈':
                print(f'{"<몬스터 발견!>":>32}\n')
                fight(party_list, boss_monster_list)
                fgt += 1
            # 이동하는 곳의 값이 🚪이면 포탈 이벤트 발생
            elif dungeon.maze[mx - 1][my] == '🚪':
                print(f'{"<다음 던전으로 이동합니다...>":>33}\n')
                if dungeon.maze[0][0] == '🍰':  # 1층에서 2층으로
                    start(dungeon2)
                elif dungeon.maze[0][0] == '🍀':  # 2층에서 3층으로
                    start(dungeon3)
                elif dungeon.maze[0][0] == '🧊':  # 3층에서 4층으로
                    start(dungeon4)
                elif dungeon.maze[0][0] == '🍞':  # 4층에서 5층으로
                    start(dungeon5)
            # 이동하는 곳의 값이 🍖면 포션 획득
            elif dungeon.maze[mx - 1][my] == '🍖':
                print(f'{"<포션을 획득했습니다!>":>33}')
                Party.potion += 1
            mx -= 1
            cnt += 1
        # 왼쪽 이동
        elif key == "left" and dungeon.maze[mx][my - 1] != dungeon.maze[0][0]:
            # 기존 주인공 자리 ⬜으로 초기화
            dungeon.maze[mx][my] = '⬜'
            print(f'{"<왼쪽으로 전진!>":>33}\n')
            # 이동하는 곳의 값이 😈이면 몬스터 이벤트 발생
            if dungeon.maze[mx][my - 1] == '😈':
                print(f'{"<몬스터 발견!>":>32}\n')
                fight(party_list, boss_monster_list)
                fgt += 1
            # 이동하는 곳의 값이 🚪이면 포탈 이벤트 발생
            elif dungeon.maze[mx][my - 1] == '🚪':
                print(f'{"<다음 던전으로 이동합니다...>":>33}\n')
                if dungeon.maze[0][0] == '🍰':  # 1층에서 2층으로
                    start(dungeon2)
                elif dungeon.maze[0][0] == '🍀':  # 2층에서 3층으로
                    start(dungeon3)
                elif dungeon.maze[0][0] == '🧊':  # 3층에서 4층으로
                    start(dungeon4)
                elif dungeon.maze[0][0] == '🍞':  # 4층에서 5층으로
                    start(dungeon5)
            # 이동하는 곳의 값이 🍖면 포션 획득
            elif dungeon.maze[mx][my - 1] == '🍖':
                print(f'{"<포션을 획득했습니다!>":>40}')
                Party.potion += 1
            my -= 1
            cnt += 1
        # 아래 이동
        elif key == "down" and dungeon.maze[mx + 1][my] != dungeon.maze[0][0]:
            # 기존 주인공 자리 ⬜으로 초기화
            dungeon.maze[mx][my] = '⬜'
            print(f'{"<아래로 전진!>":>32}\n')
            # 이동하는 곳의 값이 😈이면 몬스터 이벤트 발생
            if dungeon.maze[mx + 1][my] == '😈':
                print(f'{"<몬스터 발견!>":>32}\n')
                fight(party_list, boss_monster_list)
                fgt += 1
            # 이동하는 곳의 값이 🚪이면 포탈 이벤트 발생
            elif dungeon.maze[mx + 1][my] == '🚪':
                print(f'{"<다음 던전으로 이동합니다...>":>33}\n')
                if dungeon.maze[0][0] == '🍰':  # 1층에서 2층으로
                    start(dungeon2)
                elif dungeon.maze[0][0] == '🍀':  # 2층에서 3층으로
                    start(dungeon3)
                elif dungeon.maze[0][0] == '🧊':  # 3층에서 4층으로
                    start(dungeon4)
                elif dungeon.maze[0][0] == '🍞':  # 4층에서 5층으로
                    start(dungeon5)
            # 이동하는 곳의 값이 🍖면 포션 획득
            elif dungeon.maze[mx + 1][my] == '🍖':
                print(f'{"<포션을 획득했습니다!>":>33}')
                Party.potion += 1
            mx += 1
            cnt += 1
        # 오른쪽 이동
        elif key == "right" and dungeon.maze[mx][my + 1] != dungeon.maze[0][0]:
            # 기존 주인공 자리 ⬜으로 초기화
            dungeon.maze[mx][my] = '⬜'
            print(f'{"<오른쪽으로 전진!>":>33}\n')
            # 이동하는 곳의 값이 😈이면 이벤트 발생
            if dungeon.maze[mx][my + 1] == '😈':
                print(f'{"<몬스터 발견!>":>32}\n')
                fight(party_list, boss_monster_list)
                fgt += 1
            # 이동하는 곳의 값이 🚪이면 포탈 이벤트 발생
            elif dungeon.maze[mx][my + 1] == '🚪':
                print(f'{"<다음 던전으로 이동합니다...>":>33}\n')
                if dungeon.maze[0][0] == '🍰':  # 1층에서 2층으로
                    start(dungeon2)
                elif dungeon.maze[0][0] == '🍀':  # 2층에서 3층으로
                    start(dungeon3)
                elif dungeon.maze[0][0] == '🧊':  # 3층에서 4층으로
                    start(dungeon4)
                elif dungeon.maze[0][0] == '🍞':  # 4층에서 5층으로
                    start(dungeon5)
            # 이동하는 곳의 값이 🍖면 포션 획득
            elif dungeon.maze[mx][my + 1] == '🍖':
                print(f'{"<포션을 획득했습니다!>":>33}')
                Party.potion += 1
            my += 1
            cnt += 1
        # 이동 불가
        else:
            print(f'{"<그 쪽으론 갈 수 없습니다.>":>33}')

        # 3번 이동하면 몬스터 위치 바뀜
        if cnt == 3:
            dungeon.make_maze()
            dungeon.theme()
            if dungeon.maze[0][0] == '🍱':  # 마지막 층이면 포탈 안생기게 함
                pass
            else:
                dungeon.potal()
            print(f'{"<던전의 모양이 바꼈습니다!>":>33}')
            cnt = 0

        # 전투 10번 하면 포탈 위치 바뀜
        if fgt == 10:
            while True:
                dungeon.maze[dungeon.potal_x][dungeon.potal_y] = '⬜'
                potal_x = random.randrange(2, len(dungeon.maze) - 1)
                potal_y = random.randrange(2, len(dungeon.maze) - 1)

                if (dungeon.potal_x == potal_x) and (dungeon.potal_y == potal_y):
                    continue
                else:
                    dungeon.potal_x = potal_x
                    dungeon.potal_y = potal_y
                    dungeon.maze[dungeon.potal_x][dungeon.potal_y] = '🚪'
                    print(f'{"<포탈의 위치가 바꼈습니다>":>33}')
                    break
            fgt = 0

        dungeon.maze[mx][my] = "😊"

        # 이동한 던전이 잘 만들어졌는지 출력하는 코드
        print(f'{"─" * 60}\n\n{"<방향키를 눌러 이동해주세요>":>33}\n')
        for i in range(len(dungeon.maze)):
            print(f'{"":>12}', end='')
            for j in range(len(dungeon.maze)):
                if (i == (mx - 1) and j == (my - 1)) or (i == mx and j == (my - 1)) or (i == (mx + 1) and j == (my - 1)) \
                        or (i == (mx - 1) and j == my) or (i == mx and j == my) or (i == (mx + 1) and j == my) \
                        or (i == (mx - 1) and j == (my + 1)) or (i == mx and j == (my + 1)) or (
                        i == (mx + 1) and j == (my + 1)):
                    print('\033[103m' + dungeon.maze[i][j] + '\033[0m', end='')
                # 주인공 주변 3x3이 아니면 그림자 출력
                else:
                    print('\033[100m' + '⬛' + '\033[0m', end='')
            print()
        print(f'\n\n{"─" * 60}\n')

        # 파티원 이름 출력
        print(f"{'[':>6}{party_list[0].name}]{'[':>7}{party_list[1].name}]"
              f"{'[':>7}{party_list[2].name}]{'[':>7}{party_list[3].name}]")

        # 파티원 HP 출력
        for j in range(len(party_list)):
            party_list[j].party_hp()
        print()

        # 파티원 MP 출력
        for j in range(len(party_list)):
            party_list[j].party_mp()
        print('\n')

        print(f'{"포션":>15}🍖 ({Party.potion})  엘릭서🍭 ({Party.elixir})  라면🍜 ({Party.ramen})\n'
              f'{"콘푸로스트":>15}🐯🥛({Party.confu})  떡하나🍡({Party.ricecake})  담배🚬({Party.cigarette})\n')

        print(f'{"─" * 60}\n')


start()
