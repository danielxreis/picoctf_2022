# Safe Opener
 | 100 points
Tags: 
AUTHOR: MUBARAK MIKAIL

Description
Can you open this safe?
I forgot the key to my safe but this [program](SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?
Put the password you recover into the picoCTF flag format like:
picoCTF{password}

## Solution
Even not knowing much about Java, we can easily spot in line 6 that SafeOpener has a variable being defined as Base64 Enconder. 

```java
Base64.Encoder encoder = Base64.getEncoder();
```

```java
String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
        
if (password.equals(encodedkey)) {
    System.out.println("Sesame open");
    return true;
}
```

Using `echo` combined with `base64 -d`, the string `cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz` is easily decoded and our flag is retrived. 

```bash
echo "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz" | base64 -d
```


## **Flag:** `picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}`
---
Daniel Reis - [@danielxreis](https://twitter.com/DanielXReis) - Developer and Cyber Security Researcher