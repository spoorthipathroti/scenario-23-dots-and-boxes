import unittest

from board import Board
from rules import valid_move, completed_boxes


class TestDotsAndBoxes(unittest.TestCase):

    def test_valid_horizontal_move(self):
        board = Board()

        self.assertTrue(valid_move(board, "H", 0, 0))

        board.add_line("H", 0, 0)

        self.assertFalse(valid_move(board, "H", 0, 0))

    def test_valid_vertical_move(self):
        board = Board()

        self.assertTrue(valid_move(board, "V", 0, 0))

        board.add_line("V", 0, 0)

        self.assertFalse(valid_move(board, "V", 0, 0))

    def test_invalid_and_repeated_move(self):
        board = Board()

        # Invalid orientation
        self.assertFalse(valid_move(board, "X", 0, 0))

        # Invalid coordinates
        self.assertFalse(valid_move(board, "H", 99, 99))
        self.assertFalse(valid_move(board, "V", 99, 99))

        # Repeated horizontal line
        board.add_line("H", 0, 0)
        self.assertFalse(valid_move(board, "H", 0, 0))

        # Repeated vertical line
        board.add_line("V", 0, 0)
        self.assertFalse(valid_move(board, "V", 0, 0))

    def test_completion_of_box(self):
        board = Board()

        before = set(board.completed)

        board.add_line("H", 0, 0)
        board.add_line("H", 1, 0)
        board.add_line("V", 0, 0)

        # Three sides are present, so no box is complete yet.
        self.assertEqual(
            completed_boxes(board, before),
            0
        )

        board.add_line("V", 0, 1)

        newly_completed = completed_boxes(
            board,
            before
        )

        self.assertEqual(newly_completed, 1)
        self.assertIn((0, 0), board.completed)

    def test_end_of_game_condition(self):
        board = Board()

        # Fill all 12 lines of the 2x2 board.
        moves = [
            ("H", 0, 0),
            ("H", 0, 1),
            ("H", 1, 0),
            ("H", 1, 1),
            ("H", 2, 0),
            ("H", 2, 1),
            ("V", 0, 0),
            ("V", 0, 1),
            ("V", 0, 2),
            ("V", 1, 0),
            ("V", 1, 1),
            ("V", 1, 2),
        ]

        for orientation, row, col in moves:
            board.add_line(orientation, row, col)

        self.assertTrue(board.is_complete())


if __name__ == "__main__":
    unittest.main()