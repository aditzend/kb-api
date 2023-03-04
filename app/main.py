from fastapi import FastAPI
from pydantic import BaseModel
import json
import re
import openai
import os
from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator

load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")


def kb_qa(query):
    print(f"QUESTION: {query} | Querying knowledge base...")
    loader = DirectoryLoader("./kb")
    index = VectorstoreIndexCreator().from_loaders([loader])
    result = index.query_with_sources(query)
    print(result)
    return result


app = FastAPI()


class Question(BaseModel):
    text: str


@app.post("/boti/qa")
async def parse_text(request: Question):

    kb_qa_response = kb_qa(query=request.text)
    # if kb_qa_response:
    #     p = json.loads(kb_qa_response)
    # entities = []
    # response = {
    #     "text": request.text,
    #     "answer": p["answer"],
    #     "source": p["source"],
    # }
    return kb_qa_response
