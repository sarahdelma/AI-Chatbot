# AI‑Chatbot

A Python‑based AI chatbot application that demonstrates conversational AI capabilities using large language models (LLMs) with backend logic and optional database integration. This repository provides the core application logic, data ingestion, and model integration needed to run a simple chatbot.

---

## 🧠 Features

- Conversational chatbot backend using Python
- Data ingestion and storage logic
- Modular LLM chain integration (`llm_chain.py`)
- Configurable via environment and Docker
- Easily extensible for new models or front‑ends

---

## 🚀 Installation

### Clone the repository
>> git clone https://github.com/sarahdelma/AI-Chatbot.git
>> cd AI-Chatbot


## Create & activate a virtual environment
>> python -m venv venv
>> source venv/bin/activate 

## Install dependencies
>> pip install -r requirements.txt


## Configuration

OPENAI_API_KEY=your_api_key_here
DB_URL=your_database_url
- Keep your keys secret and never commit .env to Git. Add it to .gitignore.

## Running the Chatbot
- Run locally
  >> python main.py
- Using Docker (optional)
  >> docker build -t ai‑chatbot
- Run with Docker Compose:
  >> docker‑compose up


  ### OUTPUT
  - Example Usage
    
  > python main.py
    Hello! Ask anything:
  > What’s the weather today?
    Bot: …


Customize prompting and logic by editing llm_chain.py
