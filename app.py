import streamlit as st
import pandas as pd
import numpy as np
import time
st.title("Hello World")
st.write("This is a simple Streamlit app.")
st.write("You can use Streamlit to create web applications easily.")
st.header("Streamlit Functions in Action")
st.subheader("Here are some commonly used Streamlit functions in action:")

# Title
st.title("Streamlit Demo")

# Header and Subheader
st.header("Header Example")
st.subheader("Subheader Example")

# Text
st.text("This is an example of fixed-width text.")

# Write
st.write("This is an example of the st.write() function. You can write text, data, or other elements.")

# Button
if st.button("Click Me"):
    st.write("Button clicked!")

# Checkbox
if st.checkbox("Check Me"):
    st.write("Checkbox checked!")

# Radio
choice = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {choice}")

# Selectbox
dropdown = st.selectbox("Select an option:", ["Option A", "Option B", "Option C"])
st.write(f"You selected: {dropdown}")

# Slider
slider_value = st.slider("Select a value:", 0, 100, 50)
st.write(f"Slider value: {slider_value}")

# Text Input
text_input = st.text_input("Enter some text:")
st.write(f"You entered: {text_input}")

# Number Input
number_input = st.number_input("Enter a number:", 0, 100, 50)
st.write(f"You entered: {number_input}")

# File Uploader
uploaded_file = st.file_uploader("Upload a file:")
if uploaded_file:
    st.write(f"Uploaded file: {uploaded_file.name}")

# Image
st.image("https://via.placeholder.com/150", caption="Sample Image")

# Video
st.video("https://www.w3schools.com/html/mov_bbb.mp4")

# Audio
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# Map
df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(df)

# Dataframe
st.dataframe(df)

# Table
st.table(df.head())

# Progress
progress_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    progress_bar.progress(percent_complete + 1)