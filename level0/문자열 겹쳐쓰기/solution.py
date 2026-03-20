# 오답 ❌
def solution(my_string, overwrite_string, s):
    replace_txt = my_string[s:s+len(overwrite_string)]
    return my_string.replace(replace_txt, overwrite_string)



# 다른 풀이
def solution2(my_string, overwrite_string, s):
    return my_string[0:s:1]+overwrite_string[::1]+my_string[s+len(overwrite_string)::1]

