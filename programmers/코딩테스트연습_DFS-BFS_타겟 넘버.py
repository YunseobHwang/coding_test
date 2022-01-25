numbers = [1, 1, 1, 1, 1]
target = 3

answer = 0
def solution(numbers, target):
    def dfs(idx, numbers, target, value):
        global answer
        if idx == len(numbers) and value == target:
            answer += 1
            return
        elif idx == len(numbers):
            return

        dfs(idx + 1, numbers, target, value + numbers[idx])
        dfs(idx + 1, numbers, target, value - numbers[idx])

    dfs(0, numbers, target, 0)
    return answer

print(solution(numbers, target))
