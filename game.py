from board import Board 
from group import Group

board = Board(9)
group1 = Group('black',(0,0))
group2 = Group('white',(1,2))
board.addGroup(group1)
board.addGroup(group2)
print(board.groups)


