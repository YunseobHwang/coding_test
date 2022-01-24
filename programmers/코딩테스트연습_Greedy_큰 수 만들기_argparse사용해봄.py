import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--number', action='store', type=str, default='0', help='given number')
    parser.add_argument('--k', action='store', type=int, default=0, help='elimination number')
    args = parser.parse_args()
    print(f'args={args}\n')
    return args

def solution(number, k):
    answer = ''
    for n in number:
        while len(answer) > 0 and n > answer[-1] and k > 0:
            answer = answer[:-1]
            k -= 1
        answer += n

    if k > 0:
        answer = answer[:-k]
    print(answer)
    return answer

if __name__=='__main__':
    args = parse_arguments()
    solution(args.number, args.k)
