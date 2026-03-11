def solution(n):

    answer = 0
    if n % 2 == 1:
        for i in range(n):
            even = 2*i + 1
            if n >= even:
                answer += even
            else:
                break
    else:
        for i in range(n):
            odd = 2*i + 2
            if n >= odd:
                answer += odd*odd
            else:
                break

    return answer


#  다른 풀이
def solution2(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])