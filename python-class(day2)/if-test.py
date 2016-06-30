"""
둘째날
"""

bool_one = False and False
bool_two = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5
bool_three = 19 % 4 != 200 / 10 / 10 and False
bool_four = -(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2

print(bool_one)
print(bool_two)
print(bool_three)
print(bool_four)

score = 92
if score >= 90:
    print('grade A')

score = 59
if score >= 60:
    print("합격하셨습니다")
    print('this is also if scope')
elif score < 60:
    print("불합격 하셨습니다.")

score = 100
if score >= 60:
    print("합격하셨습니다")
    print('this is also if scope')
else:
    print("불합격 하셨습니다.")


def the_flying_circus(score):
    if score > 50 and score%2 == 0:
        return True
    elif score > 70:
        return True

print(the_flying_circus(60))



my_score = 95
if my_score >= 90:
    print('A')
elif my_score >= 80:
    print('B')
elif my_score >= 70:
    print('C')
elif my_score >= 60:
    print('D')
else:
    print('F')

my_number = input("input a number: ")
print(my_number)

my_word = input("input a word : ")
if len(my_word) > 0 and my_word.isalpha() :
    first = my_word[0]
    my_word_len = len(my_word)
    my_new_word = my_word[1:my_word_len] + first + "ay"
    print("new word is " + my_new_word)
else:
    print("invalid word")


my_word = input("input a word : ")
if len(my_word) == 0 or not my_word.isalpha() :
    print("invalid word")
else:
    first = my_word[0]
    my_new_word = my_word[1:] + first + "ay"
    print("new word is " + my_new_word)


