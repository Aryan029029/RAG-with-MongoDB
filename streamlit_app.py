import streamlit as st

from src.ingest import ingest
from src.retrieval import retrieve
from src.generator import generate_answer

st.set_page_config(
    page_title="LittleMongo AI",
    page_icon="🤖",
    layout="wide",
)

if "loaded" not in st.session_state:
    with st.spinner("Loading knowledge base..."):
        ingest()
    st.session_state.loaded = True

st.markdown("""
<style>

.main{
background:#F5F7FB;
}

.block-container{
max-width:900px;
padding-top:2rem;
}

h1{
text-align:center;
font-size:54px!important;
font-weight:800!important;
}

.subtitle{
text-align:center;
font-size:20px;
color:#6B7280;
margin-bottom:35px;
}

.stTextArea textarea{
border-radius:20px!important;
border:1px solid #E5E7EB!important;
background:white!important;
box-shadow:0 10px 30px rgba(0,0,0,.08)!important;
}

.stButton>button{

width:100%;

height:56px;

border-radius:16px;

background:#2563EB;

color:white;

font-size:18px;

font-weight:700;

border:none;

}

.answer{

background:white;

padding:28px;

border-radius:20px;

box-shadow:0 12px 30px rgba(0,0,0,.06);

margin-top:20px;

}

.source{

background:white;

padding:18px;

border-radius:16px;

margin-top:10px;

box-shadow:0 8px 20px rgba(0,0,0,.05);

}

</style>
""", unsafe_allow_html=True)

st.markdown("<h1> LittleMongo AI</h1>", unsafe_allow_html=True)

st.markdown(
'<div class="subtitle">Understand MongoDB Documentation using Retrieval-Augmented Generation</div>',
unsafe_allow_html=True
)

question = st.text_area(
"",
placeholder="Ask anything about MongoDB..."
)

if st.button("Ask AI"):

    docs = retrieve(question)

    answer = generate_answer(question, docs)

    st.markdown(
        f"""
<div class="answer">

<h3>🤖 AI Response</h3>

{answer}

</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("### 📚 Sources")

    for doc in docs:

        page = doc.metadata.get("page","?")

        st.markdown(
            f"""
<div class="source">

📄 MongoDB Documentation — Page {page}

</div>
""",
            unsafe_allow_html=True,
        )