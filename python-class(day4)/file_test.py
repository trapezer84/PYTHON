# open 함수는 내장 함수라 import 필요 없음
"""
f = open("list_sample.txt", "r")
print("f 타입")
print(type(f))
print("-----------------")

line = f.readline()
print("line 타입")
print(type(line))
print(line)

line2 = f.readline()
print(line2)

print("-----------------")
lines = f.readlines()
print("readlines lines 타입")
print(type(lines))
print(lines)

print("-----------------")
print("for문 돌려서 알기")
for line in lines :
    print(line, end= " ")

print()
print("-----------------")
print("while문 돌려서 알기")
while True :
    line = f.readline()
    if not line : break
    print(line, end=" ")


try :
    f = open("list_sample.txt", "r")
except FileNotFoundError :
    print("file not found")
else:
    while True :
        line = f.readline()
        if not line : break
        print(line)
finally:
    f.close()
"""

with open("list_sample.txt", "r", encoding="UTF-8") as f :
    f.readlines()


my_file = open("test.txt", "a")
my_file.write("hello world!")
my_file.close()

