def calc_day(n):
    year, month, day = map(int, n.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    today = calc_day(today)

    for term in terms:
        a, b = term.split(' ')
        terms_dict[a] = int(b)

    for (idx, privacy) in enumerate(privacies):
        target, t = privacy.split(' ')
        temp = calc_day(target) + terms_dict[t] * 28

        if today >= temp:
            answer.append(idx + 1)
    return answer