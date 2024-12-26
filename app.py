import streamlit as st
import pandas as pd
import os
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# Get the current date in DD-MM-YYYY format
current_date = datetime.now().strftime("%d-%m-%Y")

# Auto-refresh the page every 2 seconds, up to a maximum of 100 times
count = st_autorefresh(interval=2000, limit=100, key="fizzbuzz_counter")

# FizzBuzz logic based on the counter
if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")

# Define the path to the attendance file
attendance_dir = "Attendance"
attendance_file = f"{attendance_dir}/Attendance_{current_date}.csv"

# Check if the attendance file exists
if os.path.exists(attendance_file):
    # Read the CSV file and display it
    df = pd.read_csv(attendance_file)
    st.dataframe(df.style.highlight_max(axis=0))
else:
    # Display an error message if the file is missing
    st.error(f"Attendance file for {current_date} not found: {attendance_file}")
    st.write("Please ensure the file exists in the 'Attendance' directory.")
