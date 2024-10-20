import os
import random

def clear_screen():
  os.system("clear")

class Player:

  def __init__(self):
    self.name = ""
    self.symbol = ""

  def choice_name(self):
    while True:
      name = input("Enter your name: ")
      if name.isalpha():
        self.name = name
        break
      print("Invalid name. Please use letters only.")

  def choice_symbol(self):
    while True:
      symbol = input(f"{self.name}, chooes your symbol a single letter: ")
      if symbol.isalpha() and len(symbol) == 1:
        self.symbol = symbol.upper()
        break
      print("Invalid symbol. Please use only one letter.")

class Menu:

  def display_main_menu(self):
    while True:
      print("Welcome to my X_O game")
      print("1. start game")
      print("2. play with the cumpeuter")
      print("3. quit game")
      choice = input("Enter your chooic (1, 2 or 3): ")
      if choice not in ["1", "2", "3"]:
        print("plieas enter (1, 2 or 3)")
      break
    return choice

  def display_endgame_menu(self):
    while True:
      print("game is over ")
      print("1. restart the game")
      print("2. quit the game")
      choice = input("Enter your chooic (1 or 2): ")
      if choice not in ["1", "2"]:
        print("plieas enter (1 or 2)")
      break
    return choice

class Board:

  def __init__(self):
    self.board = [str(i) for i in range(1, 10)]

  def display_board(self):
    for i in range(0, 9, 3):
      print(" | ".join(self.board[i:i + 3]))
      if i < 6:
        print("-" * 10)

  def update_board(self, choice, symbol):
    if self.is_valid_move(choice):
      self.board[choice - 1] = symbol
      return True
    return False

  def is_valid_move(self, choice):
    return self.board[choice - 1].isdigit()

  def reset_board(self):
    self.board = [str(i) for i in range(1, 10)]

  def is_empty(self, pos):
   return self.board[pos - 1].isdigit()


class Game:

  def __init__(self):
    self.players = [Player(), Player()]
    self.board = Board()
    self.menu = Menu()
    self.curren_player_index = 0

  def start_game(self):
    choice = self.menu.display_main_menu()
    if choice == "1":
      self.steup_player()
      self.play_game()

    elif choice == "2":
     self.compiuter()
     self.play_game()
     self.steup_player()
    
    else:
      self.quit_game()

  def steup_player(self):
    for number, Player in enumerate(self.players, start=1):
      print(f"Player {number} enter your data.")
      Player.choice_name()
      Player.choice_symbol()
      print("-" * 20)

  def play_game(self):
    while True:
      self.play_turn()
      if self.chack_win() or self.chack_draw():
        print(f"{self.players[self.curren_player_index].name} wins!")
        choice = self.menu.display_endgame_menu()
        if choice == "1":
          self.restart_game()
        else:
          self.quit_game()
          break

  def restart_game(self):
    self.board.reset_board()
    self.curren_player_index = 0
    self.play_game()

  def chack_win(self):
    wining_combos = [
        [1, 5, 9],
        [3, 5, 7],
        [3, 6, 9],
        [2, 5, 8],
        [1, 4, 7],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    for combo in wining_combos:
      if self.board.board[combo[0]-1] == self.board.board[
          combo[1]-1] == self.board.board[combo[2]-1]:
        return True
    return False

  def chack_draw(self):
    return all(not num.isdigit() for num in self.board.board)

  def play_turn(self):
    player = self.players[self.curren_player_index]
    clear_screen()
    self.board.display_board()
    print(f"{player.name}'s turn ({player.symbol})")
    while True:
      try:
        cell_choice = int(input("Chooce call (1_9): "))
        if 1 <= cell_choice <= 9 and self.board.update_board(
            cell_choice, player.symbol):
          break
        else:
          print("invald move pleas try agen.")

      except ValueError:
        print("please enter a number betwen 1 and 9.")
    self.suich_playr()

  def suich_playr(self):
    self.curren_player_index = 1 - self.curren_player_index

  def compiuter(self):
    winning_combos = [
      [1, 5, 9],
      [3, 5, 7],
      [3, 6, 9],
      [2, 5, 8],
      [1, 4, 7],
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ]

    for combo in winning_combos:
      empty_positions = [pos for pos in combo if self.board.is_empty(pos)]
      if empty_positions:
          chosen_position = random.choice(empty_positions)
          self.board.update_board(chosen_position, self.players[self.curren_player_index].symbol)
          break
    

  def quit_game(self):
    print("Think you for plying.")

game = Game()
game.start_game()
