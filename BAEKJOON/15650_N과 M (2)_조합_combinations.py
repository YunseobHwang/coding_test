from itertools import *
N, M = map(int, input().split())
for i in combinations(range(1,N+1), M):
    print(*i)
