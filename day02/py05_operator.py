# py05_operator.py
# 연산자

# 사칙연산 : + - * /
a = 15
b = 14
# Shift + Del 는 한줄 삭제(매우 효율적!)
print(a + b)
print(a - b)
print(a * b)

# 나누기 연산자 /, //, %
a = 14
b = 4
print(a / b)    # 나눈 결과, float
print(a // b)   # 나눈 몫, int
print(a % b)    # 나머지, int

current = '2025-02-04'
print(current.split('-'))

str_A = ''
str_A = 'TISTESTSTRINGT'
result = str_A.split('T')
print(result)
str_A = 'TEST'  # '' ' ' 
result = str_A.split('T')
print(result)

# 거듭제곱(Power)
print(2 ** 10)
print(pow(2,10))

# 연산자 우선순위
## 계산식이 복잡해서 연산자 우선순위를 잘 모르겠으면 () 사용
print((3 + 4) * 7)
print(3 + (4 * 7))

## 리스트 연산
## last index = len(list) - 1
listSample = [1,3,5,7,9]
print(listSample[0])
print(listSample[1])
print(listSample[2])
print(listSample[3])
print(listSample[4])

listSample[4] = 11

print(len(listSample)) # 리스트의 길이
print(listSample[len(listSample) - 1])

# 문자열 연산 : +, * 만 존재
greeting = 'Hello'
target = 'World'
print(greeting, target) # 문자열 연산 X
print(greeting + ' ' +target) # 문자열 연산 + string concatenate
print(f'{greeting} {target}')
print(f'{greeting}{target}')
print('{0} {1}'.format(greeting, target))
print('{0}{1}'.format(greeting, target))

print((greeting + target + ' ') * 5) # 해당 문자열을 * 수로 반복

## 문자열(Charactor Array) : List와 유사하지만 값 수정 불가
print(greeting[1]) # 리스트 연산
#greeting[0] = 'C'  # 
print(greeting)

## 리스트 연산, 슬라이싱
listSample = ['2', '0', '2', '5', '-', '0', '2', '-', '0', '4']
current = '2025-02-04'

print('listSample :', listSample,'\n','current :', current, sep='')

for i in listSample:
    print(i, end='')
print()

print(current)
# 준비 끝

# 인덱싱, 인덱스에 있는 값을 가져오기
print(listSample[-1]) # 역순으로 -1, -2, ...
print(current[9]) 

# 슬라이싱, 리스트를 자르기
## [start:end] : end값 -1까지만 추출
print(listSample[0:3 + 1])
print(current[0:3 + 1])

# 2025-02-04
year = current[0:3 + 1]
month = current[5:6 +1]
day = current[8:] # end 끝까지는 숫자 생략
print(year, month, day)
print(current[-2:])

## 문자열 연산 중 함수를 사용
# fullNameString 카멜(낙타 등 모양)
# 자르기
full_name = "Do hyeong. Kwon" # 스네이크
print(full_name.split())
print(full_name.split(' '))
print(full_name.split(sep=' '))

names = full_name.split(' ')
print(type(names),'\n', names, sep='')

names = full_name.split('.')
print(type(names),'\n', names, sep='')

# 바꾸기
print(full_name.replace('hyeong','Ryeong'))

# 공백제거
origin = '     Hello  ~     '
print(f'//{origin}//')
print(f'//{origin.strip()}//')
print(f'//{origin.lstrip()}//')
print(f'//{origin.rstrip()}//')

# 단어찾기
print(full_name.find('h'))
print(full_name.find('H')) # -1 : h를 찾을 수 없음!

print(full_name.count('o')) # o가 문장에 몇번 존재
print(full_name.index('h')) # index에 찾는 문자 없을 시 오류 발생, find로 찾은 후 진행
print(full_name.upper())    # 모든 글자 대문자
print(full_name.lower())    # 모든 글자 소문자

## T로 자를 때
# '' == Empty(비어있다) <-> None과 다름
# ' ' == Space(공백존재)
origin = 'ITESTSTRING'
print(origin.split('T'))
origin = 'TESTSTRING'
print(origin.split('T'))

