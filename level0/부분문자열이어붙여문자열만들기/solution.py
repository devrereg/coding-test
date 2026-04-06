def solution(arr, flag):
    answer = []
    for num, boolean in list(zip(arr, flag)):
        if boolean:
            answer += [num]*num*2
        else:
            answer = answer[:len(answer) - num]

    return answer


def solution2(arr, flag):
    answer = []
    for num, boolean in list(zip(arr, flag)):
        if boolean:
            answer += [num]*num*2
        else:
            answer = answer[:len(answer) - num]

    return answer

