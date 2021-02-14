# Terribubble

## Authors
- @abiramen

## Category
- Recon

## Description
Hello! I'm part of the Student Integrity unit at Terribubble Universitee. At Terribubble, we take reports of academic misconduct very seriously.

Recently, we sent someone undercover in a private Discord server after reports of a student allegedly committing academic misconduct. Our undercover agent was able to take some screenshots of messages sent by this student. However, we have been unable to confirm their identity.

Would you be able to use these screenshots to investigate and find out who they are, so that we can deliver the appropriate disciplinary action? We'll also give you access to our student database to be able to confirm their identity. Thanks!

[link to student management system](https://terribubble.unswsecurity.com/)

**Note:** Sometimes recon challenges require you to scour the internet!

## Difficulty
- Medium

## Points
70

## Files
- academic-misconduct-investigation.zip: a collection of screenshots

## Solution
<details>
<summary>Spoiler</summary>

### Idea
Check for smaller details that leak through, and for usernames across the internet

### Walkthrough
The memes in the screenshots are irrelevant - what is of use to us is the username 'trivialaxolotl47', the ID card and the fact that they said that they found memes on Instagram.

1. Identify that the user failed to censor the barcode on their ID card. Either use a barcode scanning app on your phone, or crop the barcode out, and upload it to a site like [this](https://online-barcode-reader.inliteresearch.com/) to get its contents.
We get a 13 digit number out, which matches the length of the ID number requested by the Student Management System, suggesting that this is the ID.
2. Check the internet to see if the username trivialaxolotl47 is used anywhere, such as common social media platforms like Twitter, Reddit and Instagram. In this case, the username is taken on Instagram, which happens to be the platform mentioned in the screenshots. We seem to have a last name on the profile.
3. Enter the ID and last name to get the flag.

### Flag
`OWEEK{m15c0ndUcT_i5_3viL_d0nT_d0_1t!}`
</details>
