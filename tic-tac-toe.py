# assignment: W02 Prove: Developer - Solo Code Submission
# author: Adil rafi

import time

print("Welcome to the world of Tic Tac Toe")
print()

time.sleep(1)

print("Let's start")
print()

time.sleep(1)

# Global Variables

# This is our game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_on = True

winner = None

current_player = "X"

# Functions

# main functions
def main():
  display_board()
  # Loop until the game stops (winner or tie)
  while game_still_on:
    #handle a turn
    handle_turn(current_player)
    #check if game is over
    check_if_game_over()
    #Flip to the other player
    flip_player()
  #Game is over, print the winner or tie
  if winner == "X" or winner == "O":
    print(winner  + " won.")
  elif winner == None:
    print("Game tie.")

#handle turn function
def handle_turn(player):

  print(player + "'s turn.")
  position = input("Select your position from 1-9: ")
  valid = False
  while not valid:
    #make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Invalid selection. Select a position from 1 to 9: ")
    #get corrct index in our board list
    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else: 
      print("You can't go there. Go again.")

  board[position] = player

  display_board()


# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])
  print("\n")

#check if one of the players has won
def check_if_game_over():
  check_if_win()
  check_if_tie()

#check if one of the players has won
def check_if_win():
  #global veriable
  global winner

  row_winner = check_rows()
  column_winner = check_columns()
  diagnal_winner = check_diagnals()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagnal_winner:
    winner = diagnal_winner
  else:
    winner = None


def check_rows():
  #global veriable
  global game_still_on
  #check if any of the rows have all the same value (and is not empty)
  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board[5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"
  #if any row does have a match, flag that there is a win
  if row1 or row2 or row3:
        game_still_on = False
  #return the winner
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]
  #or return None if there was no winner
  else:
    return None

def check_columns():
  #global variable    
  global game_still_on
  #check if any of the columns have all the same value (and is not empty)
  column1 = board[0] == board[3] == board[6] != "-"
  column2 = board[1] == board[4] == board[7] != "-"
  column3 = board[2] == board[5] == board[8] != "-"
  #if any row does have a match, flag that there is a win
  if column1 or column2 or column3:
    game_still_on = False
  #return the winner
  if column1:
    return board[0]
  if column2:
    return board[1]
  if column3:
    return board[2]
  #or return None if there was no winner
  else:
    return None

def check_diagnals():
  #global variable      
  global game_still_on
  #check if any of the diagnals have all the same value (and is not empty)
  diagnal1 = board[0] == board[4] == board[8] != "-"
  diagnal2 = board[2] == board[4] == board[6] != "-"
  #if any row does have a match, flag that there is a win      
  if diagnal1 or diagnal2:
    game_still_on = False
  #return the winner
  if diagnal1:
    return board[0]
  if diagnal2:
    return board[2]
  #or return None if there was no winner
  else:
    return None

#check if there is a tie function
def check_if_tie():
  #global variable
  global game_still_on
  if "-" not in board:
    game_still_on = False
    return True
  else:
    return False

#flip the current player from X to O, or O to X function
def flip_player():
  #global variable
  global current_player
  #if the current player was X, make it O
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"

if __name__ == "__main__":
    main()