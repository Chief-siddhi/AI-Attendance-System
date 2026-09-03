import streamlit as st 

def header_home():
    st.markdown("""
        <div style="display: flex; flex-direction:column; align-items: center; justify-content: center; margin-top: 30px;">
    """, unsafe_allow_html=True)
    
    # st.image handles local file paths properly
    st.image("src/ui/images/logo.png", width=100)
    
    st.markdown("""
            <h1 style='text-align:center; color: #E0E3FF; margin-top: 10px; margin-bottom:30px;'>SNAP<br/>CLASS</h1>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    st.markdown("""
        <div style="display: flex;align-items: center; justify-content: center; margin-top: 30px; gap:10px;">
    """, unsafe_allow_html=True)
    
    # st.image handles local file paths properly
    st.image("src/ui/images/logo.png", width=100)
    
    st.markdown("""
            <h2 style='text-align:left; color: #5865F2;'>SNAP<br/>CLASS</h2>
        </div>
    """, unsafe_allow_html=True)
    