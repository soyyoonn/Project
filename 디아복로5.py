import random
import keyboard
import time

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
    potal_a = random.randrange(1, len(pm_maze))
    potal_b = random.randrange(1, len(pm_maze))

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
                # 다음 던전으로 랜덤 이동
                a = random.choice(map_list)
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
                # 다음 던전으로 랜덤 이동
                a = random.choice(map_list)
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
                # 다음 던전으로 랜덤 이동
                a = random.choice(map_list)
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
                # 다음 던전으로 랜덤 이동
                a = random.choice(map_list)
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
    si_choco = ['초코의용군', [100, 150], [500, 500], 0, 0]
    print(f'{"던전에 입장합니다...":^33}')
    print_map(maze, si_choco)


main()
