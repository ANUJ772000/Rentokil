import streamlit as st
from pathlib import Path
st.set_page_config(page_title="Rentokil Platform Intelligence",layout="wide")
st.markdown("<style>body{font-family:Arial;} .red{color:#E31E24}</style>", unsafe_allow_html=True)
st.title("From Pest Control to Platform Intelligence")
st.caption("Upload assets/logo.png, assets/team.png, assets/intro.mp4, assets/vision.mp4")
if Path("assets/logo.png").exists(): st.image("assets/logo.png", width=220)
c1,c2=st.columns([2,1])
with c1:
    st.header("Strategic Transformation")
    st.write("Interactive presentation covering all 13 sections.")
with c2:
    if Path("assets/team.png").exists(): st.image("assets/team.png")
st.header("1. Company Intro Video")
if Path("assets/intro.mp4").exists(): st.video("assets/intro.mp4")
for title in ["2. Current Business Model","3. Why Change Now?","4. Emerging Tech Gaps","5. Proposed Transformation","6. New Platform Business Model","7. Before vs After","8. MOAT Transformation","9. Financial Impact","10. Roadmap","11. Risks & Mitigation"]:
    st.header(title); st.write("Content section ready for customization.")
st.header("Vision Video")
if Path("assets/vision.mp4").exists(): st.video("assets/vision.mp4")
st.header("Thank You / Q&A")
