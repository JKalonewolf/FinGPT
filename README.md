# 🧠 FinGPT - AI-Powered Financial Assistant

FinGPT is an open-source financial assistant powered by a local Large Language Model (LLM). It helps users analyze market trends, generate financial reports, answer finance-related questions, and more — all privately and offline.

> ⚠️ **Model Note:** This project uses the `llama-2-7b-chat.gguf` model, which will be automatically downloaded from the author’s Google Drive during first run.

---

## 🧠 Model Setup (Auto-Downloaded)

### ✅ First-Time Use:

When you run the project for the first time, it will automatically:

1. Download the required LLM model from the developer's **Google Drive**.
2. Create a folder named `FinGPT/` in your local environment.
3. Inside `FinGPT/`, you'll find:
    ```
    FinGPT/
    ├── data/
    └── models/
            └── llama-2-7b-chat.gguf
    ```

4. Go to:
5. Ensure that the file `llama-2-7b-chat.gguf` is present in that folder.

> ✅ **This version (`llama-2-7b-chat.gguf`) is required** for correct operation of the FinGPT system.

If the model file is missing or corrupted, please manually download and place it in that directory.

---

## 📁 Project Structure

```bash
FinGPT/
├── backend/                # (if exists) Flask/FastAPI backend
├── data/                   # Stores processed data
├── ingestion/              # PDF/document ingestion logic
├── models/                 # Holds downloaded model files
│   └── models/
│       └── llama-2-7b-chat.gguf
├── PythonProject/          # (if used as submodule or template)
├── streamlit/              # Streamlit frontend UI
├── uploaded_pdfs/          # Uploaded PDFs for analysis
├── utils/                  # Utility scripts
├── .env                    # Environment variables
├── app.py                  # Main Streamlit app entry
├── api_handler.py          # Handles model and app API logic
├── download_models.py      # Downloads llama model automatically
├── faiss_indexer.py        # Vector store indexing
├── huggingface_api.py      # (if used) HuggingFace fallback support
├── local_llama.py          # Loads and runs local llama model
├── pdf_extractor.py        # PDF parsing logic
├── requirements.txt        # Python dependencies
└── README.md               # You're here!
## 🛠️ Quick Start

```bash
git clone https://github.com/JKalonewolf/FinGPT.git
cd FinGPT

python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux

pip install -r requirements.txt


Run the App
Make sure your virtual environment is active.
bash
python app.py


---

✅ Let me know when you're ready to insert this into your `README.md` file directly, or if you'd like a downloadable version.

Also, **share the Google Drive model link**, so I can update the `[Google Drive Link Here]` with the actual clickable download.

