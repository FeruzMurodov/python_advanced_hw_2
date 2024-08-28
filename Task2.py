number = int(input("Enter a number: "))
print(hex(number))
flag = ''
if number == 0:
    print(0)
elif number < 0:
    flag = 'minus'
    number = abs(number)
result = ''
while number > 0:
    rest = str(number % 16)
    number //= 16
    if rest == '10':
        rest = 'a'
    elif rest == '11':
        rest = 'b'
    elif rest == '12':
        rest = 'c'
    elif rest == '13':
        rest = 'd'
    elif rest == '14':
        rest = 'e'
    elif rest == '15':
        rest = 'f'
    result = rest + result

if flag == 'minus':
    print(f'-{result}')
else:
    print(result)
