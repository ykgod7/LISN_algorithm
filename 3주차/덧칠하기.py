def solution(n, m, section):
    answer = 1

    temp = section[0]

    for num in section[1:]:    
        if num - temp >= m:
            answer += 1
            temp = num

    return answer