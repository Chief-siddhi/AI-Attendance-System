import streamlit as st 

def style_background_home():

    st.markdown("""
    <style>
        
        .stApp {
            background: #5865F2 !important;
        }

        .stApp div[data-testid="stColumn"] {
            background-color: #3E0E3F !important;
            padding: 1.25rem 1.25rem !important;
            border-radius: 2rem !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            justify-content: center !important;
            text-align: center !important;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15) !important;
        }

        .stApp div[data-testid="stColumn"] > div {
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            width: 100% !important;
        }

        .stApp div[data-testid="stColumn"] [data-testid="stMarkdownContainer"] {
            text-align: center !important;
            width: 100% !important;
        }

        .stApp div[data-testid="stColumn"] [data-testid="stImage"] {
            display: flex !important;
            justify-content: center !important;
            margin: 0.25rem 0 !important;
            width: 100% !important;
        }

        .stApp div[data-testid="stColumn"] [data-testid="stImage"] img {
            margin: 0 auto !important;
            display: block !important;
        }

        .stApp div[data-testid="stColumn"] button {
            margin-top: 0.5rem !important;
            width: 100% !important;
        }

        .card-title {
            font-family: 'Alfa Slab One', serif !important;
            font-size: 1.8rem !important;
            color: #E0E3FF !important;
            text-align: center !important;
            margin: 0 0 0.4rem 0 !important;
            white-space: nowrap !important;
            line-height: 1 !important;
        }
    </style>

    """, unsafe_allow_html=True)

def style_background_dashboard():

    st.markdown("""
    <style>
        
        .stApp{
            background: #E0E3FF !important;
        }
    </style>
    """,unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Alfa+Slab+One&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
        
        /* hide top bar of streamlit */
        header[data-testid="stHeader"] {
            display: none !important;
        }

        .block-container {
            padding-top: 0.5rem !important;
            padding-bottom: 0.5rem !important;
            max-width: 800px !important;
        }

        [data-testid="stMarkdownContainer"] {
            width: 100% !important;
        }

        h1 {
            font-family: 'Alfa Slab One', serif !important;
            font-size: 2.8rem !important;
            font-weight: 400 !important;
            line-height: 0.95 !important;
            margin-bottom: 0rem !important;
        }

        h2 {
            font-family: 'Alfa Slab One', serif !important;
            font-size: 2rem !important;
            font-weight: 400 !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important; 
        }

        h3, h4, p {
            font-family: 'Outfit', sans-serif;
        }

        button {
            border-radius: 1.5rem !important;
            background-color: #EB459E !important;
            color: white !important;
            padding: 8px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="secondary"] {
            border-radius: 1.5rem !important;
            background-color: #EB459E !important;
            color: white !important;
            padding: 8px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button[kind="tertiary"] {
            border-radius: 1.5rem !important;
            background-color: #EB459E;
            color: white !important;
            padding: 8px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
        }

        button:hover {
            transform: scale(1.02) !important;
        }
    </style>

    """, unsafe_allow_html=True)