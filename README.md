# project_three
Python project battleships

Project 3 Details
Basic battleships game, written in python. 
Preliminary Thoughts
The battleships game has a grid shaped “board” on which players search for their opponent’s fleet. Initially, the search is by more-or-less random “shots”. If a hit is scored, however, then there is an attempt to zero in on the ship by shooting around the initial hit until a new hit is made. As ships are either horizontally or vertically aligned this completes the process of finding the ship and the next shots will all be hits. The program will mimic this process, by algorithm, so initially shots will be random. Once a hit is registered then a process of elimination will disclose the rest of the ship which can then be destroyed logically.
The second major algorithm to consider is the placement of ships. Each fleet is a pyramid distribution of differently sized ships with the battleship being the largest. Alignment is random, the ships can be either horizontal or vertical. As ships fill up the grid, the chances of superimposition of one ship on another increases. This will be one of the most important problems to solve in this algorithm.



For the random assignments, the math module is imported.


