def get_neighbors(x, y, width, height):
    # Return the indices of the neighbors of the cell at (x, y)
    neighbors = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i >= 0 and i < width and j >= 0 and j < height and (i, j) != (x, y):
                neighbors.append((i, j))
    return neighbors

def get_next_state(x, y, board):
    # Return the next state of the cell at (x, y) based on its current state and the states of its neighbors
    width, height = len(board), len(board[0])
    neighbors = get_neighbors(x, y, width, height)
    live_neighbors = sum(board[i][j] for i, j in neighbors)
    if board[x][y]:
        return live_neighbors in (2, 3)
    else:
        return live_neighbors == 3

def update_board(board):
    # Update the state of the board based on the states of the cells
    width, height = len(board), len(board[0])
    new_board = [[0] * height for _ in range(width)]
    for i in range(width):
        for j in range(height):
            new_board[i][j] = get_next_state(i, j, board)
    return new_board

def display_board(board):
    # Print the board to the console
    for row in board:
        print(' '.join('#' if cell else '.' for cell in row))

def run_game(board, num_iterations):
    # Run the game of life for the specified number of iterations
    for _ in range(num_iterations):
        display_board(board)
        print()
        board = update_board(board)

# Example usage:
board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
run_game(board, 50)