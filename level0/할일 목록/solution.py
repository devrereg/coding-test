def solution(todo_list, finished):
    remains = []
    for index, is_finish in enumerate(finished):
        if not is_finish:
            remains.append(todo_list[index])

    return remains


def solution2(todo_list, finished):
    remains = []
    for a,b in zip(todo_list, finished):
        if not b:
            remains.append(a)

    return remains