def solution(survey, choices):
    answer = ''
    survey_dict = { 'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0 }
    survey_point = { 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3 }
    survey_arr = list(survey_dict.keys())
    
    for (string, choice) in zip(survey, choices):
        if choice > 4:
            survey_dict[string[1]] += survey_point[choice]
        else:
            survey_dict[string[0]] += survey_point[choice]
            
    for (left, right) in zip(survey_arr[::2], survey_arr[1::2]):
        if survey_dict[left] < survey_dict[right]:
            answer += right
        else:
            answer += left
    
    return answer

