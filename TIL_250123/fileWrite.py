## 250123 Today I Learned

# 읽기 모드 : r
# 쓰기 모드 : w
# 추가 모드 : a

# 상대경로('../, ./'), 절대 경로('User/...')

# 1. 읽기
f = open('./resource/it_news.txt', 'r', encoding = 'UTF-8')
print(dir(f))
print(f.encoding)
print(f.name)
print(f.mode)
cts = f.read()
print(cts)

f.close()


# with문
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    #print(list(c))
print()

# read() : 전체 읽기, read(10) : 10Byte
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    c = f.read(10)
    print(c)
    c = f.read(10)
    print(c)
    c = f.read(10)
    print(c)
    c = f.read(10)
    print(c)
    f.seek(0, 0)
    print(c)
    #print(list(c))
print()


# readline : 한 줄씩 읽기
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    line = f.readline()
    print(line)
print()


# readlines : 전체를 읽은 후 라인 단위로 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for c in cts:
        print(c, end='')
print()


# 2. 파일 쓰기

with open('./resource/contents1.txt', 'w') as f:
    f.write('I love Python\n')

with open('./resource/contents1.txt', 'a') as f:
    f.write('I love Python2\n')

with open('./resource/contents2.txt', 'w') as f:
    list = ['Kim\n', 'Eun\n', 'Sang\n']
    f.writelines(list)

