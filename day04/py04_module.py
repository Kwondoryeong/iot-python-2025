# py04_module.py

# 수학모듈 : 수학함수들이 모여있는 파이썬 모듈
import math
import random

print(math.pi)

# x ** y : int
print(math.pow(2, 10)) # pow(x,y) : float
print(math.sqrt(4))
print(math.log10(2))


# 초간단 로또
numbers = [i for i in range(1, 45 + 1)] # 1 ~ 45 리스트로
result = []

for i in range(6):  # 여섯번 반복
    result.append(random.choice(numbers))

print(result)
# weight : 가중치
numbers = weight = list(range(1, 45 + 1))
random.shuffle(weight)
print(random.shuffle(weight))

result = random.choices(numbers, weights=weight, k=6)
print(result)
# 한꺼번에 여섯개를 추출하는 란댐