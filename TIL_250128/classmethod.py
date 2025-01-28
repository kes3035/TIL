## 250128 Today I Learned

class Car():
    """
    Car class
    Author: Elyot
    Date: 2025.01.28
    """

    #Class Variable == Static variable in swift?
    carCount = 0

    def __init__(self, brand, details):
        self.brand = brand
        self.details = details # 인스턴스 변수는 _를 앞에 붙이고, 클래스 변수는 안붙이는 관행이 있긴 함
        Car.carCount += 1

    def __str__(self):
        return '__str__ : brand-{}, details-{}'.format(self.brand, self.details)
    
    def __repr__(self):
        return '__repr__ : brand-{}, details-{}'.format(self.brand, self.details)

    def detailInfo(self):
        print('its ID : {}'.format(id(self)))
        print('Car detail information : {} {}'.format(self.brand, self.details.get('cost')))

    def __del__(self):
        Car.carCount -= 1

porche = Car('Porche', {'cost' : 16000, 'hp' : 320, 'torque' : 50})
ferrari = Car('Ferrari', {'cost' : 36000, 'hp' : 1000, 'torque' : 120})
mercedes = Car('Mercedes', {'cost' : 12000, 'hp' : 270, 'torque' : 30})

print(id(porche))
print(id(ferrari))
print(id(mercedes))

print(porche.brand == mercedes.brand)
print(porche is ferrari)

print(dir(porche)) # 해당 object가 가진 메서드를 리스트로 표현
print(dir(mercedes))

print(porche.__dict__) # 불필요한 메서드는 보여주지 않고, 내용물만 dict 형태로
print(ferrari.__dict__)

# Doctring?
print(ferrari.__doc__)

porche.detailInfo()

print(porche.__class__, ferrari.__class__)
print(id(porche.__class__), id(ferrari.__class__))


# Error Situation
#Car.detailInfo()
# self가 없으니 에러가 날 수밖에..
Car.detailInfo(porche)

