# credstuff
Tags: Cryptography
AUTHOR: WILL HONG / LT 'SYREAL' JONES

**Description**
We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it?
Download the leak [here](leak.tar).
The first user in `usernames.txt` corresponds to the first `password` in passwords.txt. The second user corresponds to the second password, and so on.

## Solution

I started extracting the content of `leak.tar` with 7zip. It gave me a folder with two files. Aalysing the challenge I could just search the user in the file `usernames.txt`, get the line number and then look for its corresponding number in the `passwords.txt`, but, C'mon... 🤷‍♂️

![I am once again asking for your python support](https://i.imgflip.com/6ofsmn.jpg)

I created a [python script](leak/leak.py) inside the [leak folder](leak) that would do this:

Since all the usernames are in each line, I had to use the bult-in function in python `split()` to get every user and password as a value into a list, then we were ready to go. I stored users and passwords in their respective variables.

```python
with open("usernames.txt") as f:    
    usernames = f.read().split()

with open("passwords.txt") as f:
    passwords = f.read().split()
```
I created a dictionary variable named `database` and with a simple `for` loop following the range of the length of the variable username, I get all users being key with their respective passwords being the value.

```python
database = {}
for x in range(0, len(usernames)):
    database[usernames[x]] = passwords[x]
```

Now, I just printed the value attached to the "cultiris" key of the database dictionary. It showed me a text very similar to the flag format.

```python
print(database["cultiris"])
```

`cvpbPGS{P7e1S_54I35_71Z3}`

I got the first part of the string `cvpbPGS` and google it, found the [rot13.com](https://rot13.com/) and then it gave me the result:

### **Flag:** `picoCTF{C7r1F_54V35_71M3}`

But, when I found that was rot13, for fun purposes, I searched a little more and found a [stackoverflow answer](https://stackoverflow.com/questions/47002483/decode-python-rot13-string) that helped me continue the python script to make it show the final flag without the need of website. 

```python
import codecs
rot13 = lambda s : codecs.getdecoder("rot13")(s)[0]
print(rot13(database["cultiris"]))
```

---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher