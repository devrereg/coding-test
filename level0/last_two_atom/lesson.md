python의 append 함수는
list 에 요소를 추가하지만 None 을 반환한다.


```python
nums = [1, 2, 3]
result = nums.append(4)

print(result)   # None
print(nums)     # [1, 2, 3, 4]
```

<다른 풀이>   
```python
def solution(num_list):
    n1, n2 = num_list[-1], num_list[-2]
    if n1 > n2:
        num_list.append(n1 - n2)
    else:
        num_list.append(n1 * 2)
    return num_list
```