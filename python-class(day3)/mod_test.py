""" 함수 사용의 예시2 """

def cube(number) :
    if type(number) == int:
        return number ** 3
    elif type(number) == str:
        return False
    else:
        return 0

def by_three(number) :
    if (number%3 == 0) :
        return cube(number)
    elif type(number) == str:
        return False
    else :
        return False

print(by_three(90))


"""함수 리뷰 문제"""

def shut_down(s) :
    if s == 'yes' :
        return "Shutting down"
    elif s == "no" :
        return "Shutdown aborted"
    else :
        return "Sorry"


import math
print(math.sqrt(100))

from math import sqrt
print(sqrt(100))


""" 내장 함수 예시 문제"""
def distance_from_zero (my_build_in) :
    if type(my_build_in) == int or type(my_build_in) == float :
        return abs(my_build_in)
    else:
        return "Nope"


print(distance_from_zero(-100.2929))
print(distance_from_zero('abc'))

""" 기본 파라미터 """
def times(a = 10, b = 20) :
    return a * b

x = times()
y = times(5)
z = times(5, 10)

print(x)
print(y)
print(z)

print("hello", "world", sep=" ,")
print("hello", "world", sep=" ,", end="!!")
print("hello", "world", sep=" ,")
print("hello", "world", sep=" ,", end="")
print("hello", "world", sep=" ,")


def connect_URI (server, port) :
    str = "http://" + server + ":" + port
    return str

connect_URI("test.com", "8080")
connect_URI(port="8080", server="test.com")

connect_URI("test.com", port="8080")


g = lambda x, y : x * y
g(2,3)

a = (lambda  x : x* y)(3)
globals()

