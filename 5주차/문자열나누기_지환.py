def solution(s):
    answer = 0
    x = ""
    count_target, count_else = 0, 0
    
    for idx, letter in enumerate(s):
        if not x:
            x = letter
            count_target += 1
        else:
            if x == letter:
                count_target += 1
            else:
                count_else += 1
        
        if idx == len(s) - 1:
            answer += 1
        else:
            if count_target == count_else:
                answer += 1
                x = ""
                count_target, count_else = 0, 0
            
    return answer