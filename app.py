# app.py
import streamlit as st
from firebase import db  # Import Firestore instance
from streamlit_cookies_manager import CookieManager

# Function to register users
def register_user(email, name, role):
    user_data = {
        "email": email,
        "name": name,
        "role": role,
        "registration_date": firestore.SERVER_TIMESTAMP,
        "is_active": True
    }
    db.collection(role + "s").add(user_data)  # Save in 'admins' or 'users' collection

# Function to check login
def login_user(email, role):
    users_ref = db.collection(role + "s").where("email", "==", email).limit(1).get()
    return len(users_ref) > 0  # Return True if user exists

# Streamlit app
def main():
    st.title("User Authentication")

    # Cookie Manager
    cookies = CookieManager()
    cookies.load()

    if cookies.get("logged_in"):
        st.success(f"Logged in as {cookies.get('user_role')}")
        if cookies.get('user_role') == 'admin':
            st.write("Welcome Admin!")
            # Admin functionalities here
        else:
            st.write("Welcome User!")
            # User functionalities here
    else:
        menu = st.sidebar.selectbox("Select Action", ["Login", "Register"])

        if menu == "Login":
            st.subheader("Login")
            email = st.text_input("Email")
            role = st.selectbox("Role", ["user", "admin"])
            if st.button("Login"):
                if login_user(email, role):
                    cookies.set("logged_in", True, max_age=3600)  # 1 hour expiry
                    cookies.set("user_role", role)
                    st.success(f"Logged in as {role}")
                    st.experimental_rerun()  # Refresh the app
                else:
                    st.error("Invalid email or role")

        elif menu == "Register":
            st.subheader("Register")
            email = st.text_input("Email")
            name = st.text_input("Name")
            role = st.selectbox("Role", ["user", "admin"])
            if st.button("Register"):
                register_user(email, name, role)
                st.success("Registration successful!")

if __name__ == "__main__":
    main()
