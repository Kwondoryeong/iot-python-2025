# py90_list_op.py

# append() 요소로 추가하고 싶을 경우
x = ['W', 'Y', 'Z']
y = ['A', 'C', 'E']

x.append(y)
print(x)

# 4번째 요소로 추가 됨

# extend() 1차원 배열로 쭉 늘리고 싶을 경우

x = ['W', 'Y', 'Z']
y = ['A', 'C', 'E']

x.extend(y)
print(x)

# 합쳐짐 총 6개