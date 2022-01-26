def solution(user_id, banned_id):
    answer = 0
    name_number = {name: [i] for i, name in enumerate(user_id)}
    possible_id = {a: [] for a in banned_id}

    for a in possible_id:
        for b in user_id:
            if len(a) == len(b) and a.count('*') == [a_i != b_i for a_i, b_i in zip(a, b)].count(True):
                possible_id[a] += name_number[b]

    possible_number = []
    for b_id in banned_id:
        possible_number.append(possible_id[b_id])

    from itertools import product

    cases = []
    for case in product(*possible_number):
        if len(set(case)) < len(banned_id):
            continue
        elif list(set(case)) in cases:
            continue
        else:
            cases.append(list(set(case)))

    return len(cases)