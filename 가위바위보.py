import random
a = 0
b = 0
game = ['x', 'x', 'o', 'x', 'x']
# a = random.randrange(0, 3)
# b = random.randrange(0, 3)
win = random.randrange(0, 2)

while True:
    if win == 0: #a가 이기면 오른쪽으로 이동
        game.pop(-1)
        game.insert(1,'x')
        print(game)
        print("a 승리")
        if game[4] == 'o':
            print("a 최종승리")
            break
    elif win == 1: #b가 이기면 왼쪽으로 이동
        game.pop(0)
        game.insert(-1, 'x')
        print(game)
        print("b 승리")
        if game[0] == 'o':
            print("b 최종승리")
            break