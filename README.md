# Othello
A Python-based Othello game built with Python3 and [Processing Python mode](https://py.processing.org/).

This repository contains a demo of my project for *CS5001 Intensive Foundations of CS*. You can see the full video for the game in `game-demo.mp4`. Please note that this is only a demo and the full source code cannot be shared due to potential plagiarism issues.

If you are interested in learning more about my project or seeing the full source code, please feel free to contact me directly.

## Game Basics

The game is played with black-and-white tiles on an 8x8 board. The object of the game is to have more tiles of your color than your computer opponent has of its. Play begins with 4 tiles in the middle, two white and two black.

![demo1](https://user-images.githubusercontent.com/88084099/221275289-82163057-5941-4a50-8dfc-75e6984e2011.gif)


- Play begins with 4 tiles in the middle: two white and two black. The user plays the black tile while the computer plays the white tile.
- Black goes first. That player lays down a tile, which must be in a legal position. Any white tiles in between the new black Cancel changestile and an existing black tile get flipped.
- Play continues, with the players taking turns until the whole board is covered or there are no more legal moves.
- When the board is completely covered in tiles, or there are no more legal moves, then the game is over. Whichever player has more tiles of their color on the board wins. The program will announce the winner and how many tiles they have on the board. The program will also prompt the user for their name and save their name and score (# of black tiles on the board) in a file. Ties can happen, too.

![demo2](https://user-images.githubusercontent.com/88084099/221275632-1ad92c49-b312-4946-b2c3-6ebcd247f9b1.gif)
