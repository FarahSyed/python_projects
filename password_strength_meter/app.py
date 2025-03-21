import streamlit as st
import random
import string
import re

# App set up
st.set_page_config(page_title="Password Strength Meter")
st.title("🔐 Password Strength Meter")


# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        feedback.append("✅ Strong Password!")
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")
    
    return feedback

# Function to generate a strong password
def generate_strong_password():
    all_characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = random.sample(all_characters, 12)  # Random 12-character password
    random.shuffle(password)
    return ''.join(password)

# Function to check if the password is blacklisted
def is_password_blacklisted(password):
    blacklisted_passwords = ["password", "password123", "qwerty", "123456", "letmein", "welcome", "admin"]
    if password.lower() in blacklisted_passwords:
        return True
    return False

# Function for Streamlit UI
def main():    
    password = st.text_input("Enter your password:", type="password")
    
    if password:
        # Check if password is blacklisted
        if is_password_blacklisted(password):
            st.warning("❌ This password is too common and easily guessed!")
        else:
            feedback = check_password_strength(password)
            for line in feedback:
                st.write(line)


    if st.button("Generate Strong Password"):
        st.session_state['generated_password'] = generate_strong_password()
        st.markdown(f"**Suggested Strong Password:** <span style=\"color:blue;\">Copy it!</span>", unsafe_allow_html=True)
        st.code(st.session_state['generated_password'], language="plaintext")  # Display password in a code block
        st.info("💡 Use this generated password or create one with similar complexity.")

# Run the app
if __name__ == "__main__":
    main()
