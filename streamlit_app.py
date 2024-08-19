import streamlit as st
st.title("The Miron App")
st.title("Logic Operations Section")
st.write("""Welcome to the Logic Operations section.
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
