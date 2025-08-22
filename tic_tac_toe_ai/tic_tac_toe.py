from ai_agent import best_move, is_winner, is_draw

def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print('| ' + ' | '.join(row) + ' |')

def play_game():
    board = [' '] * 9
    current_player = 'X'

    while True:
        print_board(board)
        if current_player == 'X':
            move = int(input("Enter your move (0-8): "))
            if board[move] != ' ':
                print("Invalid move. Try again.")
                continue
        else:
            print("AI is making a move...")
            move = best_move(board)

        board[move] = current_player

        if is_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
