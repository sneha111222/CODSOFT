import math

def is_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diags
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)

def is_draw(board):
    return ' ' not in board

def get_available_moves(board):
    return [i for i in range(9) if board[i] == ' ']

def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    if is_winner(board, 'O'): return 1
    if is_winner(board, 'X'): return -1
    if is_draw(board): return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            max_eval = max(max_eval, score)
            alpha = max(alpha, score)
            if beta <= alpha: break  # Alpha-Beta pruning
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            min_eval = min(min_eval, score)
            beta = min(beta, score)
            if beta <= alpha: break
        return min_eval

def best_move(board):
    best_score = -math.inf
    move = None
    for i in get_available_moves(board):
        board[i] = 'O'
        score = minimax(board, 0, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    return move
