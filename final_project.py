import os
import streamlit as st
from dotenv import load_dotenv

# LangChain Imports
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

# Fixed imports
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# Load env
load_dotenv()

# UI
st.set_page_config(page_title="First-Aid Assistant", page_icon="🩺")
st.title("🩺 First-Aid AI Assistant")
st.write("Ask about symptoms and get immediate first-aid steps.")

# ⚠️ REMOVE CACHE (important for now)
def setup_rag():

    # 1. Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 2. LLM
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.3-70b-versatile"
    )

    # 3. Load PDF
    if not os.path.exists("first_aid_manual.pdf"):
        st.error("❌ first_aid_manual.pdf not found in project folder")
        st.stop()

    loader = PyPDFLoader("first_aid_manual.pdf")
    documents = loader.load()

    # 4. Split
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)

    # 5. Vector DB (SAFE persistent version)
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    retriever = vector_db.as_retriever(search_kwargs={"k": 2})

    # 6. Prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a First-Aid Assistant.

Identify the condition and give clear steps.

FORMAT STRICTLY:
Symptom:
<symptom>

Steps:
1. ...
2. ...
3. ...

If not found, say:
"This condition is not available in the guide."

Context:
{context}
"""),
        ("human", "{input}")
    ])

    # 7. Chain
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, combine_docs_chain)

    return rag_chain


# Initialize safely
try:
    rag_chain = setup_rag()
except Exception as e:
    st.error(f"Initialization Error: {e}")
    st.stop()


# Query enhancer
def enhance_query(user_input):
    mapping = {
        "cut": "Cuts and Bleeding",
        "bleeding": "Cuts and Bleeding",
        "burn": "Thermal Burns",
        "choking": "Choking Adults Heimlich Maneuver",
        "heat": "Heat Exhaustion",
        "sprain": "Sprains and Strains"
    }

    for key in mapping:
        if key in user_input.lower():
            return mapping[key]

    return user_input


# UI input
user_input = st.text_input("Describe symptom or injury:")

if st.button("Get First Aid"):

    if not user_input.strip():
        st.warning("Please enter a symptom.")
    else:
        query = enhance_query(user_input)

        try:
            with st.spinner("Analyzing..."):
                response = rag_chain.invoke({"input": query})

            st.subheader("🧾 First-Aid Instructions")
            st.write(response["answer"])

        except Exception as e:
            st.error(f"❌ Error while processing: {e}")

        st.caption("⚠️ This is AI-generated advice. Not a substitute for professional medical help.")