
def numberToBase(number, base):
    #აბრუნებს სიმბოლოს ნომერს;
    if number == 0:
        return [0]
    digits = []
    while number:
        digits.append(int(number % base))
        number //= b
    return digits[::-1] #Flip

def NumberToSymbolos(symbolIDs, base):
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if(len(characters) > base):
        return [characters[i] for i in symbolIDs]
    elif( base < 16777215):
        return [numberToBase(i,16777215) for i in symbolIDs]

n =6211124
b = 2115221

print(NumberToSymbolos(numberToBase(n,b),b))
