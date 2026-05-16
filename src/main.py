from typing import List

class tictactoe:
    """
    A simple Tic-Tac-Toe game manager.
    """
    def __init__(self) -> None:
        self.board: List[str] = [' '] * 10
        self.player_turn = 'X'

    def show_board(self) -> None:
        print('\n')
        print(self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('-' * 9)
        print(self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('-' * 9)
        print(self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('\n')

    def fix_point(self, choice_player: int) -> None:
        self.board[choice_player] = self.player_turn 
         
    def swap_player_turn(self) -> None:
        self.player_turn = 'O' if self.player_turn == 'X' else 'X' 

    def has_payer_won(self) -> bool:
        combinations = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),
            (1, 4, 7), (2, 5, 8), (3, 6, 9),
            (1, 5, 9), (3, 5, 7)
        ]
        for combination in combinations: 
            if self.board[combination[0]] == self.player_turn:
                if self.board[combination[1]] == self.player_turn:
                    if self.board[combination[2]] == self.player_turn:
                        return True
        return False
            
    def board_filled(self) -> bool:
        if ' ' in self.board[1:]:
            return False
        return True        
           

main = tictactoe()
main.show_board()
filled_posotions = set()

while True:
    u1 = input('Enter a position (Or q): ').lower()

    if u1 == 'q':
        break
    
    elif int(u1) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if u1 in filled_posotions:
            print(f'Position {u1} is not empty.')
            continue
        main.fix_point(int(u1))
        main.show_board()
        filled_posotions.add(u1)
        if main.has_payer_won():
            print('U won')
            break 

        elif main.board_filled():
            print('Game finished')
            break

    else:
        print('Invalid Input, try again: ')
        continue

    main.swap_player_turn()
