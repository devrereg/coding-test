def solution(myString):
    return sorted([c for c in myString.split('x') if c != ''])


# 다른풀이
def solution2(myString):
    return sorted([c for c in myString.split('x') if c])
