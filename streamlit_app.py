import streamlit as st
import random

# ---------------- Sidebar Rules ----------------
with st.sidebar:
    st.header("HOW TO PLAY")
    st.write("-> A tile can only be moved to an empty spot.")
    st.write("-> A tile can be moved only if it is adjacent to the empty spot")
    st.write("-> To move a tile, you must tap on it.")
    st.header("OBJECTIVE")
    st.write("Arrange the tiles as follows:")
    st.write(" 1  2  3  4")
    st.write(" 5  6  7  8")
    st.write(" 9 10 11 12")
    st.write("13 14 15  _")

# ---------------- Board Logic ----------------
def init_board():
    return [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]

def find_empty(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i, j

def is_adjacent(i, j, ei, ej):
    return abs(i - ei) + abs(j - ej) == 1

def is_solved(board):
    return board == init_board()

def shuffle_board(board, moves=50):
    ei, ej = find_empty(board)

    for _ in range(moves):
        neighbors = []
        if ei > 0: neighbors.append((ei - 1, ej))
        if ei < 3: neighbors.append((ei + 1, ej))
        if ej > 0: neighbors.append((ei, ej - 1))
        if ej < 3: neighbors.append((ei, ej + 1))

        ni, nj = random.choice(neighbors)
        board[ei][ej], board[ni][nj] = board[ni][nj], board[ei][ej]
        ei, ej = ni, nj

# ---------------- Session State ----------------
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.board = init_board()
    shuffle_board(st.session_state.board)

# ---------------- UI ----------------
st.title("🧩 15 Puzzle")

board = st.session_state.board
ei, ej = find_empty(board)

for i in range(4):
    cols = st.columns(4)
    for j in range(4):
        val = board[i][j]
        if val == 0:
            cols[j].button(" ", disabled=True)
        else:
            if cols[j].button(str(val), key=f"{i}-{j}"):
                if is_adjacent(i, j, ei, ej):
                    board[ei][ej], board[i][j] = board[i][j], board[ei][ej]

# ---------------- Win Message ----------------
if is_solved(board):
    st.success("🎉 Puzzle Solved!")

# ---------------- Controls ----------------
if st.button("🔀 Shuffle"):
    st.session_state.board = init_board()
    shuffle_board(st.session_state.board)
