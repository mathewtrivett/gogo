from board import Board 
from group import Group

board = Board(9)
group1 = Group('black',[(0,0)])
group2 = Group('white',[(2,2),(1,0),(0,1)])
group3 = Group('white',[(5,5)])

board.addGroup(group1)
board.addGroup(group2)
board.addGroup(group3)
board.getGroup((0,0))
