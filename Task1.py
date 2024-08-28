import math

number_a = int(input("Enter number a: "))
number_b = int(input("Enter number b: "))
more = 0
less = 0
if number_a > number_b:
    more = number_a
    less = number_b
else:
    more = number_b
    less = number_a
remainder = 1
result = less
while remainder > 0:
    remainder = more % less
    more = less
    less = remainder
    if remainder > 0:
        result = remainder
print("Greatest common divisor is ", result)
print("Greatest common divisor is ", math.gcd(number_a, number_b))

