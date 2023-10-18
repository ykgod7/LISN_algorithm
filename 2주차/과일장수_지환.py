def solution(k, m, score):
    answer = 0

    new_list = sorted(score, reverse=True)

    for i in range(m-1, len(new_list), m):
        answer += new_list[i] * m

    return answer