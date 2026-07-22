# 🤖 Личный AI Ассистент

Полнофункциональный AI агент на Python с поддержкой чата, обработки текста, интеграцией с OpenAI API и БД.

## 📋 Возможности

- ✅ **Интерактивный чат-бот** - общение в реальном времени
- ✅ **Интеграция с OpenAI API** - использование GPT-3.5-turbo
- ✅ **База данных SQLite** - сохранение диалогов и данных
- ✅ **Обработка текста** - анализ тональности, извлечение ключевых слов
- ✅ **REST API** - веб-интерфейс для чата
- ✅ **Управление сессиями** - отслеживание разговоров
- ✅ **Логирование** - запись всех API запросов

## 🚀 Быстрый старт

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Настройка окружения

Создай файл `.env`:

```
OPENAI_API_KEY=your-api-key-here
```

### 3. Запуск чат-бота

```bash
python main.py
```

### 4. Запуск API сервера

```bash
python main.py --api
```

Сервер будет доступен на `http://127.0.0.1:5000`

## 📡 API Endpoints

### Отправить сообщение

```bash
POST /api/chat
Content-Type: application/json

{
  "message": "Привет! Как дела?"
}
```

### Получить информацию о сессии

```bash
GET /api/session
```

### Сбросить сессию

```bash
POST /api/reset
```

### Health Check

```bash
GET /health
```

## 📁 Структура проекта

```
ai-agent/
├── config.py           # Конфигурация
├── main.py            # Точка входа
├── agent.py           # Основной класс агента
├── database.py        # Работа с БД
├── api_handler.py     # OpenAI API интеграция
├── text_processor.py  # Обработка текста
├── chatbot.py         # Интерфейс чат-бота
├── requirements.txt   # Зависимости
└── README.md          # Этот файл
```

## 🔧 Команды в чат-боте

- `/info` - показать информацию о текущей сессии
- `выход` или `exit` - завершить сессию

## 📊 Пример использования

```python
from agent import AIAgent

agent = AIAgent()
agent.start_session()

result = agent.process_user_input("Что такое машинное обучение?")
print(result['response'])
```

## 🔐 Переменные окружения

- `OPENAI_API_KEY` - API ключ OpenAI (обязательно)

## 📝 Логирование

Все API запросы и диалоги сохраняются в SQLite БД:
- Таблица `conversations` - диалоги
- Таблица `api_logs` - логи API запросов
- Таблица `user_data` - данные пользователя

## 🤝 Расширение функциональности

Легко добавлять новые возможности:

1. Новые обработчики текста в `text_processor.py`
2. Новые API интеграции в `api_handler.py`
3. Новые endpoints в `main.py`

## 📄 Лицензия

MIT
