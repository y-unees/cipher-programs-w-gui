# Cryptography Tool: Multi-Cipher Suite

This project is a comprehensive desktop application built with Python and `CustomTkinter`. It provides a graphical user interface (GUI) to encrypt and decrypt messages using several classic cryptographic algorithms.

## Features

* **Caesar Cipher:** A simple substitution cipher that shifts characters by a fixed number.
* **Rail Fence Cipher:** A transposition cipher that writes a message in a zigzag pattern across multiple "rails."
* **Hill Cipher:** A polygraphic substitution cipher based on linear algebra using a 2x2 matrix.
* **Vigenère Cipher:** A method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword.

---

## Project Structure

```text
├── main.py             # Entry point; contains the TabView GUI switcher
├── ciphers_logic.py    # Core mathematical logic for all ciphers
├── gui.py              # Caesar Cipher frame
├── rf_gui.py           # Rail Fence Cipher frame
├── hill_gui.py         # Hill Cipher frame
└── vignere_gui.py      # Vigenère Cipher frame
```
---

## Installation

1.  **Clone the repository** or download the source files.
2.  **Install Dependencies:** This project requires `customtkinter`. You can install it via pip:
    ```bash
    pip install customtkinter
    ```

## Usage

1.  Run the main application:
    ```bash
    python main.py
    ```
2.  **Navigate** through the tabs at the top to select the desired cipher.
3.  **Input** your plaintext or ciphertext.
4.  **Configure** the keys:
    * **Caesar:** Uses a default shift (Key: 3).
    * **Rail Fence:** Input the number of rails (integer).
    * **Hill:** Select a mathematically valid 2x2 matrix from the dropdown menu.
    * **Vigenère:** Enter a keyword (string).
5.  Click **Encrypt** or **Decrypt** to see the result.

---

## Technical Notes

### Hill Cipher Mathematical Constraint
The Hill Cipher requires the key matrix to be invertible modulo 26. To ensure a smooth user experience, the GUI provides a selection of "Known Good Keys" where the determinant is coprime to 26.

### Rail Fence Pattern
The logic calculates the zigzag path to correctly place characters in the grid for encryption and determines the specific rail lengths for accurate reconstruction during decryption.

---

**Note:** This README has been generated in collaboration w/ Gemini.