from itertools import *

N, M = map(int, input().split())
# *starmap(print, permutations(range(1, N + 1), M)),

for p in permutations(range(1,N+1),M):
    print(*p) # print(p[0], p[1], ... , p[M])