Name : Puja Ankitha Ivaturi
Id   : 1002083111
Programming Language used: Python 3

How the code is structured?
I have used sys module to import system arguments, inf value, -inf value.
I have implemented 4 functions in it.
They are:
evaluate_score() - This helps in getting the score we may get on the choice of selecting a node (red, blue)
updated_piles() - This helps in traversing down the tree by the depth of 1 without changing the current redpile bluepile numbers. Used just to check the value of selecting a node in depth limit to find the optimal solution in minmax
minmax_by_depth_limit() - finding the best possible move to take by the computer confining to the depth search so that it won't go till longer depths on big inputs
red_blue_nim() - Starts the game and calls the function by turns. Human gives input manually, and for computers' move it calls minmax function


How to run the code?
Commands:
python red_blue_nim.py 2 2 human 5
python red_blue_nim.py 2 2 computer 2
python red_blue_nim.py 5 3
