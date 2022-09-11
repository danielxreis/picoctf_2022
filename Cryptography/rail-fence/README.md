# rail-fence
Tags: Cryptography
AUTHOR: WILL HONG

Description
A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it?
Download the message [here](./message.txt).
Put the decoded message in the picoCTF flag format, picoCTF{decoded_message}.

## Solution

Looking into Google and searching for decoder rail fence ciper, in the [first link](https://www.boxentriq.com/code-breaking/rail-fence-cipher), we can set the number of rails and get the result from the string:

`The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3`

Wraping it into the correct format output, we get the flag.

## Flag: `picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3}`

---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher