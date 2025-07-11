from setuptools import find_packages, setup

setup(
    name="RAG QA System with Haystack, MistralAI, Pinecone and FastAPI",
    author="Atharva Chundurwar",
    author_email="atharvachundurwar841@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["pinecone-haystack", "haystack-ai", "fastapi", "uvicorn", "python-dotenv", "pathlib"]
)