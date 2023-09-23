# Sliding-Puzzle-Game
A puzzle that can be slid horizontally or vertically and has one empty space among it.

## Overview
At the start of the game, the user will be asked to input a username. Then, it will output a brief introduction of the game to tell the user how to finish it. The user is asked to input the dimensions of the puzzle, ranging from 3x3 to 10x10. The user is also asked to input four letters separated by space used for the left, right, up, and down movement. A randomized puzzle will be outputted, and the game begins.
Users can only move the tiles adjacent to the empty tile in the direction outputted by the program. If the user gives a wrong input, it repeatedly asks for a new one. The program will output the updated puzzle whenever a correct input is provided. The number of steps will be printed out when the user has solved the puzzle. The program will ask the user if the user wants to play again or end the game.

## Program structure
1.	Take the input of the dimension of the puzzle. 
2.	Create the ordered list and the randomized list.
    - Reformat the lists to form a nested list of the ordered list (the solved puzzle).
    - Reformat the lists to form a nested list of the randomized list (the puzzle).
      * Check if the puzzle is solvable or not.
      * If it is not solvable, reshuffle the list.
4.	Take the input of the four letters used for the movement during the game.
5.	Print the puzzle.
6.	While the puzzle is not ordered,
    - The program will print different output according to the position of the blank tile.
    -	The user can swap the tiles in the puzzle if the letters are inputted before, and it is a valid movement in the puzzle.
    -	The program will print the updated puzzle.
7.	If the puzzle is solved, the program will print the number of steps used and ask if the user wants to play again or end the game.
