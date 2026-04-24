import chromadb
from chromadb.utils import embedding_functions

# Define the embedding function using SentenceTransformers
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.Client()

collection_name = "my_grocery_collection"


def main():
    try:
        collection = client.create_collection(
            name=collection_name,
            metadata={"description": "A collection for storing grocery data"},
            configuration={
                "hnsw": {"space":"cosine"},
                "embedding_function": ef
            }
        )

        print(f"Collection created: {collection.name}")


        # Array of grocery-related text items
        texts = [
            'fresh red apples',
            'organic bananas',
            'ripe mangoes',
            'whole wheat bread',
            'farm-fresh eggs',
            'natural yogurt',
            'frozen vegetables',
            'grass-fed beef',
            'free-range chicken',
            'fresh salmon fillet',
            'aromatic coffee beans',
            'pure honey',
            'golden apple',
            'red fruit'
        ]

        # Create a list of unique IDs for each text item in the 'texts' array
        # Each ID follows the format 'food_<index>', where <index> starts from 1
        ids = [f"food_{index + 1}" for index, _ in enumerate(texts)]

        collection.add(
            documents=texts,
            ids=ids,
            metadatas=[{"source": "grocery_store", "category": "food"} for _ in texts]
        )

        all_items = collection.get()

        # Log the retrieved items to the console for inspection
        # This will print out all the documents, IDs, and metadata stored in the collection
        print("Collection contents:")
        print(f"Number of documents: {len(all_items['documents'])}")

        def perform_similarity_search(collection, all_items):
            try:
                query_term = ["red", "fresh"]

                results = collection.query(
                    query_texts=query_term,
                    n_results=3
                )

                print(f"Query results for '{query_term}':")
                print(results)

                # Check if no results are returned or if the results array is empty
                if not results or not results['ids'] or len(results['ids'][0]) == 0:
                    # Log a message indicating that no similar documents were found for the query term
                    print(f'No documents found similar to "{query_term}"')
                    return

                for q in range(len(query_term)):
                    print(f'Top 3 similar documents to "{query_term}":')
                    # Access the nested arrays in 'results["ids"]' and 'results["distances"]'
                    for i in range(min(3, len(results['ids'][q]))):
                        doc_id = results['ids'][q][i]  # Get ID from 'ids' array
                        score = results['distances'][q][i]  # Get score from 'distances' array
                        # Retrieve text data from the results
                        text = results['documents'][q][i]
                        if not text:
                            print(f' - ID: {doc_id}, Text: "Text not available", Score: {score:.4f}')
                        else:
                            print(f' - ID: {doc_id}, Text: "{text}", Score: {score:.4f}')
            except Exception as e:
                print(f"Error in similarity search: {e}")
        
        perform_similarity_search(collection, all_items)
    except Exception as e:
        print(e)
    finally:
        client.close()

if __name__ == "__main__":
    main()