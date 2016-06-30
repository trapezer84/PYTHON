def shut_down(s) :
    if s == 'yes' :
        return "Shutting down"
    elif s == "no" :
        return "Shutdown aborted"
    else :
        return "Sorry"

"""

모듈을 사용해 봅시다

"""
from trip_util import rental_car_cost

print(rental_car_cost(5, 35))
print(rental_car_cost(5, fee_a_day=35))

"""

시간을 출력할 수 있는 함수

"""
import datetime

print(datetime.time())


