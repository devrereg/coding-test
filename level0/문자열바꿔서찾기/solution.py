def solution(myString, pat):
    new_string = ''.join(['B' if c == 'A' else 'A' for c in myString])
    return int(pat in new_string)



#  다른풀이
def solution2(myString, pat):
    return pat in myString.replace('A', 'C').replace('B', 'A').replace('C','B')
