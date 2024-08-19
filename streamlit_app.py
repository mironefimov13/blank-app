import streamlit as st
# st.title("Streamlit Tutorial App")
# st.write("This is my new app")
# button1 = st.button("Click Me")
# if button1:
#     st.write("This is some text")
# like = st.checkbox("Do you like this app?")
# button2 = st.button("Submit")
# if button2:
#     if like:s
#         st.write("Thanks. I like it too")
#     else:
#         st.write("I'm sorry. You have bad tastes!")
st.title("Logic Operations App")
st.write("""Welcome to the Logic Operations app.
         This will calculate any different Operations.""")
st.header("AND")#hello
and1 = st.checkbox(":1 AND")
and2 = st.checkbox(":2 AND")
if and1 and and2:
    st.write(True)
else:
    st.write(False)

st.header("OR")
or1 = st.checkbox(":1 OR")
or2 = st.checkbox(":2 OR")
if or1 or or2:
    st.write(True)
else:
    st.write(False)

st.header("XOR")
xor1 = st.checkbox(":1 XOR")
xor2 = st.checkbox(":2 XOR")
if xor1 != xor2:
    st.write(True)
else:
    st.write(False)
