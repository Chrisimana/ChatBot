import tkinter as tk
from tkinter import scrolledtext, ttk, messagebox, filedialog
import tkinter.font as tkFont
from config import Config

class ChatGUI:
    def __init__(self, root, chat_core, chat_manager):
        self.root = root
        self.chat_core = chat_core
        self.chat_manager = chat_manager
        
        self.setup_gui()
        self.setup_bindings()
        
    def setup_gui(self):
        """Setup GUI components"""
        self.root.title(Config.GUI_TITLE)
        self.root.geometry(f"{Config.GUI_WIDTH}x{Config.GUI_HEIGHT}")
        self.root.configure(bg=Config.COLORS['bg_dark'])
        
        # Setup custom styles
        self.setup_styles()
        
        # Create main frames
        self.create_header()
        self.create_chat_area()
        self.create_input_area()
        self.create_sidebar()
        
    def setup_styles(self):
        """Setup custom styles untuk widgets"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure styles
        self.style.configure('TFrame', background=Config.COLORS['bg_dark'])
        self.style.configure('TButton', 
                           background=Config.COLORS['accent'],
                           foreground=Config.COLORS['text_light'],
                           font=Config.GUI_FONT)
        
    def create_header(self):
        """Membuat header"""
        header_frame = ttk.Frame(self.root, style='TFrame')
        header_frame.pack(fill='x', padx=10, pady=10)
        
        # Title
        title_label = tk.Label(header_frame, 
                              text=Config.GUI_TITLE,
                              font=("Arial", 20, "bold"),
                              bg=Config.COLORS['bg_dark'],
                              fg=Config.COLORS['text_light'])
        title_label.pack(side=tk.LEFT)
        
        # Status indicator
        self.status_label = tk.Label(header_frame,
                                   text="● Online",
                                   font=("Arial", 10),
                                   bg=Config.COLORS['bg_dark'],
                                   fg="#4CAF50")
        self.status_label.pack(side=tk.RIGHT)
        
    def create_chat_area(self):
        """Membuat area chat"""
        chat_frame = ttk.Frame(self.root, style='TFrame')
        chat_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Chat display area dengan custom styling
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            width=60,
            height=25,
            font=Config.GUI_FONT,
            bg=Config.COLORS['bg_light'],
            fg=Config.COLORS['text_light'],
            insertbackground=Config.COLORS['text_light'],
            relief='flat',
            padx=10,
            pady=10
        )
        self.chat_display.pack(fill='both', expand=True)
        self.chat_display.config(state=tk.DISABLED)
        
        # Configure tags untuk styling pesan
        self.chat_display.tag_config('user', 
                                   foreground='#ffffff',
                                   background=Config.COLORS['user_msg'],
                                   lmargin1=20, 
                                   lmargin2=20, 
                                   rmargin=20,
                                   spacing1=5,
                                   spacing3=5)
        
        self.chat_display.tag_config('bot',
                                   foreground=Config.COLORS['text_light'],
                                   background=Config.COLORS['bot_msg'],
                                   lmargin1=20,
                                   lmargin2=20,
                                   rmargin=20,
                                   spacing1=5,
                                   spacing3=5)
        
        self.chat_display.tag_config('timestamp',
                                   foreground=Config.COLORS['text_gray'],
                                   font=("Arial", 8))
        
        self.chat_display.tag_config('system',
                                   foreground='#FF9800',
                                   font=("Arial", 9, "italic"))
    
    def create_input_area(self):
        """Membuat area input"""
        input_frame = ttk.Frame(self.root, style='TFrame')
        input_frame.pack(fill='x', padx=10, pady=10)
        
        # Input field
        self.input_field = tk.Text(input_frame,
                                 height=3,
                                 font=Config.GUI_FONT,
                                 bg=Config.COLORS['bg_light'],
                                 fg=Config.COLORS['text_light'],
                                 insertbackground=Config.COLORS['text_light'],
                                 relief='solid',
                                 bd=1)
        self.input_field.pack(side=tk.LEFT, fill='x', expand=True, padx=(0, 10))
        
        # Button frame
        button_frame = ttk.Frame(input_frame, style='TFrame')
        button_frame.pack(side=tk.RIGHT)
        
        # Send button
        self.send_button = ttk.Button(button_frame,
                                    text="Kirim 🚀",
                                    command=self.send_message)
        self.send_button.pack(pady=2)
        
        # Clear button
        self.clear_button = ttk.Button(button_frame,
                                     text="Clear 🗑️",
                                     command=self.clear_chat)
        self.clear_button.pack(pady=2)
        
        # Export button
        self.export_button = ttk.Button(button_frame,
                                      text="Export 💾",
                                      command=self.export_chat)
        self.export_button.pack(pady=2)
    
    def create_sidebar(self):
        """Membuat sidebar untuk info tambahan"""
        self.sidebar = ttk.Frame(self.root, style='TFrame', width=200)
        self.sidebar.pack(side=tk.RIGHT, fill='y', padx=(0, 10), pady=10)
        
        # Info panel
        info_label = tk.Label(self.sidebar,
                            text="📊 Chat Info",
                            font=("Arial", 12, "bold"),
                            bg=Config.COLORS['bg_dark'],
                            fg=Config.COLORS['text_light'])
        info_label.pack(pady=10)
        
        # Stats
        self.stats_text = scrolledtext.ScrolledText(self.sidebar,
                                                  height=10,
                                                  width=25,
                                                  font=("Arial", 9),
                                                  bg=Config.COLORS['bg_light'],
                                                  fg=Config.COLORS['text_light'])
        self.stats_text.pack(fill='both', expand=True)
        self.stats_text.config(state=tk.DISABLED)
        
        self.update_stats()
    
    def setup_bindings(self):
        """Setup keyboard bindings"""
        self.input_field.bind('<Return>', self.on_enter_pressed)
        self.input_field.bind('<Shift-Return>', self.on_shift_enter)
        self.root.bind('<Control-n>', lambda e: self.clear_chat())
        self.root.bind('<Control-s>', lambda e: self.export_chat())
        
        # Focus on input field
        self.input_field.focus_set()
    
    def on_enter_pressed(self, event):
        """Handle Enter key press"""
        self.send_message()
        return 'break'  # Prevent default behavior
    
    def on_shift_enter(self, event):
        """Allow new line with Shift+Enter"""
        return  # Allow default behavior
    
    def send_message(self):
        """Mengirim pesan"""
        message = self.input_field.get('1.0', tk.END).strip()
        
        if message:
            # Clear input field
            self.input_field.delete('1.0', tk.END)
            
            # Tampilkan pesan user
            self.display_message(message, 'user')
            
            # Dapatkan respons dari chatbot
            response = self.chat_core.process_message(message)
            
            # Handle special commands
            if response == "CLEAR_CHAT":
                self.clear_chat()
            else:
                # Tampilkan respons bot
                self.display_message(response, 'bot')
                
                # Simpan ke history
                self.chat_manager.save_message(message, response)
                
                # Update stats
                self.update_stats()
    
    def display_message(self, message, sender):
        """Menampilkan pesan di chat area"""
        self.chat_display.config(state=tk.NORMAL)
        
        # Tambahkan timestamp
        timestamp = Config.get_timestamp()
        self.chat_display.insert(tk.END, f"[{timestamp}] ", 'timestamp')
        
        # Tambahkan pesan
        if sender == 'user':
            self.chat_display.insert(tk.END, f"You: {message}\n\n", 'user')
        else:
            self.chat_display.insert(tk.END, f"Bot: {message}\n\n", 'bot')
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def clear_chat(self):
        """Membersihkan chat"""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete('1.0', tk.END)
        self.chat_display.config(state=tk.DISABLED)
        
        # Mulai chat baru
        self.chat_manager.start_new_chat()
        self.update_stats()
        
        # Tampilkan pesan system
        self.display_system_message("Chat telah dibersihkan. Memulai percakapan baru!")
    
    def display_system_message(self, message):
        """Menampilkan pesan system"""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"System: {message}\n\n", 'system')
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def export_chat(self):
        """Export chat history"""
        try:
            filename = self.chat_manager.export_chat('txt')
            if filename:
                messagebox.showinfo("Success", f"Chat berhasil diexport ke:\n{filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengexport chat: {str(e)}")
    
    def update_stats(self):
        """Update statistics sidebar"""
        history = self.chat_manager.get_chat_history()
        total_messages = len(history)
        
        user_messages = len([m for m in history if m['user_message']])
        bot_messages = len([m for m in history if m['bot_response']])
        
        stats_text = f"""
💬 Total Pesan: {total_messages}
👤 Pesan Anda: {user_messages}
🤖 Pesan Bot: {bot_messages}

📅 Chat Dimulai:
{self.chat_manager.current_chat_file or 'Baru'}

💡 Tips:
• Enter: Kirim pesan
• Shift+Enter: Baris baru
• Ctrl+N: Chat baru
• Ctrl+S: Export chat
        """
        
        self.stats_text.config(state=tk.NORMAL)
        self.stats_text.delete('1.0', tk.END)
        self.stats_text.insert('1.0', stats_text)
        self.stats_text.config(state=tk.DISABLED)