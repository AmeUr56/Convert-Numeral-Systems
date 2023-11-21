import string

binary = [0,1]
octal = list(range(0,8))
decimal = list(range(0,10))
hexadecimal = [f'{digit}' for digit in range(0,11)]+list(string.ascii_uppercase[:6])

#Decimal To others
def DecimalToBinary(number):
    temp = number
    if number < 0:
        number *= -1
    result = []
    quotient = number
    while True:
        quotient = int(quotient / 2)
        reminder = number - quotient * 2 
        result.append(reminder)
        number = quotient
        if quotient == 1:
            result.append(1)
            break
    result.reverse()
    result = [str(i) for i in result]
    result = int(''.join(result))
    if temp < 0:
        return -result
    return result

def DecimalToOctal(number):
    temp = number
    if number < 0:
        number *= -1
    result = []
    quotient = number
    while True:
        quotient = int(quotient / 8)
        reminder = number - quotient * 8
        result.append(reminder)
        number = quotient
        if quotient == 0:
            break
    result.reverse()
    result = [str(i) for i in result]
    result = int(''.join(result))
    if temp < 0:
        return -result
    return result

def DecimalToHexadecimal(number):
    dictionary = dict(zip(list(range(10,16)),list(string.ascii_uppercase[:6])))
    temp = number
    if number < 0:
        number *= -1
    result = []
    quotient = number
    while True:
        quotient = int(quotient / 16)
        reminder = number - quotient * 16
        result.append(reminder)
        number = quotient
        if quotient == 0:
            break
    result.reverse()
    
    result = [dictionary.get(value,value) for value in result]
        
    result = [str(i) for i in result]
    if temp < 0:
        result.insert(0,'-')
        result = ''.join(result)
        return result
    result = ''.join(result)
    return result

#Others To Decimal
def BinaryToDecimal(number):
    temp = number
    if number < 0:
        number *= -1
    number = str(number)[::-1]
    result = 0
    for i in range(len(number)):
        digit = int(number[i])
        result += digit * 2**i
    if temp < 0:
        return -result
    return result
        
def OctalToDecimal(number):
    temp = number
    if number < 0:
        number *= -1
    number = str(number)[::-1]
    result = 0
    for i in range(len(number)):
        digit = int(number[i])
        result += digit * 8**i
    if temp < 0:
        return -result
    return result

def HexadecimalToDecimal(number):
    temp = number
    dictionary = dict(zip(list(string.ascii_uppercase[:6]),list(range(10,16))))
    number = str(number)[::-1]
    number = [dictionary.get(value,value) for value in number]
    result = 0
    for i in range(len(number)):
        digit = int(number[i])
        result += digit * 16**i

    return result

#Binary To others
def BinaryToOctal(number):
    result = DecimalToOctal(BinaryToDecimal(number))
    return result

def BinaryToHexadecimal(number):
    result = DecimalToHexadecimal(BinaryToDecimal(number))
    return result

#Octal To others
def  OctalToBinary(number):
    result = DecimalToBinary(OctalToDecimal(number))
    return result

def  OctalToHexadecimal(number):
    result = DecimalToHexadecimal(OctalToDecimal(number))
    return result

#Hexadecimal To others
def  HexadecimalToBinary(number):
    result = DecimalToBinary(HexadecimalToDecimal(number))
    return result

def  HexadecimalToOctal(number):
    result = DecimalToOctal(HexadecimalToDecimal(number))
    return result


