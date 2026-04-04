def solution(myString):
    return ''.join(['A' if c in ['a','A'] else c.lower() for c in myString])


# 다른 풀이
def solution2(myString):
    return myString.lower().replace('a', 'A')