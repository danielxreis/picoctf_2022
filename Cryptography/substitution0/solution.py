import string 

def decodeFlag(textToDecode : str, keyToDecode : str):
    """
    Decode substitution cipher
    ----------

    This function decodes some text encrypted with substitution cipher and decode using a key. It requires both parameters to decode it.
    The function will covert the text it to list, get each letter and decode using the key and then it will wrap the result transforming it back to string.

    This function handles uppercase, lowercase, underline, spaces, curly brackets and numbers.

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
        # Get curly brackets, underlines, spaces and numbers as they are
        specialCharacteres = ["{", "}", "_", " "]
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
print(decodeFlag(message, key))