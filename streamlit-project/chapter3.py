import streamlit as st

st.title("Chai poll")

col1 , col2 = st.columns(2)

with col1:
    st.header("Masala chai")
    vote1 = st.button("vote masala chai")

with col2:
    st.header("Adarak chai")
    vote2 = st.button("vote Adarak chai")

if vote1:
    st.success("you voted masala chai")
elif vote2:
    st.success("you voted asrak chai")

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("choose your chai",["masala","adrak","tulsi"])

st.write(f"welcome {name} and your {tea} chai is getting ready")

with st.expander("Show chai making instruction: "):
    st.write(""" 
    1. Boil water with tea leaves
    2. Add milk and spices
    3. Serve Hot
""")