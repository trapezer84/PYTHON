print("Hello World!")

my_name = "lee"
print("hello " + my_name)

my_int = 7
my_float = 1.23
my_bool = False

print(my_int)
print(my_float)

print(my_int + my_float)

print(my_bool)

#싱글라인


""" 따음표 3개는 이를 따로 문서화 해주는 기능이 있다. """
print("사칙연산")

addition = 72 + 45
subtraction = 100 - 40
multiplication = 100 * 4
division = 100 / 3

test = 10.2 + 3

print(addition)
print(subtraction)
print(multiplication)
print(division)
print(test)

print("제곱연산")
eggs = 100 ** 2
print(eggs)

print("모듈러 연산")
spam = 100 % 2
print(spam)


print("연습예제; 파이썬으로 여행경비 계산하기")

one_plane_ticket_fee = 953200
total_plane_ticket_fee = (one_plane_ticket_fee * 3) + (one_plane_ticket_fee * 0.1)

one_day_hotel_fee = 125
one_day_resort_fee = 45
ond_day_total_hotel_fee = one_day_hotel_fee + one_day_resort_fee
total_hotel_fee = ond_day_total_hotel_fee * 5 * 1.055

change_money = 1147
total_change_money = 3000 * change_money * 1.0045

dinner_fee = 135.52
total_dinner_fee = (dinner_fee * 1.0675) + (dinner_fee * 0.15)

parking_time = 200
parking_fee = 1.25
total_parking_fee = 2.50 + ( (parking_time - 30) % 15) * 1.25

print("1. 비행기")
print(total_plane_ticket_fee )
print("2. 호텔")
print(total_hotel_fee)
print("3. 달러 환전")
print(total_change_money )
print("4. 저녁 식사")
print(total_dinner_fee )
print("5. 주차비")
print(total_parking_fee )


print("3.14의 특이함")
my_int = 3.0
my_pie = 3.14
my_float = 3.15

print(my_int + my_pie)
print(  (my_int + my_pie)  )

print(my_int + my_float)


my_string1 = "hello"
my_string2 = 'hello'

print("총 길이")
print(len('hello'))

print("첫문자만 대문자로")
my_string3 = 'hello'.capitalize()
print(my_string3)

print("전체 다 대문자로")
my_string4 = 'hello'.upper()
print(my_string4)

my_string5 = "hello, world!"

print(my_string5[0:5])
print(my_string5[3:7])

print("I have " + str(2) + " apple")


portal_site = 'naver daum'
splited = portal_site.split(' ')[1]

print(splited)

print( type(700) )
print( type(3.14) )
print( type('hello') )
print( type("python") )

from datetime import datetime
print ( datetime.now() )

now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

print(current_year)
print(current_month)
print(current_day)


