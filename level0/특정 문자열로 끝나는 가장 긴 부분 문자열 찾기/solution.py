def solution(myString, pat):
    answer = myString
    str_len = len(myString)
    for i in range(str_len):
        if answer.endswith(pat): return answer
        answer = myString[0:str_len - i + 1]
    return answer

# 다른 풀이
def solution2(myString, pat):
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]