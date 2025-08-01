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

## 🛠️ Quick Start

```bash
git clone https://github.com/JKalonewolf/FinGPT.git
cd FinGPT
