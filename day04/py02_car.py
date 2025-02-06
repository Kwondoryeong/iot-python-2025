# py02_car.py

# 객체지향 다시
# str(), int() ... 클래스로 되어있음
class Car():
    ## __new__ 사용빈도X, __init__ 많이 사용
    ## 내부적으로 __new__ 자동실행 후 __init__ Car()로 초기화
    ## Car() 호출하면 아래의 메서드가 실행
    # Company, name, plateNumber 모를때 None(값모름)
    def __init__(self, company=None, name=None, plateNumber=None):    
        self.__company = company    # 멤버변수이름 앞에 __ 쓰면 외부접근 불가
        self.__name = name
        self.__plateNumber = plateNumber
        print('Car 클래스를 새로 생성!!')
    
    # print(myCar)시 클래스 자체가 출력되는데, __str__ 문자열로 출력되도록 바꿔줌
    def __str__(self):
        return f'제차는 {self.__name}이고, 차번호는 {self.__plateNumber}입니다.'
    
    # 외부에서 잘못된 차번호 넣을 시 변경X, 문자열인 경우만 차번호 변경
    def setPlateNumber(self, newPlateNumber):
        if type(newPlateNumber) is str:
            self.__plateNumber = newPlateNumber

    def setName(self, newName='글쎄요'): # 이름을 모를 때 '글쎄요'로 대체
        self.__name = newName

    def getName(self):
        return self.__name


    def setCarPlateNum(self):            
        print(f'변경 전 차번호는 {self.__plateNumber}입니다.')
        plateNumber = input(f'변경할 차번호를 입력하세요 > ')
        self.__plateNumber = plateNumber
        print(f'변경 후 차번호는 {self.__plateNumber}입니다.')

    def getCarInfo(self):
        print(f'myCarInfo [제조사] : {self.__company} [차량명] : {self.__name} [차번호] : {self.__plateNumber}')
    
    def setCarInfo(self):
        print(f'변경 전 [제조사] : {self.__company} [차량명] : {self.__name} [차번호]] : {self.__plateNumber}')
        company, name, plateNumber = input(f'회사명, 차량명, 번호판 순(,구분) > ').split(',')
        self.__company = company
        self.__name = name
        self.__plateNumber = plateNumber
        print(f'변경 후 [제조사] : {self.__company} [차량명] : {self.__name} [차번호] : {self.__plateNumber}')
        
# 모듈화 하려면 예제소스는 없어야 함
# myCar = Car('kia','k8','6367') # __init__ 특수함수

# myCar = Car(name='아이오닉', plateNumber='12가1234', company='현대차') # 파라미터명=값 으로 매개변수 순서를 변경가능
# print(myCar) # 차의 번호를 출력하고 싶음
# myCar.__plateNumber = 2018 # 클래스 외부에서 잘못된 데이터를 넣어도 문제가 발생X self.__
# print(myCar)
# myCar.setPlateNumber('3333')
# print(myCar)

# yourCar = Car()
# print(yourCar)

# yourCar.setName('제네시스')
# print(yourCar)
# yourCar.setPlateNumber('1233')
# print(yourCar)
# yourCar.getName()


# myCar.setCarPlateNumber()
# myCar.setCarInfo()
# myCar.getCarInfo()


        