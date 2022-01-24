N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]

from collections import deque

meeting = deque(sorted(meeting, key=lambda x:(x[1], x[0])))
_, end = meeting.popleft()
meeting_cnt = 1
while meeting:
    i, j = meeting.popleft()
    if i >= end:
        end = j
        meeting_cnt += 1

print(meeting_cnt)