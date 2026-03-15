def solution(n):
    arr = [n]
    while n != 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        arr.append(n)

    return arr

if __name__ == "__main__":
    print(solution(10))