# Konfigurasi aplikasi chatbot
import os
from datetime import datetime

class Config:
    # Pengaturan GUI
    GUI_TITLE = "Chatbot"
    GUI_WIDTH = 800
    GUI_HEIGHT = 700
    GUI_BG_COLOR = "#1e1e1e"
    GUI_FONT = ("Arial", 10)
    
    # Pengaturan warna tema dark
    COLORS = {
        'bg_dark': '#1e1e1e',
        'bg_light': '#2d2d2d',
        'accent': '#007acc',
        'user_msg': '#005a9e',
        'bot_msg': '#2d2d2d',
        'text_light': '#ffffff',
        'text_gray': '#cccccc'
    }
    
    # Pengaturan file
    CHAT_HISTORY_DIR = "chat_history"
    EMOJIS_ENABLED = True
    
    @staticmethod
    def get_timestamp():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def ensure_directory():
        if not os.path.exists(Config.CHAT_HISTORY_DIR):
            os.makedirs(Config.CHAT_HISTORY_DIR)