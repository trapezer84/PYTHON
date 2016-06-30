my_list = [0,1,2,3,4,5,6,7,8,9,10]

for item in my_list:
    print(item, end=" ")

print()
# range는 가장 뒤에 있는 것이 표함되지 않습니다.
for item in range(0, 11) :
    print(item, end=" ")

print('\n')
# for문을 돌릴때 변수명을 직관적으로 하면 더 좋다
favorite_hobby = ['reading', 'fishing', 'shopping']
for hobby in favorite_hobby :
    print('%s is my favorite hobby' %hobby)

print()

# 키 값과 value를 동시에 다룰 수 있다
wish_travel_city = { 'bangkok' : 'Thai' ,
                     'Las Vegas' : 'USA' ,
                     'Manila' : 'philiphines'}

#키 값과 벨류
for city, country in wish_travel_city.items() :
    print('%s in %s' %(city, country))
# 키 값만
for key in wish_travel_city.keys() :
    print(key)
#벨류 값만
for value in wish_travel_city.values() :
    print(value)

