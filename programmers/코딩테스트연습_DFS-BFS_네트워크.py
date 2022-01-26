def solution(n, computers):
    def dfs(computers, current_computer, visited):
        visited[current_computer] = 1
        for i in range(len(computers)):
            if i != current_computer and computers[current_computer][i] == 1 and visited[i] == 0:
                visited[i] = 1
                dfs(computers, i, visited)

    visited = [0] * n
    answer, i = 0, 0

    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, i, visited)
            answer += 1
        i += 1

    return answer