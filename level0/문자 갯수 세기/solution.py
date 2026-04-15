def solution(my_string):
    upper_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    lower_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    answer = [0] * 52
    for index, alph in enumerate(upper_list + lower_list):
        if alph in my_string:
            answer[index] = len([c for c in my_string if c == alph])

    return answer

# 다른풀이
def solution2(my_string):
    return [my_string.count(alphabet) for alphabet in 'abcdefghijklmnopqrstuvwxyz'.upper()+'abcdefghijklmnopqrstuvwxyz']