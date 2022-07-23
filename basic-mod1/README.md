# basic-mod1
Tags: Cryptography
AUTHOR: WILL HONG

Description
We found this weird message being passed around on the servers, we think we have a working decryption scheme.

Download the message [here](message.txt).

Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.

Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Solution

Searching for "mod 37 decoder" on Google, I found [this website](https://www.dcode.fr/modulo-cipher). The page suggests that 'mod' is **Modulo Cipher**, within *Homophonic Substitution Cipher*. 

In the link above, there is more explanation about how the **Modulo Cipher** works, in the end of this README, you will find all the important links to solve this challenge.

Basically, what we need to know to decrypt a modulo cipher is the Modulo number and the numbers we want to decode. In the page, I got more details about it:

> For each number N, calculate the value of the remainder in the **euclidean division** of N by the modulo to get the plain number.

In the same website, we can find a brief explanation on how the [euclidean division](https://www.dcode.fr/euclidean-division) works and learn how to get the remainder.

Now we have in hands all we need to decode the message. So I created a [simple python script](decode_euclidean.py) to decode the message:

```python
import string

def euclidean(Dividend, Divisor):
    # https://www.dcode.fr/euclidean-division
    Quotient = Dividend // Divisor
    Remainder = Dividend - Quotient * Divisor
    return Remainder

message = [202, 137, 390, 235, 114, 369, 198, 110, 350, 396, 390, 383, 225, 258, 38, 291, 75, 324, 401, 142, 288, 397]

alphabet = string.ascii_uppercase
decimals = string.digits
underscore = "_"

decryptGuide = alphabet + decimals + underscore

result = ""
for x in message:
    result += str(decryptGuide[euclidean(x, 37)])

print("picoCTF{" + result + "}")
```

1. Imported the python library ``string`` to be used in the step 4.
2. Created a function called ``euclidean()``, which will accept two arguments following the instructions to get the remainder of the euclidean division.
3. I created a first list called ``message`` with the text from the [message.txt](message.txt)
4. A second list called ``decryptGuide`` with the orientations to decode the result: 

- **Alphabet:** 0-25 is the alphabet in uppercase using the lib ``string``
- **Decimals:** 26-35 are the decimal digits
- **Underscore:** 36 is an underscore

5. Finally, a ``for`` loop which will get every number of the ``message`` and run it in the euclidean function with the modulo 37 provided by the challenge and turn into a decrypted number, after that, get the current number as an index in the ``decryptGuide`` to get the result in the print at the end.

**Flag:** ``picoCTF{R0UND_N_R0UND_B6B25531}``

## Update
After watching the [John Hammond's solution](https://www.youtube.com/watch?v=nIB1IxK1FmY) to this code, I made a few improviments in to the code. I also learned better abou the modulus, must check it out. 

## References

1. *Modulo Cipher* on dCode.fr [online website], retrieved on 2022-07-17, https://www.dcode.fr/modulo-cipher
2. *Modulo N Calculator* on dCode.fr [online website], retrieved on 2022-07-17, https://www.dcode.fr/modulo-n-calculator
3. *Euclidean Division* on dCode.fr [online website], retrieved on 2022-07-17, https://www.dcode.fr/euclidean-division

---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher