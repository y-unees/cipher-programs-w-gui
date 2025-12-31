import customtkinter as ctk
import tkinter as tk
from ciphers_logic import HillCipher

class HillFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        self.label = ctk.CTkLabel(self, text="Hill Cipher (2x2 Matrix)", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)

        self.entry_txt = ctk.CTkEntry(self, placeholder_text="Enter text", width=300)
        self.entry_txt.pack(pady=10)

        ctk.CTkLabel(self, text="Select a Valid Key Matrix:").pack(pady=0)
        
        self.valid_keys = ["3 3 2 5", "5 17 8 3", "7 12 11 13", "3 2 3 5", "5 8 17 3", 
                           "2 3 5 23", "9 7 11 2", "3 7 5 12", "7 8 11 11", "11 8 3 7", 
                           "15 2 19 3", "2 5 9 18", "19 2 11 7", "23 20 1 1"]
        
        self.key_selection = ctk.StringVar(value=self.valid_keys[0])
        self.key_dropdown = ctk.CTkOptionMenu(self, values=self.valid_keys, variable=self.key_selection)
        self.key_dropdown.pack(pady=10)

        self.btn_encrypt = ctk.CTkButton(self, text="Encrypt", command=self.to_encrypt, fg_color="#2c3e50") 
        self.btn_encrypt.pack(pady=10)

        self.btn_decrypt = ctk.CTkButton(self, text="Decrypt", command=self.to_decrypt, fg_color="#2c3e50") 
        self.btn_decrypt.pack(pady=10)

        self.var_text = tk.StringVar(value="")
        self.output_label = ctk.CTkLabel(self, textvariable=self.var_text, wraplength=350, font=("Consolas", 14), text_color='#27ae60')
        self.output_label.pack(pady=20)
    
    def parse_key(self):
        nums = list(map(int, self.key_selection.get().split()))
        return [[nums[0], nums[1]], [nums[2], nums[3]]]

    def to_encrypt(self):
        text = self.entry_txt.get()
        if not text: return
        ciph = HillCipher(text, self.parse_key())
        self.var_text.set(f"ENCRYPTED:\n{ciph.encrypt()}")

    def to_decrypt(self):
        text = self.entry_txt.get()
        if not text: return
        ciph = HillCipher(text, self.parse_key())
        self.var_text.set(f"DECRYPTED:\n{ciph.decrypt()}")