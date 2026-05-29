import streamlit as st

st.title("Chai making App")

if st.button("Make chai"):
    st.success("Your chai is being brewed")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala is added")

tea_type = st.radio("Pick your chai base: ",["Water","Milk","Almond milk"])
st.write(f"you selected{tea_type}")

flavour = st.selectbox("Choose flavour:",["Adarak","kesar","tulsi"])
st.write(f"selcted flavour: {flavour}")

sugar = st.slider("sugar level", 0,5,2)

cups = st.number_input("How many cups:" ,min_value=1,max_value=10,step=1)
st.write(f"selcted cups: {cups}")

st.date_input("your DOB")