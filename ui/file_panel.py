import customtkinter as ctk
from tkinter import filedialog
from core.file_transfer import FileTransfer

class FilePanel(ctk.CTkFrame):
    def __init__(self, master, file_transfer: FileTransfer, send_callback, other_user_id: str):
        super().__init__(master)
        self.file_transfer = file_transfer
        self.send_callback = send_callback
        self.other_user_id = other_user_id

        self.select_button = ctk.CTkButton(self, text="Chọn tệp", command=self.select_file)
        self.select_button.pack(pady=10)

        self.selected_file_label = ctk.CTkLabel(self, text="Chưa chọn tệp")
        self.selected_file_label.pack(pady=5)

        self.send_button = ctk.CTkButton(self, text="Gửi tệp", command=self.send_file, state="disabled")
        self.send_button.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.selected_file = file_path
            self.selected_file_label.configure(text=f"Đã chọn: {file_path.split('/')[-1]}")
            self.send_button.configure(state="normal")

    def send_file(self):
        if hasattr(self, 'selected_file'):
            result = self.file_transfer.upload_file(self.selected_file, self.other_user_id)
            if result:
                self.send_callback(result)
                self.selected_file_label.configure(text="Chưa chọn tệp")
                self.send_button.configure(state="disabled")
            else:
                # Error handling
                pass