def solution(my_string, indices):
    arr = list(my_string)
    for num in indices:
        arr[num] = 0

    return ''.join([c for c in arr if c != 0])


# 다른풀이
def solution2(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:answer+=my_string[i]
    return answer