import streamlit as st
import json
from tools.tavily_tool import search_person
from agents.profile_agent import generate_profile
from groq import Groq

st.set_page_config(
    page_title="AI Powered Affluent Profile Generator",
    page_icon="🤖",
    layout="wide"
)
st.title("🤖 AI Powered Affluent Profile Generator")
st.caption("Generate detailed profiles using Groq + Tavily AI")
st.sidebar.write("Generate professional profiles using AI.")
st.sidebar.markdown("---")

st.title("AI Powered Affluent Profile Generator")

name = st.text_input("Enter Person Name")
context = st.text_input("Enter Context")

if st.button("Generate Profile"):

    query = f"{name} {context}"

    search_results = search_person(query)

    profile = generate_profile(
        name,
        context,
        search_results
    )

    st.success("Profile Generated Successfully!")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image("images/sundar pichai.jpg",width=500
        )

    with col2:
        st.markdown(profile)

    with open("output/profile.json", "w") as file:
        json.dump(
            {"profile": profile},
            file,
            indent=4
        ) 
    with open("output/profile.md", "w", encoding="utf-8") as file:
        file.write(profile)
    
    st.download_button(
    label="📥 Download Profile",
    data=profile,
    file_name=f"{name}_profile.md",
    mime="text/markdown"
)