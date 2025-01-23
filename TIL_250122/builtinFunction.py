## 250122 Today I learned

# 외울 필요 없음

# 절대값 == abs()
# iterable요소 검사 == all()

# 아스키 -> 문자 == chr
# 문자 -> 아스키 == ord

print(chr(67))
print(ord('C'))

# 인덱스 + iterable객체 생성 == enumerate

for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)

# 반복가능한 객체 요솔ㄹ 지정한 함수 조건에 맞는 값 추출 == fiter

def convert_position(x):
    return abs(x) > 2

print(list(filter(convert_position, [1, -3, 2, 0, -5, 6])))

print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6])))

# 객체의 주소값 반환 == id
print(id(int(5)))
print(id("3"))

# 요소의 길이 == len
print(len([1, 3, 2, 1, 4]))

# 최댓값, 최솟값 == max, min


# 반복가능한 객체 요소를 지정한 함수 실행 후 추출 == map

def convert_abs(x):
    return abs(x)

print(list(map(convert_abs, [1, -3, 2, 0, -5, 6])))
print(list(map(lambda x: abs(x), [1, -3, 2, 0, -5, 6])))

# 제곱 == pow
print(pow(2, 10))

# 반복가능한 객체 반환 == range
print(list(range(1, 10, 2)))

# 반올림 == round
print(round( 6.5781, 2))
print(round(5.1))

# 정렬 == sort
print(sorted([0, 1, -2 , 3, 6]))




