"""
override test
"""

class Employee (object) :
    def __init__(self, name):
        self.name = name
    def greet (self, other) :
        print("hello, %s" %other.name)


class CEO(Employee) :
    def greet(self, other):
        print("Get back to work, $s!" %other.name)

emp = Employee("lee")
ceo = CEO('leina')

emp.greet(ceo)
ceo.greet(emp)


