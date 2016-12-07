# GoGo


## Download

To play GoGo:

1. Make sure you have [git](https://git-scm.com/) installed.
2. In your Command Line run:
`git clone https://github.com/mathewtrivett/gogo`

3. Then:
`cd gogo`


## Install Dependencies

[Python3](https://www.python.org/downloads/) - GoGo will only work with Python3.x to make sure you have Python 3 installed run:
`python3 --version`

[PyGame](http://www.pygame.org/hifi.html) - To make sure your pygame installation is compatible with Python 3 run:
`pip3 install pygame`

[DotMap](https://github.com/drgrib/dotmap) - Allows for dot notation access of a dict object.
`pip install dotmap`


## Launch GoGo

`python3 gogo`


## Playing Gogo

#### Go

Go is a classic turn based strategy game for two players.  Your goal is to surround your opponent, claiming territory and taking prisoners.


#### Placing Stones

Players take it in turns to place stones on the points made by intersecting lines on the board.  When two or more of your stones connect either vertically or horizontally, they become part of a group.  A group essentially behaves in the same way as a single stone


#### Liberties

The lines on the board are called liberties.  You can think of liberties as life lines to each stone.  When a group of your stones are surrounded by your opponent, that group no longer has liberties and they are taken as prisoners.


#### Winning GoGo

+ **Timeout**

If a player runs out of time, they automatically lose.

+ **Pass**

Players can pass.  A consecutive pass from each player ends the game and the game is scored.  The winner is the player with the most prisoners and territory.

+ **Resign**

Players can resign, handing the win to their opponent.


#### Scoring



#### Suicide

You can't play a stone on a point that would mean you immediately had no liberties.  That would be SUICIDE!!!  Although

#### Ko









