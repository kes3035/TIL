## 2025.01.17 Today I learned
# 파이썬에서의 패키지
# 작성 및 사용법
# 상대경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서 사용

# 패키지 속 모듈 가져오기
import sub.sub1.module1
import sub.sub2.module2

# 가져온 모듈 사용하기
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()



# 패키지 경로가 길어지면 비효율적이기에 아래와 같은 방법도 가능
from sub.sub1 import module1
from sub.sub2 import module2 as md2

module1.mod1_test1()
module1.mod1_test2()

md2.mod2_test1()
md2.mod2_test2()

# 패키지 전체를 가져올 수 있음
from sub.sub1 import *
from sub.sub2 import *


module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()