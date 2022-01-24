N, target = map(int, input().split())
coin = [int(input()) for _ in range(N)]

cnt = 0
for c in coin[::-1]:
    if target == 0:
        break

    cnt += target//c
    target = target%c

print(cnt)

