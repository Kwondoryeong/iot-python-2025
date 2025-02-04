# py03_inout.py
# 화면입출력

print('출력입니다.')

# # 기본입력
# number = input('만 나이를 입력하세요 > ') # 입력방법 
# # input 입력값, 출력값 모두 문자열!
# print('타입 :',type(number), sep='')
# number = int(number)
# print('타입 :',type(number), sep='')
# print('현재 나이는 ', number + 1, '세 입니다.', sep='') # 여러값을 같이 출력하려면 ,로 구분

x, y = (input('합산할 두 수를 입력하세요 > ')).split() # split() 기본 - 공백으로 자르기기
sum = int(x) + int(y)
print('타입 : ', type(sum), ', sum값 : ', sum, sep='')