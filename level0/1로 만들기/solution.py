def solution(num_list):
    count = 0
    for num in num_list:
        while num != 1:
            num = (num - 1) / 2 if num % 2 == 1 else num / 2
            count += 1

    return count


# 다른풀이
def solution2(num_list):
    answer = 0

    for n in num_list:
        while n != 1:
            n //= 2
            answer += 1

    return answer
