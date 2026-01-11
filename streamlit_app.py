import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button('Click me'):
    st.session_state.count += 1

st.write('You have clicked the button ', st.session_state.count, ' times.')
