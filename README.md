Poker Game
============

## Prerequisites

You should have python installed.
Follow this steps if python is not installed
https://wiki.python.org/moin/BeginnersGuide/Download

You should also have pip installed as a python library
Follow this steps if pip is not installed
https://pip.pypa.io//en/latest/installing/

## Installation

```
pip install deuces
```

If it prompts that some package is not there then do
```
pip install <package-name>
```

## Prepare Input

For testing I have already created a input.txt file 

If you want to test some other logs then
1. Copy predefined sample steps or logs to input.txt file
2. Suits should be second and Ranks should be first and also capitalized.
	Example:-	Instead of c8 replace it with 8c
				Instead of cj replace it with Jc
3. For Rank 10 user T instead
	Example:-	Instead of h10 replace it with Th
4. For different moves during USER TURN
	Example:-	For "CALL" use "called"
				For "FOLD" use "folded"
				For "RAISE" use "raised"
				For "CHECK" use "checked"
				For "TIMEOUT" use "timedout"
	
For checking what changes I have made to the input do a diff checking by pasting
original input on the left and my version on the right in following website, you will see the difference
https://www.diffchecker.com/diff

## Execution

Once you are done with all of the above things now is the time to run a poker game
```
python interface.py
```

Then it will prompt you things which you have to input one by one.
This program suggests from the already existing log what next step a player should take.

Enjoy modifying the input.txt and testing it !!!