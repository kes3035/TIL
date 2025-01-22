## 250122 Today I Learned

# sys, pickle, shutil, temfile, time, random

import sys
print(sys.argv)

# 강제종료 
# sys.exit()

# 패키지 위치
print(sys.path)

# 객체 파일 쓰기 == pickle
import pickle

# 쓰기
f = open("text.ipt", 'wb')
ipt = {1: 'python', 2:'study', 3:'basic'}
pickle.dump(ipt, f)
f.close()

# 읽기

f = open('text.ipt', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()

# os : 환경변수, 디렉토리 처리 관련, 운영체제 작업 등
# mkdir, rmdir

import os
print(os.environ)
print(os.environ["USERNAME"])

print(os.getcwd())

# 시간 관련 처리 == time
import time
print(time.time())

print(time.localtime(time.time()))

print(time.ctime())

print(time.strftime('%Y-%m-%d %H:%M:$S', time.localtime(time.time())))

for i in range(5):
    print(i)
    time.sleep(1)


# 난수 == random
import random

print(random.random())

print(random.randint(1, 45))
print(random.randrange(1, 45))

ran = [1, 2, 3, 4, 5]
random.shuffle(ran)
print(ran)

c = random.choice(ran)
print(c)

# webbrowser == 웹 브라우저 실행

import webbrowser

webbrowser.open("https://google.com")

webbrowser.open_new("https://naver.com")
