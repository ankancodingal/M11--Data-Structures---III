# Swap 2 Numbers
def swap(a,b):
  a = a^b
  b = a^b
  a = a^b
  print("After swapping: a =",a,"and b =",b)

def swap2(a,b):
  a = (a&b)+(a|b)
  b = a+(~b)+1
  a = a+(~b)+1
  print("After swapping: a =",a,"and b =",b)

swap(10,20)
swap2(10,20)
  
# -----------------------------------
# Divide Without Divide
def divide(ourdividend, ourDivisor):
  sign = (-1 if((ourdividend < 0) ^ (ourDivisor < 0)) else 1);
  ourdividend = abs(ourdividend);
  ourDivisor = abs(ourDivisor);

  quotientNumber = 0
  tempNumber = 0
  for i in range(31, -1, -1):
    if (tempNumber + (ourDivisor << i) <= ourdividend):
      tempNumber += ourDivisor << i
      quotientNumber |= 1 << i
  if sign == -1:
    quotientNumber = -quotientNumber
  return quotientNumber

a = int(input("Enter a for a/b: ""))
b = int(input("Enter b for a/b: ""))
print("Result of", a, "/", b, "is", divide(a, b)")
# -----------------------------------
# Longest 1’s
# Program to find the longest consecutive 1's in binary representation of a number

def max1(number):

	# Initialize result
	count = 0

	# Count the number of iterations to reach number = 0.
	while (number!=0):
	
		# This operation reduces length
		# of every sequence of 1s by one.
		number = (number & (number << 1))

		count=count+1
	
	return count

number = int(input("Enter your number : "))
print("Longest consecutive 1's length : ",max1(number))
