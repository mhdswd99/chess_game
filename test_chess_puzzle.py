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
    assert bq4.can_move_to(4,4, B3) == False
def test_can_move_to4():
    assert wq1.can_move_to(5,4, B1) == False
def test_can_move_to5():
    assert bq1.can_move_to(3,3, B1) == True


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
    #check if actual board has same contents as expected 
    assert(equal_lists(Actual_B,Expected_B))==True

def test_move_to2():
    wq1a = Queen(5,5, True)

    Actual_B = wq1.move_to(5,5, B1)
    Expected_B = (5, [wq1a, wk1, wq2, wq3, bq1, bk1])
    #check if actual board has same contents as expected 
    assert(equal_lists(Actual_B,Expected_B))==False

def test_move_to3():
    wk1a = King(4,5, True)

    Actual_B = wk1.move_to(4,5, B1)
    Expected_B = (5, [wq1, wk1a, wq2, wq3, bq1, bk1])
    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


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

def test_is_checkmate1():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_checkmate(True, B2) == False

def test_read_board1():
    B = read_board("board_examp.txt")
    assert B[0] == 5

    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


def test_conf2unicode1():
    assert conf2unicode(B1).rstrip("\n") == "  ♔  \n   ♕ \n ♚  ♛\n     \n  ♕  "
