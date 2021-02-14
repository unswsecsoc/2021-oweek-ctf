# You Found Me - 0

## Authors
- @abiramen

## Category
- Forensics

## Description
i'm lost can you tell me what street i'm on

Format: `OWEEK{Streetname_Streettype}`. For example, if I was on George St, my answer would be `OWEEK{George_Street}`. If I were on Anzac Pde, my answer would be `OWEEK{Anzac_Parade}`.

## Difficulty
- Easy

## Points
50

## Files
- youfoundme-hopefully-0.jpg

## Solution
<details>
<summary>Spoiler</summary>

### Idea
Checking file metadata.

### Walkthrough
1. Identify that this is a JPEG file. JPEG files tend to have extra 'metadata' (or data about the data), known as EXIF data associated with them. This metadata can include **location** if the uploader of the image is not careful.
2. Use the latitude and longitude information to find the image on Google Maps. Alternatively, find a tool like [pic2map](https://www.pic2map.com/), which plops the location on a map for you.
3. You can identify the street.

### Flag
`OWEEK{Burran_Avenue}`
</details>
