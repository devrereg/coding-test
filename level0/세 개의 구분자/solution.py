def solution(myStr):
    arr = myStr.replace('a', ',').replace('b', ',').replace('c', ',').split(',')
    answer = [s for s in arr if len(s) > 0]
    return answer if len(answer) > 0 else ["EMPTY"]



# 다른풀이
def solution2(myStr):
    answer = [s for s in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split()]
    return answer if len(answer) > 0 else ["EMPTY"]