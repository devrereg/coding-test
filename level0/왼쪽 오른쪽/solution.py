def solution(str_list):
    for index, c in enumerate(str_list):
        if c == 'l':
            return str_list[:index]
        if c == 'r':
            return str_list[index + 1:]

    return []