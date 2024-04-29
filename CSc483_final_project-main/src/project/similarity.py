from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# NOTE: run pip install sentence-transformers transformers scikit-learn as an admin on terminal before running this

model = SentenceTransformer('bert-base-nli-mean-tokens')

def calculate_similarity(query, dataset):
    query_embedding = model.encode([query])
    similarities = []

    for item in dataset:
        item_embedding = model.encode([item])
        similarity = cosine_similarity(query_embedding, item_embedding)[0][0]
        similarities.append((item, similarity))

    # Sort by similarity in descending order, i.e the most relevant categories at the front
    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities

# Example usage
query = "machine rental"
dataset = ["machine & tool rental", "clothing rental", "karaoke rental"]

similarities = calculate_similarity(query, dataset)
for item, similarity in similarities:
    print(f"{item}: {similarity:.4f}")