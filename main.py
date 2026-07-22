from chatbot import Chatbot
from flask import Flask, request, jsonify
from agent import AIAgent
import threading

# Flask приложение для API
app = Flask(__name__)
agent = AIAgent()

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint для чата"""
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({"error": "Message is required"}), 400
    
    result = agent.process_user_input(user_message)
    return jsonify(result)

@app.route('/api/session', methods=['GET'])
def get_session():
    """API endpoint для информации о сессии"""
    return jsonify(agent.get_session_info())

@app.route('/api/reset', methods=['POST'])
def reset_session():
    """API endpoint для сброса сессии"""
    agent.start_session()
    return jsonify({"status": "Session reset"})

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok", "agent": agent.name})

def run_server():
    """Запустить Flask сервер"""
    print("🌐 API сервер запущен на http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=False)

def run_chatbot():
    """Запустить интерактивный чат-бот"""
    chatbot = Chatbot()
    chatbot.start()

if __name__ == "__main__":
    import sys
    
    print("""
    ╔═══════════════════════════════════════╗
    ║     🤖 Личный AI Ассистент 🤖        ║
    ╚═══════════════════════════════════════╝
    """)
    
    if len(sys.argv) > 1 and sys.argv[1] == '--api':
        # Запустить API сервер
        run_server()
    else:
        # Запустить интерактивный чат-бот (по умолчанию)
        run_chatbot()
