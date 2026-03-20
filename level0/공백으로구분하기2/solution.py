def solution(my_string):
    answer = []
    for s in my_string.split(' '):
        if s != '':
            answer.append(s)

    return answer


# 다른 풀이
solution2=lambda x:x.split()