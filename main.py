from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware


from db import init_db
from data_ingest import save_dataset, load_dataframe
from llm_chain import answer_question
from pathlib import Path

app = FastAPI()
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload(file: UploadFile):
    path = save_dataset(file)
    return {"message": f"Uploaded {file.filename}", "path": path}

@app.post("/ask")
async def ask(file_path: str, question: str):
    df = load_dataframe(file_path)
    answer = answer_question(df, question)
    return {"answer": answer}
