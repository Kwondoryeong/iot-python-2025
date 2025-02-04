# py04_stringformat.py
# 문자열 포맷팅

# loginTemp = '안녕하세요, %s님!'
# name = '도형'

# print(loginTemp % (name))
# name = input('로그인할 이름 입력 > ')
# print(loginTemp % (name))

## 구세대 문자열 포맷팅
intro = '나는 %s(이)고, %d살입니다. 몸무게 %fkg입니다.'
print(intro % ('도형', 30, 55.5))

intro = '나는 %10s(이)고, %03d살입니다. 몸무게 %3.1fkg입니다.'
print(intro % ('도형', 30, 55.55))

## 중간세대 문자열 포맷팅
## {0:>10s} : 오른쪽정렬, 10칸, 문자열 == %10s
intro = '나는 {0:>10s}이고, {1}살입니다. 몸무게 {2}kg입니다.'
print(intro.format('권도형', 31, 56.5))

## 신세대 문자열 포맷팅
name = '도혛'
age = 29
weight = 60.6
print(f'나는 {name:>10s}이고, {age}살입니다. 몸무게 {weight}kg입니다.')

