import streamlit as st
from datetime import time

st.set_page_config(page_title="Nilesh's Daily Routine Tracker", layout="wide")

st.title("📅 Daily Routine Dashboard")
st.markdown("Track your personal growth, office work, and family time with clarity and peace of mind.")

# --- Morning Block ---
st.header("🌅 Morning Routine")

wake_time = st.radio("Wake-up time", ["5:00 AM", "7:00 AM"])
corel_done = st.checkbox("✅ CorelDRAW learning done?")
corel_topic = st.text_input("Topic learned today:")
snacks_done = st.checkbox("Morning snacks taken?")
shower_done = st.checkbox("Shower completed?")
play_time = st.checkbox("Played with little boy?")

# --- Office Block ---
st.header("🏢 Office Routine")

office_start = st.time_input("Office start time", time(9, 15))
lunch_start = st.time_input("Lunch break start", time(12, 45))
office_end = st.time_input("Office end time (approx)", time(20, 30))
work_highlight = st.text_area("Work highlight of the day:")

# --- Evening Block ---
st.header("🌇 Evening Routine")

family_time = st.checkbox("Spent time with family?")
mood = st.radio("Mood after evening", ["Peaceful", "Tired", "Joyful"])
gratitude = st.text_input("🙏 One gratitude thought:")
sleep_time = st.time_input("Sleep time", time(23, 45))

# --- Weekly Review ---
st.header("🗓️ Weekly Reflection")

with st.expander("Fill this on Sunday night"):
    corel_week = st.number_input("CorelDRAW topics mastered this week:", min_value=0)
    wake_5am_days = st.number_input("Days with 5:00 AM wake-up:", min_value=0, max_value=7)
    bonding_days = st.number_input("Balako sathe bonding days:", min_value=0, max_value=7)
    avg_office_end = st.text_input("Average office end time:")
    peace_moment = st.text_area("One moment that gave peace:")
    improve_next = st.text_area("One thing to improve next week:")

st.success("✅ Routine logged! Keep growing with clarity and consistency.")
