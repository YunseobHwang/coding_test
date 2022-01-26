from itertools import combinations

def prime_number(num):
    cnt = 0
    for i in range(2, num):
        if num % i == 0:
            cnt += 1
        if cnt != 0:
            return False
    return True

def solution(nums):
    nums = list(map(sum, combinations(nums, 3)))
    prime_nums = [prime_number(n) for n in nums]
    return prime_nums.count(True)

nums = list(map(int, input().split()))

print(solution(nums))

