def solution(myString):
    answer = [0]
    index = 0
    for i, c in enumerate(myString):
        if c == 'x':
            answer += [0]
            index += 1
        else:
            answer[index] += 1

    return answer


def solution2(myString):
    return [len(w) for w in myString.split('x')]