import re
import streamlit as st

st.set_page_config(page_title="Password Strength Meter Created by Rizwana Perveen", page_icon="", layout="centered")

st.markdown(
    """
    <style>
    .main {
    text-align: center;
    }
    .stTextInput {
    width: 60% 
    !important; 
    margin: auto;
    }
    .stButton button {
    width: 20%;
    background-color: blue;
    color: #ffffff;
    font-size: 18px;
    !important;
    margin: auto;
    }
    .stButton button:hover {
    background-color: black;
    color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("PASSWORD STRENGH METER")
st.write("Enter your password")
def check_password_strength(password):
    score=0
    feedback=[]

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("password should be '8' characters long!")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]",password):
        score += 1    
    else:
        feedback.append("password should be include both uppercase and lowercase!")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("password should include atleast one number (0-9)!")

    if re.search(r"[@$%!#^&*]", password):
        score += 1
    else:
        feedback.append("password should include atleast one special character (@$%!#^&*)!")

    if score ==4:
        st.success("Strong Password")
    elif score == 3:
        st.info("Moderate Password, suggest you to improve your password strength!")
    else:
        st.error("Your password is weak")

    if feedback:
        with st.expander("improve your password!"):
            for item in feedback:
                st.write(item) 
password = st.text_input("Enter your password", type= "password", help="Ensure your password should be strong")

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password first!")
