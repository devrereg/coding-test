def solution(num_list):
    sum_even = 0
    sum_odd = 0
    for index, num in enumerate(num_list):
        if index % 2:
            sum_odd += num
        else:
            sum_even += num

    return sum_odd if sum_odd > sum_even else sum_even


# 다른 풀이
def solution2(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))