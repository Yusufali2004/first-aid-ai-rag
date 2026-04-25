# 🩺 First-Aid AI Assistant

An intelligent **First-Aid Assistant Web App** built using **Streamlit + LangChain + Groq LLM** that provides **instant first-aid guidance** based on a structured medical PDF.

---

## 🌐 Live Demo

👉 [https://first-aid-ai-rag-73bndzqebswuybxqqcodbt.streamlit.app/](https://first-aid-ai-rag-73bndzqebswuybxqqcodbt.streamlit.app/)

---

## 🚀 Features

* 📄 **PDF-Based Knowledge**
  Uses a structured first-aid manual as the knowledge source

* ⚡ **Fast AI Responses (Groq - LLaMA 3.3 70B)**
  Ultra-fast and high-quality answers

* 🧾 **Structured Output**

  * Symptom
  * Step-by-step first-aid instructions

* 🌐 **Streamlit Web Interface**
  Clean, simple, and interactive UI

* 🔍 **Smart Query Understanding**
  Converts user input like *“burn on hand”* → relevant medical context

* ⚙️ **Lightweight & Deployment-Friendly**
  Optimized to run smoothly on cloud platforms

---

## 🧠 How It Works

1. Load the **First Aid PDF**
2. Extract relevant medical text
3. Match user query with known conditions
4. Provide context to LLM
5. Generate structured first-aid response

---

## 📁 Project Structure

```
├── app.py
├── first_aid_manual.pdf
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Yusufali2004/first-aid-ai-rag
cd first-aid-ai-rag
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Add API Key

Create `.env` (for local use):

```
GROQ_API_KEY=your_groq_api_key_here
```

👉 Get key: [https://console.groq.com](https://console.groq.com)

---

### 4. Run the App

```bash
streamlit run app.py
```

---

## ☁️ Deployment

This app is deployed using **Streamlit Cloud**

👉 Make sure to add secrets:

```
GROQ_API_KEY = "your_key"
```

---

## 💬 Example

### Input

```
burn on hand
```

### Output

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
* **PDF Processing:** PyPDF

---

## 🔥 Future Improvements

* 🎤 Voice input
* 💬 Chat history
* 🌍 Multi-language support
* 🚑 Emergency detection system
* 📱 Mobile UI optimization

---

## 👥 Authors

| Name                                            | Role                 |
| ----------------------------------------------- | -------------------- |
| [Md Yusuf Ali](https://github.com/Yusufali2004) | Developer & Designer |
| [Md Irfan](https://github.com/irfan-789/)       | Developer            |
| Md Naquibur Rahman                              | Contributor          |
| Md Shadab Talib                                 | Contributor          |

---

## ⭐ Support

If you found this useful, give it a ⭐ on GitHub

👉 [https://github.com/Yusufali2004/first-aid-ai-rag](https://github.com/Yusufali2004/first-aid-ai-rag)

---

