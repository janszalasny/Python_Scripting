import tkinter as tk
from app.gui import ChatApplication

if __name__ == "__main__":
    """
    Main entry point for the chatbot application.
    """
    root = tk.Tk()
    app = ChatApplication(root)
    root.mainloop()
