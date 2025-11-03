import random
import re
from datetime import datetime
from src.features import FeatureManager

class ChatbotCore:

    def __init__(self):
        self.feature_manager = FeatureManager()
        self.user_name = "Pengguna"
        self.conversation_context = {}
        
    def process_message(self, message, user_name="Pengguna"):
        """Memproses pesan dan mengembalikan respons"""
        self.user_name = user_name
        message_lower = message.lower()
        
        # Cek fitur khusus terlebih dahulu
        special_response = self.feature_manager.check_special_commands(message_lower)
        if special_response:
            return special_response
        
        # Logika respons utama
        response = self._generate_response(message_lower)
        
        # Update konteks percakapan
        self._update_context(message_lower, response)
        
        return response
    
    def _generate_response(self, message):
        """Generate respons berdasarkan konten pesan"""
        
        # Greetings
        if any(word in message.lower() for word in [
            'halo', 'hai', 'hi', 'hello', 'hey', 'hola', 'hallo',
            'yo', 'oi', 'p', 'pagi', 'siang', 'sore', 'malam'
            ]):

            return random.choice([
                f"Halo {self.user_name}! Ada yang bisa saya bantu?",
                f"Hai {self.user_name}! Senang bertemu denganmu!",
                f"Hello {self.user_name}! Bagaimana harimu?",
                f"Apa kabar, {self.user_name}? Ada yang bisa saya carikan?",
                f"Selamat datang kembali, {self.user_name}! Bagaimana kabarmu hari ini?",
                f"Yo {self.user_name}! Siap beraksi.",
                f"Senang mendengarmu, {self.user_name}! Aku siap membantumu."
                ])
        
        # Perkenalan
        elif any(phrase in message.lower() for phrase in [
            'nama kamu', 'siapa kamu', 'kamu siapa', 
            'siapa namamu', 'nama kamu siapa', 'kamu ini siapa', 'kamu apa',
            'siapa nama anda', 'nama anda', 'apakah nama kamu', 'apakah nama anda',
            'boleh tahu nama', 'siapakah'
            ]):
            
            return random.choice([
            "Saya adalah Chatbot! Dibuat dengan Python. Senang berkenalan denganmu!",
            "Aku adalah asisten virtual kamu, Chatbot! Aku dibuat untuk menjawab pertanyaanmu.",
            "Bukan siapa-siapa, hanya sebuah program Python sederhana yang siap membantumu. Panggil saja aku Chatbot.",
            "Nama saya Chatbot, sebuah program yang dirancang untuk berinteraksi dengan Anda. Apa yang ingin Anda ketahui?",
            "Saya adalah program bernama Chatbot. Jadi, apa misi kita hari ini?"
            ])
        
        # Kabar
        elif any(phrase in message.lower() for phrase in [
            'apa kabar', 'how are you', 'kabar', 
            'gimana kabar', 'kabar kamu', 'gimana', 
            'gimana hari', 'apa kabar hari ini', 'sehat', 'sehatkah', 'kabar kalian'
            ]):

            return random.choice([
                "Saya selalu baik! Ready untuk membantu kamu!",
                "Luar biasa! Apalagi kalau bisa membantu kamu!",
                "Sangat baik! Terima kasih sudah bertanya!",
                "Aku baik-baik saja, terima kasih sudah bertanya! Semoga kamu juga baik ya.",
                "Sebagai program, aku tidak punya perasaan, tapi aku berfungsi dengan sangat optimal! Apa kabar kamu?",
                "Super lancar! Sama seperti hari-hari biasa, siap melayani. Gimana dengan kabarmu?",
                "Baik sekali, terutama sekarang kamu sudah menghubungiku. Ada yang mendesak?"
                ])
        
        # Terima kasih
        elif any(phrase in message.lower() for phrase in [
            'terima kasih', 'thanks', 'thank you', 'makasih', 
            'terima kasi', 'terimakasi', 'sukron', 'matur nuwun', 
            'mksh', 'tq', 'thx', 'cheers', 'appreciate it', 'many thanks', 'tengkyu', 
            'trimakasih'
            ]):

            return random.choice([
                "Sama-sama! Senang bisa membantu!",
                "Dengan senang hati!",
                "Terima kasih kembali! Kamu luar biasa!",
                "Tugas saya adalah melayani Anda! Ada lagi yang bisa saya lakukan?",
                "Tidak masalah! Senang bekerja sama denganmu.",
                "Kapan pun kamu butuh!",
                "Sip! Jangan sungkan untuk tanya lagi ya.",
                "Pleasure is all mine.",
                "Terima kasih kembali atas kepercayaannya! Sampai jumpa lagi!"
                ])
        
        # Perpisahan
        elif any(phrase in message.lower() for phrase in [
            'bye', 'selamat tinggal', 'sampai jumpa', 'dadah', 'goodbye',
            'sampai ketemu', 'sampai nanti', 'pamit', 'sudah dulu',
            'dada', 'duluan ya', 'cabut', 'wassalam',
            'cya', 'gotta go', 'later', 'adios'
        ]):

            return random.choice([
                f"Selamat tinggal {self.user_name}! Senang berbicara denganmu!",
                f"Sampai jumpa lagi! Jangan lupa kembali ya!",
                f"Dadah {self.user_name}! Terima kasih sudah mengobrol!",
                f"Sampai ketemu lagi, {self.user_name}! Saya tunggu pertanyaanmu berikutnya.",
                f"Aku akan standby di sini. Kapan pun butuh, panggil saja. Selamat tinggal!",
                f"Adios! Jika ada yang ingin kamu cari, aku siap 24/7.",
                f"Bye! Semoga harimu menyenangkan!",
                f"Jaga diri, {self.user_name}! Sampai nanti.",
                f"Senang sudah bisa bantu. Sampai jumpa!"
                ])
        
        # Bantuan
        elif any(phrase in message.lower() for phrase in [
            'bantuan', 'help', 'tolong', 'fitur', 
            'bantu aku', 'tolong saya', 'apa saja', 'panduan', 
            'cara pakai', 'bisa apa', 'apa yang', 'ada menu',
            'how to use', 'commands', 'guide', 'can you'
            ]):

            return self.feature_manager.show_help()
        
        # Matematika
        elif any(word in message for word in ['hitung', 'kalkulator', 'matematika', 'berapa']):
            return self.feature_manager.calculate_expression(message)
        
        # Waktu
        elif any(phrase in message for phrase in ['jam berapa', 'waktu', 'sekarang jam', 'tanggal']):
            return self.feature_manager.get_current_time()
        
        # Cuaca (simulasi)
        elif any(word in message for word in ['cuaca', 'weather', 'hujan', 'panas']):
            return self.feature_manager.get_weather_info()
        
        # Humor
        elif any(phrase in message for phrase in ['cerita lucu', 'joke', 'humor', 'lucu']):
            return self.feature_manager.tell_joke()
        
        # Python
        elif any(word in message for word in ['python', 'programming', 'kode', 'coding']):
            return random.choice([
                "Python adalah bahasa pemrograman yang amazing!",
                "Saya dibuat dengan Python! Bahasa yang powerful dan mudah dipahami!",
                "Python + Tkinter = GUI yang keren! Itu yang membuat saya bisa berdialog seperti ini!"
            ])
        
        # Motivasi
        elif any(word in message for word in ['motivasi', 'semangat', 'inspirasi', 'quote']):
            return self.feature_manager.get_motivational_quote()
        
        # Default response dengan AI sederhana
        else:
            return self._get_intelligent_response(message)
    
    def _get_intelligent_response(self, message):
        """Respons AI sederhana berdasarkan pola"""
        if '?' in message:
            return random.choice([
                "Pertanyaan yang menarik! Bisa kamu jelaskan lebih detail?",
                "Wah, saya perlu memikirkan itu... Ada hal lain yang ingin ditanyakan?",
                "Itu pertanyaan yang bagus! Tapi saya masih belajar untuk memahami pertanyaan kompleks."
            ])
        
        elif any(word in message for word in ['sedih', 'marah', 'kesal', 'frustasi']):
            return random.choice([
                "Wah, jangan sedih ya! Semua masalah pasti ada solusinya!",
                "Hey, everything will be okay! Kamu kuat!",
                "Aku di sini untuk mendengarmu. Ingin cerita lebih banyak?"
            ])
        
        elif any(word in message for word in ['senang', 'bahagia', 'gembira', 'happy']):
            return random.choice([
                "Wah, senang mendengarnya! 🎉 Terus pertahankan energi positifnya! ✨",
                "Keren! Kebahagiaanmu membuat hariku juga cerah! 🌞",
                "Yes! Spread the positive vibes! 🥳"
            ])
        
        else:
            return random.choice([
                "Menarik sekali! 😊 Bisa cerita lebih banyak?",
                "Wah, saya belajar sesuatu yang baru hari ini! 📚",
                "Terima kasih sudah berbagi! Ada hal lain yang ingin kamu bicarakan? 🌟",
                "Ooh, saya mengerti! Kamu ingin membahas tentang itu ya? 🤔",
                "Pembicaraan yang seru! Lanjutkan! 🚀"
            ])
    
    def _update_context(self, message, response):
        """Update konteks percakapan"""
        self.conversation_context['last_message'] = message
        self.conversation_context['last_response'] = response
        self.conversation_context['timestamp'] = datetime.now()
    
    def get_conversation_summary(self):
        """Mendapatkan ringkasan percakapan"""
        return self.conversation_context