"""
ttt_logic
  This module contains the logic to drive a two-player Tic-Tac-Toe
 game.
"""
player="X"
board=[ None, None, None, None, None, None, None, None, None]
boardReference=["NorthWest", "North", "NorthEast", "West", "Center", "East", "SouthWest", "South", "SouthEast"]



#---------------------------------------------------------------
#  Define any global variables this module may need to maintain the
#  state of a Tic-Tac-Toe game.
#---------------------------------------------------------------


def check_status():
    """
    Checks to see if either player has won or if the board is filled.
    Returns a two-tuple in which the first component is the string
    "X" or the string "O" or the value None; the second component
    of the tuple is one of the following strings that indicates the
    Tic-Tac-Toe board's status:
      "Playing"     No one has won and a move is available
      "Win_NW_NE"   Win across top row
      "Win_W_E"     Win across middle row
      "Win_SW_SE"   Win across bottom row
      "Win_NW_SW"   Win along left colunm
      "Win_N_S"     Win along center column
      "Win_NE_SE"   Win along right column
      "Win_NW_SE"   Win from left-top corner to right-bottom
      "Win_NE_SW"   Win from right-top corner to left-bottom
      "Draw"        All squares filled with no winner
    The first component of the resulting tuple represents the game
    winner, and the second component of the tuple represents the
    winning configuration.  If the status component is "Playing" or
    "Draw", the winner component should be None; for example, the
    tuple ("X", "Win_NE_SE") would be a valid return value, but
    neither ("X", "Draw") nor ("O", "Playing") represents a valid
    result.
    """
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    winref=[ "Win_NW_NE" ,"Win_W_E" ,"Win_SW_SE" ,"Win_NW_SW" ,"Win_N_S" ,"Win_NE_SE" ,"Win_NW_SE" ,"Win_NE_SW"]
    for i in win:
        won1 = board[i[0]]
        won2 = board[i[1]]
        won3 = board[i[2]]
        if won1==won2 and won2==won3:
            if won1 != None:
                return won1,winref[win.index(i)]
    if None not in board :
        return None,"Draw"
    else:
        return None, "Playing"




def move(location):
    """
    Places the current player's mark at the given location, if possible.
    The caller must pass one of the following strings specifying
    the location:
      "NorthWest"   Top, left square
      "North"       Top, middle square
      "NorthEast"   Top, right square
      "West"        Left, middle square
      "Center"      Center square
      "East"        Right, middle square
      "SouthWest"   Bottom, left square
      "South"       Bottom, middle square
      "SouthEast"   Bottom, right square

    Returns True if the specified location is available (that is,
    the global variable keeping track of that position is None);
    otherwise the function returns False for an illegal move.
    If the current player makes a valid move, the function ensures
    that control passes to the other player; otherwise, the move
    function does not affect the current player.
    """
    mover=boardReference.index(location)
    global board
    global player
    current_player=player

    if board [mover]==None:
        board[mover]=current_player
        change_player()
        return True
    else:
        return False

def current_player():
    """
    Returns the player whose turn it is to move.  This allows the
    presentation to report whose turn it is.
    Return value is one of either "X" or "O".
    """
    return player   # Replace with your implementation


def set_player(new_player):
    """
    Sets the current player.  Useful for games that require the
    player to answer a question correctly before a move.  If the
    player answers incorrectly, the turn moves to the opponent.
    Valid values for new_player are "X" or "O"; any other strings
    will not change the current player.
    """
    if "X"==new_player:
        player="X"
    elif "O"==new_player:
        player="O"
            # Replace with your implementation


def change_player():
    """
    Alternates turns between players.  X becomes O, and O becomes X.
    """
    global player
    if player=="O":
        player="X"
    elif player=="X":
        player="O"    # Replace with your implementation


def look(location):
    """
    Returns the mark at the given location.  The caller must pass
    one of the following strings specifying the location:
      "NorthWest"   Top, left square
      "North"       Top, middle square
      "NorthEast"   Top, right square
      "West"        Left, middle square
      "Center"      Center square
      "East"        Right, middle square
      "SouthWest"   Bottom, left square
      "South"       Bottom, middle square
      "SouthEast"   Bottom, right square

    The function's valid return values are None, "X", or "O".
    Returns None if neither player has marked
    the given location.  The function also returns None if the
    caller passes any string other than one of the location strings
    listed above.
    This function allows the presentation to draw the contents
    of the Tic-Tac-Toe board.
    """
    return board[boardReference.index(location)]   # Replace with your implementation


def initialize_board():
    """
    Make all the board locations empty and set current player to
    "X" (that is, reset the board to the start of a new game)
    """
    global player
    global board

    player="X"
    board=[ None, None, None, None, None, None, None, None, None]
    # Replace with your implementation


if __name__ == "__main__":
    print(look("Center"))
    # pass   #  This module is not meant to be run as a standalone program
