# 131
import math

과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)

# 132
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print('####')

# 133
for 변수 in ["A", "B", "C"]:
    print(변수)

# 134
for item in ["A", "B", "C"]:
    print("출력: ", item)

# 135
for 변수 in ["A", "B", "C"]:
    b = 변수.lower()
    print("변환:", b)

# 136
for i in range(10, 31, 10):
    print(i)


for i in [10, 20, 30]:
    print(i, end="\n------\n")


# 141


# 151
for i in [3, -20, -3, 44]:
      i < 0 and print(i)


# 152
리스트 = [3, 100, 23, 44]
for i in 리스트:
    i % 3 or print(i)

# 153
print("153---")
for i in [13, 21, 12, 14, 30, 18]:
    i < 20 and not(i % 3) and print(i)


# 154
for i in ["I", "study", "python", "language", "!"]:
    len(i) >= 3 and print(i)

# 155
for i in ["A", "b", "c", "D"]:
    i.isupper() and print(i)


# 156
for i in ["A", "b", "c", "D"]:
    not i.isupper() and print(i)

# 157
for i in ['dog', 'cat', 'parrot']:
    print(i.capitalize())


# 158
for i in ['hello.py', 'ex01.py', 'intro.hwp']:
    print(i.split('.')[0])

# 159
for i in ['intra.h', 'intra.c', 'define.h', 'run.py']:
    i.split('.')[-1] == 'h' and print(i)

# 160
for i in ['intra.h', 'intra.c', 'define.h', 'run.py']:
    확장자 = i.split('.')[-1]
    if (확장자 == 'h'):
        print(i)
    if (확장자 == 'c'):
        print(i)

print("161---")


print("162---")
for year in range(2002, 2051, 4):
    print(year)

print("163---")
for i in range(3, 30 + 1, 3):
    print(i)

print("164---")
for i in range(99, 0 - 1, -1):
    print(i)

print("165---")
for i in range(10):
    print(i / 10)

print("168---")
print(sum(range(1, 10 + 1)))

print("169---")
print(sum(range(1, 10 + 1, 2)))

print("170---")
print(math.prod(range(1, 11)))