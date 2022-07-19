# describe problem
def my_function():
    # for i in range(1, 20):
    for i in range(1, 21):
        if i == 20:
            print("You got it.")


my_function()

# reproduce the bug
from random import randint

dice_imgs = ["e", "f", "g", "h", "i"]
# dice_num = randint(1, 5)
dice_num = randint(1, 4)
print(dice_imgs[dice_num])

# play computer
year = int(input("what's your year of birth?"))
if year > 1988 and year < 1994:
    print("You are a millenial.")
# elif year > 1994:
elif year >= 1994:
    print("You are Gen Z.")

# fix the error
# age = input("how old are you?")
age = int(input("how old are you?"))
if age > 18:
    # print("You can drive at age {age}")
    print(f"You can drive at age {age}")

# print is your friend
pages = 0
word_per_pages = 0
pages = int(input("number of pages :"))
# word_per_pages == int(input("number of words per page: "))
word_per_pages = int(input("number of words per page: "))
total_words = pages * word_per_pages
"""check with print"""
print(f"pages = {pages}")
print(f"word_per_page = {word_per_pages}")
print(total_words)


# use a debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        """visualize python"""
        # b_list.append(new_item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 4])

# take a break
# practice1
number = int(input("which number do you want to check?"))
# if number % 2 = 0:
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# practice 2
# year1 = input("Which year do you want to check?")
year1 = int(input("Which year do you want to check?"))
if year1 % 4 == 0:
    if year1 % 100 == 0:
        if year1 % 400:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")

# practice 3
for number1 in range(1, 101):
    """print(f"currently on number {number1}")"""
    # if number1 % 3 == 0 or number1 % 5 == 0:
    if number1 % 3 == 0 and number1 % 5 == 0:
        print("fizzbuzz")
    elif number1 % 3 == 0:
        print("fizz")
    elif number1 % 5 == 0:
        print("buzz")
    else:
        print(number1)

