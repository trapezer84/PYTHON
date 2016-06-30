"""연습문제"""
plane_pay = 953200
adult = plane_pay
child = adult * 0.9
result_plane = (adult * 3) + (child * 1)

hotel_pay_without = 125 + 45 + ((125+45) * 5.5 / 100)
hotel_pay = hotel_pay_without + (hotel_pay_without * 0.47)

dinner_pay = 135.52 + (135.52 * 6.75) + (135.52 * 15)

parking_pay = 2.50 + (12 * 1.25)

print(result_plane)
print(hotel_pay * 5)
print(dinner_pay * 1147)
print(parking_pay * 1147)