import fractions
import math
from fractions import Fraction

fraction_a = input('Enter fractional  number a: ')
fraction_b = input('Enter fractional  number b: ')
numerator_a = int(fraction_a[0])
denominator_a = int(fraction_a[2])
numerator_b = int(fraction_b[0])
denominator_b = int(fraction_b[2])

# multiply
number_a = numerator_a * numerator_b
number_b = denominator_a * denominator_b
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

print('Multiplication of fractions:', f'{number_a // result}/{number_b // result}')
a = Fraction(numerator_a, denominator_a)
b = Fraction(numerator_b, denominator_b)
print('Multiplication of fractions:', a * b)
# add
res_numerator = denominator_b * numerator_a + denominator_a * numerator_b
res_denominator = denominator_a * denominator_b
gcd = math.gcd(res_numerator, res_denominator)
print('Sum of fractions:', f'{res_numerator // gcd}/{res_denominator // gcd}')
print('Sum of fractions:', a + b)
