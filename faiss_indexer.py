import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from pdf_extractor import extract_text_from_pdf


class FaissDocumentIndexer:
    def __init__(self, pdf_folder, model_name='all-MiniLM-L6-v2'):
        self.pdf_folder = pdf_folder
        self.model = SentenceTransformer(model_name)
        self.documents = {}
        self.paragraphs = []
        self.doc_map = []
        self.index = None
        self.load_and_index()

    def load_and_index(self):
        print("🔄 Loading and indexing documents...")
        self.paragraphs = []
        self.doc_map = []
        self.documents = {}

        # Load and extract text from all PDFs
        for file in os.listdir(self.pdf_folder):
            if file.endswith(".pdf"):
                path = os.path.join(self.pdf_folder, file)
                text = extract_text_from_pdf(path)
                self.documents[file] = text

                paragraphs = [p.strip() for p in text.split("\n") if len(p.strip()) > 20]
                self.paragraphs.extend(paragraphs)
                self.doc_map.extend([file] * len(paragraphs))

        # Generate embeddings
        if self.paragraphs:
            print("🔍 Generating embeddings...")
            embeddings = self.model.encode(self.paragraphs, show_progress_bar=True)
            self.index = faiss.IndexFlatL2(embeddings.shape[1])
            self.index.add(np.array(embeddings, dtype='float32'))
            print(f"✅ Indexed {len(self.paragraphs)} paragraphs from {len(self.documents)} documents.")

    def search(self, query, top_k=3):
        if not self.index or not self.paragraphs:
            return "No documents loaded or indexed."

        print(f"🔎 Searching for: '{query}'")
        query_vec = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_vec, dtype='float32'), top_k)

        results = []
        for i in range(len(indices[0])):
            idx = indices[0][i]
            source_file = self.doc_map[idx]
            paragraph = self.paragraphs[idx]
            results.append((source_file, paragraph, distances[0][i]))

        return results


""
