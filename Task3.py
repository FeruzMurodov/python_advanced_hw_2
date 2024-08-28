number = int(input('Enter a number: '))
list_arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
list_roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

roman_num = ''
i=0
while number > 0:
    for _ in range(number // list_arabic[i]):
        roman_num += list_roman[i]
        number -= list_arabic[i]
    i += 1
print(roman_num)