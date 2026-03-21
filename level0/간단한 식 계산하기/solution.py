def solution(binomial):
    arr = binomial.split()
    a = int(arr[0])
    b = int(arr[2])
    calc = arr[1]
    if calc == '+':
        return a + b
    elif calc == '-':
        return a - b
    else:
        return a * b


# 다른 풀이
solution2 = eval

# 다른 풀이
def solution3(binomial):
    a, op, b = binomial.split()

    a = int(a)
    b = int(b)

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b

    return result