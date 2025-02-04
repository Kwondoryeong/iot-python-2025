# py02_datastruct.py
# 복합자료형
# 자료구조 및 알고리즘

# 리스트
a = 1
b = 2
c = 3
d = 4
e = 5

sum = a + b + c + d + e
print(sum)

# 리스트(배열) [] - 다른언어에선 리스트와 배열은 다름(파이썬에서 같음)
list_A = [1,2,3,4,5]
print(list_A[0])
print(type(list_A))

list_A = ['Life', 'is', True, 0, None, [1,2,3]]
print(list_A)
print(list_A[0], list_A[5][0])

# 리스트의 한 요소에도 값을 할당 가능
list_A[3] = 100
print(list_A)

## 튜플 ()
# 리스트와 거의 흡사. 값을 변경할 수 없음
tp = (1,2,3,4)
print('값 : ',tp,', 타입 : ',type(tp),sep='')
# tp[0] = 4 # 주석토글 Ctrl + / 사용
print(tp[3])

## 딕셔너리(사전형) {key : value} 의 집합, 데이터베이스와 가장 근접한 자료형
spiderman = { 'name' : 'Peter Parker', 'age': 20, 'weapon' : 'Web Shooter' }
print('값 : ',spiderman,', 타입 : ',type(spiderman),sep='')
print(spiderman['weapon'])
spiderman['age'] = 21
print(spiderman)

## 집합(set) (), {}, [] 사용 가능 - ([v1,v2]), 수학의 집합과 동일, 중복제거, 리스트와 다르게 인덱스 없음
st = set([1,3,5,7,5,3,1])
print('값 : ',st,', 타입 : ',type(st),sep='')

st = set('Hello World')
print('값 : ',st,', 타입 : ',type(st),sep='') # 순서없음, 공백도 값

## 변수명 지정 방식
## 의미있는 단어들의 조합으로 만들것
PhoneNumber = '010-1234-1234'
SalaryBankAccount = '111-12-333456'

sam = ''
sam1 = ''
#samsung = '' # 숫자로 변수명 시작불가
_samsung = ''
samsung_ = ''
# samsung! = '' # _이외 특수문자 사용불가
sam_1 = ''
# samsung - apple = '' # 파이썬 연산자는 사용불가
