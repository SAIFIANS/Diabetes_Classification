import streamlit as st
import time as t

# to display an image
# st.image("IMG-20210402-CV-removebg-preview.png")

# title
st.title("Diabetes Prediction")

#Header
st.header("Machine Learning")

#sub header
st.subheader("Linear Regression")

#information
st.info("Information deatils of a user")


#Warning Message
st.warning("Come on time or else you will be marked absent")

# write
st.write("Employee Name")
st.write(range(50))

#Error Message
st.error("Invalid Input")

#Success Message
st.success("Values Entered Successfully")

#Markdown
st.markdown("# Heading")
st.markdown("## Heading")
st.markdown("## Heading")
st.markdown(":moon:")

st.text("Any text")

#to write a caption
st.caption("Caption")

# to display mathematical equation
st.latex(r'''a+b x^2+c''')

# Widgets

# Checkbox
st.checkbox("Login")


# button
st.button("Click")

# radio widget
st.radio("Pick you Gender", ["Male", "Female", "Other"])

# select box
st.selectbox("Pick your course", ["ML", "Cloud", "Cyber Security"])

# mutli select
st.multiselect("Choose the Department", ["Content", "Sales", "Marketing"])

# selectslider
st.select_slider("Rating", ["Bad", "Good", "Excellent", "Outstanding"])

# slider
st.slider("Enter your number", 0,30)

# number_input
st.number_input("Pick a number", 0,100)

# text_input
st.text_input("Enter your email address")

# date_input
st.date_input("Opening ceremony")

# time_input
st.time_input("Choose your slot ?")


# text_area - to multiple text lines
st.text_area("Welcome")

# file_uploader
st.file_uploader("Upload your resume")

# color_picker
st.color_picker("color")

# progress
st.progress(90)

# spinner - to diplay a temp waiting
with st.spinner("Processing your request"):
    t.sleep(2)

# balloons
st.balloons()

# sidebar - pins the functions/widget to the side
st.sidebar.title("This is the sidebar")
st.sidebar.text_input("Mail Address")
st.sidebar.text_input("Password")
st.sidebar.radio("Choose your profession", ["Student", "Employed", "Unemployed"])
st.sidebar.checkbox("Save for future")
st.sidebar.button("Submit")


# Data Visualization

import pandas as pd
import numpy as np
st.title("Bar Chart")
data = pd.DataFrame(np.random.randn(50,2), columns=["x","y"])
st.bar_chart(data)
st.title("Line Chart")
st.line_chart(data)
st.title("Area Chart")
st.area_chart(data)



