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
#if statments can use the word and? why?#

# 2 Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(lst):
  #if empty list, return 0
  if len(lst) == 0:
    return 0
  #product starts with first element of list
  prod = lst[0]

  #go through list elements and multiply them together
  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i

  return prod
    
print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([15]))

#first try by self#
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

def rev_string(my_str):
  return my_str[::-1]

print(rev_string(""))
print(rev_string("apple"))
print(rev_string("mt string"))

#first try#
def rev_string(string):
  string = string[::-1]
  return string


s = "applesauce"

print(reversed(s))

#Questions for above#
#why have string equal itself???#
#Why does this code not work?#

# 4 Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))

#questions for above#
#what was the point of this function?#


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)

#questions for above#
#need a run down on how this is done and why its set up the way it is?#