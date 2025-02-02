# 2 Equal Numbers
def  checkIfSame(number1,number2):
  if((number1 ^ number2)!= 0):
    print("numbers are not equal")

  else:
    print("both numbers are equal")

number1 = int(input("Enter first number to compare"))
number2 = int(input("Enter second number to compare"))
checkIfSame(number1,number2)
# --------------------------------------------
# One Odd Occuring
def OddOccuring(arr):
  res = 0
  for element in arr:
    res = res ^ element
  return res

arr = []
n = int(input("Enter array size:"))
while(n):
  num = int(input("Enter number:"))
  arr.append(num)
  n-=1

print("OddOccuring number is",OddOccuring(arr))
# --------------------------------------------
# Two Odd Occuring
def TwoOdd(arr, size):
  xorof2 = arr[0]
  x = 0
  y = 0
  SetBit = 0
  for i in range(1,size):

    xorof2 = xorof2 ^ arr[i]
  SetBit = xorof2 & ~(xorof2-1)
  for i in range(size):
    if(arr[i]& SetBit):
      x = x ^ arr[i]
    else:
      y = y ^ arr[i]

  print("TwoOdd elements are",x,"&",y)

arr = []
arr_size = int(input("Enter the size of the array"))
for i in range(0,arr_size):
  z = int(input("Enter element"))
  arr.append(z)

print("TwoOdd")
# ---------------------------------------------
# Reverse Bits
# Program to reverse all bits of a number
 
def reverseBits(number) :

	# Below variable will hold the reversed bit number 
    reversed = 0
     
    # While number is not 0
    while (number > 0) :
         
        # Shift reversed number to left
        reversed = reversed << 1
         
        # Check if last bit is 0 or 1
		# If 1 add it using OR operator else leave 
        if (number & 1 == 1) :
            reversed = reversed ^ 1
         
        # Right shift the orignal number
        number = number >> 1
         
    return reversed
     
number = int(input("Enter your number : "))
print("Number with reversed bits : ",reverseBits(number))
