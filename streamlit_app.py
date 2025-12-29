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
    if board==[[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 0]]:
        return True

# --------------- shuffle board -------------------------

def shuffle_board(board):
    for _ in range(200):
        moved = False
        for row in range(4):
            for col in range(4):
                if board[row][col] == 0:
    

                    
                    if row == 0 and col == 0:
                        new_row, new_col = random.choice([(1,0),(0,1)])
                    elif row == 0 and col == 3:
                        new_row, new_col = random.choice([(0,2),(1,3)])
                    elif row == 3 and col == 0:
                        new_row, new_col = random.choice([(2,0),(3,1)])
                    elif row == 3 and col == 3:
                        new_row, new_col = random.choice([(2,3),(3,2)])
                    elif row == 0:
                        new_row, new_col = random.choice([(0,col-1),(0,col+1),(1,col)])
                    elif row == 3:
                        new_row, new_col = random.choice([(3,col-1),(3,col+1),(2,col)])
                    elif col == 0:
                        new_row, new_col = random.choice([(row+1,col),(row-1,col),(row,col+1)])
                    elif col == 3:
                        new_row, new_col = random.choice([(row+1,col),(row-1,col),(row,col-1)])
                    else:
                        new_row, new_col = random.choice([(row+1,col),(row-1,col),(row,col+1),(row,col-1)])

                    board[row][col], board[new_row][new_col] = board[new_row][new_col], 0
                    moved = True
                    break
            if moved:
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

if "board" not in st.session_state:
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





