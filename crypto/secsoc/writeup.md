# secsoc

## Authors
- @N-Tandiono

## Category
- Crypto

## Description
secsoc

## Difficulty
- Easy

## Points
65

## Hints
1. There is only sec and soc

## Solution
<details>
<summary>Spoiler</summary>

### Walkthrough
We seem to have the strings 'sec' and 'soc' as base units here - this seems very much like a binary system!

There also seems to be exactly 8 sec or socs in a group, or exactly a byte! This suggests that the flag could be encoded in ASCII.

We know that all ASCII characters represented as a binary byte start with 0. Since all the groups start with sec, we can guess that sec is 0, and soc is 1.

Replacing, we get

```
01001111 01010111 01000101 01000101 01001011 01111011 01000010 00110001 01001110 01100001 01010010 01111001 01011111 01010011 00110011 01000011 00110101 00110000 01100011 01011111 01000011 01001000 01100001 01101100 00110001 00110011 01001110 01100111 00110011 01111101
```

Converting into ASCII values, we get our flag.

### Flag
`OWEEK{B1NaRy_S3C50c_CHal13Ng3}` (case sensitive)
</details>

