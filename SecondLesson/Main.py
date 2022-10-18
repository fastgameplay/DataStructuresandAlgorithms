def DecToBin(n):
    s = ""
    if(n > 1):
        s += DecToBin(n//2)

    return s + str(n % 2)




def SignedMagnitude(number):
    sign = "0"
    if(number < 0): 
        sign = "1"
        number = -number
    return sign + DecToBin(number)

class RadixComplement():
    def Represent(self, number):
        pass

class DiminishedRadixComplement():
    def Represent(self, number):
        pass
class Excess():
    def Represent(self, number):
        pass


print(SignedMagnitude(-109))

