from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai.metadata_extraction import extract_metadata
from ai.note_taking import summarize_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Management System"}

@app.post("/extract-metadata/")
def extract_metadata_endpoint(file: bytes):
    metadata = extract_metadata(file)
    return {"metadata": metadata}

@app.post("/summarize/")
def summarize_endpoint(text: str):
    summary = summarize_text(text)
    return {"summary": summary}