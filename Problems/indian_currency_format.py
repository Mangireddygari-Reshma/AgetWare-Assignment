def indian_currency_format(amount):
    if '.' in str(amount):
        integer_part, decimal_part = str(amount).split('.')
    else:
        integer_part, decimal_part = str(amount), ''

    sign = ''
    if integer_part.startswith('-'):
        sign = '-'
        integer_part = integer_part[1:]

    last_three = integer_part[-3:]
    rest = integer_part[:-3]

    formatted_rest = ''
    while len(rest) > 0:
        formatted_rest = rest[-2:] + (',' + formatted_rest if formatted_rest else '')
        rest = rest[:-2]

    if formatted_rest:
        formatted_number = sign + formatted_rest + ',' + last_three
    else:
        formatted_number = sign + last_three

    if decimal_part:
        formatted_number += '.' + decimal_part

    return formatted_number
try:
    raw_input = input("Enter currency amount: ")
    number = float(raw_input)
    result = indian_currency_format(number)
    print("Indian currency format:", result)
except ValueError:
    print("Incorrect format. Please enter a valid numeric amount like 123456.78. Avoid extra decimal points or symbols.")