import customtkinter as ctk
import tkinter as tk
from ciphers_logic import RailFenceCipher

class RailFenceFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.entry_txt = ctk.CTkEntry(self, placeholder_text="Type input text", width=300)
        self.entry_txt.pack(pady=10)

        self.rail_entry = ctk.CTkEntry(self, placeholder_text="Enter rails (default = 3)", width=300)
        self.rail_entry.pack(pady=10)

        self.btn_encrypt = ctk.CTkButton(self, text="Encrypt", command=self.to_encrypt) 
        self.btn_encrypt.pack(pady=10)

        self.btn_decrypt = ctk.CTkButton(self, text="Decrypt", command=self.to_decrypt) 
        self.btn_decrypt.pack(pady=10)

        self.var_text = tk.StringVar(value="")
        self.output_label = ctk.CTkLabel(self, textvariable=self.var_text, wraplength=350)
        self.output_label.pack(pady=20)
    
    def get_rails(self):
        val = self.rail_entry.get()
        return int(val) if val.isdigit() else 3

    def to_encrypt(self):
        ciph = RailFenceCipher(self.entry_txt.get(), self.get_rails())
        self.var_text.set(f"Result: {ciph.encrypt()}")

    def to_decrypt(self):
        ciph = RailFenceCipher(self.entry_txt.get(), self.get_rails())
        self.var_text.set(f"Result: {ciph.decrypt()}")