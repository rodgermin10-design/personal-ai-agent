from agent import AIAgent

class Chatbot:
    def __init__(self):
        self.agent = AIAgent()
        self.is_running = False
    
    def start(self):
        """Запустить чат-бот"""
        self.is_running = True
        self.agent.start_session()
        
        print("\n💬 Введи сообщение (или 'выход' для завершения):\n")
        
        while self.is_running:
            try:
                user_input = input("Ты: ").strip()
                
                if user_input.lower() in ['выход', 'exit', 'quit']:
                    self.stop()
                    break
                
                if not user_input:
                    continue
                
                # Специальные команды
                if user_input.lower().startswith('/info'):
                    info = self.agent.get_session_info()
                    self._print_session_info(info)
                    continue
                
                # Обработать сообщение
                result = self.agent.process_user_input(user_input)
                
                print(f"\n🤖 {self.agent.name}: {result['response']}\n")
                print(f"📊 Тональность: {result['sentiment']}")
                print(f"🔑 Ключевые слова: {', '.join(result['keywords'][:5])}\n")
            
            except KeyboardInterrupt:
                print("\n\n⚠️ Прервано пользователем")
                self.stop()
                break
            except Exception as e:
                print(f"❌ Ошибка: {e}\n")
    
    def stop(self):
        """Остановить чат-бот"""
        self.is_running = False
        self.agent.end_session()
    
    def _print_session_info(self, info):
        """Вывести информацию о сессии"""
        print("\n" + "="*50)
        print(f"📋 Информация о сессии:")
        print(f"ID сессии: {info['session_id'][:16]}...")
        print(f"��гент: {info['agent_name']}")
        print(f"Всего сообщений: {info['messages_count']}")
        print("="*50 + "\n")
