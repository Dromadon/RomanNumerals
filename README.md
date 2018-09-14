# Roman Numerals

This is a quite easy kata for working your TDDness. Taken from [coding dojo](https://codingdojo.org/kata/RomanNumerals/)

## Learnings
Although not so difficult, this kata can be challenging. Indeed, it showed me something that you can clearly see in the history log of this repo: if you do not pick the right test, having a design emerging can be very difficult. I ran too fast on tests needing the "generic" part of the algorithm: with 4,6,9 you already cover all the _weird_ cases of Roman numbers. Just add 14 and you're good for implementing all the generic algorithm. Things sorted out when I removed the 14 test case, and rather focused on scaling to 20,30, 40. Then the magic happned.

I may go further, and say that this is an example that _sometimes,_ you may need to think part of your code upfront. I know it hurts some of the TDD beliefs… but here I do not see how I could have known that testing 20 and 30 would make it easier than testing the next number (14). To be discussed…
