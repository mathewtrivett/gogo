# GoGo

Go is a classic turn based strategy game for two players.  Your goal is to surround your opponent, claiming territory and taking prisoners.

## Download

To play GoGo:

1. Make sure you have [git](https://git-scm.com/) installed.
2. In your Command Line run:
`git clone https://github.com/mathewtrivett/gogo`

3. Then:
`cd gogo`


## Install Dependencies

[Python3](https://www.python.org/downloads/) - GoGo will only work with Python3.x. To make sure you have Python 3 installed run:
`python3 --version`.  If you don't have Python3, install it by visiting [Python3](https://www.python.org/downloads/) and follow the instructions there.

[PyGame](http://www.pygame.org/hifi.html) - Make sure your pygame installation is compatible with Python 3 run:
`pip3 install pygame`

[DotMap](https://github.com/drgrib/dotmap) - Allows for dot notation access of a dict object.
`pip install dotmap`


## Launch GoGo

`python3 gogo`


## Playing Gogo


#### Placing Stones

Players take it in turns to place stones on the points made by intersecting lines on the board.  When two or more of your stones immediately connect vertically or horizontally, they become part of a group. Groups behave in the same way as a single stone and so must be completely surrounded to be captured.  Stones of the same colour diagonal to each other are not part of a group.


#### Liberties

The lines on the board are called liberties.  Think of liberties as the life lines to each stone.  When a group of your stones are surrounded by your opponent, that group no longer has liberties and they are taken as prisoners.


#### Winning GoGo

+ **Timeout**

If you run out of time, you automatically lose.

+ **Pass**

Players can pass.  A consecutive pass from each player ends the game and the game is scored.  The winner is the player with the most prisoners and territory.

+ **Resign**

You can resign, handing the win to your opponent.

#### Scoring

At the end of the game...

#### Suicide

You can't play a stone on a point that would leave your group with no liberties.  That would be SUICIDE!!!  Although....you can play this move if it would immediately take the liberties of your opponents.


#### Ko


