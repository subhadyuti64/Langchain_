# import streamlit as st

# # Initialize session state
# if "votes" not in st.session_state:
#     st.session_state.votes = {"A": 0, "B": 0}

# # Vote handlers
# def vote(option):
#     st.session_state.votes[option] += 1

# def reset():
#     st.session_state.votes = {"A": 0, "B": 0}

# # UI
# st.title("Voting App")
# st.button("Vote A", on_click=vote, args=("A",))
# st.button("Vote B", on_click=vote, args=("B",))
# st.button("Reset", on_click=reset)

# st.write(f"Votes A: {st.session_state.votes['A']}, B: {st.session_state.votes['B']}")

import streamlit as st

st.title("Voting App")

# Initialize session state
if "votes" not in st.session_state:
    st.session_state.votes = {"A": 0, "B": 0}

# Vote handlers
def vote(option):
    st.session_state.votes[option] += 1

def reset():
    st.session_state.votes = {"A": 0, "B": 0}

# Buttons
if st.button("Vote A"):
    vote("A")
if st.button("Vote B"):
    vote("B")
if st.button("Reset"):
    reset()

# Display vote counts
st.write(f"Votes A: {st.session_state.votes['A']}, B: {st.session_state.votes['B']}")

# Debug message
st.write("App loaded successfully!")

st.run()