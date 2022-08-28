# Lookey here
Tags: forensics
AUTHOR: LT 'SYREAL' JONES / MUBARAK MIKAIL

Description
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.
Download the data [here](anthem.flag.txt).

## Solution

How we search for a certain text inside a huge text? Using Windows, any simple text editor can solve the trick. In general, the shortcut to find something is `CTRL` + `F`. We are looking for a flag, since we are in picoCTF, we can look for this word and get the flag.

But, if we are using in Linux terminal, that would need a few more steps. We have a very nice command called `grep`

According to `man grep` page, this command prints lines that matches the pattern we provide, we can see in this manual page a few commands and tips for usage, but for this case, it will be not needed.

For a good tutorial for grep, check this [blog post](https://www.thegeekstuff.com/2009/03/15-practical-unix-grep-command-examples/).

For me, I'll use grep with `-o` to output only the matched query, `-E` to use regex patterns in my search - we will probably learn more about it in the near future - and then I'll use "picoCTF" with the following regex to find a pattern of flag and everything inside the curly braces `{.*?}`, finally the command `> flag.txt` the output the result to a file called flag.txt.

`grep -oE 'picoCTF{.*?}' anthem.flag.txt > flag.txt`

## **Flag**: `picoCTF{gr3p_15_@w3s0m3_2116b979}`