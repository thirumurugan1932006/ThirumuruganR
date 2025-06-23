import streamlit as st
from auth import signup, login
from chatbot import find_story, save_history

st.title("📖 தமிழ் கதைகள் BOT")

menu = ["Signup", "Login"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Signup":
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type='password')
    if st.button("Signup"):
        if signup(new_user, new_pass):
            st.success("Account created successfully.")
        else:
            st.error("Username already exists.")

elif choice == "Login":
    st.subheader("Login to Chat")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        user = login(username, password)
        if user:
            st.success(f"Welcome {username}!")
            query = st.text_input("உங்கள் கேள்வி/கதை தலைப்பு")
            if st.button("Search Story"):
                result = find_story(query)
                st.write(result)
                save_history(user[0], query, result)
        else:
            st.error("Invalid credentials.")
          
