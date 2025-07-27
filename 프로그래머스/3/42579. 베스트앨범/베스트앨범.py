import collections

def solution(genres, plays):
    answer = []
    
    freq = collections.defaultdict(list)
    order = collections.defaultdict(list)
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        freq[genre].append(play)
        order[genre].append(idx)
    
    sorted_freq = dict(sorted(freq.items(), key = lambda item: sum(item[1]), reverse = True))
    for key, value in sorted_freq.items():
        for _ in range(2):
            if value == []:
                break
            idx = value.index(max(value))
            rel_idx = order[key][idx]
            answer.append(rel_idx)
            del value[idx]
            order[key].remove(rel_idx)
    return answer