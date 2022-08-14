# GDB Test Drive
Tags: Reverse Engineering
AUTHOR: LT 'SYREAL' JONES

Description
Can you get the flag?
Download this [binary](gdbme).
Here's the test drive instructions:

```bash
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```

## Solution

GBD is well-knwon as GNU Debugger, its used to debugging in unix-systems and it supports programing languages like C, C++, Java and so more. This program allows you to see what is going on "inside" another program while it executes -- or what another program was doing at the moment it crashed.

The challenge ask us to run a series of commands, the first one is `chmod +x`, we used this one before in others challenges. It will make the file executable. 

The second command is to run the file `gdbme` with the debugger `gdb`.

The third command is to displays the file disassembled.

The fourth command set a breakpoint in the specified location, in our case, is in this line:

`0x132a <main+99>        callq  0x1110 <sleep@plt>`

The fifth line, the program will run and then, the sixth line, will continue the program at specified line, just after the break we made just now.

When we follow the comands, it will return the flag

### Flag: `picoCTF{d3bugg3r_dr1v3_7776d758}`

---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher