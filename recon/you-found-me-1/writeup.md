# You Found Me - 1

## Authors
- @abiramen

## Category
- Recon

## Description
im lost i somehow found a comfy spot on Sydney Trains and fell asleep and missed my stop aaaaaa. the guard woke me up because we had reached the end of the train line, and im slightly dazed. i guess i could just take a train from the other platform at the station to get home, but first im going to find a nice spot to nap. what station am i at?

**Format**: `OWEEK{Station}`. For example, if I was at Exampletown Station, my answer would be `OWEEK{Exampletown}`.

**Photo acknowledgements**: Google Street View

## Difficulty
- Easy

## Points
40

## Files
- youfoundme-hopefully-1.png

## Solution
<details>
<summary>Spoiler</summary>

### Idea
Some basic research if you don't know about Sydney train lines, and observing details in the image.

### Walkthrough
There are only 14 Sydney Trains stations in which train lines end at:

- Berowra (T1)
- Emu Plains (T1)
- Parramatta (T2)
- Museum (T2)
- Leppington (T2, T5)
- Central (T3, T7)
- Bondi Junction (T4)
- Waterfall (T4)
- Cronulla (T4)
- Schofields (T5)
- Lidcombe (T5)
- Olympic Park (T5)
- Macarthur (T7)
- Hornsby (T9)
- Gordon (T9)

We can filter out some of these stations:
- 'the other platform' in the description suggests that this station only has two platforms. This narrows our search down to
    - Emu Plains
    - Museum
    - Bondi Junction
    - Waterfall
    - Cronulla
    - Schofields
    - Macarthur
    - Richmond
- The image clearly suggests that the station is not underground. This rules out:
    - Museum
    - Bondi Junction
    - Olympic Park

If we were just to use these two pieces of information, we'd be left with 5 stations that we would have to manually search. However, looking closely, we can also see that the train tracks also seem to end at this station, with a concrete bollard terminating it. Looking at a map of the Sydney Trains network, we can only see three stations that seem to truly be 'ends' to the train network - the others continue on to other NSW TrainLink lines (for example, Macarthur to the Southern Highlands Line). This would narrow it down to just three stations (and just two if you use our prior criteria as well):

- Richmond
- Leppington
- Cronulla

At this point, you can either just check the remaining stations on Street View, or even just guess through them, yielding Richmond Station as your answer.

### Flag
`OWEEK{Richmond}`
</details>
