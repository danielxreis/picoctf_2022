import string

def euclidean(Dividend, Divisor):
    # https://www.dcode.fr/euclidean-division
    Quotient = Dividend // Divisor
    Remainder = Dividend - Quotient * Divisor
    return Remainder

message = [202, 137, 390, 235, 114, 369, 198, 110, 350, 396, 390, 383, 225, 258, 38, 291, 75, 324, 401, 142, 288, 397]

alphabet = list(string.ascii_uppercase)
decimals = [0,1,2,3,4,5,6,7,8,9]
underscore = ["_"]

decryptGuide = alphabet + decimals + underscore

result = ""
for x in message:
    result += str(decryptGuide[euclidean(x, 37)])

print("picoCTF{" + result + "}")