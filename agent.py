import uuid
from datetime import datetime
from database import Database
from api_handler import APIHandler
from text_processor import TextProcessor
from config import AGENT_NAME, AGENT_DESCRIPTION, MAX_HISTORY

class AIAgent:
    def __init__(self):
        self.name = AGENT_NAME
        self.description = AGENT_DESCRIPTION
        self.db = Database()
        self.api = APIHandler()
        self.text_processor = TextProcessor()
        self.session_id = str(uuid.uuid4())
        self.conversation_history = []
    
    def start_session(self):
        """Начать новую сессию"""
        self.session_id = str(uuid.uuid4())
        self.conversation_history = []
        print(f"🤖 {self.name}: Привет! Сессия начата. ID: {self.session_id[:8]}...")
    
    def process_user_input(self, user_message):
        """Обработать входное сообщение пользователя"""
        # Анализ тональности
        sentiment = self.text_processor.analyze_sentiment(user_message)
        
        # Извлечение ключевых слов
        keywords = self.text_processor.extract_keywords(user_message)
        
        # Добавить сообщение в историю
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Получить ответ от AI
        ai_response = self._get_ai_response()
        
        # Сохранить в БД
        self.db.save_conversation(user_message, ai_response, self.session_id)
        
        # Добавить ответ в историю
        self.conversation_history.append({
            "role": "assistant",
            "content": ai_response
        })
        
        # Ограничить размер истории
        if len(self.conversation_history) > MAX_HISTORY:
            self.conversation_history = self.conversation_history[-MAX_HISTORY:]
        
        return {
            "response": ai_response,
            "sentiment": sentiment,
            "keywords": keywords
        }
    
    def _get_ai_response(self):
        """Получить ответ от OpenAI"""
        system_message = {
            "role": "system",
            "content": f"Ты {self.name} - {self.description}. Ты помогаешь пользователю ответами на вопросы и выполнением задач. Отвечай дружелюбно и кратко."
        }
        
        messages = [system_message] + self.conversation_history
        response = self.api.call_openai(messages)
        return response
    
    def get_session_info(self):
        """Получить информацию о текущей сессии"""
        history = self.db.get_conversation_history(self.session_id, limit=10)
        return {
            "session_id": self.session_id,
            "agent_name": self.name,
            "agent_description": self.description,
            "messages_count": len(self.conversation_history),
            "recent_history": history
        }
    
    def end_session(self):
        """Завершить сессию"""
        print(f"🤖 {self.name}: Спасибо за разговор! До свидания!")
        self.conversation_history.clear()
