import streamlit as st
st.title("The Miron App")
st.write("""Hi! I am Miron Efimov. I am a Programmer and Engineer. This is my page of stuff.""")
st.title("Logic Operations Section")
st.write("""In this section, you can use operations like AND, OR, and XOR.""")
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

st.title("The Graph Section")
st.write("Here, you can mess around with graphs and charts. Or even make random charts.")
