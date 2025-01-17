## 2025.01.17 Today I learned
# 파이썬에서의 클래스

# 파이썬에서의 클래스도 큰 틀에서 보면 Swift처럼 객체를 찍어내는 틀

class Menu: # 기본적으로 object를 상속
    # 클래스 속성
    name = 'americano'


    # 초기화/인스턴스 속성
    def __init__(self, name, count):
        self.name = name
        self.count = count


# print(Menu)


# 인스턴스(instance)화? == 변수에 할당

myMenu1 = Menu('latte', 1)
myMenu2 = Menu('americano', 2)
myMenu3 = Menu('latte', 1)

# print(myMenu1 == myMenu2, id(myMenu1), id(myMenu2), id(myMenu3))

print('-------')

# 네임스페이스? == 해당 클래스가 가진 프로퍼티들 확인하기
# print('Menu1', myMenu1.__dict__)
# print('Menu2', myMenu2.__dict__)

# 인스턴스의 속성 확인하기

print('---------')

# print('{} is {} and {} is {}'.format(myMenu1.name, myMenu1.count, myMenu2.name, myMenu2.count))


# self란?

class SelfTest:
    def funcionTest1():
        print('Function1 called')
    def functionTest2(self):
        print('Function2 called')

    ## __init__이 없어도 내부적으로 자체 생성.
    ## 약간 swift의 Struct 같은 느낌

test = SelfTest()

# print(test.funcionTest1())
# TypeError: SelfTest.funcionTest1() takes 0 positional arguments but 1 was given
test.functionTest2()

 # 클래스 내부 함수를 선언할 때 self가 없다? == 클래스 메소드
 # 클래스 내부 함수를 선언할 때 self가 있다? == 인스턴스 메소드
SelfTest.funcionTest1()

class Student:
    # 클래스 변수 (Swift의 static과 비슷한 느낌)
    count = 0

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Student.count += 1

    def __del__(self):
        Student.count -= 1


student1 = Student('Park')
student2 = Student('Kim')

# print(Student.count)


del student2
# print(Student.count)

print('-----------------')

class Car:
    brand = 'hyundai'

    def __init__(self, name, vehicleType):
        self.name = name
        self.vehicleType = vehicleType

    def info(self):
        return '{} is {} car.'.format(self.name, self.vehicleType)
    

    def blowHorn(self):
        return '{} is blowing the horn.'.format(self.name)


genesis = Car('gv70', 'SUV')

# print(genesis.info())

# print(genesis.blowHorn())

