from tkinter import * # type: ignore

current_player = "x"
game_over = False

def on_button_click(row, col):
    global current_player, game_over
    
    if buttons[row][col].cget("text") == "" and not game_over:
        buttons[row][col].config(text=current_player)
        board[row][col] = current_player
        if check_winner(board):
            print(f"{current_player} is the winner!")
            game_over = True
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = "o" if current_player == "x" else "x"

def check_winner(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            return True
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return True
    
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

a = Tk()
a.title("Tic-Tac-Toe")
a.geometry("400x400")

frame = Frame(a)
frame.pack()

buttons = []
board = [["" for _ in range(3)] for _ in range(3)]

for row in range(3):
    button_row = []
    for col in range(3):
        button = Button(frame, text="", font=("Arial", 20), height=3, width=6,
                        command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

a.mainloop()