def del_brackets(num):
    b = 0
    for symbol in num:
        if symbol == '(':
            b += 1
        elif symbol == ')':
            b -= 1
            if b < 0:
                return 'error'
    if b:
        return 'error'
    else:
        return num.replace('(', '').replace(')', '')


def del_dash(num):
    if '--' in num:
        return 'error'
    return num.replace('-', '')


def _8_7(num):
    if num[0] == '8':
        return '+7' + num[1:]
    return num


def del_space(num):
    return num.replace(' ', '')


num = input()
num = del_brackets(num)
if num == 'error':
    print('error')
    exit()
num = del_dash(num)
if num == 'error':
    print('error')
    exit()
num = del_space(num)
num = _8_7(num)
if len(num[1:]) < 11 or num[:2] != '+7':
    print('error')
    exit()
print(num[:13])
