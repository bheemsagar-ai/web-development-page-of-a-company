import streamlit as st
import pandas as pd

st.set_page_config(page_title="The Best Company", layout="wide", page_icon="🏢")

st.markdown("""
    <style>
        .hero-title { font-size: 3rem; font-weight: 800; color: #1a1a2e; text-align: center; }
        .hero-sub { font-size: 1.1rem; color: #555; text-align: center; margin-bottom: 2rem; }
        .divider { border-top: 2px solid #e0e0e0; margin: 2rem 0; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero-title">🏢 THE BEST COMPANY</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Innovation · Technology · Excellence</div>', unsafe_allow_html=True)

st.markdown("""
> 🚀 A forward-thinking company committed to solving real-world problems through innovation and technology.  
> 💡 Empowering individuals and industries with reliable, scalable, and user-centric solutions.  
> 🌐 Continuously evolving to shape a smarter, more connected future.
""")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

col_a, col_b, col_c, col_d = st.columns(4)
col_a.metric("Team Members", "12")
col_b.metric("Projects Delivered", "50+")
col_c.metric("Years of Experience", "5+")
col_d.metric("Happy Clients", "100+")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("## 👥 Meet Our Team")

df = pd.read_csv("data.csv", sep=",")

cols = st.columns(3)
for i, (_, row) in enumerate(df.iterrows()):
    with cols[i % 3]:
        st.image("images/" + row["image"], use_container_width=True)
        st.markdown(f"**{row['first name']} {row['last name']}**")
        st.caption(row["role"])
        st.markdown("---")
