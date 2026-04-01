def solution(str1, str2):
    answer = ''
    for i in range(len(str1 + str2)):
        answer += str1[i // 2] if i % 2 == 0 else str2[i // 2]
    return answer


# 다른 풀이
def solution2(str1, str2):
    res=''
    for s1,s2 in zip(str1,str2):
        res+=s1+s2
    return res