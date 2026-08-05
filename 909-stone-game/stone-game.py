class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
Solution sauce: https://leetcode.com/problems/stone-game/solutions/8435492/solution-by-la_castille-s2sg

This one is so weird. Just trust the process
We can take the piles array, and divide it into all the numbers on even indices and all the numbers on odd indices.
Let's color the even indices pink and odd indices blue (0-indexed)
So [5, 3, 6, 4, 2, 5] becomes
pink: 5, 6, 2
blue: 3, 4, 5
The elements will be kept the same color as the game goes on.

Now remember the constraints that the array always starts off as even number of elements
And that sum(piles) is odd to prevent ties

Now notice that since Alice starts first, whenever it's her turn, the array has an even number of elements
That means one end will be pink and another end will be blue

And when Bob goes, the array will have an ODD number of elements, so BOTH ends will be either blue or pink

That means Alice ALWAYS gets a choice between picking a blue or pink item
So Alice can legit just pick either ALL the pink items or ALL the blue items
And whichever color has the larger sum will make Alice win.
So when it's her turn the optimal choice is the color that gives you the largest sum

But Bob DOESN'T have a choice
So if Alice plays optimally, Bob just gets the other color, which will be the smaller sum

So Alice always wins. In code... literally just return true
And Bob is always a loser like me :(
        """
        return True