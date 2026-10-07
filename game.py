from board import Board
from rules import valid_move, completed_boxes, can_undo


class DotsAndBoxes:
    def __init__(self):
        self.board = Board()
        self.current = 0
        self.scores = [0, 0]
        self.history = []

    def run(self):
        print("Dots and Boxes")
        print("Enter moves as H row col, V row col, or U to undo.")
        print("Rows and columns start at 0.")
        print("Example: H 0 1 or U")

        while not self.board.is_complete():
            self.board.display(self.scores, self.current)

            raw = input(
                f"Player {self.current + 1}, move: "
            ).strip().upper()

            parts = raw.split()

            if not parts:
                continue

            # Handle Undo command
            if len(parts) == 1 and parts[0] == "U":
                if not can_undo(self.history):
                    print("No moves to undo.")
                    continue

                (
                    orientation,
                    row,
                    col,
                    player,
                    score_gained,
                    prev_completed,
                ) = self.history.pop()

                self.board.remove_line(
                    orientation,
                    row,
                    col,
                    prev_completed,
                )

                self.scores[player] -= score_gained
                self.current = player

                print(
                    f"Undid Player {player + 1}'s move "
                    f"({orientation} {row} {col})."
                )

                continue

            if len(parts) != 3:
                print("Invalid format.")
                continue

            orientation, row, col = parts

            if not row.isdigit() or not col.isdigit():
                print("Row and column must be numbers.")
                continue

            row, col = int(row), int(col)

            if not valid_move(self.board, orientation, row, col):
                print("Invalid or already-used move.")
                continue

            before = set(self.board.completed)

            self.board.add_line(orientation, row, col)

            newly_completed = completed_boxes(
                self.board,
                before,
            )

            # Save the move so it can be undone later
            self.history.append(
                (
                    orientation,
                    row,
                    col,
                    self.current,
                    newly_completed,
                    before,
                )
            )

            if newly_completed:
                self.scores[self.current] += newly_completed

                if not self.board.is_complete():
                    print(
                        f"Player {self.current + 1} "
                        f"completed {newly_completed} box(es) "
                        f"and plays again."
                    )
                else:
                    print(
                        f"Player {self.current + 1} "
                        f"completed {newly_completed} box(es)."
                    )

            else:
                self.current = 1 - self.current

        self.board.display(self.scores, self.current)

        print("Game over!")

        if self.scores[0] == self.scores[1]:
            print("The game is a draw.")
        else:
            winner = 1 if self.scores[0] > self.scores[1] else 2
            print(f"Player {winner} wins!")