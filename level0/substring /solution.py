def solution(my_string, target):
    arr = []

    max_len = len(my_string)
    target_len = len(target)
    for i in range(int(len(my_string))):
        if i + target_len <= max_len:
            arr.append(my_string[i:len(target) + i])
        else:
            break

    for atom in arr:
        if atom == target:
            return 1

    return 0


# 다른 풀이
def solution2(my_string, target):
    return int(target in my_string)