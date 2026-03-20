.replace 가 안되는 이유는 아래 예시인 경우 이다.


```python

my_string = "andrewWithScrew"
overwrite_string = "zoe"
s=3

def solution(my_s, ov_s, s):
    replace_txt = my_s[s:s+len(ov_s)] # replace_txt = "rew"
    return my_s.replace(replace_txt, ov_s)

solution(my_string, overwrite_string, 3) # 결과: andzoeWithSczoe

# 원하는 결과 => andzoeWithScrew
# 즉 이후에 겹치는 문자열까지 바꿔버린다.

```

replace 를 쓸때는 모든 대체 문자를 바꿔버린다는것을 항상 염두할 것!