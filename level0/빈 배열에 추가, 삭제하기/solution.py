def solution(my_strings, parts):
    return ''.join([my_strings[i][s:e+1] for i, [s,e] in enumerate(parts)])




# 다른 풀이
def solution2(my_strings, parts):
    answer = ''
    for s, (x, y) in zip(my_strings, parts):
        answer += s[x:y+1]
    return answer