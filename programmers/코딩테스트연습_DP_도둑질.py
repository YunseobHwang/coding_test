def solution(m):
    n = len(m)

    x1, x2 = m[0], max(m[0], m[1])
    y1, y2 = m[1], max(m[1], m[2])

    if n > 3:
        for i in range(1, n - 2):
            x1, x2 = x2, max(x2, m[i + 1] + x1)
            y1, y2 = y2, max(y2, m[i + 2] + y1)

    return max(x2, y2)