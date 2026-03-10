다른 풀이 직접 짜보기
```python

def solution(my_string, num_list):
    return ''.join([my_string[x] in x for num_list])
```
