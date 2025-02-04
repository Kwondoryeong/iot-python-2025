# 변수와 자료형
# 변수는 => 변하는 수(Variable) <-> 상수(Constant)
# Pi = 3.141592...

# 변수
varA = None # 특수형, None타입
print('값 : ',varA,', 타입 : ',type(varA),sep='') # a라는 변수에 무슨 값이 들어있는지 콘솔에 출력


varA = 10 # 정수(소수점 없는 수), Integer
print('값 : ',varA,', 타입 : ',type(varA),sep='') # 함수는 늘 괄호를 같이 사용

varA = 12.34 # 실수(소수점 아래 수까지 표현), Float
print('값 : ',varA,', 타입 : ',type(varA),sep='')

varA = 0b11111110 # 2진수(0과 1로 수를 표현), Binary
print('값 : ',varA,', 타입 : ',type(varA),sep='')

varA = 0xfe # 16진수(0~9,A[10]~F[15]로 표현), Hex
print('값 : ',varA,', 타입 : ',type(varA),sep='')

varA = 1_900_000_000 # 천단위마다 쉼표와 같이 표현
print('값 : ',varA,', 타입 : ',type(varA),sep='')

varA = "Life is short, You need Python!" # 문자열, String
print('값 : ',varA,', 타입 : ',type(varA),sep='')

varA = 'Life is short, You need Python!' # 문자열
print('값 : ',varA,', 타입 : ',type(varA),sep='')

varA = (3 > 1) # 불형 True | False, Boolean - 논리형 변수
print('값 : ',varA,', 타입 : ',type(varA),sep='')







