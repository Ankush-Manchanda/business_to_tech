import streamlit as st
from ai_pipeline import analyze_requirement

st.set_page_config(page_title="Biz ➜ Tech Auto Tool", layout="centered")

st.title("📊 Business ➜ Technical Breakdown")
st.markdown("Convert high-level business requirements into modules, schemas, and pseudocode using AI")

# Input box
requirement = st.text_area("📝 Enter your high-level business requirement", height=200)

# Buttons
col1, col2 = st.columns([1, 1])
with col1:
    generate = st.button("🔍 Generate Breakdown")
with col2:
    clear = st.button("❌ Clear")

# Output area
if generate and requirement:
    with st.spinner("Analyzing... Please wait ⏳"):
        result = analyze_requirement(requirement)
    st.subheader("✅ Result")
    st.code(result, language='markdown')

if clear:
    st.rerun()
