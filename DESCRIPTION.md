## Playing Gogo

Go is a classic turn based strategy game for two players.  Your goal is to surround your opponent, claiming territory and taking prisoners.

## Controls

### Black Player

![Left Player's Move Cursor Controls](/README_IMG/wasd_cursor_controls.png "Left Player WASD move controls")

##### Move your cursor around the board to select a point using the W,A,S,D keys to move Up,Left,Down and Right.

![Left Player Place Stone Controls](/README_IMG/space_place_stone_controls.png "Left Player Place controls")

##### Press Enter to place your stone.

### White Player

![Right Player's Move Cursor Controls](/README_IMG/arrows_move_cursor_controls.png "Right Player Player Arrows move controls")

##### Move your cursor around the board to select a point using the arrow keys to move Up,Left,Down and Right.

![Right Player Place Stone Controls](/README_IMG/enter_place_stone_controls.png "Right Player Place controls")

##### Press Enter to place your stone.


## Placing Stones

Players take it in turns to place stones on the points made by intersecting lines on the board.  When two or more of your stones immediately connect vertically or horizontally, they become part of a group. Groups behave in the same way as single stones and so must be completely surrounded to be captured.  Stones of the same colour diagonal to each other are not part of a group.


## Liberties

The lines on the board are called liberties.  Think of liberties as the life lines to each group of stones.  When a group of your stones is surrounded by your opponent, that group no longer has liberties and they are taken as prisoners.


## Winning GoGo

+ **Timeout**

If you run out of time, you automatically lose.

+ **Pass**

Players can pass.  A consecutive pass from each player ends the game and the game is scored.  The winner is the player with the most prisoners and territory.

+ **Resign**

You can resign, handing the win to your opponent.


## Scoring

At the end of the game...

Territory is counted....
Any stones your opponent has taken as prisoners are deducted from your territory score.


## Suicide

You can't play a stone on a point that would leave your group with no liberties.  That would be SUICIDE!!!  Although....you can play this move if it would immediately take all the liberties of your opponent's group.


## Ko

You can't play a move that would return the board to its previous state.  This is called Ko.  You risk getting into an endless loop.  If the move is Ko, you could attack somewhere else breaking the Ko and allowing you to move forwards with play.