import customtkinter as ctk
from tkinter import scrolledtext, messagebox
from core.messaging import Messaging
from core.file_transfer import FileTransfer
from ui.file_panel import FilePanel

class ChatWindow(ctk.CTk):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.messaging = Messaging(user.id)
        self.file_transfer = FileTransfer(user.id)
        self.other_user_id = "some_other_user_id"  # For MVP, assume chatting with one user

        self.title("Chat - Messenger")
        self.geometry("600x500")

        self.chat_area = scrolledtext.ScrolledText(self, wrap=ctk.WORD, state='disabled')
        self.chat_area.pack(pady=10, padx=10, fill=ctk.BOTH, expand=True)

        self.message_entry = ctk.CTkEntry(self, placeholder_text="Nhập tin nhắn...")
        self.message_entry.pack(side=ctk.LEFT, padx=10, pady=10, fill=ctk.X, expand=True)

        self.send_button = ctk.CTkButton(self, text="Gửi", command=self.send_message)
        self.send_button.pack(side=ctk.RIGHT, padx=10, pady=10)

        self.file_panel = FilePanel(self, self.file_transfer, self.display_file, self.other_user_id)
        self.file_panel.pack(side=ctk.BOTTOM, fill=ctk.X)

        self.load_history()
        self.messaging.subscribe_to_messages(self.other_user_id, self.receive_message)

    def send_message(self):
        content = self.message_entry.get()
        if content:
            if self.messaging.send_message(self.other_user_id, content):
                self.display_message(f"Bạn: {content}")
                self.message_entry.delete(0, ctk.END)
            else:
                messagebox.showerror("Lỗi", "Gửi tin nhắn thất bại")

    def receive_message(self, message):
        self.display_message(f"{message['sender_id']}: {message['content']}")

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(ctk.END, message + '\n')
        self.chat_area.config(state='disabled')
        self.chat_area.see(ctk.END)

    def display_file(self, file_metadata):
        self.display_message(f"Bạn gửi tệp: {file_metadata['filename']}")

    def load_history(self):
        history = self.messaging.get_chat_history(self.other_user_id)
        for msg in history:
            sender = "Bạn" if msg['sender_id'] == self.user.id else msg['sender_id']
            self.display_message(f"{sender}: {msg['content']}")

if __name__ == "__main__":
    # For testing
    class MockUser:
        id = "test_user_id"
    app = ChatWindow(MockUser())
    app.mainloop()