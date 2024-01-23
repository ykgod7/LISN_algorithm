def solution(ingredient):
    answer = 0
    s = []
    
    for _ in ingredient:
      s.append(_)
      
      if s[-4:] == [1, 2, 3, 1]:
        answer += 1
        
        for i in range(4):
          s.pop()

    return answer