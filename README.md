# 🩺 First-Aid AI Assistant (RAG-Based)

An intelligent **First-Aid Assistant Web App** built using **Streamlit + LangChain + Groq LLM** that provides **instant first-aid guidance** based on a structured medical PDF.

---

## 🚀 Features

- 📄 **PDF-Based Knowledge**  
  Uses a first-aid manual as the knowledge source

- 🧠 **RAG (Retrieval-Augmented Generation)**  
  Retrieves relevant medical context before answering

- ⚡ **Fast LLM (Groq - LLaMA 3.3 70B)**  
  Ultra-fast and high-quality responses

- 🧾 **Structured Output**
  - Symptom
  - Step-by-step first-aid instructions

- 🌐 **Streamlit Web App UI**
  Clean and interactive interface

- 🔍 **Smart Query Understanding**
  Maps user inputs like “burn” → “Thermal Burns”

---

## 🧠 How It Works

1. Load the **First Aid PDF**
2. Split into meaningful chunks
3. Convert into **embeddings**
4. Store in **Chroma Vector DB**
5. User asks a question
6. System retrieves relevant chunks
7. LLM generates a structured answer

---

## 📁 Project Structure

```

├── app.py                  # Streamlit application
├── first_aid_manual.pdf   # Knowledge base
├── requirements.txt
├── .env
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/first-aid-ai.git
cd first-aid-ai
````

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Setup Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get API key from: [https://console.groq.com](https://console.groq.com)

---

### 4. Add PDF File

Make sure this file exists:

```
first_aid_manual.pdf
```

---

### 5. Run the App

```bash
streamlit run app.py
```

---

## 💬 Example Usage

### Input:

```
burn on hand
```

### Output:

```
Symptom:
Redness, pain, or blistering caused by heat or fire.

Steps:
1. Cool the burn under running water
2. Remove jewelry
3. Do not pop blisters
4. Cover loosely with sterile gauze
```

---

## ⚠️ Disclaimer

This application provides **AI-generated first-aid guidance** based on a static document.
It is **NOT a substitute for professional medical advice**.

---

## 🛠 Tech Stack

* **Frontend:** Streamlit
* **LLM:** Groq (LLaMA 3.3 70B)
* **Framework:** LangChain
* **Embeddings:** HuggingFace (MiniLM)
* **Vector DB:** ChromaDB
* **PDF Processing:** PyMuPDF

---

## 🔥 Future Improvements

* 🎤 Voice input support
* 📱 Mobile-friendly UI
* 🧠 Memory-based conversation
* 🌍 Multi-language support
* 🚑 Emergency detection system

---
## 👥 Authors

| Name | Role |
|------|------|
| [Md Yusuf Ali](https://github.com/Yusufali2004) | Developer & Designer |
| [Md Irfan](https://github.com/irfan-789/) | Developer |
| [Md Naquibur Rahman]() | Contributor |
| [Md Shadab Talib]() | Contributor |

---
## ⭐ If You Like This Project

Give it a star ⭐ on GitHub and share it!
