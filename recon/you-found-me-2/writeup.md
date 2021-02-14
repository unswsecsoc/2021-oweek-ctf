# You Found Me - 2

## Authors
- @abiramen

## Category
- Recon

im lost im walking to my friends house from Summer Hill station, and i dont know where i am. all i know is that ive been walking for roughly ten minutes, and that theres a pretty sunset up ahead of me on the street im walking on. here's a picture of my surroundings, can you tell me where i am? 

**Format**: `OWEEK{Streetname_Streettype}`. For example, if I was on George St, my answer would be `OWEEK{George_Street}`. If I were on Anzac Pde, my answer would be `OWEEK{Anzac_Parade}`.

**Photo acknowledgements**: Google Street View

## Difficulty
- Easy

## Points
60

## Files
- youfoundme-hopefully-2.png

## Solution
<details>
<summary>Spoiler</summary>

### Idea

Small bits of information can easily give away where you are.

### Walkthrough

There's a few things that we can identify here:
- We're about a kilometer out from the station at most.
- Looking closely at the image, we can pick out the "dragon's teeth" road markings indicating a school zone, as well as the yellow rectangle with the speed limit.
- 'theres a pretty sunset up ahead of me on the street im walking on' strongly suggests that we're walking west, so this street must run east to west.

Pulling up Google Maps, we can see a few streets that run east to west near a school zone within the region:

- Junction Rd (near Summer Hill Public School)
- Herbert St (near Summer Hill Public School)
- Drynan St (near St Patrick's Primary School)
- Robert St (near St Patrick's Primary School)
- Seaview St (a bit far, but near Trinity Grammar)

With some quick checking on Google Street View, we can figure out what street we were on!

### Flag
`OWEEK{Drynan_Street}`
</details>
