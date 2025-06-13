from haystack_integrations.document_stores.pinecone import PienconeDocumentStore
import os
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

print("Key imported successfully")

from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key = PINECONE_API_KEY)

print("Available indexes:", pc.list_indexes())

