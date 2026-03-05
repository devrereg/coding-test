def solution(num, n):
    result = 0 if num % n != 0 else 1
    return result

# 다른 풀이
def solution2(num, n):
    print(not(0), not(1), not(-1))

    return int(not(num % n))

if __name__ == "__main__":
    print(solution(98, 2))
    print(solution2(34, 3))
