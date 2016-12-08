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

[DotMap](https://github.com/drgrib/dotmap) - Allows for dot notation access of a dictionary object.
`pip install dotmap`


## Launch GoGo

`python3 gogo`


## Playing Gogo


#### Controls

![Left Player's Move Cursor Controls](/README_IMG/arrows_move_cursor_controls.png "Left Player Arrows move controls")

![Right Player's Move Cursor Controls](/README_IMG/wasd_cursor_controls.png "Right Player WASD move controls")

##### Move your cursor around the board to select a point using the arrow keys.

![Left Player Place Stone Controls](/README_IMG/space_place_stone_controls.png "Left Player Place controls")
![Right Player Place Stone Controls](/README_IMG/enter_place_stone_controls.png "Right Player Place controls")

##### Press Spacebar to place your stone.


#### Placing Stones

Players take it in turns to place stones on the points made by intersecting lines on the board.  When two or more of your stones immediately connect vertically or horizontally, they become part of a group. Groups behave in the same way as single stones and so must be completely surrounded to be captured.  Stones of the same colour diagonal to each other are not part of a group.


#### Liberties

The lines on the board are called liberties.  Think of liberties as the life lines to each group of stones.  When a group of your stones is surrounded by your opponent, that group no longer has liberties and they are taken as prisoners.


#### Winning GoGo

+ **Timeout**

If you run out of time, you automatically lose.

+ **Pass**

Players can pass.  A consecutive pass from each player ends the game and the game is scored.  The winner is the player with the most prisoners and territory.

+ **Resign**

You can resign, handing the win to your opponent.


#### Scoring

At the end of the game...

Territory is counted....
Any stones your opponent has taken as prisoners are deducted from your territory score.


#### Suicide

You can't play a stone on a point that would leave your group with no liberties.  That would be SUICIDE!!!  Although....you can play this move if it would immediately take all the liberties of your opponent's group.


#### Ko


