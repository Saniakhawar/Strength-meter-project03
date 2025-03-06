import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Checker By Sania Khawar", page_icon="📄", layout="centered")

# Custom CSS for centering elements
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton {display: flex; justify-content: center;}
    .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 14px; padding: 10px;}
    .stButton button:hover {background-color: #45a049;}
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔏 Password Strength Checker")
st.write("Enter your password below and click **Check Strength** to see its security level. 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at **least 8 characters long**.")

    # Check uppercase and lowercase
    if re.search("[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **both uppercase (A-Z) and lowercase (a-z) letters**.")

    # Check digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one digit**.")

    # Check special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one special character**.")

    return score, feedback

# User input
password = st.text_input("Enter your password:", type="password")

# Centering the button using a container
col1, col2, col3 = st.columns([1, 2, 1])  # Create 3 columns and place button in the center column
with col2:
    if st.button("Check Strength"):
        if password:
            score, feedback = check_password_strength(password)

            # Strength level messages with improved symbols
            strength_levels = {
                0: "❌ Very Weak",
                1: "⚠️ Weak",
                2: "⚠️ Moderate",
                3: "✔️ Strong",
                4: "💪 Very Strong"
            }

            st.subheader(f"Password Strength: {strength_levels.get(score, 'Unknown')}")

            # Display feedback messages
            if feedback:
                for msg in feedback:
                    st.write(msg)
            else:
                st.success("✅ Your password is strong!")
        else:
            st.warning("⚠️ Please enter a password before checking.")
