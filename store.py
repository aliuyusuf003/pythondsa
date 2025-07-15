#cool picture
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

#iterate overpicture
#if 0, print('')
#if 1, print('*')
#use print('',end='')  to remove default newline

for img in picture:
    for pix in img:
        if pix == 1:
            print('*',end='')
        else:
           print(' ',end='')
    print('')
#    *    
#   ***   
#  *****  
# ******* 
#    *    
#    * 


mystring = "StringReversal"

# swapping extreme items        
def reverse_str(str):
#     reversed = ''
#     for char in str:
#         reversed = char + reversed
     str = str[::-1]
     return str

print(reverse_str(mystring))

my_array = [64,34,25,12,22,11,90]
# swapping extreme items        
def reverse_array(arr):
    start =0
    end = len(arr) -1
    while start < end:
        arr[start],arr[end] = arr[end], arr[start]
        return arr

print(reverse_array(my_array))

# get the shortest student in the list of heights

heights = [7, 12, 9, 4, 11,8]

def shortest(heights):
    minval = heights[0]
    for currval in heights:
        if currval < minval:
            minval = currval
    return minval

# print(shortest(heights))


# get the tallest student in the list of heights

# heights = [7, 12, 9, 4, 11,8]

def tallest(heights):
    maxval = heights[0]
    for currval in heights:
        if currval > maxval:
            maxval = currval
    return maxval

print(shortest(heights))
print(tallest(heights))




def fib(n):
    if n <=1:
        return n
    else:
        return fib(n -1) + fib(n -2)
# print(fib(19))

# Efficient fibonacci

def F(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(F(19000))