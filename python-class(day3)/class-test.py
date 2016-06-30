class Person :
    name = "leina lee"
    gender = "female"
    address = "soul"

    def set_name(self, name):
        self.name = name

    def print(self):
        print("my name is {0}".format(self.name))

class Animal :

    # init : 생성자 , 내부적으로 정해진 함수
    # self : this와 같다. 자기 자신의 객체
    def __init__(self, name='cat', how_many_legs=4):
        self.name = name
        self.how_many_legs = how_many_legs

cat = Animal('lee', 4)
print(cat.name)

class Address :

    def __init__(self, name, email, phonenumber, gender ):
        self.__name = name
        self.__email = email
        self.__phonenumber = phonenumber
        self.__gender = gender

chanho = Address('park chanho', 'hello@naver.com', '010-2727-2828', 'male')

print(chanho.name)
print(chanho.email)
print(chanho.phonenumber)
print(chanho.gender)
