
from client import create_collection

collection_name = "my_book_collection"

# List of book dictionaries with comprehensive details for advanced search
books = [
    {
        "id": "book_1",
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "year": 1925,
        "rating": 4.1,
        "pages": 180,
        "description": "A tragic tale of wealth, love, and the American Dream in the Jazz Age",
        "themes": "wealth, corruption, American Dream, social class",
        "setting": "New York, 1920s"
    },
    {
        "id": "book_2",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "year": 1960,
        "rating": 4.3,
        "pages": 376,
        "description": "A powerful story of racial injustice and moral growth in the American South",
        "themes": "racism, justice, moral courage, childhood innocence",
        "setting": "Alabama, 1930s"
    },
    {
        "id": "book_3",
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "year": 1949,
        "rating": 4.4,
        "pages": 328,
        "description": "A chilling vision of totalitarian control and surveillance society",
        "themes": "totalitarianism, surveillance, freedom, truth",
        "setting": "Oceania, dystopian future"
    },
    {
        "id": "book_4",
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "year": 1997,
        "rating": 4.5,
        "pages": 223,
        "description": "A young wizard discovers his magical heritage and begins his education at Hogwarts",
        "themes": "friendship, courage, good vs evil, coming of age",
        "setting": "England, magical world"
    },
    {
        "id": "book_5",
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "year": 1954,
        "rating": 4.5,
        "pages": 1216,
        "description": "An epic fantasy quest to destroy a powerful ring and save Middle-earth",
        "themes": "heroism, friendship, good vs evil, power corruption",
        "setting": "Middle-earth, fantasy realm"
    },
    {
        "id": "book_6",
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "genre": "Science Fiction",
        "year": 1979,
        "rating": 4.2,
        "pages": 224,
        "description": "A humorous space adventure following Arthur Dent across the galaxy",
        "themes": "absurdity, technology, existence, humor",
        "setting": "Space, various planets"
    },
    {
        "id": "book_7",
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Science Fiction",
        "year": 1965,
        "rating": 4.3,
        "pages": 688,
        "description": "A complex tale of politics, religion, and ecology on a desert planet",
        "themes": "power, ecology, religion, politics",
        "setting": "Arrakis, distant future"
    },
    {
        "id": "book_8",
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "genre": "Dystopian",
        "year": 2008,
        "rating": 4.2,
        "pages": 374,
        "description": "A teenage girl fights for survival in a brutal televised competition",
        "themes": "survival, oppression, sacrifice, rebellion",
        "setting": "Panem, dystopian future"
    },
]

def main():
    try:
        collection = create_collection(
            name=collection_name,
            metadata={"description": "A collection for storing book data"}
        )
        print(f"Collection created: {collection.name}")
        
        documents = []
        for book in books:
            document = f"""
                {book['title']} is a book written by {book['author']} about {book['genre']}. "
                It was published in {book['year']} and has {book['pages']} pages. "
                It is rated {book['rating']} by users. "
                The book is about {book['description']} and has themes of {book['themes']}. "
                The book is set in {book['setting']}.
            """
            documents.append(document)
            

        collection.add(
            documents=documents,
            ids=[book['id'] for book in books],
            metadatas=[{
                "title": book['title'],
                "author": book['author'],
                "genre": book['genre'],
                "year": book['year'],
                "rating": book['rating'],
                "pages": book['pages'],
            } for _ in books]
        )
        all_items = collection.get()
        print("Collection contents:")
        print(f"Number of documents: {len(all_items['documents'])}")
        
        def perform_similarity_search():
            try:
                # Similarity search for "magical fantasy adventure"
                # Filter books by genre (Fantasy or Science Fiction)
                # Filter books by rating (4.0 or higher)
                # Combined search: Find highly-rated dystopian books with similarity search
                
                print("======= Similarity Search ======")
                query_text = "magical fantasy adventure"
                results = collection.query(
                    query_texts=[query_text],
                    n_results=3,
                )

                for i, (id, score) in enumerate(zip(results['ids'][0],  results['distances'][0])):
                    metadata = results['metadatas'][0][i]
                    print(f"  {i+1}. {metadata['title']} ({id}) - Distance: {score:.4f}")
                    print(f"     Author: {metadata['author']}, Genre: {metadata['genre']}, Year: {metadata['year']}")
                    print(f"     Rating: {metadata['rating']}")

                # Filter books by genre (Fantasy or Science Fiction)
                print("\n======= Filter by Genre (Fantasy or Science Fiction) =======")
                results = collection.get(
                    where={
                        "genre": {"$in": ["Fantasy", "Science Fiction"]}
                    }
                )

                for i, doc_id in enumerate(results['ids']):
                    metadata = results['metadatas'][i]
                    print(f"  {i+1}. {metadata['title']} ({doc_id})")
                    print(f"     Author: {metadata['author']}, Genre: {metadata['genre']}, Year: {metadata['year']}")
                    print(f"     Rating: {metadata['rating']}")

                # Filter books by rating (4.0 or higher)
                print("\n======= Filter by Rating (4.0 or higher) =======")
                results = collection.get(
                    where={
                        "rating": {"$gte": 4.0}
                    }
                )

                for i, doc_id in enumerate(results['ids']):
                    metadata = results['metadatas'][i]
                    print(f"  {i+1}. {metadata['title']} ({doc_id})")
                    print(f"     Author: {metadata['author']}, Genre: {metadata['genre']}, Year: {metadata['year']}")
                    print(f"     Rating: {metadata['rating']}")

                # Combined search: Find highly-rated dystopian books with similarity search
                print("\n======= Combined Search: Highly-rated Dystopian Books =======")
                results = collection.query(
                    query_texts=[query_text],
                    n_results=3,
                    where={
                        "$and": [
                            {"genre": "Dystopian"},
                            {"rating": {"$gte": 4.0}}
                        ]
                    }
                )

                for i, (id, score) in enumerate(zip(results['ids'][0],  results['distances'][0])):
                    metadata = results['metadatas'][0][i]
                    print(f"  {i+1}. {metadata['title']} ({id}) - Distance: {score:.4f}")
                    print(f"     Author: {metadata['author']}, Genre: {metadata['genre']}, Year: {metadata['year']}")
                    print(f"     Rating: {metadata['rating']}")

                # Check if the results are empty or undefined
                if not results or not results['ids'] or len(results['ids'][0]) == 0:
                    # Log a message if no similar documents are found for the query term
                    print(f'No documents found similar to "{query_text}"')
                    return
                # Log the header for the top 3 similar documents based on the query term
                print(f'Top 3 similar documents to "{query_text}":')
                # Loop through the top 3 results and log the document details
                for i in range(min(3, len(results['ids'][0]))):
                    # Extract the document ID and similarity score from the results
                    doc_id = results['ids'][0][i]
                    score = results['distances'][0][i]
                    # Retrieve the document text corresponding to the current ID from the results
                    text = results['documents'][0][i]
                    # Check if the text is available; if not, log 'Text not available'
                    if not text:
                        print(f' - ID: {doc_id}, Text: "Text not available", Score: {score:.4f}')
                    else:
                        print(f' - ID: {doc_id}, Text: "{text}", Score: {score:.4f}')


            except Exception as e:
                print(f"Error in perform_similarity_search: {e}")
            
        perform_similarity_search()
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()