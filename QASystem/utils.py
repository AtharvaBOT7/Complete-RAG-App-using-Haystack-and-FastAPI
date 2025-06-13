from haystack_integrations.document_stores.pinecone import PienconeDocumentStore
import os
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

HF_TOKEN = os.getenv("HF_TOKEN")
os.environ['HF_API_TOKEN'] = HF_TOKEN

print("Key imported successfully")

from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key = PINECONE_API_KEY)

print("Available indexes:", pc.list_indexes())

def pinecone_config():
    document_store = PienconeDocumentStore(
        environment="gcp-starter",
        index="haystackfastapi",
        namespace="default",
        dimension=768
    )
    return document_store