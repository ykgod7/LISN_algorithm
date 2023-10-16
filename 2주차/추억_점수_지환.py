def solution(name, yearning, photo):
    answer = []
    new_dictionary = dict(zip(name, yearning))
    
    for name_list in photo:
        count = 0
        
        for person in name_list:
            if person in new_dictionary:
                count += new_dictionary[person]
        
        answer.append(count)
            
    return answer