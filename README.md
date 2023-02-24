# Othello
A Python-based Othello game built with [Processing Python mode](https://py.processing.org/).
## Instructions

[Processing 3.5.4](https://processing.org/releases) and Python3 are needed for playing the game. To start the game, open the folder in Processing and start with `othello.pyde`. 

## Game Basics

The game is played with black-and-white tiles on an 8x8 board. The object of the game is to have more tiles of your color than your computer opponent has of its. Play begins with 4 tiles in the middle, two white and two black.

- Play begins with 4 tiles in the middle: two white and two black. The user plays the black tile while the computer plays the white tile.
- Black goes first. That player lays down a tile, which must be in a legal position. Any white tiles in between the new black Cancel changestile and an existing black tile get flipped.
- Play continues, with the players taking turns until the whole board is covered or there are no more legal moves.
- When the board is completely covered in tiles, or there are no more legal moves, then the game is over. Whichever player has more tiles of their color on the board wins. The program will announce the winner and how many tiles they have on the board. The program will also prompt the user for their name and save their name and score (# of black tiles on the board) in a file. Ties can happen, too.

## Disclaimer
This is a personal project for *CS5001 Intensive Foundations of CS*. A Git repository was not used originally. For academic integrity, please do NOT reuse any code in this repository if you are working on your project for a related course.
