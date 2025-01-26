## 250126 Today I Learned

# 클래스 기반 개발 설명
# 절차 지향과 객체 지향


class Car():

    def __init__(self, brand, details):
        self.brand = brand
        self.details = details

    def __str__(self):
        return '__str__ : brand-{}, details-{}'.format(self.brand, self.details)
    
    def __repr__(self):
        return '__repr__ : brand-{}, details-{}'.format(self.brand, self.details)
    

porche = Car('Porche', {'cost' : 16000, 'hp' : 320, 'torque' : 50})
ferrari = Car('Ferrari', {'cost' : 36000, 'hp' : 1000, 'torque' : 120})
mercedes = Car('Mercedes', {'cost' : 12000, 'hp' : 270, 'torque' : 30})


print(porche)

# __str__ 메서드와 __repr__ 메서드 두개 다 있으면 str우선적으로
# __str__ 은 디버깅으로 확인할 때, __repr__ 은 개발자 단에서 사용할 때

print(ferrari.__dict__)