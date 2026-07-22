import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")
OPENAI_MODEL = "gpt-3.5-turbo"

# Database Configuration
DB_PATH = "agent_database.db"

# Agent Configuration
AGENT_NAME = "PersonalAI"
AGENT_DESCRIPTION = "Мой личный AI ассистент"
MAX_HISTORY = 50  # Максимум сообщений в памяти

# Server Configuration
FLASK_HOST = "127.0.0.1"
FLASK_PORT = 5000
