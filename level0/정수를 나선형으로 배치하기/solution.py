def solution(n):
    answer = []
    for i in range(n):
        answer.append([0] * n)
    num = 0
    i = 0

    while num < n * n:
        for col in range(i, n - i):
            num += 1
            answer[i][col] = num
        if n - 1 - i >= 0:
            for row in range(i + 1, n - i):
                num += 1
                answer[row][n - 1 - i] = num

            for col in range(n - 2 - i, i - 1, -1):
                num += 1
                answer[n - 1 - i][col] = num
        if n - 2 - i >= 0:
            for row in range(n - 2 - i, i, -1):
                num += 1
                answer[row][i] = num
        i += 1

    return answer

# 다른풀이 => 가독성과 코드 이해하기 쉽다.
def solution2(n):
    answer = [([0]*n) for _ in range(n)]
    j = 1
    top, bottom, right, left = 0, n-1, n-1, 0


    while j <= n**2:
        # 오른쪽
        for i in range(left, right+1):
            answer[top][i] = j
            j += 1
        top += 1

        # 아래쪽
        for i in range(top, bottom+1):
            answer[i][right] = j
            j += 1
        right -= 1

        # 왼쪽
        for i in range(right,left-1,-1):
            answer[bottom][i] = j
            j += 1
        bottom -= 1

        # 위쪽
        for i in range(bottom, top-1,-1):
            answer[i][left] = j
            j += 1
        left += 1

    return answer

# 좌표계를 이용한 풀이
def solution3(n):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    y, x = 0, -1

    arr = [[0] * n for _ in range(n)] # 2차원 배열 세팅
    cnt = 1
    direction = 0
    while cnt <= n**2:
        ny, nx = y + dy[direction], x + dx[direction]
        if 0 <= ny < n and 0 <= nx < n and not arr[ny][nx]:
            arr[ny][nx] = cnt
            cnt += 1
            y, x = ny, nx
        else:
            direction = (direction + 1) % 4

    return arr