def solution(babbling):
    answer = 0
    word_list = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        for word in word_list:
            if word*2 not in b:
                b = b.replace(word, ' ')

        if len(b.replace(" ", "")) == 0:
            answer += 1

    return answer