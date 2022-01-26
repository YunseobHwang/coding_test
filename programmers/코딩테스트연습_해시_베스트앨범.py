from collections import *

def solution(genres, plays):
    song_info = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        song_info[g] += [(p, i)]
    genre_sort = sorted(song_info.keys(), key = lambda x: -sum(map(lambda y: y[0], song_info[x])))
    answer = []
    for g in genre_sort:
        songs = [i for _, i in sorted(song_info[g], key = lambda x: (-x[0], x[1]))]
        answer += songs[:min(len(songs), 2)]
    return answer