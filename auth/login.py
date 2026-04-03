import customtkinter as ctk
from core.supabase_client import supabase
from tkinter import messagebox

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Đăng nhập - Messenger")
        self.geometry("400x300")

        self.email_label = ctk.CTkLabel(self, text="Email:")
        self.email_label.pack(pady=10)
        self.email_entry = ctk.CTkEntry(self)
        self.email_entry.pack(pady=5)

        self.password_label = ctk.CTkLabel(self, text="Mật khẩu:")
        self.password_label.pack(pady=10)
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = ctk.CTkButton(self, text="Đăng nhập", command=self.login)
        self.login_button.pack(pady=20)

        self.signup_button = ctk.CTkButton(self, text="Đăng ký", command=self.signup)
        self.signup_button.pack(pady=5)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        try:
            response = supabase.auth.sign_in_with_password({"email": email, "password": password})
            self.user = response.user
            self.destroy()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đăng nhập thất bại: {str(e)}")

    def signup(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        try:
            supabase.auth.sign_up({"email": email, "password": password})
            messagebox.showinfo("Thành công", "Đăng ký thành công. Vui lòng kiểm tra email để xác nhận.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đăng ký thất bại: {str(e)}")

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()