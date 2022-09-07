# patchme.py
Tags: Reverse Engineering
AUTHOR: LT 'SYREAL' JONES

Description
Can you get the flag?
Run this [Python program](./patchme.flag.py) in the same directory as this [encrypted flag](./flag.txt.enc).

## Solution 

To accomplish this challenge, you need python installed. When we run the script, it will request you a password. Looking the source of the [(patchme.flag.py](./patchme.flag.py),  you find a conditional that checks if what the user put in the prompt is equal to the password. Very unsecure way to check the password, because it is in plainsight:

```python
if( user_pw == "ak98" + \
                "-=90" + \
                "adfjhgj321" + \
                "sleuth9000"):
```

Putting all these strings agove together we get: `ak98-=90adfjhgj321sleuth9000`. Using it as password, we retrieve the flag. 

```
Please enter correct password for flag: ak98-=90adfjhgj321sleuth9000
Welcome back... your flag, user:
picoCTF{p47ch1ng_l1f3_h4ck_21d62e33}
```

We could also change this if conditional in the python file to anything we want, or even better, just remove the exceprt that do any kind of check. 

## **Flag:** `picoCTF{p47ch1ng_l1f3_h4ck_21d62e33}`

---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher