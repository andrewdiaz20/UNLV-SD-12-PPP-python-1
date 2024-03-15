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
            print(f"first i eat {food}")     