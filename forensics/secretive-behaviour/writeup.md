# Secretive Behaviour

## Authors
- @N-Tandiono

## Category
- Forensics

## Description
_(This is one of the more technical challenges! Feel free to try others and come back to it later.)_

HQ is up to it again... Hiding messages inside of messages.

## Difficulty
- Medium

## Points
70

## Hint
Clues you might have picked up:
1.    Lots of whitespaces in the text
2.    Messages inside of messages
Putting together the clues, you might have found [stegsnow]( http://manpages.ubuntu.com/manpages/bionic/man1/stegsnow.1.html)

## Solution
<details>
<summary>Spoiler</summary>

## Idea
Text Steganography

### Walkthrough
1. Looking at the file provided, it would seem that the file looks very normal
2. Highlighting the text on the file in your text editor will show:
![image](https://user-images.githubusercontent.com/78247052/106602297-e96fcd80-65b0-11eb-90ce-30514bbdeb61.png)
3. You can see that there are a lot of whitespace/blank spaces here
4. If you did not know this was a steganography challenge there was a slight hint in the description: `messages inside of messages` which the first result will be a wikipedia of steganography
5. If you were to put what you found in 3 + 4 together, and Google something along the lines of 'whitespace steganography', you will see a linux library (as most likely the one of the very first results) [stegsnow](http://manpages.ubuntu.com/manpages/bionic/man1/stegsnow.1.html)
6. Note that you are also given a password in the file given in Base64
7. Decoding the Base64 encryption, you will get `BeSecretive`
8. `$ stegsnow -C -p "BeSecretive" redacted.txt` in the file directory will give the flag

Additional Comments:
- Placing it in forensics was not a mistake, few thought it was a crypto challenge because of the more obvious Base64
- This was one of the more technical questions, so don't be sad if you didn't get it
- Congrats to everyone who persisted and ended up finding the flag!

### Flag
`OWEEK{N1C3_F1Nd_aG3nt}` (case sensitive)
</details>
