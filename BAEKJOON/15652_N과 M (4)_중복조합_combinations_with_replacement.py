n, m = map(int, input().split())
from itertools import *
*starmap(print, combinations_with_replacement(range(1, n+1), m)),