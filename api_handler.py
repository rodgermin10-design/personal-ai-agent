import requests
import json
from config import OPENAI_API_KEY, OPENAI_MODEL
from database import Database

class APIHandler:
    def __init__(self):
        self.api_key = OPENAI_API_KEY
        self.model = OPENAI_MODEL
        self.base_url = "https://api.openai.com/v1"
        self.db = Database()
    
    def call_openai(self, messages, temperature=0.7, max_tokens=500):
        """Запрос к OpenAI API"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            
            # Логирование
            self.db.log_api_call("/chat/completions", "POST", response.status_code)
            
            if response.status_code == 200:
                data = response.json()
                return data['choices'][0]['message']['content']
            else:
                return f"Ошибка API: {response.status_code}"
        
        except requests.exceptions.Timeout:
            return "Ошибка: Истекло время ожидания ответа от API"
        except Exception as e:
            return f"Ошибка при обращении к API: {str(e)}"
    
    def get_external_api(self, url, params=None):
        """Запрос к внешнему API"""
        try:
            response = requests.get(url, params=params, timeout=10)
            self.db.log_api_call(url, "GET", response.status_code)
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Status code: {response.status_code}"}
        
        except Exception as e:
            return {"error": str(e)}
