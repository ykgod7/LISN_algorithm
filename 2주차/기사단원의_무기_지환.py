# 더 간결하지만 속도가 살짝 느림
def solution(number, limit, power):
    def cf(n):
        a = []

        for i in range(1, int(n**0.5)+1):
            if n%i == 0:
                a.append(i)
                a.append(n//i)

        return len(set(a))

    return sum([cf(i) if cf(i) <= limit else power for i in range(1, number+1)])

# 속도가 조금 더 빠름
def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        count = 0
        
        for j in range(1, int(i**(1/2))+1):
            if i%j == 0:
                if i/j == j:
                    count += 1
                else:
                    count += 2
            
            if count > limit:
                answer += power
                break
        else:
            answer += count
            
    return answer