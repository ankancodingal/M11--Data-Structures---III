# Ones and Zeros
def numberOfBits(n):
  ones = 0
  zeroes= 0
  while (n):
      if (n & 1 == 1):
          ones += 1
      else:
          zeroes += 1
      n >>= 1
  print("Number of ones =", ones, "\nNumber of zeroes =", zeroes)

number = int(input("Enter your number: "))
numberOfBits(number)
# -------------------------------------
# nth Bit Set or Not
def setOrNot(number, n):
  # You need to define 'mask' before using it
  mask = 1  # Assuming you want to check if the bit is set or not 
  if (n & mask) == 1 or (n & mask) == 0:  # Corrected comparison and OR operator
    if number & (1 << (n - 1)):
      print("SET")
    else:
      print("NOT SET")
number = int(input("Enter the number: "))
n = int(input("Enter the bit position: "))
setOrNot(number, n)
# ------------------------------------------------
# First Set Bit
# Program to check the right most set bit is a number
 
# function to find the
# rightmost set bit
def FirstSetBit(number):
 
    # Position and mask variable
    position = 1
    mask = 1
 
    while (not(number & mask)) :
 
        # left shift mask to check next bit
        mask = mask << 1
        position += 1
     
    return position
 
number = int(input("Enter number : "))
 
# function call
print("Position of the first set bit : ",FirstSetBit(number))
