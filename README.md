# 🤖 AI-MEDIMATE-MEDICAL-CHATBOT

AI MEDIMATE is an intelligent medical chatbot built using Streamlit, NLP, Semantic Search, and Large Language Models (LLMs).
It provides accurate and user-friendly answers to general medical queries by combining verified NIH medical data with LLM-enhanced responses using a RAG (Retrieval-Augmented Generation) approach.

📌 Features

🦠 Ask questions about diseases (diabetes, cancer, asthma, etc.)

⚠ Get details on symptoms (fever, cough, chest pain, weakness)

🔍 Understand diagnosis & medical conditions

💊 Learn about treatments, medicines & side effects

🧪 Information on medical tests (CBC, MRI, X-ray, etc.)

📚 Uses 47,000+ verified medical Q&A pairs from NIH MedQuAD

🧠 Hybrid AI: Semantic Search + LLM

💬 ChatGPT-style conversational UI

🗑️ Clear Chat option

⚡ Fast, simple, and interactive interface

🛠️ Tech Stack

Python

Streamlit – Web UI

Sentence Transformers – Text embeddings

Scikit-learn – Cosine similarity

Ollama – LLM inference

Pandas – Dataset handling

📂 Project Structure
AI-MEDIMATE-MEDICAL-CHATBOT/
│
├── App.py                 # Streamlit frontend
├── model4.py              # Hybrid RAG + LLM backend
├── dataset_QA.csv         # NIH MedQuAD medical dataset
├── Medichatbot_demo.mp4   # Demo video
├── README.md              # Documentation

⚙️ How the System Works (RAG Pipeline)

User enters a medical query

Query is converted into embeddings using SentenceTransformer

Similar medical Q&A pairs are retrieved using cosine similarity

Retrieved answer is passed to an LLM via Ollama

Chatbot displays:

🧠 LLM Answer (refined & conversational)

📚 Database Answer (original dataset response)

🧠 LLM Models Used (via Ollama)

AI MEDIMATE supports multiple local LLMs using Ollama.
📊 Dataset

This project uses the NIH MedQuAD (Medical Question Answering Dataset), a trusted and publicly available medical dataset.

🔗 Dataset Link: 👉 https://github.com/abachaa/MedQuAD

Dataset Highlights

47,000+ medical question–answer pairs

Curated from NIH-trusted medical sources

Covers diseases, drugs, diagnosis, treatments & tests

🔹 Supported Models
Model Name	Ollama Identifier	Description
LLaMA 3.2 (13B)	llama3.2:latest	High-quality medical explanations
Mistral 7B	mistral:latest	Fast and efficient responses
Falcon 7B	falcon:latest	Lightweight and reliable

You can switch models easily inside model4.py.

💻 LLM System Requirements
🔹 Minimum Requirements

OS: Windows / Linux / macOS

RAM: 8 GB (for Mistral / Falcon)

CPU: Modern multi-core CPU

Storage: 10–15 GB free space

🔹 Recommended (Best Performance)

RAM: 16 GB or more

GPU: Optional (NVIDIA GPU improves speed)

Storage: 20+ GB free

⚠ LLaMA 13B models require higher RAM and run slower on low-end systems.

🔧 Ollama Installation & Setup
1️⃣ Install Ollama

👉 https://ollama.com

2️⃣ Pull a model
ollama pull llama3.2


(or)

ollama pull mistral

3️⃣ Verify installation
ollama list

🚀 Run the Application
Install Python dependencies
pip install streamlit pandas sentence-transformers scikit-learn ollama

Start the chatbot
streamlit run App.py

🎥 Demo

📹 Refer to Medichatbot_demo.mp4 for a full demonstration of the chatbot workflow and UI.

⚠️ Disclaimer

This chatbot is intended for educational and informational purposes only.
It does not replace professional medical advice, diagnosis, or treatment.

👨‍💻 Developer

Vishesh Chavda
Data Scientist | Machine Learning Enthusiast
