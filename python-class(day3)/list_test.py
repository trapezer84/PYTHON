"""

리스트

"""
colors = ["red", "blue", "gold"]
print(colors)
print(colors[0])

#새로운 리스트가 생성되는 것과 같다
print(colors[0:2])

#추가해 넣음
print('\nappend 예제')
colors.append('green')
print(colors)

#중간에 끼워 넣음 : insert (인덱스 자리, 넣을 값) 인덱스 자리에 들어가게 된다.
print('\ninsert 예제')
print(colors)
colors.insert(1, 'yellow')
print(colors)

#update
print('\n업데이트')
print(colors[2])
colors[2] = 'sky blue'
print(colors[2])

#extends 와 += 의 함수는 같다
print('\nextends 실습')
colors.extend(['white', 'gray'])
print(colors)

colors += ['red']
colors += "red"
print(colors)

#del 로 삭제할 수 있다. 인덱스를 이용해서 삭제
print('\ndel 삭제 : 인덱스를 이용한 삭제')
print(colors)
del colors[0]
print(colors)

#remove 는 값으로 삭제 할 수 있다. 동일한 컨텐츠 확인시 삭제
print('\nremove 삭제 : value를 이용한 삭제')
print(colors)
colors.remove('gray')
print(colors)

print('\nremove 삭제 : 중복 또한 가능할까? NO 가장 처음 만난 값만 삭제됨')
print(colors)
colors.append('yellow')
colors.append('yellow')
print(colors)
colors.remove('yellow')
print(colors)

#pop : read와 다른 점은 읽으면서 삭제를 한다는 점이다.
print('\npop 실행')
print(colors)
colors.pop()
print(colors)

#sort
print('\nsort 실행')
print(colors)
colors.sort()
print(colors)

#reverse 를 제공해준다.
print('\nreverse 실행')
print(colors)
colors.reverse()
print(colors)

#create subset
print('\ncreste subset')
print(colors)
colors = colors[-3:]
print(colors)