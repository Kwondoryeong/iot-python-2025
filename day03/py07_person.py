# py07_person.py

class Person:
    # 명사(속성)인 멤버변수
    name = '도형'
    age = 30
    weight = 55.5
    gender = 'male'

    # 초기화 메서드(파이썬 기본으로 포함)
    def __init__(self, name, age, weight, gender): # __메서드__
        self.name = name # 매개변수로 받은 값 사용
        self.age = age
        self.weight = weight
        self.gender = gender
        pass # 생성하면서 초기화, 멤버 함수들은 self있어야함
    
    def __str__(self): # 객체 출력을 문자열 포맷팅!
        retStr = (f'{self.name}\n{self.age}\n{self.weight}\n{self.gender}')
        return retStr
    

    # 동사(기상)인 멤버함수(메서드 - 클래스에 속해 있는 함수)
    def getup(self): # myself(person 자신)
        print(f'{self.name}(이)가 일어납니다')
    
    def setWeight(self, weight): # 객체 출력을 문자열 포맷팅!
        print(f'{self.name}의 몸무게가 변경됩니다.')
        print(f'현재 몸무게 : {self.weight}kg')
        self.weight = weight
        print(f'변경 후 몸무게 : {self.weight}kg')
      
    def getGender(self):
        return self.gender
man = Person('권도형', 30, 66.6, 'man') # __init__() 특수함수를 실행
man.getup()
man.setWeight(56.7)

print(f'{man.name}의 성별은 {man.getGender()}입니다.')
print('----------------------------')
print('객체 정보')
print(man)