def hello():
    print("hello world")

def pack(el_1, el_2, el_3):
    return [el_1, el_2, el_3]    

def eat_lunch(my_lunch):
    if len(my_lunch) == 0:
        print("My lunch box it empty")
    for food_index in range(len(my_lunch)):
        food = my_lunch[food_index]
        if food_index == 0:
            print(f"first i eat {my_lunch[food_index]}")
        elif food_index < len(my_lunch - 1):
            print(f"first i eat {my_lunch[food_index]}")



# Please complete the following functions.
# arb_args - Takes in any number of arguments and prints them one at a time.
# inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
# lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
# sum_n_product - Accepts two integers and returns both the sum and the product.
# alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
# arb_mean - Accepts any number of integers and prints their average.
# arb_longest_string - Accepts any number of strings and returns the longest one.

def arb_args(*args):
    for i in args:
        print(i)


def inner_func(num1, num2):

    def add_func():
        print(num1 + num2)

    def sub_func():
        print(num2 - num1)    

def sum_n_product(x,product):
    return(x,product)
print(2.00,"handbag")
