import streamlit as st
from model import predict_email

st.set_page_config(page_title="Phishing Email Detector", layout="centered")

st.title("📧 Phishing Email Detector")

st.markdown("Enter the **body of an email**, and this app will predict whether it's a phishing attempt or legitimate.")

# Initialize session state for clear counter
if "clear_counter" not in st.session_state:
    st.session_state.clear_counter = 0

# Using a form to control the order better
with st.form("email_form", clear_on_submit=False):
    # Email text input
    email_text = st.text_area(
        "Email Body", 
        height=200, 
        placeholder="Paste your email text here...",
        key=f"email_text_{st.session_state.clear_counter}"
    )
    
    # Button layout below the textbox
    col1, col2 = st.columns([1, 1])
    
    with col1:
        analyze_clicked = st.form_submit_button("Analyze")
    
    with col2:
        clear_clicked = st.form_submit_button("Clear")

# Handle button clicks outside the form
if clear_clicked:
    st.session_state.clear_counter += 1
    st.rerun()

if analyze_clicked:
    if not email_text.strip():
        st.warning("Please enter some email content.")
    else:
        prediction = predict_email(email_text)

        if prediction == 1:
            st.error("⚠️ This email is likely a phishing attempt.")
        else:
            st.success("✅ This email appears to be legitimate.")

