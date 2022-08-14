# file-run2
Tags: Reverse Engineering
AUTHOR: WILL HONG

Description
Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?
Download the program [here](run).

## Solution
This challenge has the same goal of [the previous one](../file-run1/), even though you could get the flag using `cat` or `head` commands and inspecting the output, the objective here is to learn how to execute programs with the command line.

We will use again the `chmod +x` to change it rights and make it executable, and then execute it with `./`. The diference here is the argument. As the challenge requests, the argument we must input is "Hello!", attention to the details, capital H and ! are mandatory. 

```bash
$ chmod +x run
$ ./run Hello!
The flag is: picoCTF{F1r57_4rgum3n7_f65ed63e}
```

### **Flag:** `picoCTF{F1r57_4rgum3n7_f65ed63e}`

---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher