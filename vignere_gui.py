import customtkinter as ctk
import tkinter as tk
from ciphers_logic import VigenereCipher

class VigenereFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.label = ctk.CTkLabel(self, text="Vigenère Cipher", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        self.entry_txt = ctk.CTkEntry(self, placeholder_text="Enter Message", width=300)
        self.entry_txt.pack(pady=10)

        self.entry_key = ctk.CTkEntry(self, placeholder_text="Enter Keyword", width=300)
        self.entry_key.pack(pady=10)

        self.btn_encrypt = ctk.CTkButton(self, text="Encrypt", command=self.to_encrypt) 
        self.btn_encrypt.pack(pady=10)

        self.btn_decrypt = ctk.CTkButton(self, text="Decrypt", command=self.to_decrypt) 
        self.btn_decrypt.pack(pady=10)

        self.var_text = tk.StringVar(value="")
        self.output_label = ctk.CTkLabel(self, textvariable=self.var_text, wraplength=350, font=("Arial", 14))
        self.output_label.pack(pady=20)
    
    def to_encrypt(self):
        text, key = self.entry_txt.get(), self.entry_key.get()
        if not text or not key: return
        ciph = VigenereCipher(text, key)
        self.var_text.set(f"Result: {ciph.encrypt()}")

    def to_decrypt(self):
        text, key = self.entry_txt.get(), self.entry_key.get()
        if not text or not key: return
        ciph = VigenereCipher(text, key)
        self.var_text.set(f"Result: {ciph.decrypt()}")