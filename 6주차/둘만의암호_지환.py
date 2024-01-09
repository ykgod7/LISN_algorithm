def solution(s, skip, index):
    answer = ''
    alphabets = [chr(i) for i in range(97, 123) if chr(i) not in skip]

    for _ in s:
        answer += alphabets[(alphabets.index(_) + index) % len(alphabets)]

    return answer
