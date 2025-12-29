import streamlit as st
import random 

# --------------- RULES --------------------------------
with st.sidebar:
    st.header("HOW TO PLAY")
    st.write("-> A tile can only be moved to an empty spot.")
    st.write("-> A tile can be moved only if it is adjacent to the empty spot")
    st.write("-> To move a tile, you must tap on it.")
    st.header("OBJECTIVE")
    st.write("You must rearrange the tiles such that it is arranged as follows:")
    st.write(" 1  2  3  4")
    st.write(" 5  6  7  8")
    st.write(" 9  10  11  12")
    st.write(" 13  14  15  _")
    st.write("'_' represents an empty spot")


# -------------- initial board ---------------------------
def init_board():
    board=[[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 0]]
    return board

# -------------- finding empty spot -----------------------
def find_empty_spot(board):
    for row in range(4):
        for col in range(4):
            if board[row][col]==0:
                return row,col

# --------------- check if solved ----------------------
def is_solved(board):
    return board == [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]

# --------------- shuffle board -------------------------

def shuffle_board(board):
    for _ in range(200):
        for row in range(4):
            for col in range(4):
                if board[row][col] == 0:

                    neighbors = []

                    if row > 0:
                        neighbors.append((row - 1, col))
                    if row < 3:
                        neighbors.append((row + 1, col))
                    if col > 0:
                        neighbors.append((row, col - 1))
                    if col < 3:
                        neighbors.append((row, col + 1))

                    new_row, new_col = random.choice(neighbors)
                    board[row][col], board[new_row][new_col] = (
                        board[new_row][new_col],
                        board[row][col],
                    )
                    break
            else:
                continue
            break
            
# ----------------------------------- find empty -------------------------------------------------------------------
def find_empty(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i, j
# ---------------------------------- check adjacent -----------------------------------------------------------
def is_adjacent(i, j, ei, ej):
    return abs(i - ei) + abs(j - ej) == 1
# ---------------------------------- session state ------------------------------------------------------------

if "started" not in st.session_state:
    st.session_state.started = True
    st.session_state.board = init_board()
    shuffle_board(st.session_state.board)

# ----------------------------------- UI ----------------------------------------------------------------------

st.title("🧩 15 Puzzle")

board = st.session_state.board
ei, ej = find_empty(board)

for i in range(4):
    cols = st.columns(4)
    for j in range(4):
        val = board[i][j]

        if val == 0:
            cols[j].button(" ", key=f"{i}-{j}", disabled=True)
        else:
            if cols[j].button(str(val), key=f"{i}-{j}"):
                if is_adjacent(i, j, ei, ej):
                    board[ei][ej], board[i][j] = board[i][j], board[ei][ej]
                    st.rerun()

# ---------- Win ----------
if is_solved(board):
    st.success("🎉 Puzzle Solved!")

# ---------- Controls ----------



    
if st.button("🔀 Shuffle"):
    st.session_state.board = init_board()
    shuffle_board(st.session_state.board)
    st.rerun()





