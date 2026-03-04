def solution(num_list):
    last_index = len(num_list) - 1
    num1 = num_list[last_index - 1]
    num2 = num_list[last_index]

    last_num = num2 - num1 if num2 - num1 > 0 else 2 * num2
    num_list.append(last_num)
    return num_list


def solution2(num_list):
    n1, n2 = num_list[-1] , num_list[-2]
    num_list.append(n1 - n2) if n1 - n2 > 0 else num_list.append(2*n1)
    return num_list

if __name__ == "__main__":
    print(solution([2,1,6]))
    print(solution([5,2,1,7,5]))

    print(solution2([2,1,6]))
    print(solution2([5,2,1,7,5]))