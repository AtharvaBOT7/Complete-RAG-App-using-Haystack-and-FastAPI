# from haystack import Pipeline
# from haystack.components.writers import DocumentWriter
# from haystack.components.preprocessors import DocumentSplitter
# from haystack.components.embedders import SentenceTransformersDocumentEmbedder
# from haystack_integrations.components.retrievers.pinecone import PineconeEmbeddingRetriever
# from haystack.components.converters import PyPDFToDocument
# from pathlib import Path
# import os
# from dotenv import load_dotenv

# from QASystem.utils import pinecone_config

# def ingest(document_store):
#     indexing = Pipeline()

#     # Adding components to the Haystack Pipeline
#     indexing.add_component("converter", PyPDFToDocument())
#     indexing.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=2))
#     indexing.add_component("embedder", SentenceTransformersDocumentEmbedder)
#     indexing.add_component("writer", DocumentWriter(document_store))

#     indexing.connect("converter", "splitter")
#     indexing.connect("splitter", "embedder")
#     indexing.connect("embedder", "writer")

#     indexing.run({"converter": {"sources": [Path("Data/2312.00752v2.pdf")]}})

# if __name__=="__main__":
    
#     document_store = pinecone_config()
#     ingest()


from haystack import Pipeline
from haystack.components.converters import PyPDFToDocument
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.components.writers.pinecone import PineconeEmbeddingWriter
from pathlib import Path

from QASystem.utils import pinecone_config

def ingest(index_name):
    indexing = Pipeline()

    # Add components to the pipeline
    indexing.add_component("converter", PyPDFToDocument())
    indexing.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=2))
    indexing.add_component("embedder", SentenceTransformersDocumentEmbedder(model="sentence-transformers/all-MiniLM-L6-v2"))
    indexing.add_component("writer", PineconeEmbeddingWriter(
        index=index_name,
        namespace="default"
    ))

    indexing.connect("converter", "splitter")
    indexing.connect("splitter", "embedder")
    indexing.connect("embedder", "writer")

    indexing.run({"converter": {"sources": [Path("Data/2312.00752v2.pdf")]}})
    print("✅ Ingestion complete.")

if __name__ == "__main__":
    index_name = pinecone_config()
    ingest(index_name)
