def solution(num_list):
    answer = -1
    for i in range(len(num_list)):
        print(i)
        if num_list[i] < 0:
            answer = i
            break
    return answer


#  다른 풀이
def solution2(num_list):
    for i, num in enumerate(num_list):
        if num < 0:
            return i

    return -1