import streamlit as st

st.title("Hello Everyone")
st.subheader("I am Ayush ")
st.text("lets do some work wirh streamlit")
st.write("take a example ")

data = st.selectbox("Your fav game: ",["Cricket","Football","Hockey","Kabaddi"])

st.write(f"You chose game: {data}")
st.success("well done")