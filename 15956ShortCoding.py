# 15955 Booster
import sys
import heapq

MAX_N = 250001
root = [i for i in range(MAX_N)]
answer = [0 for i in range(MAX_N)]

N, Q = map(int, sys.stdin.readline().split())

class ck():
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx

class quest():
    def __init__(self, X, A, B, idx):
        self.X = X
        self.A = A
        self.B = B
        self.idx = idx
    def __lt__(self, other):
        return self.X < other.X

class vertex():
    def __init__(self, dist, A, B):
        self.dist = dist
        self.A = A
        self.B = B

    def __lt__(self, other):
        return self.dist < other.dist


def find(x):
    if (root[x] == x):
        return x
    else:
        root[x] = find(root[x])
        return find(root[x])

def union(a, b):
    a = find(a)
    b = find(b)
    if (a == b):
        return
    root[b]=a

cklist=[]

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    cklist.append(ck(a, b, i))

cklist_x = sorted(cklist, key = lambda cklist: cklist.x)
cklist_y = sorted(cklist, key = lambda cklist: cklist.y)


pq = []

for i  in range(N-1):
    heapq.heappush(pq, vertex((cklist_x[i+1].x - cklist_x[i].x), cklist_x[i].idx, cklist_x[i + 1].idx))
    heapq.heappush(pq, vertex((cklist_y[i+1].y - cklist_y[i].y), cklist_y[i].idx, cklist_y[i + 1].idx))


q_list =[]
for i in range(Q):
    A, B, X = map(int, sys.stdin.readline().split())
    q_list.append(quest(X, A, B, i))

q_list.sort()

# q_list = sorted(q_list, key = lambda q_list: q_list.X)


for i in range(Q):
    while(len(pq) != 0) and (pq[0].dist <= q_list[i].X):
        union(pq[0].A, pq[0].B)
        heapq.heappop(pq)
    answer[q_list[i].idx] = (find(q_list[i].A) == find(q_list[i].B))

    # while(len(pq) != 0):
    #     current = pq[0].dist
    #     if (current > q_list[i].X):
    #         break
    #     union(pq[0].A, pq[0].B)
    #     heapq.heappop(pq)
    # answer[q_list[i].idx] = (find(q_list[i].A) == find(q_list[i].B))

    if answer[i] == 0:
        print('Yes')
    else:
        print('No')

# for i in range(Q):
#     if answer[i] == 0:
#         print('Yes')
#     else:
#         print('No')

