# Strings Theory

## Authors

- @Sequeli

## Category

- Reversing

## Description

Hello, doctor, in order to increase security to protect our new string theory research better,
top scientists in our IT department have made this program to store all your work.
It was made _specifically_ for you, and our experts assure us it is extremely secure.

## Difficulty

- Medium

## Points

80

## Files

- admin: binary you should take a look at

## Solution

<details>
<summary>Spoiler</summary>

### Idea

Use `strings` to find the username and password "hidden" inside the binary

### Walkthrough

Looking at a binary can be intmidating at first, especially if you haven't worked with them before.
But I hope I put in "string" enough times in the challenge to be a clue.

The program drops you into a login console, if you enter a random password, you can't get in.

```
Welcome to the super secret admin console. Hope I don't need to remind you to keep the company's research on string theory secret
To proceed, enter your username: sequeli
Password: super_hackah
Invalid password. Your mind just hasn't been the same since the electro-shock, has it??
```

Now that you know what it does, you want to do some static analysis on it.

1. To start with, use the `file` command to look at the type of file:

   ```
   admin: ELF 32-bit LSB shared object, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=d540456874e608289134bc3c4664b11a05465935, not stripped
   ```

   It might look complicated, but all it means is that its a 32-bit C program.

### **(fix this up, but essentially, use strings to look stuff inside the data section)**

2. Then, see if there's any hidden data in the file look using `strings`. You should see some suspicious strings:

   ```
   The_Admin
   tHis_-PaSSw0rD_iS_Super-sEcURe_I_swear
   ```

3. When you put these in as your username and password, you're in!

The C file should be in the repository if you want to have a look **(insert link here)**.

### Flag

`OWEEK{57R1rN95_15_N1C3_8U7_hav3-y0u_7R13d_radAR3}`

</details>
