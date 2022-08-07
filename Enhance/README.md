# Enhance!
AUTHOR: LT 'SYREAL' JONES

Description
Download this image file and find the flag.
[Download image file](drawing.flag.svg)

## Solution

At first glance, it is a SVG file. Opening the file directly in the browser give me a big black circle with a tiny white circle in the middle.

![Image in SVG](drawing.flag.svg)

Knowing this is a SVG file, this file can be opened with Dev console in browsers or NotePad and knowing this is a PicoCTF challenge, I just searched for "{" with "Ctrl" + "F", I could find the span tag 

```html
<tspan
         sodipodi:role="line"
         x="107.43014"
         y="132.11147"
         style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;
         stroke-width:0.26458332;"
         id="tspan3764">F { 3 n h 4 n </tspan>
```

Looking the tags above it, I get the "PicoCT" and in the tag below, `tspan3752`, I got the rest of the flag.

### **Flag:** `PicoCTF{3nh4nc3d_d0a757bf}`

---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher