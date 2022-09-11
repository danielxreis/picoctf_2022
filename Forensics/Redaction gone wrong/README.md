# Redaction gone wrong
Tags: 
AUTHOR: MUBARAK MIKAIL

Description
Now you DON’T see me.
This [report](./Financial_Report_for_ABC_Labs.pdf) has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?

## Solution

Reading the document, we can see a hint: *Just painted over in MS word.* Since it was just painted over, the text are the available, we can't see in the PDF, but we can copy and paste it into another text editor.

```
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021. 
Breakdown - Just painted over in MS word. 
 
Cost Benefit Analysis
Credit Debit
This is not the flag, keep looking
Expenses from the 
picoCTF{C4n_Y0u_S33_m3_fully}
Redacted document
```

Doing that, we get the flag

## Flag: `picoCTF{C4n_Y0u_S33_m3_fully}`
---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher