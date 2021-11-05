# John Conway's Game of Life
Dear gamers I present you the most engaging game You have __ever__ played. 

So, are you ready? 

Are you ready for this?

Are you hanging on the edge of your seat?

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
3. Go ahead and click the plane as much as You want.
4. When You are ready click the __START__ button.

## But how it works?
This application is a simulation of certain cellular automaton. According to Wikipedia:
>The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.
>It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.
>One interacts with the Game of Life by creating an initial configuration and observing how it evolves.
>It is Turing complete and can simulate a universal constructor or any other Turing machine.

So, the game takes place on a plane with a given size( 50x50 by default) and in this case the plane is sphere like
which means that ceiling wraps with the floor and right side wraps with the left. In simpler words: the plane have no boundaries.

>It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.

All cells on the plane can be in two states: alive or dead.
You can alter their state by simply clicking on them and by this You determine the initial state of the game.
(Notice: I doesn't mean You cannot alter the cell's state during the simulation.)
When simulation starts every next state of every cell is calculated by this rules:
- If a cell is __alive__ and have __2 or 3__ living_ neighbours it __will live on__. Otherwise it will die due to underpopulation or overpopulation.
- If a cell is __dead__ and have __exactly 3__ living neighbours it __becomes alive__ due to reproduction.

A quick word about the neighborhood: Every cell have 8 neighbors(up, down, left, right and 4 corners)

Knowing this You can start your adventure. Game on!

## Tips
There are some pattern categories like still lifes, oscillators and spaceships. I will give you a quick look but it is more fun if You figure that out on Your own.

![Beehive](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Game_of_life_beehive.svg/98px-Game_of_life_beehive.svg.png)

![Pulsar](https://upload.wikimedia.org/wikipedia/commons/0/07/Game_of_life_pulsar.gif)

![Lightwight_spaceship](https://upload.wikimedia.org/wikipedia/commons/3/37/Game_of_life_animated_LWSS.gif)
