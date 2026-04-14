def solution(arr):
    x = 0
    while True:
        arr_x = arr.copy()

        for i in range(len(arr)):
            if arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
            elif arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] / 2
            else:
                arr[i] = arr[i]
        if arr_x == arr:
            return x
        x += 1

