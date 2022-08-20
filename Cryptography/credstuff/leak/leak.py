# Transform every line into one item in a list using split()
with open("usernames.txt") as f:    
    usernames = f.read().split()

with open("passwords.txt") as f:
    passwords = f.read().split()

database = {}
for x in range(0, len(usernames)):
    database[usernames[x]] = passwords[x]

print(database["cultiris"])

import codecs

rot13 = lambda s : codecs.getdecoder("rot13")(s)[0]

print(rot13(database["cultiris"]))