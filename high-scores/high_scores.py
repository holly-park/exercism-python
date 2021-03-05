def latest(scores):
    print(scores)
    if min(scores) == 0:
        scores.remove(0)
        return min(scores)


def personal_best(scores):
    print(scores)
    return max(scores)


def personal_top_three(scores):
    print(scores)
    scores.sort()
    scores.reverse()
    return scores[0:3]
