import heapq as hq

def solution(jobs):
    hq.heapify(jobs)
    n_jobs = len(jobs)
    start, taken = hq.heappop(jobs)
    total = taken
    end = start + taken

    while jobs:

        # 현재 작업이 끝나기 전에 다른 작업이 없으면 바로 실행
        if jobs[0][0] > end:

            start, taken = hq.heappop(jobs)
            total += taken
            end = start + taken

        # 현재 작업을 끝나기 전(jobs[0][0]<end)에 있는 작업들이 있다면 불러와서
        # 걸리는 시간(taken_2) 기준으로 힙 구조 가장 적은 걸 빼서 우선배치
        elif jobs[0][0] <= end:

            work_rearrange = []
            hq.heapify(work_rearrange)

            while jobs[0][0] <= end:
                start_2, taken_2 = hq.heappop(jobs)
                hq.heappush(work_rearrange, [taken_2, start_2])
                if len(jobs) == 0: break

            taken_2, start_2 = hq.heappop(work_rearrange)
            total += (end - start_2) + taken_2
            end = end + taken_2

            while work_rearrange:
                taken_2, start_2 = hq.heappop(work_rearrange)
                hq.heappush(jobs, [start_2, taken_2])

    return total // n_jobs