import sys
N = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
time.sort()

time_taken = [(i+1)*t for i, t in enumerate(time[::-1])]

print(sum(time_taken))

