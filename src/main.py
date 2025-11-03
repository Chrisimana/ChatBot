import tkinter as tk
from src.chatbot_core import ChatbotCore
from src.chat_manager import ChatManager
from src.gui_interface import ChatGUI
from src.config import Config

class SuperChatbotApp:
    def __init__(self):
        self.root = tk.Tk()
        self.chatbot = ChatbotCore()
        self.chat_manager = ChatManager()
        
        # Start new chat session
        self.chat_manager.start_new_chat()
        
        # Initialize GUI
        self.gui = ChatGUI(self.root, self.chatbot, self.chat_manager)
        
    def run(self):
        """Menjalankan aplikasi"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("\nChatbot dihentikan oleh pengguna")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("🚀 Memulai Chatbot...")
    print("📁 History chat disimpan di folder:", Config.CHAT_HISTORY_DIR)
    
    app = SuperChatbotApp()
    app.run()