# substitution0
AUTHOR: WILL HONG

Description
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?
Download the [message here](message.txt).

## Solution
Finally, I can use some python code again 😍! It's a substitution cipher, since the key is at the beginning, we just need to code it!

```python
import string 

def decodeFlag(textToDecode : str, keyToDecode : str):
    """
    Decode substitution cipher
    ----------

    This function decodes some text encrypted with substitution cipher and decode using a key. It requires both parameters to decode it.
    The function will covert the text into to list, get each letter and decode using the key and then it will wrap the result transforming it back to string.
    This function handles uppercase, lowercase, spaces, curly brackets and numbers.

    Attributes
    ----------
    textToDecode : str
        a formatted string encoded with substitution cipher.
    decodingKey : str
        a formatted string with the key to decode the message.
    
    Returns
    ----------
    result : str
        a formatted string with the decoded text.
    """

    alphabet = string.ascii_uppercase
    numbers = string.digits

    decodedResult = []
    for x in list(textToDecode):
        x = str(x)
        # Get numbers, space and curly brackets as they are
        specialCharacteres = ["{", "}", " "]
        if x in specialCharacteres or x in numbers:
            decodedResult.append(x)
        # Treat the lowercase letters when they appear
        elif x.islower():
            decodedResult.append(alphabet.lower()[keyToDecode.lower().find(x)])
        else:
            decodedResult.append(alphabet[keyToDecode.find(x)])
    result = "".join(decodedResult)
    return result

# Open the message and store in a variable
with open ("message.txt", 'r') as f:
    message = f.read()

# Get the key and the flag to decode
key, flag = message.split()[0], message.split()[-1]

# Get the flag using the function above
print(decodeFlag(flag, key))
```

With the [code ready](solution.py) and well-documented, we just need to run it in the same folder of the `message.txt`

```bash
python3 solution.py
```

## **Flag:** `picoCTF{5UB5717U710N_3V0LU710N_357BF9FF}`
---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher