def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == arr[j][i]:
                continue
            else:
                return 0

    return 1

# 다른풀이
def solution2(arr):
    return int(arr == list(map(list, zip(*arr))))

if __name__ == "__main__":
    print(solution2([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))