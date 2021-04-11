# 상금 헌터 15953
import sys

T = int(input())

def first(a):
    if a == 1:
        return 5000000
    elif a== 2 or a == 3:
        return 3000000
    elif a >= 4 and a<= 6:
        return 2000000
    elif a >= 7 and a<= 10:
        return 500000
    elif a >= 11 and a <= 15:
        return 300000
    elif a >= 16 and a <= 21:
        return 100000
    else:
        return 0

def second(a):
    if a == 1:
        return 5120000
    elif a== 2 or a == 3:
        return 2560000
    elif a >= 4 and a<= 7:
        return 1280000
    elif a >= 8 and a<= 15:
        return 640000
    elif a >= 16 and a <= 31:
        return 320000
    else:
        return 0


for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(first(a) + second(b))