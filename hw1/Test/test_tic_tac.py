"""
Pytest module
"""
from hw1.tic_tac_toe import TicTacGame, GameOverPlayerWinException
import pytest


class TestClass:
    """
    Test class
    """

    def test_one(self):
        """
        One test step
        :return:
        """
        game = TicTacGame(TicTacGame.GameMode.PVP, "3", "Player 1", "Player 2")

        user_input = "0"
        index = game.validate_input(user_input)
        game.make_turn(index)

        assert game.play_board[0] == 'o'

    def test_missing_values(self):
        """
        Missing values
        :return:
        """
        game = TicTacGame(TicTacGame.GameMode.PVP, "", "", "")

        assert game.play_board_size == 3
        assert game.player_1 == 'Player 1'
        assert game.player_2 == 'Player 2'

    def test_first_wins(self):
        """
        First player wins
        :return:
        """
        game = TicTacGame(TicTacGame.GameMode.PVP, "3", "M", "K")

        # first move
        user_input = "0"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # second move
        user_input = "3"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # third move
        user_input = "1"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # forth move
        user_input = "4"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # fifth move
        user_input = "2"
        index = game.validate_input(user_input)
        with pytest.raises(GameOverPlayerWinException) as exc_info:
            game.make_turn(index)

    def test_second_wins(self):
        """
        Second player wins
        :return:
        """
        game = TicTacGame(TicTacGame.GameMode.PVP, "3", "M", "K")

        # first move
        user_input = "1"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # second move
        user_input = "3"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # third move
        user_input = "0"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # forth move
        user_input = "4"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # fifth move
        user_input = "8"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # 6th move
        user_input = "5"
        index = game.validate_input(user_input)
        with pytest.raises(GameOverPlayerWinException) as exc_info:
            game.make_turn(index)

    def test_draw(self):
        """
        Draw
        :return:
        """
        game = TicTacGame(TicTacGame.GameMode.PVP, "3", "Mike", "Kate")

        # first move
        user_input = "0"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # second move
        user_input = "3"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # third move
        user_input = "4"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # 4th move
        user_input = "1"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # 5th move
        user_input = "5"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # 6th move
        user_input = "2"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # 7th move
        user_input = "6"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # 8th move
        user_input = "8"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
        # 9th move
        user_input = "7"
        index = game.validate_input(user_input)
        game.make_turn(index)
        game.change_player()
