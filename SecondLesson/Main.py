
from audioop import bias


def DecToBin(n):
    s = ""
    if(n > 1):
        s += DecToBin(n//2)
    return s + str(n % 2)

def BinToDec(n):
    return int(n,2)

# Signed magnitude
def Signed(number): 
    sign = "0"
    if(number < 0): 
        sign = "1"
        number = -number
    return sign + DecToBin(number)


# Radix complement
def Radix(number, digits = None):
    if ( digits is None): digits = len(str(number))
    maximum = 10 ** digits
    return DecToBin(maximum - number)

# Diminished Radix complement
def DRadix(number, digits = None): 
    if ( digits is None): digits = len(str(number))
    maximum = (10 ** digits) - 1
    return DecToBin(maximum - number)

def Excess(number, Bias):
    return DecToBin(number - Bias)


print((Excess(-2,-8)))

