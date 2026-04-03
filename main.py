import customtkinter as ctk
from auth.login import LoginWindow
from ui.chat_window import ChatWindow

def main():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    login_window = LoginWindow()
    login_window.mainloop()

    if hasattr(login_window, 'user'):
        chat_window = ChatWindow(login_window.user)
        chat_window.mainloop()

if __name__ == "__main__":
    main()