"""
error test
"""

def divide (a, b) :
        return a / b

try :
    result = divide(3, "a")
except ZeroDivisionError :
    #예외 처리 코드
    print("0으로 나누면 안됩니다!")
except TypeError :
    #예외 처리 코드
    print("number only!")
except :
    print("알수없는 에러가 발생!")
else :
    print(result)
finally:
    print("수고하셨습니다!")

