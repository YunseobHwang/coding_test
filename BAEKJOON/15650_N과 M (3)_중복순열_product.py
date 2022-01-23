from itertools import *
N, M = map(int, input().split())

*starmap(print, product(*[range(1,N+1)]*M)),
# for i in product(range(1,N+1), repeat = M):
#     print(*i)
