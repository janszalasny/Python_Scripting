import tkinter as tk
from tkinter import scrolledtext
from app.chatbot import ChatBot

class ChatApplication:
    """
    A class to create the GUI for the chatbot application.
    """
    def __init__(self, master):
        """
        Initializes the ChatApplication.

        :param master: The root Tkinter window.
        """
        self.master = master
        master.title("CodeHelper Bot")
        master.geometry("500x600")

        self.chatbot = ChatBot()

        self.chat_history = scrolledtext.ScrolledText(master, state='disabled')
        self.chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.msg_entry = tk.Entry(master, width=50)
        self.msg_entry.pack(pady=10, padx=10, fill=tk.X, expand=False)
        self.msg_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

    def send_message(self, event=None):
        """
        Handles sending a message from the user and displaying the response.
        """
        user_input = self.msg_entry.get()
        if user_input.strip() == "":
            return

        self._display_message(f"You: {user_input}")
        self.msg_entry.delete(0, tk.END)

        response = self.chatbot.get_response(user_input)
        self._display_message(f"Bot: {response}")

    def _display_message(self, message):
        """
        Displays a message in the chat history.

        :param message: The message to display.
        """
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.config(state='disabled')
        self.chat_history.yview(tk.END)

