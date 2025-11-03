import json
import os
from datetime import datetime
from src.config import Config

class ChatManager:

    def __init__(self):
        Config.ensure_directory()
        self.current_chat_file = None
    
    def start_new_chat(self):
        """Memulai chat baru"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.current_chat_file = os.path.join(
            Config.CHAT_HISTORY_DIR, 
            f"chat_{timestamp}.json"
        )
        
        chat_data = {
            'start_time': Config.get_timestamp(),
            'messages': []
        }
        
        self._save_chat(chat_data)
        return self.current_chat_file
    
    # Menyimpan pesan ke history
    def save_message(self, user_message, bot_response, user_name="Pengguna"):
        """Menyimpan pesan ke history"""
        if not self.current_chat_file:
            self.start_new_chat()
            
        chat_data = self._load_chat()
        
        message_entry = {
            'timestamp': Config.get_timestamp(),
            'user': user_name,
            'user_message': user_message,
            'bot_response': bot_response
        }
        
        chat_data['messages'].append(message_entry)
        self._save_chat(chat_data)
    
    # Memuat data chat dari file
    def _load_chat(self):
        """Memuat data chat"""
        try:
            with open(self.current_chat_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {'messages': []}
    
    # Menyimpan data chat ke file
    def _save_chat(self, chat_data):
        """Menyimpan data chat"""
        with open(self.current_chat_file, 'w', encoding='utf-8') as f:
            json.dump(chat_data, f, indent=2, ensure_ascii=False)
    
    def get_chat_history(self):
        """Mendapatkan history chat saat ini"""
        if not self.current_chat_file:
            return []
        return self._load_chat().get('messages', [])
    
    def export_chat(self, format_type='txt'):
        """Export chat ke file"""
        if not self.current_chat_file:
            return None
            
        chat_data = self._load_chat()
        export_filename = self.current_chat_file.replace('.json', f'.{format_type}')
        
        if format_type == 'txt':
            with open(export_filename, 'w', encoding='utf-8') as f:
                f.write(f"Chat History - {chat_data['start_time']}\n")
                f.write("=" * 50 + "\n\n")
                
                for msg in chat_data['messages']:
                    f.write(f"[{msg['timestamp']}]\n")
                    f.write(f"{msg['user']}: {msg['user_message']}\n")
                    f.write(f"Chatbot: {msg['bot_response']}\n\n")
        
        return export_filename
    
    def list_all_chats(self):
        """Mendapatkan daftar semua chat yang tersimpan"""
        chat_files = []
        for file in os.listdir(Config.CHAT_HISTORY_DIR):
            if file.endswith('.json'):
                chat_files.append(os.path.join(Config.CHAT_HISTORY_DIR, file))
        
        return sorted(chat_files, reverse=True)