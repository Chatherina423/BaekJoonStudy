# 자리배정

# 좌석의 가로 세로 입력 받기
C, R = map(int, input().split())

# 대기 번호 입력 받기
K = int(input())

Down = C + 1
Up = 0
Left = 0
Right = R + 1

def Blocked(x, y):
    global Down, Up, Left, Right
    if x == Down:
        Down -= 1
        return True
    if x == Up :
        Up += 1
        return True
    if y == Left:
        Left -= 1
        return True
    if y == Right:
        Right += 1
        return True


dx = [0, 1, 0, -1] # 아래 위
dy = [1, 0, -1, 0]

m = 0
x = 1
y = 1
count = 1

while True:
    if count == K:
        print(x, y)
        break
    if Blocked(x + dx[m], y + dy[m]):
        m += 1
        m %= 4

    x += dx[m]
    y += dy[m]
    count += 1

    if K > C*R:
        print(0)