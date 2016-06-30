"""
과제 1
"""

inventory = {
    'gold' : 500 ,
    'pouch' : ['flint', 'twine', 'gemstone'] ,
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

inventory['pouch'].sort()
print(inventory['pouch'])


print('\n pocket이라는 키를 만든다')
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['pocket'].sort()
print("sort 된 것 " + str( inventory['pocket'] ))
inventory['pocket'].reverse()
print("reverse 된 것 " + str( inventory['pocket'] ))


print('\n backpack 키의 리스트 중 dagger를 제거한다')
print(inventory['backpack'])
inventory['backpack'].remove('dagger')
print(inventory['backpack'])

inventory['gold'] += 50

print(inventory)

"""
과제 2
"""
sales_amount = {
    "11/05" : 353500 ,
    "11/06" : 460000 ,
    "11/07" : 545000 ,
    "11/08" : 450000 ,
    "11/09" : 347000 ,
    "11/10" : 254000 ,
    "11/11" : 564500
}

# 컬럼이 3개가 넘어갈 때, 리스트로 만든다. 리스트로 큰 틀을 만든다는 것은 전체를 for loop를 이용할 수 있다는 장점을 가진다.
sales_amount = [
    {
        "date" : "11/05" ,
        "amount" : 353500
    } ,
    {
        "date": "11/06",
        "amount": 460000
    },
    {
        "date": "11/07",
        "amount": 545000
    },
    {
        "date": "11/08",
        "amount": 450000
    },
    {
        "date": "11/09",
        "amount": 347000
    },
    {
        "date": "11/10",
        "amount": 254000
    },
    {
        "date": "11/11",
        "amount": 564500
    }

]

print(min(sales_amount))
print(max(sales_amount))
print(sales_amount["11/07"])

