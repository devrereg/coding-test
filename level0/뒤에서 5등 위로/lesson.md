sort 함수와 sorted 함수

- sort: 
  - 값을 반환하지 않는다.
  - default 는 오름차순.
  - 내림차순은 arr.sort(reverse=True)
  - 정렬 기준 arr.sort(key=len) => 문자열 길이 기준 으로 정렬

- sorted:
  - 새로운 list 를 반환 한다.

```python
result = arr.sort()
print(result)   # None 
```