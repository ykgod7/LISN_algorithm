def solution(keymap, targets):
    answer = []
    alphabet_dict = {}

    for key in keymap:
        for idx, _ in enumerate(key):
            if not _ in alphabet_dict:
                alphabet_dict[_] = idx + 1
            elif alphabet_dict[_] > idx + 1:
                alphabet_dict[_] = idx + 1

    for target in targets:
        count = 0

        for _ in target:
            if _ not in alphabet_dict:
                answer.append(-1)
                break
            else:
                count += alphabet_dict[_]
        else:
            answer.append(count)

    return answer