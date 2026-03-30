def solution(date1, date2):
    return 1 if int(''.join(str(num) for num in date1)) < int(''.join(str(num) for num in date2)) else 0


#  다른풀이
def solution2(date1, date2):
    for d1,d2 in zip(date1,date2):
        if d1<d2:
            return 1
        elif d1 >d2:
            return 0
        else:
            continue
    return 0