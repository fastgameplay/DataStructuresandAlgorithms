def DecToBin(n):
    s = ""
    if(n > 1):
        s += DecToBin(n//2)

    return s + str(n % 2)


def ToSigned(number): # Signed magnitude
    sign = "0"
    if(number < 0): 
        sign = "1"
        number = -number
    return sign + DecToBin(number)

def ToRadix(number): # Radix complement
    maximum = 10 ** len(str(number))
    print(maximum - number)
    return DecToBin(maximum - number)


def ToDRadix(number): # Diminished Radix complement
    maximum = (10 ** len(str(number))) - 1
    print(maximum - number)
    return DecToBin(maximum - number)

def ToExcess(number, M):
    pass


print(ToDRadix(735))

