# py03_module.py

# 모듈 - 레고
# 모듈 사용 방법
# import 모듈명
# from 모듈명 import 상세파일명...
import py02_car

hisCar = py02_car.Car('기아차', '스팅어', '몰라')
print(hisCar)

import py02_car as c

herCar = c.Car('페라리', 'GT911', '123가1211')
print(herCar)

from py02_car import Car

thatCar = Car('람보르기니', '이름모름', '111가1111')
print(thatCar)