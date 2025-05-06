# sidebar.py
import streamlit as st

def my_sidebar():
    st.sidebar.image("typing2.png")
    # st.sidebar.markdown("---")
    st.sidebar.markdown("## ⌨️ Typing Tip")
    st.sidebar.write("Typing daily improves speed and accuracy. Try to focus and avoid looking at the keyboard!")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📬 Developer Contact")
    st.sidebar.write("📧 [Email Us](mailto:ismailahmedshahpk@gmail.com)")
    st.sidebar.write("🔗 [Connect on LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")
    st.sidebar.write("💬 [Chat on WhatsApp](https://wa.me/923322241405)")
    st.sidebar.write("🔗 [❤️ Join Us ❤️](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")
    st.sidebar.markdown("---")
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135716.png", width=90, use_container_width=True)
    st.sidebar.markdown("<p style='text-align: center; color: grey;'>Built with ❤️ by Ismail Ahmed Shah</p>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
