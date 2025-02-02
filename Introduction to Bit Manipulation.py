# Implement Bitwise
num1 = 10 
num2 = 4
print("num1 & num2 are:", num1, num2)
print("num1 | num2 are:", num1 | num2)
print("num1 ^ num2 are:", num1 ^ num2)
print("num1 << num2 are:", num1 << num2)
print("num1 >> num2 are:", num1 >> num2)
print("~num1 are:", ~num1)
print("~num2 are:", ~num2)
# ------------------------------------------------
# Odd Even Bitwise
def isEvenOdd(n):
  if(n ^ 1 == n + 1 ):
    return True;
  else:
    return False;

number = int(input("Enter your number: "))
if isEvenOdd(number):
  print(number, "is even")

else:
  print(number, "is odd")
# -----------------------------------------------------
# Number of Bits
def numberOfBits(n):
    count = 0
    while (n):
        count += 1
        n >>= 1
    return count

n = int(input("Enter a number: "))
print("Number of bits: ", numberOfBits(n))
# -------------------------------------------------------------
# Implement Circuit
# Program to solve the circuit given

# Initialize variables with default values
a=1
b=0
c=0

# Computing all bitwise operations
aANDb = a & b
bXORc = b ^ c
bORc = b | c
g = bXORc & bORc

# Calculating final result
final = aANDb ^ g

# Printing final result
print("q = ",final)
