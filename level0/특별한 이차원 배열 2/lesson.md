1. zip(*arr) => 2차원 배열을 전치 행렬로 만듦

arr = [
  [1, 2],
  [3, 4]
]

zip(*arr)
→ (1, 3), (2, 4)

2. map(list, zip(*arr)) => 전치행렬을 list 로 맵핑
→ [ [1, 3], [2, 4] ]


3. list(map(list, zip(*arr))) => 최종적으로 전치 행렬 완성

