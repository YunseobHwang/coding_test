def solution(N, number):
    if number == N:
        return 1

    total_set = []
    total_set.append({N})

    for i in range(2, 9):
        sub_set = set()
        sub_set.add(int(str(N) * i))
        for mid_i in range(0, i // 2):
            for x in total_set[mid_i]:
                for y in total_set[i - mid_i - 2]:
                    sub_set.add(x + y)
                    sub_set.add(x - y)
                    sub_set.add(y - x)
                    sub_set.add(x * y)
                    if y != 0: sub_set.add(int(x / y))
                    if x != 0: sub_set.add(int(y / x))

        if number in sub_set:
            return i
        else:
            total_set.append(sub_set)

    return -1