import streamlit as st

# Title of the app
st.title('Tic Tac Toe')

# Initializing the board with numbers 1-9
if 'board' not in st.session_state:
    st.session_state.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
if 'current_player' not in st.session_state:
    st.session_state.current_player = 'x'
if 'winner' not in st.session_state:
    st.session_state.winner = None


def display_board(board):
    st.write(f' {board[0]} | {board[1]} | {board[2]} ')
    st.write(f'---|---|---')
    st.write(f' {board[3]} | {board[4]} | {board[5]} ')
    st.write(f'---|---|---')
    st.write(f' {board[6]} | {board[7]} | {board[8]} ')


def place_marker(position, player, board):
    if board[position] not in ['x', 'o']:
        board[position] = player
        return True
    return False


def win_check(board):
    winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return True
    return False


# Display the current board state
st.write("Current Board:")
display_board(st.session_state.board)

# Input for selecting a position
position = st.selectbox('Choose your position:', range(1, 10))

# Button to submit the move
if st.button(f'Place {st.session_state.current_player}'):
    if place_marker(position - 1, st.session_state.current_player, st.session_state.board):
        # Check for a win
        if win_check(st.session_state.board):
            st.session_state.winner = st.session_state.current_player
        else:
            # Switch the player
            st.session_state.current_player = 'o' if st.session_state.current_player == 'x' else 'x'
    else:
        st.warning("Position already taken. Try another one!")

# Check if there is a winner
if st.session_state.winner:
    st.success(f"Player {st.session_state.winner} wins!")
else:
    st.write(f"It's Player {st.session_state.current_player}'s turn!")
