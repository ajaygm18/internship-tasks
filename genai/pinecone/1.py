# Import the Pinecone library
from pinecone import Pinecone

# Initialize the Pinecone client
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")



# Import ServerlessSpec
from pinecone import ServerlessSpec

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

# Create your Pinecone index
pc.create_index(
    name="my-first-index",
    dimension=256,
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)


# Set up the client with your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

# Connect to your index
index = pc.Index("my-first-index")

# Print the index statistics
print(index.describe_index_stats())

# Set up the client with your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

# Delete your Pinecone index
pc.delete_index('my-first-index')

# List your indexes
print(pc.list_indexes())


# Initialize the Pinecone client using your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

# Create your Pinecone index
pc.create_index(
    name="datacamp-index", 
    dimension=1536, 
    spec=ServerlessSpec(
        cloud='aws', 
        region='us-east-1'
    )
)

# Check that each vector has a dimensionality of 1536
vector_dims = [len(vector['values']) == 1536 for vector in vectors]
print(all(vector_dims))

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

# Connect to your index
index = pc.Index("datacamp-index")

# Ingest the vectors and metadata
index.upsert(vectors)

# Print the index statistics
print(index.describe_index_stats())


# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

index = pc.Index('datacamp-index')
ids = ['2', '5', '8']

# Fetch the vectors from the connected Pinecone index
fetched_vectors = index.fetch(ids=ids)
# Extract the metadata from each result in fetched_vectors
metadatas = [fetched_vectors['vectors'][id]['metadata'] for id in ids]
print(metadatas)

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

index = pc.Index('datacamp-index')

# Retrieve the top three most similar records
query_result = index.query(
    vector=vector,
    top_k=3
)

print(query_result)

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

# Create an index that uses the dot product distance metric
pc.create_index(
    name="dotproduct-index",
    dimension=1536,
    metric='dotproduct',
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)

# Print a list of your indexes
print(pc.list_indexes())

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

index = pc.Index('datacamp-index')

# Retrieve the MOST similar vector with the year 2024
query_result = index.query(
    vector=vector,
    filter={
        'year': {
            '$eq': 2024
        }
    },
    show_metadata=True,
    top_k=1
)
print(query_result)


# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

index = pc.Index('datacamp-index')

# Update the values of vector ID 7
index.update(
    id='7',
    values=vector
)

# Fetch vector ID 7
fetched_vector = index.fetch(ids=['7'])
print(fetched_vector)


# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

index = pc.Index('datacamp-index')

# Update the metadata of vector ID 7
index.update(
    id='7',
    set_metadata={
        'genre': 'thriller',
        'year': 2024
    }
)

# Fetch vector ID 7
fetched_vector = index.fetch(ids=['7'])
print(fetched_vector)

# Initialize the Pinecone client using your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

index = pc.Index('datacamp-index')

# Delete vectors
index.delete(ids=['3', '4'])

# Retrieve metrics of the connected Pinecone index
print(index.describe_index_stats())


def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    # Convert the iterable into an iterator
    it = iter(iterable)
    # Slice the iterator into chunks of size batch_size
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        # Yield the chunk
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))


# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

index = pc.Index('datacamp-index')

# Upsert vectors in batches of 100
for chunk in chunks(vectors):
    index.upsert(chunk) 

# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())


# Initialize the client
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc", pool_threads=20)

index = pc.Index('datacamp-index')

# Upsert vectors in batches of 200 vectors
with pc.Index('datacamp-index', pool_threads=20) as index:
    async_results = [index.upsert(vectors=chunk, async_req=True) for chunk in chunks(vectors, batch_size=200)]
    [async_result.get() for async_result in async_results]

# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())


# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")
index = pc.Index('datacamp-index')

# Upsert vector_set1 to namespace1
index.upsert(
  vectors=vector_set1,
  namespace='namespace1'
)

# Upsert vector_set2 to namespace2
index.upsert(
  vectors=vector_set2,
  namespace='namespace2'
)

# Print the index statistics
index.describe_index_stats()

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

index = pc.Index('datacamp-index')

# Query namespace1 with the vector provided
query_result = index.query(vector=vector, namespace='namespace1', top_k=3)
print(query_result)


# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")

# Create Pinecone index
pc.create_index(
    name='pinecone-datacamp', 
    dimension=1536,
    spec=ServerlessSpec(cloud='aws', region='us-east-1')
)

# Connect to index and print the index statistics
index = pc.Index(name='pinecone-datacamp')
print(index.describe_index_stats())


# Initialize the Pinecone client
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")
index = pc.Index('pinecone-datacamp')

batch_limit = 100

for batch in np.array_split(df, len(df) / batch_limit):
    # Extract the metadata from each row
    metadatas = [{
      "text_id": row['id'],
      "text": row['text'],
      "title": row['title']} for _, row in batch.iterrows()]
    texts = batch['text'].tolist()
    
    ids = [str(uuid4()) for _ in range(len(texts))]
    
    # Encode texts using OpenAI
    response = client.embeddings.create(input=texts, model="text-embedding-3-small")
    embeds = [np.array(x.embedding) for x in response.data]
    
    # Upsert vectors to the correct namespace
    index.upsert(vectors=zip(ids, embeds, metadatas), namespace='squad_dataset')

# Initialize the Pinecone client
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")
index = pc.Index('pinecone-datacamp')

query = "What is in front of the Notre Dame Main Building?"

# Create the query vector
query_response = client.embeddings.create(
    input=query,
    model="text-embedding-3-small"
)
query_emb = query_response.data[0].embedding

# Query the index and retrieve the top five most similar vectors
retrieved_docs = index.query(
    vector=query_emb,
    top_k=5,
    namespace='squad_dataset'
)

for result in retrieved_docs['matches']:
    print(f"{result['id']}: {round(result['score'], 2)}")
    print('\n')


# Initialize the Pinecone client
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")
index = pc.Index('pinecone-datacamp')

batch_limit = 100

for batch in np.array_split(youtube_df, len(youtube_df) / batch_limit):
    # Extract the metadata from each row
    metadatas = [{
      "text_id": row['id'],
      "text": row['text'],
      "title": row['title'],
      "url": row['url'],
      "published": row['published']} for _, row in batch.iterrows()]
    texts = batch['text'].tolist()
    
    ids = [str(uuid4()) for _ in range(len(texts))]
    
    # Encode texts using OpenAI
    response = client.embeddings.create(input=texts, model="text-embedding-3-small")
    embeds = [np.array(x.embedding) for x in response.data]
    
    # Upsert vectors to the correct namespace
    index.upsert(vectors=zip(ids, embeds, metadatas), namespace='youtube_rag_dataset')
    
print(index.describe_index_stats())



# Initialize the Pinecone client
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")
index = pc.Index('pinecone-datacamp')

# Define a retrieve function that takes four arguments: query, top_k, namespace, and emb_model
def retrieve(query, top_k, namespace, emb_model):
    # Encode the input query using OpenAI
    query_response = client.embeddings.create(
        input=query,
        model=emb_model
    )
    
    query_emb = query_response.data[0].embedding
    
    # Query the index using the query_emb
    docs = index.query(vector=query_emb, top_k=top_k, namespace=namespace, include_metadata=True)
    
    retrieved_docs = []
    sources = []
    for doc in docs['matches']:
        retrieved_docs.append(doc['metadata']['text'])
        sources.append((doc['metadata']['title'], doc['metadata']['url']))
    
    return retrieved_docs, sources

documents, sources = retrieve(
  query="How to build next-level Q&A with OpenAI",
  top_k=3,
  namespace='youtube_rag_dataset',
  emb_model="text-embedding-3-small"
)
print(documents)
print(sources)

# Initialize the Pinecone client
pc = Pinecone(api_key="pcsk_fxNcF<OPENAI_TOKEN>rXJvJcc")
index = pc.Index('pinecone-datacamp')

query = "How to build next-level Q&A with OpenAI"

# Retrieve the top three most similar documents and their sources
documents, sources = retrieve(query, top_k=3, namespace='youtube_rag_dataset', emb_model="text-embedding-3-small")

prompt_with_context = prompt_with_context_builder(query, documents)
print(prompt_with_context)

def question_answering(prompt, sources, chat_model):
    sys_prompt = "You are a helpful assistant that always answers questions."
    
    # Use OpenAI chat completions to generate a response
    res = client.chat.completions.create(
        model=chat_model,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    answer = res.choices[0].message.content.strip()
    answer += "\n\nSources:"
    for source in sources:
        answer += "\n" + source[0] + ": " + source[1]
    
    return answer

answer = question_answering(
  prompt=prompt_with_context,
  sources=sources,
  chat_model='gpt-4o-mini')
print(answer)


