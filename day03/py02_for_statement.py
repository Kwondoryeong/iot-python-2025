# py02_for_statement.py

# for문 : 프로그래밍의 꽃
# 반복을 처리할 때 사용
# for 변수 in 반복할 값:
#   구문안으로

# 아래와 출력되는 프로그램을 작성하시오
'''
*
**
***
****
'''

# range() 범위 생성 클래스
# 마지막 수 : max - 1
# print(range(8)) -> range(0, 8)
# print(range(0,8))

# for i in [0,1,2,3,4,5,6,7]: # 이 조건이 참인동안 반복...
# for i in range(0,8):
#     print(i)
# range(init, max, addition)
# for i in range(0,8,2):
#     print(i)

i = 0
j = 0


# num = int(input('최대 별 갯수를 입력하세요 > '))
# num += 1
# for i in range(1,num):
#     print('*' * i, end='\n')

# for i in range(num):
#     for j in range(num):
#         if(j <= i):
#             print('*',end='')
#         else:
#             print()
#             break

# for i in range(1,num):
#     if(i <= num):
#         print('*' * i)
#     else:
#         print()

# 구구단
# 2단부터 2x9 ~ 9x9
# 요구사항1 - 한줄에 각 단씩 나오도록
# 요구사항2 - x*y값이 항상 두줄 씩 표현되도록
# 단 시작을 표시
for i in range(2,10):
    # if i == 5: break
    # if i == 5: continue
    print(f'{i}단 시작')
    for j in range(1,10):
        print(f'{i} x {j} = {i * j:>2d}', end='   ')
    print() # 그냥 한줄 내리기
print('구구단 종료')

## 반복문을 빠져나올때 : break
## 반복문에서 특정 조건을 지나칠 때 : continue