# 파티원 정보 클래스
import random


class Party:
    att = [100, 150]  # 공격력 클래스 변수로 넣어줌(전부 공격력 계수는 같으니까)

    potion = 0
    elixir = 0
    ramen = 0
    boiled_ramen = 0
    confu = 0
    ricecake = 0
    cigarette = 0

    def __init__(self, name, hp, mp):
        self.name = name
        self.nowHp = hp
        self.maxHp = hp
        self.nowMp = mp
        self.maxMp = mp
        self.invincibility = 0  # 무적변수
        self.ricecake = 0  # 범규약 떡하나 효과를 받는 턴 수

    # 파티원 HP 출력 메서드
    def party_hp(self):
        print(f"{'[HP]':>6} {self.nowHp}/{self.maxHp}", end='')

    # 파티원 MP 출력 메서드
    def party_mp(self):
        print(f"{'[MP]':>6} {self.nowMp}/{self.maxMp}", end='')

    # (보라) 포션 메서드 아래부터
    def potion_mt(self):  # 포션
        if Party.potion >= 1:  # 포션개수가 1개이상
            print()
            print('포션 사용')
            print(f'{self.name}의 [HP {self.maxHp}] [MP {self.maxMp}] 회복되었습니다')
            self.nowHp = self.maxHp  # 현재 체력에 기존체력 대입
            self.nowMp = self.maxMp  # 현재 마나에 기존마나 대입
            Party.potion -= 1  # 포션 차감
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
            print(f'{self.name} {self.invincibility}턴 무적상태로 변신')
            Party.elixir -= 1  # 엘릭서 차감
            self.invincibility -= 1  # 무적변수 턴차감
            return 1
        else:  # 엘릭서가 없는 경우
            print()
            print('엘릭서가 없습니다.')
            print('전투복귀')
            return 0

    def ramen_mt(self, party_list):  # 라면
        # 라면을 끓일지 / 라면을 먹을지

        if Party.ramen >= 1:  # 라면의 개수 1개이상
            print()
            print('당신과함께라면 냠냠')
            # print(f'파티원의 체력이 {self.now_Hp * 0.5},{self.now_Mp * 0.5}회복되었습니다') # 파티원체력회복
            Party.ramen -= 1  # 라면 차감
            return 1
        else:  # 라면이 없는 경우
            print()
            print('당신과함께라면 끓이기시작')
            print('전투복귀')
            Party.ramen += 1  # 라면 증가
            return 1

    def bum_medicine_mt(self):  # 범규약
        md_choice = input('[1번 콘푸라이트] [2번 떡하나] [3번 담배] [4번 취소]')
        while True:
            if md_choice == '1':  # 콘푸라이트를 선택한 경우
                if Party.confu >= 1:  # 콘푸라이트 1개이상 사용가능
                    print()
                    print('─' * 60, '\n')
                    print(f'{"호랑이 기운이 솟아나요":>33}')
                    # 체력 5% 회복
                    print(f'{f"{self.name} 체력 회복!":>33}\n')
                    # 약범규 죽으면 회복 불가능
                    if self.nowHp == 0:
                        continue
                    # hp가 최대 hp면 회복 스킵
                    elif self.nowHp == self.maxHp:
                        continue
                    # 현재 hp가 최대 hp 보다 5% 아래면 둘 다 회복
                    elif self.nowHp + round(self.maxHp * 0.05) <= self.maxHp:
                        self.nowHp += round(self.maxHp * 0.05)
                    # 현재 hp를 5% 회복 했을 때 hp가 최대 hp 보다 많으면, 현재 hp = 최대 hp 로 설정
                    elif self.nowHp + round(self.maxHp * 0.05) > self.maxHp:
                        self.nowHp = self.maxHp
                    Party.confu -= 1  # 콘푸라이트 차감
                    return 1
                else:  # 범규약 없는 경우
                    print()
                    print('콘푸라이트가 없습니다')
                    break

            if md_choice == '2':  # 떡하나를 선택한 경우
                if Party.ricecake >= 1:  # 떡 개수 1개이상 사용가능
                    print()
                    print(f'{"떡하나주면 안잡아먹지":>33}\n')
                    # 체력 20% 회복
                    print(f'{f"{self.name} 20% 회복!":>33}\n')
                    Party.ricecake -= 1  # 떡 차감
                    # 약범규 죽으면 회복 불가능
                    if self.nowHp == 0:
                        continue
                    # hp가 최대 hp면 회복 스킵
                    elif self.nowHp == self.maxHp:
                        continue
                    # 현재 hp가 최대 hp 보다 20% 아래면 둘 다 회복
                    elif self.nowHp + round(self.maxHp * 0.2) <= self.maxHp:
                        self.nowHp += round(self.maxHp * 0.2)
                    # 현재 hp를 20% 회복 했을 때 hp가 최대 hp 보다 많으면, 현재 hp = 최대 hp 로 설정
                    elif self.nowHp + round(self.maxHp * 0.2) > self.maxHp:
                        self.nowHp = self.maxHp
                    return 1
                else:  # 떡 없는 경우
                    print()
                    print('떡이 없습니다')
                    break

            if md_choice == '3':  # 담배를 선택한 경우
                if Party.cigarette >= 1:  # 담배 개수 1개이상 사용가능
                    print()
                    print(f'{"뻐~끔 ! 뻐~끔 !":>33}\n')
                    # 체력 50% 회복
                    Party.cigarette -= 1  # 담배 차감
                    # 약범규 죽으면 회복 불가능
                    if self.nowHp == 0:
                        continue
                    # hp가 최대 hp면 회복 스킵
                    elif self.nowHp == self.maxHp:
                        continue
                    # 현재 hp가 최대 hp 보다 50% 아래면 둘 다 회복
                    elif self.nowHp + round(self.maxHp * 0.5) <= self.maxHp:
                        self.nowHp += round(self.maxHp * 0.5)
                    # 현재 hp를 50% 회복 했을 때 hp가 최대 hp 보다 많으면, 현재 hp = 최대 hp 로 설정
                    elif self.nowHp + round(self.maxHp * 0.5) > self.maxHp:
                        self.nowHp = self.maxHp
                else:  # 담배없는 경우
                    print()
                    print('담배가 없습니다')
                    break

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
                    # 죽은 파티원 부활 선택
                    i = 1
                    cnt = 0
                    for j in party_list:
                        if j.nowHp == 0:
                            print(f'{i}.{j.name}(죽음)')
                            i += 1
                            cnt += 1
                            if i >= 2:
                                select = input(f'{"[1.":>18} 초코의용] [2. 보우연재]\n'
                                            f'{"[3.":>21} 약범규] [4. 취소]\n'
                                            f'{"부활시킬 사람을 선택해주세요: ":>30}')
                                if select == '1':
                                    print(f'{i}.{j.name} 부활')
                                    j.nowHp += j.maxHp
                                    j.nowMp += (j.maxMp - j.nowMp)
                                    print("기도 완료")
                                    return 1
                                elif select == '2':
                                    print(f'{i}.{j.name} 부활')
                                    j.nowHp += j.maxHp
                                    j.nowMp += (j.maxMp - j.nowMp)
                                    print("기도 완료")
                                    return 1
                                elif select == '3':
                                    print(f'{i}.{j.name} 부활')
                                    j.nowHp += j.maxHp
                                    j.nowMp += (j.maxMp - j.nowMp)
                                    print("기도 완료")
                                    return 1
                                elif select == '4':
                                    print(f"{'<취소하기를 선택했습니다>':>33}")
                                    print(f"{'<이전 선택창으로 돌아갑니다>':>34}\n")
                                    return 0

                        elif cnt == 0:
                            print(f"{'사망한 파티원 없음.이전으로 돌아감.':>36}\n")
                            return 0

                    # for i in range(len(party_list)):
                    #     cnt = 0
                    #     if party_list[i].nowHp == 0:
                    #         print(f'{party_list[i].name} 부활')
                    #         party_list[i].nowHp += party_list[i].maxHp
                    #         party_list[i].nowMp += (party_list[i].maxMp - party_list[i].nowMp)
                    #         cnt += 1
                    #     elif cnt == 0:
                    #         print(f"{'사망한 파티원 없음.이전으로 돌아감.':>36}\n")
                    #         return 0
                    #     else:
                    #         print("기도 완료")
                    #         return 1

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

