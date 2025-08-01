import gdown
import os

# Google Drive direct file links
files = {
    "Fingpt/models/llama-2-7b-chat.gguf": "https://drive.google.com/drive/folders/1FbkMXDMzmOu3T2vZF_6sSdXlky5w5Pzr?usp=sharing",
    "Fingpt/data/sample_rbi.pdf": "https://drive.google.com/drive/folders/1wHczy_cnTotfQ43jDGJsoKRpVDAkV984?usp=sharing",
}

# Ensure the directories exist
os.makedirs("Fingpt/models", exist_ok=True)
os.makedirs("Fingpt/data", exist_ok=True)

# Download each file
for path, url in files.items():
    if not os.path.exists(path):
        print(f"🔄 Downloading {path} from Google Drive...")
        gdown.download(url, path, quiet=False)
        print(f"✅ Downloaded: {path}")
    else:
        print(f"✅ Already exists: {path}")
