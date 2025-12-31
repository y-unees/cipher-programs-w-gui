import customtkinter as ctk
import tkinter as tk
from ciphers_logic import CaesarCipher

class CaesarFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        self.key = 3

        self.entry = ctk.CTkEntry(self, placeholder_text="Type input text", width=300)
        self.entry.pack(pady=20)

        self.btn_encrypt = ctk.CTkButton(self, text="Encrypt", command=self.to_encrypt) 
        self.btn_encrypt.pack(pady=10)

        self.btn_decrypt = ctk.CTkButton(self, text="Decrypt", command=self.to_decrypt) 
        self.btn_decrypt.pack(pady=10)

        self.var_text = tk.StringVar(value="")
        self.output_label = ctk.CTkLabel(self, textvariable=self.var_text)
        self.output_label.pack(pady=20)
    
    def to_encrypt(self):
        ciph = CaesarCipher(self.entry.get(), self.key)
        self.var_text.set(ciph.encrypt())

    def to_decrypt(self):
        ciph = CaesarCipher(self.entry.get(), self.key)
        self.var_text.set(ciph.decrypt())