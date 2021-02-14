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

Cause a buffer overflow, to change the flow of the program. [Check out liveoverflow explaining it.](https://www.youtube.com/watch?v=T03idxny9jE&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN&index=13)

### Walkthrough

1. Run the program
   - Since its a 32-bit binary, you might have needed the 32-bit libraries to run it. [Stack overflow help](https://stackoverflow.com/questions/49705309/cant-run-32-bit-binary-on-64-bit-debian)
2. When the program says you can only enter 100 characters, you enter 101 (atleast)
3. Get the flag

### Why did this happen?

You just performed your (potentially first) buffer overflow!

1. Since the buffer only had space for 100 characters (and a null byte), you start writing to memory that you're not meant to write to.

   - In this case, you overwrite the integer `leet`, changing it from 1337, to whatever value you put in.
   - As `leet` is no longer equal to `1337`, you pass the `if` check, and you successfully redirect the program execution!

2. Since the program uses [gets() function](https://man7.org/linux/man-pages/man3/gets.3.html), you can enter as many characters that you want and the function will happily keep writing to memory that you shouldn't be able to write to.
   - Say for example, you entered a 1000 characters, you would also cause a segfault, because you overwrote the return address of the main function :)
   - Conversely, the program won't crash if you enter less than a certain number of characters (105 in this case), which means the attack can be hidden if the server running it only logs crashes.

_(Too complicated? Don't worry, the course COMP1521 covers the basics of how C programs handle memory)_

### Script

With the idea of an overflow in mind, you use python's inline execution (-c) flag to print out 101 'a's and pass it into the running binary

```bash
python3 -c "print('a' * 101)" | nc pwn.unswsecurity.com 5000
```

### Flag

`OWEEK{I_5W3Ar_7HI5-I5_a_900d_ID3A}`

</details>
