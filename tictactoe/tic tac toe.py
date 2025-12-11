# Nama : jona irwansyah
# Nim : D0425006

import tkinter as tk
from tkinter import messagebox

# ---------- Pengaturan awal ----------
root = tk.Tk()
root.title("Tic-Tac-Toe - JonaIrwansyah")
root.configure(bg="#d7ecff")  # biru sangat muda
root.geometry("450x600")
root.resizable(False, False)

# ---------- Variabel permainan ----------
turn_X = True
moves = 0
buttons = {}

player_X = tk.StringVar(value="Pemain X")
player_O = tk.StringVar(value="Pemain O")

# ---------- Fungsi util ----------
def update_status():
    if turn_X:
        status_label.config(text=f"Giliran: {player_X.get()} (X)")
    else:
        status_label.config(text=f"Giliran: {player_O.get()} (O)")

def highlight_win(combo):
    for (r, c) in combo:
        buttons[(r, c)].config(bg="#b3ffcc")  # hijau muda kemenangan

def clear_highlight():
    for btn in buttons.values():
        btn.config(bg="#e3f2fd")  # biru kotak default

def check_winner():
    board = [[buttons[(r, c)]["text"] for c in range(3)] for r in range(3)]
    lines = [
        ([(0,0),(0,1),(0,2)], board[0][0]),
        ([(1,0),(1,1),(1,2)], board[1][0]),
        ([(2,0),(2,1),(2,2)], board[2][0]),
        ([(0,0),(1,0),(2,0)], board[0][0]),
        ([(0,1),(1,1),(2,1)], board[0][1]),
        ([(0,2),(1,2),(2,2)], board[0][2]),
        ([(0,0),(1,1),(2,2)], board[1][1]),
        ([(0,2),(1,1),(2,0)], board[1][1]),
    ]

    for combo, val in lines:
        if val != "" and all(board[r][c] == val for (r,c) in combo):
            return val, combo
    return None

def end_round(winner):
    if winner == "X":
        messagebox.showinfo("Tic-Tac-Toe", f"{player_X.get()} (X) Menang!")
    elif winner == "O":
        messagebox.showinfo("Tic-Tac-Toe", f"{player_O.get()} (O) Menang!")
    else:
        messagebox.showinfo("Tic-Tac-Toe", "Permainan Seri!")

    for btn in buttons.values():
        btn.config(state="disabled")

def on_click(r, c):
    global turn_X, moves
    btn = buttons[(r, c)]
    if btn["text"] != "":
        return

    btn.config(text="X" if turn_X else "O")
    moves += 1

    result = check_winner()
    if result:
        winner, combo = result
        highlight_win(combo)
        end_round(winner)
        return

    if moves == 9:
        end_round(None)
        return

    turn_X = not turn_X
    update_status()

def reset_board():
    global turn_X, moves
    turn_X = True
    moves = 0
    clear_highlight()
    for btn in buttons.values():
        btn.config(text="", state="normal")
    update_status()

# ---------- Layout GUI ----------
title = tk.Label(root, text="Tic-Tac-Toe", font=("Helvetica", 25, "bold"),
                 bg="#d7ecff", fg="blue")
title.pack(pady=(12, 6))

# Input nama pemain
name_frame = tk.Frame(root, bg="#d7ecff")
name_frame.pack(pady=10)

tk.Label(name_frame, text="Nama X:", bg="#d7ecff", font=("Arial", 11)).grid(row=0, column=0, padx=5)
tk.Entry(name_frame, textvariable=player_X, width=15).grid(row=0, column=1, padx=5)

tk.Label(name_frame, text="Nama O:", bg="#d7ecff", font=("Arial", 11)).grid(row=1, column=0, padx=5)
tk.Entry(name_frame, textvariable=player_O, width=15).grid(row=1, column=1, padx=5)

# Label status
status_label = tk.Label(root, text="", font=("Helvetica", 13), bg="#d7ecff")
status_label.pack(pady=5)
update_status()

# Frame papan (3x3)
board_frame = tk.Frame(root, bg="#d7ecff")
board_frame.pack(pady=15)

btn_font = ("Arial", 30, "bold")
for r in range(3):
    for c in range(3):
        b = tk.Button(board_frame, text="", font=btn_font, width=3, height=1,
                      bg="#e3f2fd", fg="black", activebackground="#bbdefb",
                      relief="raised", bd=2,
                      command=lambda r=r, c=c: on_click(r, c))
        b.grid(row=r, column=c, padx=8, pady=8)
        buttons[(r, c)] = b

# Tombol reset
reset_btn = tk.Button(root, text="Reset Permainan", font=("Helvetica", 12),
                      command=reset_board, bg="white")
reset_btn.pack(pady=15)

hint = tk.Label(root, text="Klik kotak untuk bermain — X mulai lebih dulu",
                bg="#d7ecff", fg="gray", font=("Helvetica", 10))
hint.pack()

root.mainloop()