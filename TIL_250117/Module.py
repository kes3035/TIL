## 2025.01.17 Today I learned
# 파이썬에서의 모듈
# Module : 함수, 변수, 클래스등 구성요소들을 모아놓은 파일

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def devide(x, y):
    return x/y

def power(x, y):
    return x ** y


# print('called! inner!')

# print(add(5,5))
# print(subtract(15,5))
# print(multiply(5,5))
# print(devide(20,5))
# print(power(2,5))


# main 예약어를 통해 모듈 내부의 테스트 함수 실행 막기

if __name__ == "__main__":
    print('called! __main__!')

    print(add(5,5))
    print(subtract(15,5))
    print(multiply(5,5))
    print(devide(20,5))
    print(power(2,5))
