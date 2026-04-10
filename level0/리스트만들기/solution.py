def solution(n, slicer, num_list):
    if n == 1:
        return num_list[:slicer[1] + 1]
    if n == 2:
        return num_list[slicer[0]:]
    if n == 3:
        return num_list[slicer[0]: slicer[1] + 1]
    if n == 4:
        return num_list[slicer[0]: slicer[1] + 1: slicer[2]]
    

# 다른 사람 풀이
def solution2(n, slicer, num_list):
    a,b,c = slicer
    if n == 1:
        return num_list[:a + 1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a: b + 1]
    else:
        return num_list[a: b + 1: c]