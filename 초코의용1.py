import random

class Party:
    att = [100, 150]        # 공격력 클래스 변수로 넣어줌(전부 공격력 계수는 같으니까)

    potion = 5
    elixir = 1
    ramen = 1
    bum_medicine = 1

    def __init__(self, name, hp, mp):
        self.name = name
        self.nowHp = hp
        self.maxHp = hp
        self.nowMp = mp
        self.maxMp = mp

# 초코의용
class Choco(Party):  # Party 클래스 상속받은 Choco 클래스
    # Choco 클래스의 skill 메서드
    def skill(self, number):
        # 초코의용 스킬 3가지
        if number == 1:
            print(f'{self.name}의 꺾이지 않는 마음')
            self.nowHp = self.nowHp
            self.nowMp = self.nowMp
            # hp, mp 데미지 0. 그대로 ??
        if number == 2:
            print(f'{self.name}의 용사의 의지')
            # 공격력 2배
            self.att += round(self.att * 2)
            # mp -20%
            self.nowMp -= round(self.nowMp * 0.2)
        if number == 3:
            print(f'{self.name}의 트리플 어택')
            # 3번 연속 공격 ...??
            # mp -30%
            self.nowMp -= round(self.nowMp * 0.3)


# yong 객체. yong은 Choco의 인스턴스
yong = Choco('초코의용', [100, 150], 500, 300)


# 킹기태
class King(Party):  # Party 클래스 상속받은 King 클래스
    # King 클래스의 skill 메서드
    def skill(self, number, monster_att):
        # 킹기태 스킬 3가지
        if number == 1:
            print(f'{self.name}의 음이탈')
            # 몬스터 공격력 5% 감소
            monster_att -= round(monster_att * 0.05)
            # mp -10%
            self.nowMp -= round(self.nowMp * 0.1)
        if number == 2:
            print(f'{self.name}의 시나리오')
            # 아군의 hp, mp 10% 회복
            self.nowHp += round(self.nowHp * 0.1)  # 아군..?
            self.nowMp += round(self.nowMp * 0.1)
            # mp -20%
            self.nowMp -= round(self.nowMp * 0.2)
        if number == 3:
            print(f'{self.name}의 한마디')
            # 몬스터 공격..? 전투 선택사항에서 공격 ? 공격력 랜덤
            monster_att -= round(monster_att(random.randint))
            # mp -15%
            self.nowMp -= round(self.nowMp * 0.15)


# tae 객체. tae는 King의 인스턴스
tae = King('킹기태', [100, 150], 500, 300)


# 보우연재
class Bow(Party):  # Party 클래스 상속받은 Bow 클래스
    # Bow 클래스의 skill 메서드
    def skill(self, number):
        # 보우연재 스킬 3가지
        if number == 1:
            print(f'{self.name}의 흩날리는 앞머리')
            # 연속적 hp 감소...
            # mp -40%
            self.nowMp -= round(self.nowMp * 0.4)
        if number == 2:
            print(f'{self.name}의 latte는 말이야')
            # 크리티컬 공격력 2배
            self.att = round(self.att * 2)
            # mp -20%
            self.nowMp -= round(self.nowMp * 0.2)
        if number == 3:
            print(f'{self.name}의 집중의 황금안경')
            # 몬스터 기절 3턴 공격 불가. 피해 데미지 0으로 3턴 소비
            # mp -30%
            self.nowMp -= round(self.nowMp * 0.3)


# jae 객체. jae는 Bow의 인스턴스
jae = Bow('보우연재', [100, 150], 500, 300)


# 약범규
class Tiger(Party):  # Party 클래스 상속받은 Tiger 클래스
    # Tiger 클래스의 skill 메서드
    def skill(self, number):
        # 약범규 스킬 6가지
        if number == 1:
            print(f'{self.name}의 약제조!')
            if number == 1:
                print("콘푸로스트")
                # 공격력 10% 상승
                self.att += round(self.att * 0.1)
                # mp -10%
                self.nowMp -= round(self.nowMp * 0.1)
            if number == 2:
                print("떡하나")
                # 떡 1-3턴 동안 먹기
                # 떡 먹을 때마다 20% 회복 범규만..?
                self.nowHp += round(self.nowHp * 0.2)
                # mp -20%
                self.nowMp -= round(self.nowMp * 0.2)
            if number == 3:
                print("담배피던 시절")
                # 이전 턴의 체력으로 돌아감..?
                # mp -30%
                self.nowMp -= round(self.nowMp * 0.3)
        if number == 2:
            print(f'{self.name}의 격투!')
            if number == 1:
                print("범소리")
                # 50% 확률로 몬서터 공격 실패? 랜덤..
                # mp -20%
                self.nowMp -= round(self.nowMp * 0.2)
            if number == 2:
                print("약사세요")
                # 몬스터에게 약팔다가 기습공격 성공활률 40% 기존 공격력의 2배로 때림
                # 실패시 몬스터 체력 10% 회복
                # mp -40%
                self.nowMp -= round(self.nowHp * 0.4)
            if number == 3:
                print("호랑이 냥냥펀치")
                # 기본 공격력의 20% 딜로 때림
                self.att += (self.att * 0.2)
                # mp -20%
                self.nowMp -= round(self.nowMp * 0.2)


# beom 객체. beom은 Tiger의 인스턴스
beom = Tiger('약범규', [100, 150], 500, 300)