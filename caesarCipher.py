import time
import string
def greeting():
    print("Hello, let's encode or decode your message!")
    time.sleep(.75)
    encode_decode = ""
    while encode_decode != 'encode' or 'decode':
        encode_decode = input("Do you want to encode or decode a message: ")
        if encode_decode.lower() == 'encode':
            return encode_cipher()
        elif encode_decode.lower() == 'decode':
            return decode_cipher()
        else:
            print("seems like you mistyped: ")

def encode_cipher():
    rule = "Keep your cipher under 100 characters, and do not use spaces or symbols.\n"
    message = ""
    cipher = []
    alphabet = string.ascii_letters + string.digits
    while message == "":
        print(rule)
        message = input("What message would you like to encode: ")
        message = message.lower()
        print("")
        if len(message) > 100:
            message = ""
        for letter in message:
            if letter not in alphabet:
                message = ""
                print("You had a letter not in the alphabet or symbol that could not be encoded.")
                print("")
    shift_number = 0
    while shift_number == 0:
        shift_number = input("(type only integers: 1, 2, 3... etc.)\nYour number must be less than 26 \nHow many characters would you like to shift: ")
        try:
            shift_number = int(shift_number)
        except:
            print("Positive Whole Numbers Only")
        if not isinstance(shift_number, int):
            shift_number = 0
        if shift_number > 25:
            shift_number = 0
    alphabet = list(alphabet)
    for position in range(len(message)):
        char = message[position]
        for letter in alphabet:
            if letter == char:
                index = alphabet.index(letter)
                cipher_block = (index + shift_number - 1)
                cipher.append(alphabet[cipher_block])

    print("Your cipher is: " + "".join(cipher))

def decode_cipher():
    alphabet = (string.ascii_letters + string.digits)
    rule = "Your cipher should be under 100 characters, and does not use spaces or symbols.\n"
    message = ""
    cipher = []
    while message == "":
        print(rule)
        message = input("What cipher would you like to decode: ")
        print("")
        if len(message) > 100:
            message = ""
        for letter in message:
            if letter not in alphabet:
                message = ""
                print("You had a letter not in the alphabet or symbol that could not be decoded.")
                print("")
    shift_number = 0
    while shift_number == 0:
        shift_number = input("What cipher block was used with your cipher?\n(only type a whole number) : ")
        try:
            shift_number = int(shift_number)
        except:
            print("Positive Whole Numbers Only")
        if not isinstance(shift_number, int):
            shift_number = 0
        if shift_number > 25:
            print("Number must be less than 26... are you sure you have the right cipher block?")
            shift_number = 0
    alphabet = list(alphabet)
    for position in range(len(message)):
        char = message[position]
        for letter in alphabet:
            if letter == char:
                index = alphabet.index(letter)
                cipher_block = (index - shift_number + 1)
                cipher.append(alphabet[cipher_block])

    print("Your message is: " + "".join(cipher))

greeting()
