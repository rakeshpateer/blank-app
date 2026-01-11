import streamlit as st

st.set_page_config(page_title="Secure Model App", page_icon="🔒")

st.title("🔒 Secure Model App")

# Function to check the password
def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.write("### ✅ Access Granted")
    st.write("Welcome! You can now use the model.")

    # Placeholder for the model
    user_input = st.text_area("Enter text to process:", "Hello World")

    if st.button("Run Model"):
        with st.spinner("Running model..."):
            # Simulate model processing
            import time
            time.sleep(1)
            result = user_input[::-1] # Simple reversal as a placeholder
            st.success("Model Output:")
            st.write(result)

    st.write("---")
    st.info("This is a secure template. Replace the dummy model logic with your actual model code.")

else:
    st.write("Please log in to access the model.")
