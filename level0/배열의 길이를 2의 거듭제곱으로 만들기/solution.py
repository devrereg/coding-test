def solution(arr):
    n = 0
    arr_len = len(arr)
    while True:
        length = 2**(n)
        if arr_len <= length:
            arr += [0  for i in range(length - len(arr))]
            return arr
        n += 1

def solution2(arr):
    a = 1
    b = len(arr)
    while a < b :
        a *= 2
    return arr + [0] * (a-b)