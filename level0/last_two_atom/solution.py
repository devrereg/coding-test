def solution(num_list):
    last_index = len(num_list) - 1
    num1 = num_list[last_index - 1]
    num2 = num_list[last_index]

    last_num = num2 - num1 if num2 - num1 > 0 else 2 * num2
    num_list.append(last_num)
    return num_list


if __name__ == "__main__":
    print(solution([2,1,6]))
    print(solution([5,2,1,7,5]))