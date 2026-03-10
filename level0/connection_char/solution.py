def solution(my_string, index_list):
    answer = ''
    for num in index_list:
        answer += my_string[num]
    return answer


# 다른 풀이

def solution2(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])