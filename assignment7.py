import streamlit as st
import pandas as pd

st.title("Assignment 7")
st.image("images.jpg")

name =st.text_input("Enter your name.")

if name:
    st.write(f"Hello, {name} !! Welcome to my portal.")

age = st.slider("Select your age." , 0, 100, 25)  

st.write(f"{name}, you selected {age} years.")

date1 = st.date_input("Select a a date")
st.write(f"You selected {date1}.")

waqt = st.time_input("Select a time ")
st.write(f"You selected {waqt}.")

Fruits= ["Apples", "Oranges", "Grapes", "Kiwi"]

choice=st.selectbox("Choose your favourite fruit.", Fruits )

st.write(f"You selected {choice}")

data = {
    "Name" : ["john", "Jane", "Jake", "Jill"],
    "Age": [20, 30, 40, 50], 
    "City" : ["Karachi", "Lahore", "Islamabad", "Houston"]
}

df=pd.DataFrame(data)

df.to_csv("sampledata.csv")

st.write(df)

uploaded_file= st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
st.bar_chart(data, x="Name", y="Age")

