import pandas as pd
from pathlib import Path
from db import insert_dataset

UPLOAD_DIR = Path("data/uploaded_files")

def save_dataset(file):
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    insert_dataset(file.filename, str(file_path))
    return str(file_path)

def load_dataframe(path):
    if path.endswith(".csv"):
        return pd.read_csv(path)
    elif path.endswith(".json"):
        return pd.read_json(path)
    else:
        raise ValueError("Unsupported file format")
