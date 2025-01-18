## 250118 Today I learned
# Python exception
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError,...
# 문법적으로는 괜찮아도 실제 디버깅에서 오류가 발생할 수 있음
# 따라서 반드시 예외처리를 해야함 (로그를 남기는 것이 매우 중요)
# 예외는 Throw됨, 무시도 가능(좋은 방법은 아님)

# SyntaxError  : 문법이 잘못되었을 때
# NameError    : 참조 없음
# ZeroDivisionError : 0으로 나누었을 때
# IndexError   : 배열에 존재하지 않는 인덱스로 접근할 때
# KeyError      : 딕셔너리에서 키에 맞는 밸류가 없을 때
# AttributeError: 모듈이나 클래스에 있는 잘못된 속성을 사용할 때
# ValueError    : 참조없음 (시퀀스형 자료구조 내부에서 자료를 찾을 때 해당 자료가 존재하지 않으면 나타남)
# FileNotFoundError : 파일을 열 때
# TypeError     : 자료형이 다른 변수끼리의 연산을 할 때

# 예외가 없다고 가정하고 작성 후 예외 발생 시, 예외 처리를 권장
# 계속 예외만 고려할 순 없음

# try  : 에러가 발생할 가능성이 있는 코드일 때
# except 에러명1 :
# except 에러명1 :
# else : try에서 에러가 발생하지 않는 경우 실행
# finally : 항상 실행

name = ['Kim', 'Na', 'Park', 'Lee']

# try:
#     bumsoo = 'Kim'
#     indexOfKim = name.index(bumsoo)
#     print('찾았다! {}'.format(bumsoo))

# except ValueError:
#     print('못찾았다 ㅠㅠ - ValueError 발생')

# else:
#     print('구래')


# try:
#     bumsoo = 'Kim'
#     indexOfKim = name.index(bumsoo)
#     print('찾았다! {}'.format(bumsoo))

# except Exception:
#     print('못찾았다 ㅠㅠ - Error 발생')

# else:
#     print('구래')

try:
    bumsoo = 'Kim'
    indexOfKim = name.index(bumsoo)
    print('찾았다! {}'.format(bumsoo))

except Exception as e:
    print(e)
    print('못찾았다 ㅠㅠ - Error 발생')

else:
    print('구래')

finally:
    print('마침내!')

#raise 키워드로 예외 직접 발생 가능

try:
    a = 'Kim'
    if a == 'Park':
        print('OK! 패쓰~')
    else:
        raise ValueError
except ValueError:
    print('예외발생')

else:
    print('오케이~')