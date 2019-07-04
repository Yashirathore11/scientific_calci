def binary_to_decimal(binary):
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

def octal_to_decimal(octal):
    decimal, i = 0, 0
    while octal != 0:
        dec = octal % 10
        decimal = decimal + dec * pow(8, i)
        octal = octal // 10
        i += 1
    return decimal


def hexadecimal_to_decimal(hexadecimal):
    decimal, i = 0, 0
    while hexadecimal != 0:
        dec = hexadecimal % 10
        decimal = decimal + dec * pow(16, i)
        hexadecimal = hexadecimal // 10
        i += 1
    return decimal

def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    octal = oct(decimal).replace("0o", "")
    return octal

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    hexadecimal = hex(decimal).replace("0x", "")
    return hexadecimal

def octal_to_binary(octal):
    decimal = octal_to_decimal(octal)
    binary = bin(decimal).replace("0b", "")
    return binary


def octal_to_hexadecimal(octal):
    decimal = octal_to_decimal(octal)
    hexadecimal = hex(decimal).replace("0x", "")
    return hexadecimal


def hexadecimal_to_decimal(hexadecimal):
    decimal, i = 0, 0
    while hexadecimal != 0:
        dec = hexadecimal % 10
        decimal = decimal + dec * pow(16, i)
        hexadecimal = hexadecimal // 10
        i += 1
    return decimal


def hto():
    hexadecimal = int(input("Enter valid Hexadecimal number: "))
    decimal = hexadecimal_to_decimal(hexadecimal)
    octal = oct(decimal).replace("0o", "")
    print("Octal number is: ", octal)


def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    binary = bin(decimal).replace("0b", "")
    return binary


def decimal_to_binary(decimal):
    binary = bin(decimal).replace("0b", "")
    return binary


def decimal_to_hexadecimal(decimal):
    hexadecimal = hex(decimal).replace("0x", "")
    return hexadecimal


def decimal_to_octal(decimal):
    octal = oct(decimal).replace("0o", "")
    return octal


