# John Conway's Game of Life
Dear gamers I present you the most engaging game You have __ever__ played. 
So, are you ready? 
Are you ready for this?
Are you hanging on the edge of the sit?

## How to play?
0. Install Python3 on your machine. 
1. Open a terminal window and navigate to the __03_gol__ folder.
2. Run the file using:
  ```
  python main.py
  ```
  or if You want to specify the width and height of the plane:
  ```
  python main.py --size 100 80
  ```
3. Go ahed and click the plane as much as You want.
4. When You are ready click the __START__ butotn.

## But how it works?
This application is a simulation of certain cellullar automaton. According to Wikipedia:
>The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.
>It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.
>One interacts with the Game of Life by creating an initial configuration and observing how it evolves.
>It is Turing complete and can simulate a universal constructor or any other Turing machine.

So, the game takes place on a plane with a given size( 50x50 by default) and in this case the plane is sphere like
whisch means that ceiling wraps with the floor and right side wraphs with the left. In simpler words: the plane have no boundaries.

>It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.

All cells on the plane can be in two states: alive or dead.
You can alter thair state by simply clicking on them and by this You determine the initial state of the game.
