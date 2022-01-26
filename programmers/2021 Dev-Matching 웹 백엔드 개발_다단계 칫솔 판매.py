def solution(enroll, referral, seller, amount):
    graph = {e: r for e, r in zip(enroll, referral)}
    answer = {e: 0 for e in enroll}

    for s, a in zip(seller, amount):
        money = a * 100
        rate = money // 10
        answer[s] += money - rate

        x = graph[s]
        while x != '-':
            if rate // 10 == 0:
                answer[x] += rate
                break
            else:
                answer[x] += rate - rate // 10

            rate = rate // 10
            x = graph[x]

    return list(answer.values())