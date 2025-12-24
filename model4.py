import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import ollama


# -------------------------------------------------------
# 1. Load and Prepare Dataset
# -------------------------------------------------------
df = pd.read_csv("dataset_QA.csv")

df["question"] = df["question"].fillna("").astype(str)
df["answer"] = df["answer"].fillna("").astype(str)

# Combine Q + A (stronger retrieval like model3)
df["combined"] = (df["question"] + " " + df["answer"]).str.lower().str.strip()


# -------------------------------------------------------
# 2. Load Embedding Model (from model2)
# -------------------------------------------------------
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = embedding_model.encode(
    df["combined"].tolist(),
    convert_to_tensor=False
)


# -------------------------------------------------------
# 3. Ollama Models (from model2)
# -------------------------------------------------------
model_map = {
    "LLaMa2 13B": "llama3.2:latest",
    "Mistral 7B": "mistral:latest",
    "Falcon 7B": "falcon:latest"
}

# select model here
selected_llm = model_map["LLaMa2 13B"]



# -------------------------------------------------------
# 4. Ask Ollama to improve answer
# -------------------------------------------------------
def ask_ollama(prompt, model_name):
    response = ollama.generate(
        model=model_name,
        prompt=prompt
    )
    return response["response"]



# -------------------------------------------------------
# 5. Final Hybrid Retrieval + LLM Answer (Merged Model)
# -------------------------------------------------------
def get_answer(query, top_k=1, threshold=0.20):

    if not query or query.strip() == "":
        return [{
            "question": "",
            "dataset_answer": "",
            "llm_answer": "Please enter a valid question.",
            "score": 0
        }]

    # PREPROCESS
    query_clean = query.lower().strip()

    # Encode query (from model2)
    query_vec = embedding_model.encode(
        [query_clean],
        convert_to_tensor=False
    )

    # Similarity scores
    similarity_scores = cosine_similarity(query_vec, embeddings)[0]

    # Get top-k indices
    top_indices = similarity_scores.argsort()[::-1][:top_k]

    results = []

    for idx in top_indices:
        score = similarity_scores[idx]

        # Threshold logic (from model3)
        if score < threshold:
            results.append({
                "question": "",
                "dataset_answer": "",
                "llm_answer": "Sorry, I don't have information about that topic.",
                "score": float(score)
            })
            continue

        base_q = df.iloc[idx]["question"]
        base_a = df.iloc[idx]["answer"]

        # LLM refinement (from model2)
        prompt = f"""
You are a medical QA assistant.
Use the dataset information to give the best possible answer.

Dataset Question: {base_q}
Dataset Answer: {base_a}

User Query: {query}

Give a clear, correct final answer.
"""

        llm_output = ask_ollama(prompt, selected_llm)

        results.append({
            
            "dataset_answer": base_a,
            "llm_answer": llm_output,
            
        })

    return results



