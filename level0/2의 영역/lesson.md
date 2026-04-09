arr.index(2) 는 리스트에서 2가 첫번쨰로 있는 인덱스를 가리킨다.

```python

arr = [1, 2, 1, 4, 5, 2, 9]
arr[arr.index(2): len(arr)-arr[::-1].index(2)] 

```