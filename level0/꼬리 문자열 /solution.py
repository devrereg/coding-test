def solution(str_list, ex):
    return ''.join([s for s in str_list if not ex in s ])



#  다른풀이
def solution2(str_list, ex):
    return ''.join(filter(lambda x: ex not in x, str_list))
