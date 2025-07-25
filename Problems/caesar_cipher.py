def caesar_cipher(text, shift, mode='encode'):
    result = ''
    shift = shift % 26  

    if mode == 'decode':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - start + shift) % 26
            result += chr(start + offset)
        else:
            result += char  
    return result

message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))
mode_choice = input("Type 1 to encode or 2 to decode: ")

mode = 'encode' if mode_choice == '1' else 'decode'

result = caesar_cipher(message, shift_value, mode)
print(f"{mode.capitalize()}d Message:", result)
