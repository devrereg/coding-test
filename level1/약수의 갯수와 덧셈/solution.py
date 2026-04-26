def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        cnt = 1
        for i in range(1, num // 2 + 1):
            if not num % i: cnt += 1
        answer += -num if cnt % 2 else num

    return answer


# 다른풀이 => 제곱수는 약수의 개수가 홀수
def solution2(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    return answer
