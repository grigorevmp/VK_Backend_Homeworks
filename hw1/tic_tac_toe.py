"""
Simple Tic Tac Toe game
"""
import random
from enum import Enum


class NotDigitIOException(Exception):
    """
    Error for incorrect input: not digit
    """


class DigitOutOfRangeIOException(Exception):
    """
    Error for incorrect input: digit out of range
    """


class GameOverPlayerWinException(Exception):
    """
    Game over: player wins this game
    """


class GameOverDrawException(Exception):
    """
    Game over: draw
    """


class IndexIsAlreadySetException(Exception):
    """
    Indexation error: cell is already taken
    """


class TicTacGame:
    """
    Tic tac game class
    """

    class PlayerTurn(Enum):
        """
        Enum for player turn
        """
        FIRST = 'o'
        SECOND = 'x'

    class GameMode(Enum):
        """
        Game mode
        """
        PVP = 0
        PVE = 1

    def __init__(self, curr_game_mode, play_board_size, player_1, player_2):
        """
        Init
        :param curr_game_mode: current game mode
        :param play_board_size: play board size
        :param player_1: player 1 name
        :param player_2: player 2 name
        """
        self.game_mode = curr_game_mode
        self.player_1 = player_1 if player_1 != '' else 'Player 1'
        self.player_2 = player_2 if player_1 != '' else 'Player 2'
        self.play_board_size = self.validate_input_play_board(play_board_size)
        self.play_board = [' ' for _ in range(self.play_board_size ** 2)]
        self.player_turn = self.PlayerTurn.FIRST

    def show_board(self):
        """
        Show border
        :return: None
        """
        for i in range(self.play_board_size ** 2):
            cell = self.play_board[i] if self.play_board[i] != ' ' else i
            if i % self.play_board_size != self.play_board_size - 1:
                print(' ', cell, ' |', end='')
            else:
                print(' ', cell, end='\n')
                if i != self.play_board_size ** 2 - 1:
                    print('------------------')

    @staticmethod
    def validate_input_play_board(play_board_size: str):
        """
        Validate input play board size
        :param play_board_size: play board size
        :return: int of play board size
        """
        if play_board_size == '':
            play_board_size = '3'
        if not play_board_size.isdigit():
            raise NotDigitIOException()
        return int(play_board_size)

    def return_player_and_cell(self):
        """
        Return player and cells
        :return: curr_player, cell
        """
        curr_player = self.player_1 if self.player_turn == self.PlayerTurn.FIRST \
            else self.player_2
        cell = self.PlayerTurn.FIRST.value if self.player_turn == self.PlayerTurn.FIRST \
            else self.PlayerTurn.SECOND.value
        return curr_player, cell

    def get_enemy_move(self):
        """
        Get computer move
        :return: Exception or none
        """
        empty_cells = [i for i in range(self.play_board_size ** 2) if self.play_board[i] == ' ']
        if len(empty_cells) > 0:
            enemy_input = int(random.choice(empty_cells))
            _, cell = self.return_player_and_cell()
            print(f'Enemy turn: - {enemy_input} -> {cell}')
            self.play_board[enemy_input] = cell
            self.check_for_winner(cell)
            self.player_turn = self.change_player()
        else:
            raise GameOverDrawException()

    def get_user_move(self):
        """
        Get user move
        :return: User input
        """
        curr_player, cell = self.return_player_and_cell()
        print(f'{curr_player}, your turn: - {cell} -> ', end='')
        return input()

    def validate_input(self, user_input):
        """
        Validate input
        :param user_input: User input
        :return: New index
        """
        if not user_input.isdigit():
            raise NotDigitIOException
        index = int(user_input)
        if index > 9 or index < 0:
            raise DigitOutOfRangeIOException
        if self.play_board[index] != ' ':
            raise IndexIsAlreadySetException
        return index

    def is_free_cells(self):
        """
        Is free places
        :return: Number of free cells
        """
        return self.play_board.count(' ')

    def change_player(self):
        """
        Change current player
        :return: New current player
        """
        return self.PlayerTurn.SECOND if self.player_turn == self.PlayerTurn.FIRST \
            else self.PlayerTurn.FIRST

    def make_turn(self, index):
        """
        Make new turn
        :param index: current board index
        :return: Exception or none
        """
        if self.game_mode == self.GameMode.PVP:
            _, cell = self.return_player_and_cell()
            self.play_board[index] = cell
            self.check_for_winner(cell)
            self.player_turn = self.change_player()
        else:
            _, cell = self.return_player_and_cell()
            self.play_board[index] = cell
            self.check_for_winner(cell)
            self.player_turn = self.change_player()
            try:
                self.get_enemy_move()
            except GameOverDrawException:
                raise GameOverDrawException from Exception

    def start_game(self):
        """
        Start game
        :return: Game end
        """
        while self.is_free_cells():
            self.show_board()
            try:
                user_input = self.get_user_move()
                index = self.validate_input(user_input)
                self.make_turn(index)
            except NotDigitIOException:
                print('Your input is not a digit!')
                continue
            except DigitOutOfRangeIOException:
                print(f'Input digit between 0 and {self.play_board_size ** 2}!')
                continue
            except IndexIsAlreadySetException:
                print("This cell is already set early!")
                continue
            except GameOverDrawException:
                print("Game over: Draw!")
                return
            except GameOverPlayerWinException:
                curr_player, _ = self.return_player_and_cell()
                print(f'Game over: {curr_player} wins!')
                self.show_board()
                return
        print("Game over: Draw!")

    def mark_won_cells(self, i, j, k):
        """
        Mark cells
        :param i: first cell
        :param j: second cell
        :param k: third cell
        :return:
        """
        self.play_board[i] = '*'
        self.play_board[j] = '*'
        self.play_board[k] = '*'

    def check_for_winner(self, cell_to_win):
        """
        Check board for winner
        :param cell_to_win:
        :return: Exception
        """
        # first row
        if self.play_board[:3].count(cell_to_win) == 3:
            self.mark_won_cells(0, 1, 2)
            raise GameOverPlayerWinException
        # second row
        if self.play_board[3:6].count(cell_to_win) == 3:
            self.mark_won_cells(3, 4, 5)
            raise GameOverPlayerWinException
        # third row
        if self.play_board[6:].count(cell_to_win) == 3:
            self.mark_won_cells(6, 7, 8)
            raise GameOverPlayerWinException
        # first column
        if self.play_board[0] == self.play_board[3] == self.play_board[6] == cell_to_win:
            self.mark_won_cells(0, 3, 6)
            raise GameOverPlayerWinException
        # second column
        if self.play_board[1] == self.play_board[4] == self.play_board[7] == cell_to_win:
            self.mark_won_cells(1, 4, 7)
            raise GameOverPlayerWinException
        # third column
        if self.play_board[2] == self.play_board[5] == self.play_board[8] == cell_to_win:
            self.mark_won_cells(2, 5, 8)
            raise GameOverPlayerWinException
        # prime diagonal
        if self.play_board[0] == self.play_board[4] == self.play_board[8] == cell_to_win:
            self.mark_won_cells(0, 4, 8)
            raise GameOverPlayerWinException
        # minor diagonal
        if self.play_board[2] == self.play_board[4] == self.play_board[6] == cell_to_win:
            self.mark_won_cells(2, 4, 6)
            raise GameOverPlayerWinException


if __name__ == '__main__':
    game_mode = input('Choose game mode (PVE, PVP) -> ')
    if game_mode in ['pvp', 'PVP']:
        player_1_ = input('Hi, Player #1. Please, enter your name -> ')
        player_2_ = input('Hi, Player #2. Please, enter your name -> ')
        play_board_size_ = input('Choose play board size, 3 for default -> ')
        game = TicTacGame(TicTacGame.GameMode.PVP, play_board_size_, player_1_, player_2_)
        game.start_game()
    elif game_mode in ['pve', 'PVE']:
        player_ = input('Hi, Player. Please, enter your name -> ')
        play_board_size_ = input('Choose play board size, 3 for default -> ')
        game = TicTacGame(TicTacGame.GameMode.PVE, play_board_size_, player_, "Big brother")
        game.start_game()
    else:
        print('Wrong game mode!')
