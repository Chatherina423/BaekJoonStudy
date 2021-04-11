# 콘도선정 2246

import sys

N = int(sys.stdin.readline())

list = []
count = 0

class condo():
    def __init__(self, d, c):
        self.d = d
        self.c = c

for i in range(N):
    D, C = map(int, sys.stdin.readline().split())
    list.append(condo(D, C))

for i in range(N):
    flag = True
    for j in range(N):
        if i != j:
            if list[i].d > list[j].d:
                if list[i].c >= list[j].c:
                    flag = False
                    break
            elif list[i].c > list[j].c:
                if list[i].d  >= list[j].d:
                    flag = False
                    break
    if flag == True:
        count = count + 1

print(count)






