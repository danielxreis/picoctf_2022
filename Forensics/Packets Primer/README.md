# Packets Primer
Tags: forensics
AUTHOR: LT 'SYREAL' JONES

Description
Download the packet capture file and use packet analysis software to find the flag.
- [Download packet capture](network-dump.flag.pcap)

## Solution

PCAP files contain packages of network traffic, they are created by softwares that make such analysis. The most famouse software we use to read this kind of file (and create them too) is **Wireshark**. You can install it on any conventional operational system today. Wireshark is a powerful tool and definitly needs your attention

You can open up the file straight with Wireshark. When you do it, you'll see a list of packages captured in some network traffic. In my case, looking into the fourth package, in the area below the screen, there's the information about the packet found, one screen below, its the data in hexadecimal. 

Using the shortcut `CTRL` + `SHIFT` + `O` to `Show Packet Bytes`, it will show the data captured, which is the flag. 

## **Flag:** `picoCTF{p4ck37_5h4rk_01b0a0d6}`

---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher