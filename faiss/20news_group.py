import re
from sklearn.datasets import fetch_20newsgroups
import tensorflow_hub as hub

newsgroups = fetch_20newsgroups(subset='all')
documents = newsgroups.data

def preprocess_text(text):
    # Remove email headers
    text = re.sub(r'^From:.*\n?', '', text, flags=re.MULTILINE)
    # Remove email addresses
    text = re.sub(r'\S*@\S*\s?', '', text)
    # Remove punctuations and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove excess whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# Preprocess each document
processed_documents = [preprocess_text(doc) for doc in documents]

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

def embed_text(text):
    return embed(text).numpy()

X_use = np.vstack([embed_text([doc]) for doc in processed_documents])

dimension = X_use.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(X_use)

def search(query_text, k=5):
    preprocessed_query = preprocess_text(query_text)
    query_vector = embed_text([preprocessed_query])
    distances, indices = index.search(query_vector.astype('float32'), k)
    return distances, indices

query_text = "motocyle"
distances, indices = search(query_text)

for i, idx in enumerate(indices[0]):
    print(f"Rank {i+1}: (Distance: {distances[0][i]})\n{processed_documents[idx]}\n")