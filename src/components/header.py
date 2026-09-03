import streamlit as st 
import base64
import os

def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

def header_home():
    img_b64 = get_image_base64("src/ui/images/logo.png")
    img_html = f'<img src="data:image/png;base64,{img_b64}" style="width: 75px; height: 75px; object-fit: cover; border-radius: 12px; margin: 0 auto 8px auto; display: block;" />' if img_b64 else ''
    
    st.markdown(f"""
        <div style="width: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; margin-top: 0px; margin-bottom: 15px;">
            {img_html}
            <h1 style="text-align: center; color: #E0E3FF; margin: 0; line-height: 0.95; font-size: 2.8rem; font-family: 'Alfa Slab One', serif;">SNAP<br/>CLASS</h1>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    img_b64 = get_image_base64("src/ui/images/logo.png")
    img_html = f'<img src="data:image/png;base64,{img_b64}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 8px;" />' if img_b64 else ''
    
    st.markdown(f"""
        <div style="width: 100%; display: flex; align-items: center; justify-content: center; margin-top: 10px; margin-bottom: 15px; gap: 10px;">
            {img_html}
            <h2 style="text-align: left; color: #5865F2; margin: 0; font-size: 1.8rem; font-family: 'Alfa Slab One', serif;">SNAP<br/>CLASS</h2>
        </div>
    """, unsafe_allow_html=True)


    