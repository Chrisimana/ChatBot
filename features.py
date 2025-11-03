import random
import re
from datetime import datetime
import math

class FeatureManager:
    def __init__(self):
        self.jokes = [
            "Mengapa programmer tidak bisa tidur? Karena mereka selalu debugging mimpi mereka! 😴",
            "Apa bahasa pemrograman favorit hantu? Boo-lang! 👻",
            "Kenapa komputer tidak dingin? Karena Windows selalu terbuka! ❄️",
            "Apa yang dikatakan Python kepada programmer? 'You complete me!' 💕",
            "Mengapa developer tidak suka alam? Terlalu banyak bug! 🐛"
        ]
        
        self.quotes = [
            "Code is like humor. When you have to explain it, it's bad. - Cory House 💻",
            "First, solve the problem. Then, write the code. - John Johnson 🎯",
            "Experience is the name everyone gives to their mistakes. - Oscar Wilde 🌟",
            "The only way to learn a new programming language is by writing programs in it. - Dennis Ritchie 📚",
            "Don't comment bad code - rewrite it. - Brian Kernighan ✨"
        ]
    
    def check_special_commands(self, message):
        """Cek perintah khusus"""
        if message == '/clear':
            return "CLEAR_CHAT"
        elif message == '/help':
            return self.show_help()
        elif message == '/time':
            return self.get_current_time()
        elif message == '/joke':
            return self.tell_joke()
        elif message == '/quote':
            return self.get_motivational_quote()
        return None
    
    def show_help(self):
        """Menampilkan bantuan"""
        help_text = """
🤖 **CHATBOT HELP** 🤖

**Fitur Utama:**
• 💬 Percakapan sehari-hari
• 🧮 Kalkulator (contoh: 'hitung 2+2')
• ⏰ Waktu dan tanggal
• 😄 Cerita lucu
• 💪 Motivasi dan quotes
• 🌤️ Info cuaca (simulasi)

**Perintah Khusus:**
• /help - Tampilkan bantuan ini
• /clear - Bersihkan chat
• /time - Tampilkan waktu
• /joke - Cerita lucu
• /quote - Motivasi

**Cara penggunaan:**
Tulis pesan biasa atau gunakan perintah di atas!
        """
        return help_text
    
    def calculate_expression(self, message):
        """Kalkulator sederhana"""
        try:
            # Ekstrak ekspresi matematika
            numbers = re.findall(r'\d+\.?\d*', message)
            if '+' in message:
                result = sum(float(n) for n in numbers)
                return f"Hasil penjumlahan: {result} 🧮"
            elif '-' in message:
                if len(numbers) >= 2:
                    result = float(numbers[0]) - float(numbers[1])
                    return f"Hasil pengurangan: {result} 🧮"
            elif '*' in message or 'x' in message:
                result = 1
                for n in numbers:
                    result *= float(n)
                return f"Hasil perkalian: {result} 🧮"
            elif '/' in message:
                if len(numbers) >= 2:
                    result = float(numbers[0]) / float(numbers[1])
                    return f"Hasil pembagian: {result} 🧮"
            
            # Jika tidak ada operator jelas, coba evaluasi
            math_expr = re.findall(r'[\d\+\-\*\/\(\)\.]+', message)
            if math_expr:
                result = eval(math_expr[0])
                return f"Hasil perhitungan: {result} 🧮"
                
        except Exception as e:
            return "Maaf, saya tidak bisa menghitung itu. Pastikan ekspresi matematikanya benar! ❌"
        
        return "Saya bisa membantu menghitung! Coba: 'hitung 15 + 27' atau 'berapa 100 / 4' 🧮"
    
    def get_current_time(self):
        """Mendapatkan waktu saat ini"""
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        date_str = now.strftime("%A, %d %B %Y")
        return f"🕐 Sekarang jam **{time_str}**\n📅 Tanggal **{date_str}**"
    
    def get_weather_info(self):
        """Info cuaca (simulasi)"""
        weather_conditions = ["cerah", "mendung", "hujan ringan", "hujan lebat", "berawan"]
        temperatures = random.randint(22, 35)
        condition = random.choice(weather_conditions)
        
        emoji = "☀️" if condition == "cerah" else "🌧️" if "hujan" in condition else "⛅"
        
        return f"{emoji} **Info Cuaca Hari Ini:**\n• Kondisi: {condition}\n• Suhu: {temperatures}°C\n• Tips: {'Gunakan sunscreen!' if condition == 'cerah' else 'Bawa payung!' if 'hujan' in condition else 'Hari yang nyaman!'} {emoji}"
    
    def tell_joke(self):
        """Menceritakan joke"""
        return random.choice(self.jokes)
    
    def get_motivational_quote(self):
        """Mendapatkan quote motivasi"""
        return f"💫 **Motivasi Hari Ini:**\n{random.choice(self.quotes)}"