## 250123 Today I learned
# CSV 파일 읽기/쓰기

import csv

with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # 헤더 스킵
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        # print(c)
        # print(type(c))
        print('-'.join(c))


with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter = '|')

    for c in reader:
        print(c)


with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    
    for c in reader:
        # print(c)
        for k,v in c.items():
            print(k, v)
        print('-----------------')

w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]

with open('./resource/write1.csv', 'w', encoding='UTF-8') as f:
    print(dir(csv))
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)


with open('./resource/write2.csv', 'w', encoding='UTF-8') as f:
    fields = ['One', 'Two', 'Three']

    wt = csv.DictWriter(f, fieldnames=fields)
    wt.writeheader()

    for v in w:
        wt.writerow({'One': v[0], 'Two': v[1], 'Three': v[2]})