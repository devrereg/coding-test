enumerate 함수를 사용하면 원소와, 인덱스를 반복문에서 같이 쓸 수 있다.

 ex)
 ```python
def solution(num_list):
    for i, num in enumerate(num_list):
        if num < 0:
            return i

    return -1
```
