# Power Set
def printPowerSet(set, set_size):
    power_set_size = 2**set_size
    outer = 0
    inner = 0
    for outer in range(0, power_set_size):
        for inner in range()

# --------------------------------------
# Flip Bits
def flips(num1,num2):
  flip = 0
  while (num1 > 0 or num2 > 0):
   t1 = num1 & 1
   t2 = num2 & 1
   if t1 != t2:
    flip += 1
   num1 >>= 1
   num2 >>= 1
  return flip
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Number of flips needed: ", flips(num1, num2))


# -------------------------------------
# All Sub String
# Program to find all substring of a string

import math;

def printPowerSet(set,set_size):
	
	# Find total elements possible in the power set
	pow_set_size = (int) (math.pow(2, set_size));
	counter = 0;
	j = 0;
	
	for counter in range(0, pow_set_size):
		for j in range(0, set_size):
			
			# Check if jth bit in the counter is set If set then print jth element from set
			if((counter & (1 << j)) > 0):
				print(set[j], end = "");
		print("");

str = input("Enter string : ")
printPowerSet(str, len(str));


