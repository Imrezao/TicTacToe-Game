# Tic-Tac-Toe Game

A simple command-line Tic-Tac-Toe game written in Python. Play against another human player by taking turns to mark `X` and `O` on a 3x3 board.
 
## How to Play

- The board positions are numbered 1 to 9 as shown below:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

- Players take turns entering a number (1–9) corresponding to the empty square they wish to mark.
- Player X always moves first, then O, and so on.
- After each move, the updated board is displayed.
- The game ends when:
    - A player gets three marks in a row (horizontally, vertically, or diagonally) → that player wins.
    - The board is completely filled with no winner → the game ends in a draw.
    - A player enters q → the game terminates early.

## Code Structure
- **Class** `tictactoe` 
    - `__init__()`: Initializes a 1‑based board list (index 0 unused) and sets the starting player to `'X'`.
    - `show_board()`: Prints the current board state in a 3×3 grid.
    - `fix_point(choice_player)`: Places the current player's symbol on the chosen board cell.
    - `swap_player_turn()`: Switches the active player between `'X'` and `'O'`.
    - `has_payer_won()`: Checks all winning combinations to see if the current player has won.
    - `board_filled()`: Returns `True` if all board cells (1–9) are occupied.


## Requirements

- Python 3.6+


