import pytest
from chess_puzzle import *

def equal_lists(list1,list2):
    for i in range(len(list1)):
        item1, item2 = list1[i], list2[i]
        if type(item1) != type(item2) or item1 != item2:
            return False
    return True

def test_location2index1():
    assert location2index("e2") == (5,2)
def test_location2index2():
    assert location2index("c9") != (4,8)
def test_location2index3():
    assert location2index("a1") == (1,1)
def test_location2index4():
    assert location2index("z26") == (26,26)
def test_location2index5():
    with pytest.raises(ValueError):
        location2index("Invalid")
def test_location2index6():
    with pytest.raises(ValueError):
        location2index("7")


def test_index2location1():
    assert index2location(5,2) == "e2"
def test_index2location2():
    assert index2location(7,12) != "g21"
def test_index2location3():
    assert index2location(26,26) == "z26"
def test_index2location4():
    assert index2location(8,8) == "h8"
def test_index2location5():
    with pytest.raises(TypeError):
        index2location(8)
def test_index2location6():
    with pytest.raises(TypeError):
        index2location('a',0)


wq1 = Queen(4,4,True)
wk1 = King(3,5,True)
wq2 = Queen(3,1,True)
wq3 = Queen(1,1,True)
wq4 = Queen(2,5,True)

bq1 = Queen(5,3,False)
bk1 = King(2,3,False)
bq2 = Queen(1,3,False)
bq3 = Queen(1,5,False)
bq4 = Queen(2,4,False)

B1 = (5, [wq1, wk1, wq2, wq3, bq1, bk1])
B2 = (5, [wq1, wk1, wq2, bq1, bk1])
B3 = (5, [wq1, wq4, wk1, wq2, bq1, bq4, bk1])
"""
  ♔  
   ♕ 
 ♚  ♛
     
  ♕  
"""

def test_is_piece_at1():
    assert is_piece_at(2,2, B1) == False
def test_is_piece_at2():
    assert is_piece_at(3,1, B1) == True
def test_is_piece_at3():
    assert is_piece_at(1,3, B1) == False
def test_is_piece_at4():
    assert is_piece_at(4,4, B1) == True
def test_is_piece_at5():
    with pytest.raises(TypeError):
        is_piece_at(9,5)
def test_is_piece_at6():
    with pytest.raises(ValueError):
        is_piece_at(17,4,B1)

def test_piece_at1():
    assert piece_at(3,1, B1) == wq2
def test_piece_at2():
    assert piece_at(5,3, B1) == bq1
def test_piece_at3():
    assert piece_at(2,3, B1) == bk1
def test_piece_at4():
    with pytest.raises(TypeError):
        is_piece_at(2,1)
def test_piece_at5():
    with pytest.raises(ValueError):
        is_piece_at(6,1,B1)
def test_piece_at6():
    with pytest.raises(ValueError):
        is_piece_at(0,5,B1)

def test_can_reach1():
    assert wq1.can_reach(2,2, B1) == True
def test_can_reach2():
    assert wq2.can_reach(5,2, B1) == False
def test_can_reach3():
    assert wq2.can_reach(3,5, B1) == False
def test_can_reach4():
    assert wq3.can_reach(5,5, B1) == False
def test_can_reach5():
    assert wq3.can_reach(4,1, B1) == False
def test_can_reach6():
    assert wq2.can_reach(4,2, B1) == True  
def test_can_reach7():
    assert bq1.can_reach(3,1, B1) == True
def test_can_reach8():
    assert bq1.can_reach(4,2, B1) == True    
def test_can_reach9():
    assert bq1.can_reach(3,5, B1) == False 
def test_can_reach10():
    assert wk1.can_reach(4,4, B1) == False
def test_can_reach11():
    assert wk1.can_reach(2,4, B1) == True  
def test_can_reach12():
    assert bk1.can_reach(2,4, B1) == True 

def test_can_move_to1():
    assert wq1.can_move_to(5,4, B1) == False
def test_can_move_to2():
    assert wq1.can_move_to(3,4, B1) == False
def test_can_move_to3():
    assert bq4.can_move_to(4,4, B3) == True
def test_can_move_to4():
    assert wq1.can_move_to(5,4, B1) == False
def test_can_move_to5():
    assert bq1.can_move_to(3,3, B1) == True
def test_can_move_to6():
    assert wk1.can_move_to(2,5, B2) == True
def test_can_move_to7():
    assert bk1.can_move_to(3,3, B2) == False
def test_can_move_to8():
    assert bk1.can_move_to(2,2, B2) == False
def test_can_move_to8():
    assert bk1.can_move_to(1,2, B2) == True
def test_can_move_to9():
    assert wk1.can_move_to(2,4, B2) == False
def test_can_move_to10():
    assert wk1.can_move_to(4,5, B2) == True

"""
  ♔  
   ♕ 
 ♚  ♛
     
  ♕  
"""
def test_move_to1():
    wq2a = Queen(3,4, True)

    Actual_B = wq2.move_to(3,4, B1)
    Expected_B = (5, [wq1, wk1, wq2a, wq3, bq1, bk1])
    assert Actual_B[0] == 5
    #check if actual board has same contents as expected 
    assert(equal_lists(Actual_B,Expected_B))==True
    wq2.move_to(3,1,B1) #revert back the piece to intial position

def test_move_to2():
    wq1a = Queen(5,5, True)

    Actual_B = wq1.move_to(5,5, B1)
    Expected_B = (5, [wq1a, wk1, wq2, wq3, bq1, bk1])
    assert Actual_B[0] == 5
    #check if actual board has same contents as expected 
    assert(equal_lists(Actual_B,Expected_B))==False
    wq1.move_to(4,4,B1)

def test_move_to3():
    wk1a = King(4,5, True)

    Actual_B = wk1.move_to(4,5, B2)
    Expected_B = (5, [wq1, wk1a, wq2, bq1, bk1])
    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5
    assert(equal_lists(Actual_B,Expected_B))==True
    wk1.move_to(3,5,B2)

def test_move_to4():
    wk1a = King(2,5, True)

    Actual_B = wk1.move_to(2,4, B3) # Attempt to attack 
    Expected_B = (5, [wq1, wq4, wk1a, wq2, bq1, bq4, bk1])
    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5
    assert(equal_lists(Actual_B,Expected_B))==False
    wk1.move_to(3,5,B2)

def test_move_to5():
    wq1 = Queen(4,4,True)
    wk1 = King(3,5,True)
    wq2 = Queen(3,1,True)
    bq1 = Queen(5,3,False)
    bk1 = King(2,3,False)
    B1 = (5, [wk1, wq1, wq2, bk1, bq1])
    bk1a=King(2,3,False)
    Actual_B = bk1.move_to(3,3, B1)
    Expected_B = (5, [wk1, wq1, wq2, bk1a, bq1])
    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5
    assert(equal_lists(Actual_B,Expected_B))==True

def test_move_to6():
    wq1 = Queen(4,4,True)
    wk1 = King(3,5,True)
    wq2 = Queen(3,1,True)
    bq1 = Queen(5,3,False)
    bk1 = King(2,3,False)
    B1 = (5, [wk1, wq1, wq2, bk1, bq1])
    bq1a=Queen(4,4,False)
    Actual_B = bq1.move_to(4,4, B1)
    Expected_B = (5, [wk1, wq2, bk1, bq1a])
    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5
    assert(equal_lists(Actual_B,Expected_B))==True  # attacks and captures wq1 and takes it place
 


def test_is_check1():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_check(True, B2) == True
def test_is_check2():
    B2 = (9, [wk1, wq2, bq1, bk1])
    assert is_check(False, B2) == False
def test_is_check3():
    B2 = (6, [wk1, wq2, wq4, bq1, bk1])
    assert is_check(False, B2) == True
def test_is_check4():
    B2 = (6, [wq1, wk1, wq2, bq1, bk1])
    assert is_check(True, B2) == False
def test_is_check5():
    B2 = (6, [wk1, wq2, bq3, bk1])
    assert is_check(True, B2) == True
def test_is_check6():
    B2 = (6, [wq1, wk1, wq2, bq1, bq2, bk1])
    assert is_check(True, B2) == True
"""
  ♔ ♛ 
    ♛
 ♚   ♛
     
  ♕          ♕♛ 
"""
def test_is_checkmate1():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_checkmate(True, B2) == False
def test_is_checkmate2():
    bq2 = Queen(4,5,False)
    B2 = (5, [wk1, wq2, bq1, bq2, bk1])
    assert is_checkmate(True, B2) == False
def test_is_checkmate3():
    wq3 = Queen(4,5,True)
    B2 = (7, [wq1, wk1, wq2, wq3, bq1, bk1])
    assert is_checkmate(False, B2) == True
def test_is_checkmate4():
    B2 = (7, [wq1, wk1, wq2, bq1, bk1])
    assert is_checkmate(False, B2) == False
def test_is_checkmate5():
    wk1 = King(3,5,True)
    wq2 = Queen(3,1,True)
    bq2 = Queen(4,5,False)
    bq3 = Queen(5,4,False)
    B2 = (5, [wk1, wq2, bq1, bq2, bq3, bk1])
    assert is_checkmate(True, B2) == True
def test_is_checkmate6(): #the king can escape the cm only if bq2 eliminates wq1
    bk1=King(3,4,False)
    bq1=Queen(4,3,False)
    bq2=Queen(6,3,False)
    wk1=King(1,4,True)
    wq1=Queen(3,6,True)
    wq2=Queen(6,6,True)
    B4=(6,[bk1,bq1,bq2,wk1,wq1,wq2])
    assert is_checkmate(False,B4) == False
def test_is_stalemate1():
    wk1=King(4,5,True)
    bq1=Queen(3,3,False)
    bk1=King(5,3,False)
    B=(5,[wk1,bq1,bk1])
    assert is_stalemate(True,B) == True
def test_is_stalemate2():
    bk1=King(1,1,False)
    wk1=King(3,3,True)
    wq1=Queen(3,2,True)
    B=(3,[bk1,wk1,wq1])
    assert is_stalemate(False,B) == True
def test_is_stalemate3():
    bk1=King(1,1,False)
    wk1=King(3,3,True)
    wq1=Queen(2,2,True)
    B=(3,[bk1,wk1,wq1])
    assert is_stalemate(False,B1) == False
def test_is_stalemate3():
    bk1=King(1,1,False)
    wk1=King(3,3,True)
    wq1=Queen(3,2,True)
    B=(3,[bk1,wk1,wq1])
    assert is_stalemate(True,B) == False
def test_is_stalemate4():
    assert is_stalemate(False,B1) == False
def test_is_stalemate5():
    bk1=King(6,6,False)
    wq1=Queen(4,5,True)
    wk1=King(3,4,True)
    B=(6,[bk1,wk1,wq1])
    assert is_stalemate(False,B) == True
def test_is_stalemate6():
    bk1=King(6,6,False)
    bq1=Queen(1,3,False)
    wq1=Queen(4,5,True)
    wk1=King(3,4,True)
    B=(6,[bk1,bq1,wk1,wq1])
    assert is_stalemate(False,B) == False

def test_read_board1():
    wk1 = King(3,5,True)
    wq2 = Queen(3,1,True)
    B = read_board("board_examp.txt")
    B1 = (5, [wk1, wq1, wq2, wq3, bk1, bq1])
    assert B[0] == 5
    assert(equal_lists(B,B1))==True
def test_read_board2():
    wk1 = King(3,5,True)
    wq2 = Queen(3,1,True)
    B1 = (27, [wk1, wq1, wq2, wq3, bk1, bq1])
    with pytest.raises(IOError):
        read_board("example1.txt")
def test_read_board3():
    wk1 = King(3,5,True)
    wq2 = Queen(3,1,True)
    B = read_board("example2.txt")
    B3 = (5, [wq1, wq4, wk1, wq2, bq1, bq4, bk1])
    assert B[0]!=B3[0]
    assert(equal_lists(B,B3))==False
def test_read_board4():
    wk1 = King(3,5,True)
    wq2 = Queen(3,1,True)
    B = read_board("example3.txt")
    B3 = (10, [wq1, wq4, wk1, wq2, bq1, bq4, bk1])
    assert B[0]==B3[0]
    assert(equal_lists(B,B3))==True
def test_read_board5():
    wk1 = King(3,5,True)
    wq2 = Queen(3,1,True)
    B1 = (5, [wk1, wq1, wq2, wq3, bk1, bq1])
    with pytest.raises(IOError):
        read_board("example4.txt")
def test_read_board6():
    wk1 = King(3,5,True)
    wq2 = Queen(3,1,True)
    with pytest.raises(IOError):
        read_board("no_king.txt")
def test_conf2unicode1():
    wk1 = King(3,5,True)
    wq2 = Queen(3,1,True)
    B1 = (5, [wk1, wq1, wq2, bk1, bq1])
    assert conf2unicode(B1).rstrip("\n") == "  ♔  \n   ♕ \n ♚  ♛\n     \n  ♕  "
def test_conf2unicode2():
    wk1 = King(3,5,True)
    wq2 = Queen(3,1,True)
    bk1 = King (1,1,False)
    bq1 = Queen(1,3,False)
    B = (5, [wk1, wq2, bk1, bq1])
    assert conf2unicode(B).rstrip("\n") == "  ♔  \n     \n♛    \n     \n♚ ♕  "
def test_conf2unicode3():
    wk1 = King(3,5,True)
    wq2 = Queen(3,1,True)
    B1 = (5, [wk1, wq1, wq2, bk1, bq1])
    assert conf2unicode(B1).rstrip("\n") != "  ♔  \n   ♕ \n ♚ ♛ \n     \n  ♕  "
def test_conf2unicode4():
    wk1 = King(3,5,True)
    wq2 = Queen(3,1,True)
    bk1 = King (1,1,False)
    bq1 = Queen(1,3,False)
    B = (5, [wk1, wq2, bk1, bq1])
    assert conf2unicode(B).rstrip("\n") != "  ♔  \n     \n♛    \n    \n♚ ♕  "
def test_conf2unicode5():
    wk1 = King(3,4,True)
    wq2 = Queen(3,1,True)
    bk1 = King (1,1,False)
    bq1 = Queen(1,3,False)
    B4 = (4, [wk1, wq2, bk1, bq1])
    assert conf2unicode(B4).rstrip("\n") == "  ♔ \n♛   \n    \n♚ ♕ "
def test_conf2unicode6():
    wk1 = King(1,1,True)
    wq2 = Queen(2,1,True)
    bk1 = King (1,2,False)
    bq1 = Queen(2,2,False)
    B4 = (2, [wk1, wq2, bk1, bq1])
    assert conf2unicode(B4).rstrip("\n") == "♚♛\n♔♕"
