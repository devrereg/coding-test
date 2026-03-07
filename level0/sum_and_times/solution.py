def solution(num_list):
    sum = 0
    times = 1

    for num in num_list:
        sum += num
        times *= num

    return int(sum ** 2 > times)


#  다른 풀이
def solution2(num_list):
    s=sum(num_list)**2
    m=eval('*'.join([str(n) for n in num_list]))
    return 1 if s>m else 0