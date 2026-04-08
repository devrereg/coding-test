def solution(intStrs, k, s, l):
    answer = []
    for num_str in intStrs:
        value = int(num_str[s: s + l])
        if value > k:
            answer.append(value)

    return answer