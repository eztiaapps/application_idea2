import streamlit as st

# Set page title
st.set_page_config(page_title="My Streamlit App", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Home", "Analytics", "Settings"])

# Display Content Based on Selection
if section == "Home":
    st.title("🏠 Home Section")
    st.write("Welcome to the Home Section of the app.")

elif section == "Analytics":
    st.title("📊 Analytics Section")
    st.write("This section will display data analysis and insights.")

elif section == "Settings":
    st.title("⚙️ Settings Section")
    st.write("Configure your app settings here.")

# Run the app with: streamlit run app.py
