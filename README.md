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
Installation & Setup

bash
1. Clone the Repository

git clone https://github.com/sarahdelma/AI-Chatbot.git
cd AI-Chatbot


2. Create & Activate a Virtual Environment

python -m venv venv
source venv/bin/activate   # Linux/macOS
# For Windows:
# venv\Scripts\activate

3. Install Dependencies
   
pip install -r requirements.txt

4. Configuration

Create a .env file with your credentials:

OPENAI_API_KEY=your_api_key_here
DB_URL=your_database_url


Security tip: Never commit your .env file to Git. Add it to .gitignore.

5. Running the Chatbot
Option A: Run Locally

python main.py

Option B: Using Docker (Optional)

docker build -t ai-chatbot .
docker run -p 5000:5000 ai-chatbot

Option C: Using Docker Compose

docker-compose up

6. Example Usage

python main.py
