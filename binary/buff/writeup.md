# secsoc gets buff

## Authors

- @Sequeli

## Category

- Binary Exploit

## Description

So there were rumors SecSoc was starting a gym, I heard something about the directors wanting to become buffff.

I found a C program running on their servers which they want to use for their signups. Can you tell them it's a bad idea?

`nc pwn.unswsecurity.com 5001` or `telnet pwn.unswsecurity.com 5001`

## Difficulty
- Medium

## Points
80

## Files

- buff: redacted version of the binary running on the server
- buff.c: redacted version of the C file that the binary was made from

## Solution

<details>
<summary>Spoiler</summary>

### Idea

Cause a buffer overflow, to change the flow of the program (https://www.youtube.com/watch?v=8QzOC8HfOqU)

### Walkthrough

1. When the program says you can only enter 100 characters, you enter 101 (atleast)
2. Get the flag

What happens is that because the buffer only had space for 100 characters, you start writing to memory that you're not meant to write to.
In this case, you overwrite the integer `leet`, changing it from 1337, to whatever value you put in.
This causes it to pass the `if` statement check, and you successfully redirect the program execution!

Since the program uses `gets` (check out `man gets` btw, the description is great), you can enter as many characters that you want and the function will happily keep writing to memory that you shouldn't be able to write to.

Say for example, you entered a 1000 characters, you would also cause a segfault, because you overwrote the return address of the main function :)

### Script

With the idea in mind, you use python's inline execution (-c) flag to print out 101 'a's and pass it into the running binary

```bash
python3 -c "print('a' * 101)" | nc pwn.unswsecurity.com 5000
```

### Flag

`OWEEK{I_5W3Ar_7HI5-I5_a_900d_ID3A}`

</details>
