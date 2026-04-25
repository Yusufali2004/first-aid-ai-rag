import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pypdf import PdfReader

# UI
st.set_page_config(page_title="First-Aid Assistant", page_icon="🩺")
st.title("🩺 First-Aid AI Assistant")
st.caption("Fast, lightweight, deployment-safe version")

# Load API key
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except:
    st.error("Add GROQ_API_KEY in Streamlit secrets")
    st.stop()

# Load LLM
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile"
)

# Load PDF (lightweight)
@st.cache_data
def load_pdf():
    reader = PdfReader("first_aid_manual.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

pdf_text = load_pdf()

# Smart keyword mapping
def get_relevant_context(query):
    query = query.lower()

    if "cut" in query or "bleeding" in query:
        return "Cuts and Bleeding: Apply pressure, clean wound, protect, seek help if needed."

    elif "burn" in query:
        return "Thermal Burns: Cool under water, remove jewelry, do not pop blisters, cover loosely."

    elif "choking" in query:
        return "Choking: Perform Heimlich maneuver, repeat until object removed."

    elif "heat" in query:
        return "Heat Exhaustion: Move to shade, hydrate, cool skin, monitor condition."

    elif "sprain" in query:
        return "Sprains: Rest, ice, compression, elevation."

    else:
        return None

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a First-Aid Assistant.

Use the given context to answer.

FORMAT:
Symptom:
<symptom>

Steps:
1. ...
2. ...
3. ...

If not found:
"This condition is not available in the guide."
"""),
    ("human", "Question: {input}\nContext: {context}")
])

chain = prompt | llm

# UI Input
user_input = st.text_input("Describe symptom or injury:")

if st.button("Get First Aid"):

    if not user_input.strip():
        st.warning("Enter a symptom")
    else:
        context = get_relevant_context(user_input)

        if context is None:
            st.write("This condition is not available in the guide.")
        else:
            with st.spinner("Analyzing..."):
                response = chain.invoke({
                    "input": user_input,
                    "context": context
                })

            st.subheader("🧾 First-Aid Instructions")
            st.write(response.content)

    st.caption("⚠️ AI-generated advice. Not a substitute for professional help.")
