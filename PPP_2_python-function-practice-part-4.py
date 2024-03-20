# 1 Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    if(a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest            
a = 50
b = 80
c = 90

print(max_num(a,b,c))

# why is the word largest involved?#

# 2 Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(num):
    for x in num:
        total *= x
    return total

list1 = [1, 2, 5]
list2 = [5, 6, 4]


print(mult_list(list1))
print(mult_list(list2))

#questions for above!#
#why does this code not work???#
#why use a a for loop function and not a map()?#
#Should i keep in mind of *=?#    

# 3 Write a Python function called rev_string() to reverse a string
def rev_string(string):
  string = string[::-1]
  return string


s = "applesauce"

print(reversed(s))

#Questions for above#
#why have string equal itself???#

# 4 Write a Python function called num_within() to check whether a number falls in a given range.
def num_within():