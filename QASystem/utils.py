# from haystack_integrations.components.retrievers.pinecone import PineconeEmbeddingRetriever
# from haystack.components.embedders import SentenceTransformersTextEmbedder
# from haystack.utils import Secret
# import os
# from dotenv import load_dotenv

# load_dotenv()

# PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
# os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

# HF_TOKEN = os.getenv("HF_TOKEN")
# os.environ['HF_API_TOKEN'] = HF_TOKEN

# print("Key imported successfully")

# from pinecone import Pinecone, ServerlessSpec

# pc = Pinecone(api_key = PINECONE_API_KEY)

# print("Available indexes:", pc.list_indexes())
# index = pc.Index("haystackfastapi")

# def pinecone_config():
#     load_dotenv()
    
#     embedder = SentenceTransformersTextEmbedder(model="sentence-transformers/all-MiniLM-L6-v2")
    
#     retriever = PineconeEmbeddingRetriever(
#         namespace="default",
#         api_key=Secret.from_token(os.getenv("PINECONE_API_KEY"))
#     )
    
#     return retriever

# # def pinecone_config():
# #     embedder = SentenceTransformersTextEmbedder(model="sentence-transformers/all-MiniLM-L6-v2")

# #     retriever = PineconeEmbeddingRetriever(
# #         environment="us-east-1-aws", 
# #         index="haystackfastapi",
# #         namespace="default",
# #         embedder=embedder
# #     )
    
# #     return retriever







from dotenv import load_dotenv
import os
from pinecone import Pinecone, ServerlessSpec

load_dotenv()

# Load and set environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

HF_TOKEN = os.getenv("HF_TOKEN")
os.environ['HF_API_TOKEN'] = HF_TOKEN

print("Key imported successfully")

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Ensure index exists
index_name = "haystackfastapi"
if index_name not in [idx["name"] for idx in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=384,  # for all-MiniLM-L6-v2
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

print("Available indexes:", pc.list_indexes())


# ✅ Export the index name for use in ingestion
def pinecone_config():
    return index_name
