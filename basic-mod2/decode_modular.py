import string

decryptGuide = string.ascii_uppercase + string.digits + "_"

with open ("message.txt") as file:
    content = file.read()
    print()
    number = [int(x) % 41 for x in content.split()]
    result = ""
    for x in number:
        result += decryptGuide[pow(x, -1, 41)-1]

print(f"picoCTF{{{result}}}")