import customtkinter as ctk
from gui import CaesarFrame
from rf_gui import RailFenceFrame
from hill_gui import HillFrame
from vignere_gui import VigenereFrame

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cryptography Tool")
        self.geometry("500x600")

        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(padx=10, pady=10, expand=True, fill="both")

        self.tabview.add("Caesar")
        self.tabview.add("Rail Fence")
        self.tabview.add("Hill")
        self.tabview.add("Vigenère")

        CaesarFrame(self.tabview.tab("Caesar")).pack(expand=True, fill="both")
        RailFenceFrame(self.tabview.tab("Rail Fence")).pack(expand=True, fill="both")
        HillFrame(self.tabview.tab("Hill")).pack(expand=True, fill="both")
        VigenereFrame(self.tabview.tab("Vigenère")).pack(expand=True, fill="both")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()