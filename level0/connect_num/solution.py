def solution(num_list):
    num_even_list = [x for x in num_list if x % 2 == 0]
    num_odd_list = [x for x in num_list if x % 2 == 1]

    sum_of_even = 0
    for i in range(len(num_even_list)):
        n = len(num_even_list) - i - 1
        sum_of_even += num_even_list[i] * 10 ** n

    sum_of_odd = 0
    for i in range(len(num_odd_list)):
        n = len(num_odd_list) - i - 1
        sum_of_odd += num_odd_list[i] * 10 ** n

    return sum_of_even + sum_of_odd

# 다른 풀이
def solution2(num_list):
    answer = 0
    a=""#홀수
    b=""#짝수
    for i in num_list:
        if i%2!=0:
            a+=str(i)
        else:
            b+=str(i)
    return int(a)+int(b)