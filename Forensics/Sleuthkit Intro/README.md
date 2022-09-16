# Sleuthkit Intro
AUTHOR: LT 'SYREAL' JONES

Description
Download the disk image and use mmls on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.
Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.
- Download [disk image](disk.img.gz)
- Access checker program: nc saturn.picoctf.net 52279

## Solution
This one is the introduction of the Sleuthkit, a opensource kit of tools to make forensics analysis. We will talk about it more in the 

- Download the image

`wget https://artifacts.picoctf.net/c/114/disk.img.gz`

- Unzip it using gzip 

`gzip -d disk.img.gz`

- Install the Sleuthkit using apt 

`sudo apt install sleuthkit`

- Use the command in the challenge to obtain the answer to the get the flag in the server

```
$ mmls disk.img
```

Output:
```
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
```

- Access the checker with the command in the challenge:

```
$ nc saturn.picoctf.net 52279
```

Output:
```
What is the size of the Linux partition in the given disk image?
Length in sectors: 0000202752
0000202752
Great work!
picoCTF{mm15_f7w!}
```

`nc saturn.picoctf.net 52279`

## **Flag:** `picoCTF{mm15_f7w!}`
---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher