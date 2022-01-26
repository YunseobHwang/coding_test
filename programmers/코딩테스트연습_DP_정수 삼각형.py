def solution(triangle):
    for i in range(1, len(triangle)+1):
        for j in range(0, len(triangle[-i])-1):
            triangle[-i-1][j] += max(triangle[-i][j], triangle[-i][j+1])
    return triangle[0][0]