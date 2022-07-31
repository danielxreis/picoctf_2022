# basic-mod2
Tags: Cryptography
AUTHOR: WILL HONG

Description
A new modular challenge!
Download the message [here](message.txt).
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Solution
With the [previously challenge](../basic-mod1/) done, the part related to 'modular' will be the same, but now we have to inverse the modular to get the result.

Again I'll use Python for better coding and visualization.

The updated part of the code comes from the video from John Hammond. I didn't use the `with open` command, I dunno why, and I typed the entire list  by hand. My bad, sorry. I also wasn't aware of the string manipulation too, so in this challenge I'll use the new  acquired knowloadge.

The beginning is the same: importing `string` library but we get some minor upgrade: creating `decryptGuide` in one line and using `with open` syntax and `list comprehension` to create the `number` list with already modulus numbers.

This challenge was more about to find the right mathematical solution than the first. But, after a lot of search, there is a very fucking simple bult-in python function `pow(x, -1, 41)` that get the result pretty easy. This one has a lot of mathematical stuff that I still don't get it.

```python
import string

decryptGuide = string.ascii_uppercase + string.digits + "_"

with open ("message.txt") as file:
    content = file.read()
    number = [int(x) % 41 for x in content.split()]
    result = ""
    for x in number:
        result += decryptGuide[pow(x, -1, 41)-1]

print(f"picoCTF{{{result}}}")
```

### **Flag:** `picoCTF{1NV3R53LY_H4RD_8A05D939}`

---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher