import random

def mine_game():
    # Set up the game
    board_size = 5
    num_mines = 5
    board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
    mines = []

    # Randomly place the mines on the board
    for _ in range(num_mines):
        while True:
            row = random.randint(0, board_size - 1)
            col = random.randint(0, board_size - 1)
            if (row, col) not in mines:
                mines.append((row, col))
                break

    # Function to calculate the number of adjacent mines
    def get_adjacent_mines(row, col):
        count = 0
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                nr = row + dr
                nc = col + dc
                if 0 <= nr < board_size and 0 <= nc < board_size:
                    if (nr, nc) in mines:
                        count += 1
        return count

    # Function to reveal a cell
    def reveal_cell(row, col):
        if board[row][col] != ' ':
            return
        if (row, col) in mines:
            board[row][col] = 'X'
            return
        count = get_adjacent_mines(row, col)
        board[row][col] = str(count) if count > 0 else ' '
        if count == 0:
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < board_size and 0 <= nc < board_size:
                        reveal_cell(nr, nc)

    # Play the game
    while True:
        # Display the board
        print("=== Mine Gambling Game ===")
        print("  " + " ".join([str(i) for i in range(board_size)]))
        for i in range(board_size):
            print(f"{i} {' '.join(board[i])}")
        print("==========================")

        # Prompt for cell selection
        row = int(input("Select a row: "))
        col = int(input("Select a column: "))

        # Check if the selected cell is a mine
        if (row, col) in mines:
            print("\nOh no! You hit a mine. Game over!")
            break

        # Reveal the selected cell
        reveal_cell(row, col)

        # Check if all non-mine cells have been revealed
        if all(board[i][j] != ' ' or (i, j) in mines for i in range(board_size) for j in range(board_size)):
            print("\nCongratulations! You've revealed all non-mine cells. You win!")
            break

# Start the game
mine_game()
