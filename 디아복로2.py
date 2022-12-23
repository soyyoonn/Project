si_choco = ['초코의용군', [100, 150], [300, 500], 3, 3]
import random

# 포션 사용 함수, y 포션 사용 선택시
def sy_potion(si_choco):
    print("포션을 사용합니다")
    # 현재 hp => 최대 hp
    si_choco[2][0] = si_choco[2][1]
    print("HP가 회복됩니다")
    print(f"{si_choco[0]:>20} {si_choco[2][0]}/{si_choco[2][1]}")
    # 포션 개수 차감
    si_choco[3] -= 1

# 엘릭서 사용 함수, 엘릭서 사용 선택시
def sy_elixir(si_choco):
    print("엘릭서를 사용합니다")
    # 엘릭서 1회 10턴 사용 가능
    elixir = 10
    print("10턴동안 무적")
    # 현재 hp => 최대 hp
    si_choco[2][0] = si_choco[2][1]
    print("HP가 회복됩니다")
    # 엘릭서 개수 차감
    si_choco[4] -= 1
    return elixir

# 전투 후 승리시 보상 함수
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
        # 포션 개수 증가
        si_choco[3] += 1
    # 포션 얻은 후 엘릭서 획득 할 경우
    elif potion == 1 and elixir <= 5:
        print("엘릭서를 획득했습니다")
        # 엘릭서 개수 증가
        si_choco[4] += 1
    # 포션 획득하지 못 할 경우
    else:
        print("포션을 획득하지 못했습니다")

    return si_choco

