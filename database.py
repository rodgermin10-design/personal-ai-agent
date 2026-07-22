import sqlite3
from datetime import datetime
from config import DB_PATH

class Database:
    def __init__(self):
        self.db_path = DB_PATH
        self.init_db()
    
    def init_db(self):
        """Инициализация базы данных"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Таблица для сохранения диалогов
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_message TEXT NOT NULL,
                ai_response TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                session_id TEXT NOT NULL
            )
        ''')
        
        # Таблица для сохранения пользовательских данных
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE NOT NULL,
                value TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Таблица для логирования запросов к API
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS api_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                endpoint TEXT NOT NULL,
                method TEXT NOT NULL,
                status_code INTEGER,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def save_conversation(self, user_message, ai_response, session_id):
        """Сохранить диалог"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO conversations (user_message, ai_response, session_id)
            VALUES (?, ?, ?)
        ''', (user_message, ai_response, session_id))
        conn.commit()
        conn.close()
    
    def get_conversation_history(self, session_id, limit=50):
        """Получить историю диалогов"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT user_message, ai_response, timestamp FROM conversations
            WHERE session_id = ?
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (session_id, limit))
        result = cursor.fetchall()
        conn.close()
        return result
    
    def save_user_data(self, key, value):
        """Сохранить данные пользователя"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT OR REPLACE INTO user_data (key, value)
                VALUES (?, ?)
            ''', (key, value))
            conn.commit()
        except Exception as e:
            print(f"Ошибка при сохранении данных: {e}")
        finally:
            conn.close()
    
    def get_user_data(self, key):
        """Получить данные пользователя"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT value FROM user_data WHERE key = ?', (key,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    
    def log_api_call(self, endpoint, method, status_code):
        """Залогировать API запрос"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO api_logs (endpoint, method, status_code)
            VALUES (?, ?, ?)
        ''', (endpoint, method, status_code))
        conn.commit()
        conn.close()
