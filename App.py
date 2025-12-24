import streamlit as st
from model4 import get_answer  # your RAG function

st.set_page_config(page_title="MEDIMATE Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 MEDIMATE CHATBOT")
st.subheader("Hey, I'm your Doc Buddy! Ask me anything.")
#-----------------
with st.sidebar:
    st.header("About")

    st.write(
        """
        **🦠 Diseases**  
        Ask about health conditions like **diabetes, asthma, cancer, hypertension**, and more.

        **⚠ Symptoms**  
        Get info on symptoms such as **fever, chest pain, cough**, weakness, etc.

        **🔍 Diagnosis**  
        Understand diagnostic insights for **thyroid issues, anemia, infections**, and other conditions.

        **💊 Treatments**  
        Learn about treatment options for **arthritis, migraine, allergies**, and other problems.

        **📚 Medicines & Tests**  
        Covers medication details, side effects, and tests like **MRI, CBC, X-ray**, and more—  
        all powered by **47,000+ verified medical QA pairs** from **NIH MedQuAD**.
        """
    )

    st.write("---")
    


# -----------------------------------------------------
# Reset input safely after rerun
# -----------------------------------------------------
if st.session_state.get("clear_input"):
    st.session_state["user_query"] = ""
    st.session_state["clear_input"] = False

# ------------------ INPUT ------------------
if "user_query" not in st.session_state:
    st.session_state["user_query"] = ""

user_query = st.text_input("Ask your medical question:", key="user_query")



# --------------- CLEAR CHAT & GET ANSWER BUTTONS ---------------
col1, col2 = st.columns([6, 1])

with col1:
    get_ans = st.button("Get Answer")

with col2:
    if st.button("🗑️ Clear"):
        st.session_state["messages"] = []
        st.session_state["clear_input"] = True
        st.rerun()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []



# -----------------------------------------------------
# Get Answer logic
# -----------------------------------------------------
if get_ans:
    if user_query.strip() == "":
        st.warning("Please enter a question.")
    else:
        st.session_state["messages"].insert(0, {"role": "user", "content": user_query})

        result = get_answer(user_query)

        if isinstance(result, list) and len(result) > 0:
            final_answer = result[0].get("llm_answer", "No answer found.")
            final_answer2 = result[0].get("dataset_answer", "No answer found.")
        else:
            final_answer = "No answer found."

        
        ### 🔥 CHANGE START — store answers with type labels
        ### 🔥 CHANGE START — combine both answers into ONE message

        combined_answer = (
            "### 🧠 LLM Answer:\n"
            f"{final_answer}\n\n"
            "### 📚 Database Answer:\n"
            f"{final_answer2}"
        )
        
        st.session_state["messages"].insert(0, {
            "role": "assistant",
            "content": combined_answer
        })

        ### 🔥 CHANGE END


        # Set flag to clear input safely
        st.session_state["clear_input"] = True

        st.rerun()
# ------------------ SHOW CHAT HISTORY (NEWEST ON TOP) ------------------
# messages are stored newest first, so reverse TEMPORARILY for display
for i in range(0, len(st.session_state["messages"]), 2):
    block = st.session_state["messages"][i:i+2][::-1]  # reverse pair

    for msg in block:
        if msg["role"] == "user":
            with st.chat_message("user", avatar="👨‍⚕️"):
                st.write(msg["content"])
        else:
            with st.chat_message("assistant", avatar="📔"):
                st.write(msg["content"])


st.caption("Developed by Vishesh Chavda")