from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
import pandas as pd

def answer_question(df: pd.DataFrame, question: str):
    # Summarize the table for the model
    sample = df.head(10).to_csv(index=False)
    context = f"Here is a sample of the data:\n{sample}\n\n"
    prompt = f"{context}Answer this question using only this data: {question}"
    llm = Ollama(model="gemma3:1b")
    return llm.invoke(prompt)
