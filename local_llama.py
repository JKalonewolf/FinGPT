import os
from llama_cpp import Llama

# Auto-download if model is missing
if not os.path.exists(".fingpt/models/llama-2-7b-chat.gguf"):
    print("🔍 Model not found locally. Downloading from Google Drive...")
    from os import *  # This will trigger the download

# Initialize Llama
llm = Llama(
    model_path="./models/llama-2-7b-chat.gguf",
    n_ctx=4096,
    n_threads=8,
    n_gpu_layers=32,
    verbose=False,
)

def ask_fingpt(user_query, indexer):
    matched_docs = indexer.search(user_query)

    if not matched_docs:
        context = "No relevant documents found."
    else:
        context = "\n\n".join([f"{doc}:\n{text}" for doc, text, _ in matched_docs[:3]])

    prompt = f"""You are a legal assistant for RBI and SEBI regulations.

Context:
{context}

Question:
{user_query}
Answer:"""

    output = llm(prompt, max_tokens=512)
    return output["choices"][0]["text"].strip()
