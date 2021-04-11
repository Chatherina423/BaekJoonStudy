# ㅋㅏ카오 머니

# 정수 N 을 입력 받는
import sys

N = int(input())

def gcd(a, b):
    if(a<b):
        tmp = a
        a = b
        b = tmp

    while (b):
        tmp = a % b
        a = b
        b = tmp

    return a

# def gcd(a, b):
#     if (b == 0):
#         return a
#     return gcd(b, a % b)

# a 는 입출금 기록, b는 남은 잔액.
prev = 0
minB = pow(10,18)
M = 0
valid = True

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if prev + a < 0:
        charge = b - prev - a

        if (b != 0) and (b < minB):
            minB = b

        if M == 0:
            M = charge
        else:
            M = gcd(charge, M)

            if (minB != pow(10, 18)) and (M <= minB):
                valid = False
                break

    else:
        if prev + a != b:
            valid = False
            break

    prev = b

if (valid == True) and (M != 0):
    print(M)
elif (valid == True) and (M == 0):
    print(1)
else:
    print(-1)
    #print('i: {}'.format(i))
    #print('a = {0} b = {1}'.format(a[i], b[i]))
    #print('====================')















