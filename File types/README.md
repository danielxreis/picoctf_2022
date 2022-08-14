# File types
Tags: Forensics
AUTHOR: GEOFFREY NJOGU

Description
This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.
You can download the file from [here](Flag.pdf).

## Solution

The file in the challenge is not a real PDF. To find out what the type of the file, in this challenge, we will need to make constant use of the command `file`, it will return the filetype of the current file. 

This challenge will be some kind of *Matryoshka doll*

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Russian-Matroshka.jpg/200px-Russian-Matroshka.jpg)

The first file is a `shell archive text`, it can be extract with the command `sh Flag.pdf`.

```bash
$ file Flag.pdf
Flag.pdf: shell archive text

$ sh Flag.pdf
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.
```

The first file will output a file named `flag`. Now, on each file, we will type the command `file`, find what the type of the compressing algorithim it was used on it and then use its respective command to extract the content.

So it will be a manual loop, I recommend you search every type of file before extract. You'll see that some steps I had to create a new directory or rename the current file to match the file extensions the algorithim was requiring to extract the content or to not replace the current file being exctrated.

Here, I'll just write the steps I took till the last file.

1. **current ar archive** - `ar x flag `
2. **cpio archive** - `mkdir cpio && cpio -i -D cpio < flag && cd cpio`.
3. **bzip2 compressed data** - `bzip2 -d flag` 
4. **gzip compressed data** - `mv flag.out flag.gz && gzip -d flag.gz`
5. **lzip compressed data** - `lzip -d flag`
6. **LZ4 compressed data** - `mv flag.out flag.lz4 && lz4 -d flag.lz4`
7. **LZMA compressed data** - `mv flag flag.xz && lzma -d flag.xz`
8. **lzop compressed data** - `mv flag flag.lzop && lzop -d flag.lzop`
9. **lzip compressed data** - `lzip -d flag`
10. **XZ compressed data** - `mv flag.out flag.xz && xz -d flag.xz`

The final output is a ASCII text file, and it contents are the string below:

```
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f39353063346665657d0a
```

This is hexadecimal type of text. The web you can find a lot of tools that will convert it to text and finally the flag.

### Flag: `picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_950c4fee}`

---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher