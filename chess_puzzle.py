import copy
from random import randint

def location2index(loc: str) -> tuple[int, int]: #might need to add !isalpha exception?
    '''converts chess location to corresponding x and y coordinates'''
    return (ord(loc[0])-ord("a")+1,int(loc[1:]))
    
	
def index2location(x: int, y: int) -> str: #might need to add !isnumeric exception?
    '''converts  pair of coordinates to corresponding location'''
    return chr(x + ord('a')-1) + str(y)

class Piece:
    pos_x : int	
    pos_y : int
    side : bool #True for White and False for Black
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values'''
        self.pos_x=pos_X
        self.pos_y=pos_Y
        self.side=side_

Board = tuple[int, list[Piece]]


def is_piece_at(pos_X : int, pos_Y : int, B: Board) -> bool:
    '''checks if there is piece at coordinates pox_X, pos_Y of board B'''
    if pos_X>B[0] or pos_Y>B[0] or pos_X<1 or pos_Y<1:raise(ValueError)
    for pieces in B[1]:
        if pieces.pos_x==pos_X and pieces.pos_y==pos_Y:
            return True          
    return False



def piece_at(pos_X : int, pos_Y : int, B: Board) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B 
    assumes some piece at coordinates pox_X, pos_Y of board B is present
    '''
    if pos_X>B[0] or pos_Y>B[0] or pos_X<1 or pos_Y<1:raise(ValueError)
    for piece in B[1]:
        if piece.pos_x==pos_X and piece.pos_y==pos_Y:
            return piece


class Queen(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X,pos_Y,side_)
    def __eq__(self, other) -> bool:
        if not isinstance(other, Queen):    return False
        return (self.pos_x == other.pos_x and self.pos_y == other.pos_y and self.side == other.side)
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''
        checks if this queen can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule1] and [Rule3] (see section Intro)
        Hint: use is_piece_at
        '''
        if is_piece_at(pos_X, pos_Y, B):
            if piece_at(pos_X, pos_Y, B).side == self.side:
              return False
        if (self.pos_x == pos_X or self.pos_y == pos_Y or abs(self.pos_x - pos_X) == abs(self.pos_y - pos_Y)):
            step_x = 0 if self.pos_x == pos_X else (pos_X - self.pos_x) // abs(pos_X - self.pos_x)
            step_y = 0 if self.pos_y == pos_Y else (pos_Y - self.pos_y) // abs(pos_Y - self.pos_y)
            x, y = self.pos_x + step_x, self.pos_y + step_y
            while x != pos_X or y != pos_Y:
                if is_piece_at(x, y, B):
                    return False
                x += step_x
                y += step_y
            return True
        return False

    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''
        checks if this queen can move to coordinates pos_X, pos_Y
        on board B according to all chess rules
        
        Hints:
        - firstly, check [Rule1] and [Rule3] using can_reach
        - secondly, check if result of move is capture using is_piece_at
        - if yes, find the piece captured using piece_at
        - thirdly, construct new board resulting from move
        - finally, to check [Rule4], use is_check on new board
        '''
        q=Queen(pos_X,pos_Y,self.side)
        if self.can_reach(pos_X,pos_Y,B):
            coppied_board = (B[0], B[1].copy())
            if is_piece_at(pos_X, pos_Y, B) == False:
                coppied_board[1].remove(piece_at(self.pos_x, self.pos_y, B))
                coppied_board[1].append(q)
            elif is_piece_at(pos_X, pos_Y, B) and piece_at(pos_X, pos_Y, B).side != self.side:
                coppied_board[1].remove(piece_at(pos_X, pos_Y, B))
                coppied_board[1].append(q)
            else:
                return False

            if is_check(self.side, coppied_board):
                return False
            return True
        return False

    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this queen to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''
        if self.can_move_to(pos_X, pos_Y, B):
            self.pos_x=pos_X
            self.pos_y=pos_Y
            copied_board = (B[0], B[1].copy())
            self.can_move_to(pos_X, pos_Y, copied_board)
            return copied_board
        return B


class King(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        super().__init__(pos_X,pos_Y,side_)
    def __eq__(self, other) -> bool:
        if not isinstance(other, King):    return False
        return (self.pos_x == other.pos_x and self.pos_y == other.pos_y and self.side == other.side)
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule2] and [Rule3]'''
        if is_piece_at(pos_X, pos_Y, B):
            if piece_at(pos_X, pos_Y, B).side == self.side:
                return False
        if abs(self.pos_x-pos_X) <=1 and abs(self.pos_y-pos_Y) <=1 and (self.pos_x,self.pos_y)!=(pos_X,pos_Y):
            if is_piece_at(pos_X, pos_Y, B) and piece_at(pos_X,pos_Y,B).side==False:
                return False
            return True
        return False
    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
        k=King(pos_X,pos_Y,self.side)
        if self.can_reach(pos_X,pos_Y,B):
            coppied_board = (B[0], B[1].copy())
            if is_piece_at(pos_X, pos_Y, B) == False:
                coppied_board[1].remove(piece_at(self.pos_x, self.pos_y, B))
                coppied_board[1].append(k)
            elif is_piece_at(pos_X, pos_Y, B) and piece_at(pos_X, pos_Y, B).side != self.side:
                coppied_board[1].remove(piece_at(pos_X, pos_Y, B))
                coppied_board[1].append(k)
            else:
                return False

            if is_check(self.side, coppied_board):
                return False
            return True
        return False
    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''
        if self.can_move_to(pos_X, pos_Y, B):
            self.pos_x=pos_X
            self.pos_y=pos_Y
            copied_board = (B[0], B[1].copy())
            self.can_move_to(pos_X, pos_Y, copied_board)
            return copied_board
        return B


def is_check(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is check for side
    Hint: use can_reach
    '''
    king_pos=None
    for piece in B[1]:
        if isinstance(piece,King) and piece.side==side:
            king_pos=(piece.pos_x,piece.pos_y)
    if king_pos is None:
        raise ValueError
    for piece in B[1]:
        if piece.side != side and piece.can_reach(king_pos[0], king_pos[1], B):
            return True
    return False
def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints: 
    - use is_check
    - use can_move_to
    '''
    if not is_check(side,B): return False
    if is_check(side,B):
        for piece in B[1]:
            if piece.side == side:
                for i in range(1,B[0]+1):
                    for j in range (1,B[0]+1):
                        if piece.can_move_to(i, j, B):
                            new_board = piece.move_to(i, j, B)
                            if not is_check(side, new_board):
                                return False                  
    return True


def is_stalemate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is stalemate for side

    Hints: 
    - use is_check
    - use can_move_to 
    '''
    if is_check(side,B):    return False
    for piece in B[1]:
        if piece.side == side:
            for i in range (1,B[0]+1):
                for j in range (1,B[0]+1):
                    if piece.can_move_to(i,j,B):
                        return False
    return True

def read_board(filename: str) -> Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''
    k=1
    side=None
    all_pieces=[]
    with open(filename,'r') as fp:
        S=fp.readline().rstrip()
        if not S.isnumeric():
            raise IOError
        s=int(S)
        if s<1 or s>26:
            raise IOError
        while k<3:
            if k==1:    side=True
            else:   side=False
            lines=fp.readline().rstrip()
            if not lines:
                raise IOError
            pieces=[]
            for piece in lines.split(", "):
                pieces.append(piece.strip())
            num_king = 0
            for j in pieces:
                if not (j.startswith('K')or j.startswith('Q')):
                    raise IOError
                piece_class,pos = j[0],j[1:]
                ind=location2index(pos)
                if piece_class=='K':
                    all_pieces.append(King(ind[0],ind[1],side))
                    num_king+=1
                elif piece_class=='Q':
                    all_pieces.append(Queen(ind[0],ind[1],side))
            if num_king!=1:
                raise IOError
            k+=1
        incorrect_lines=fp.readline().strip()
        if incorrect_lines:
            raise IOError
    return (s,all_pieces)


def save_board(filename: str, B: Board) -> None:
    '''saves board configuration into file in current directory in plain format'''


def find_black_move(B: Board) -> tuple[Piece, int, int]:
    '''
    returns (P, x, y) where a Black piece P can move on B to coordinates x,y according to chess rules 
    assumes there is at least one black piece that can move somewhere

    Hints: 
    - use methods of random library
    - use can_move_to
    '''

def conf2unicode(B: Board) -> str: 
    '''converts board cofiguration B to unicode format string (see section Unicode board configurations)'''


def main() -> None:
    '''
    runs the play

    Hint: implementation of this could start as follows:
    filename = input("File name for initial configuration: ")
    ...
    '''    

if __name__ == '__main__': #keep this in
   main()


