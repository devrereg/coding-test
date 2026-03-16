def solution(num_str):
    return sum(list(map(lambda x: int(x), num_str)))



# 다른풀이
def solution2(num_str):
    return sum(map(int, num_str))