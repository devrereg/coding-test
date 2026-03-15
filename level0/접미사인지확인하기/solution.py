def solution(my_string, is_suffix):
    return int(my_string[len(my_string) - len(is_suffix):] == is_suffix)


# 다른풀이
def solution2(my_string, is_suffix):
    return my_string.endswith(is_suffix)

# 다른풀이
def solution3(my_string, is_suffix):
    return int(my_string[-len(is_suffix)] == is_suffix)