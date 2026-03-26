def solution(numLog):
    variables = {
        '1': 'w',
        '-1': 's',
        '10': 'd',
        '-10': 'a'
    }

    answer = ''
    repeat = len(numLog)
    for i in range(repeat):
        if i + 1 < repeat:
            key = str(numLog[i + 1] - numLog[i])
            answer += variables.get(key)

    return answer



# 다른풀이
def solution2(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        dif = numLog[i] - numLog[i - 1]
        if dif == 1:
            answer += 'w'
        elif dif == -1:
            answer += 's'
        elif dif == 10:
            answer += 'd'
        elif dif == -10:
            answer += 'a'
        else:
            pass
    return answer