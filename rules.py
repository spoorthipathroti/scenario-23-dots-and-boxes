def valid_move(board, orientation, row, col):
    """
    Validates orientation, coordinate bounds, and checks if the line is unplayed.
    Safely rejects non-integer or negative inputs without crashing.
    """
    if not isinstance(row, int) or not isinstance(col, int):
        return False

    if row < 0 or col < 0:
        return False

    if orientation == "H":
        if row > board.rows or col >= board.cols:
            return False
        return not board.horizontal[row][col]

    if orientation == "V":
        if row >= board.rows or col > board.cols:
            return False
        return not board.vertical[row][col]

    return False


def completed_boxes(board, before):
    return len(board.completed - before)


def can_undo(history):
    return len(history) > 0