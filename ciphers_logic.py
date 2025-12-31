class CaesarCipher:
    
    def __init__(self, text, key):
        self.text = text
        self.key = key

    def process(self, char, key):
        if char.isupper():
            start = ord('A') # 65
            return chr((ord(char) - start + key) % 26 + start)
        elif char.islower():
            start = ord('a') # 97
            return chr((ord(char) - start + key) % 26 + start)
        return char

    def encrypt(self):
        return "".join(self.process(char, self.key) for char in self.text)

    def decrypt(self):
        return "".join(self.process(char, -self.key) for char in self.text)


class RailFenceCipher:
    def __init__(self, text, rails=2):
        self.text = text
        self.rails = rails

    def encrypt(self):
        if self.rails == 1:
            return self.text
            
        fence = [[] for _ in range(self.rails)]
        rail = 0
        direction = 1 

        for char in self.text:
            fence[rail].append(char)
            rail += direction
            if rail == 0 or rail == self.rails - 1:
                direction *= -1
                    
        return "".join(["".join(r) for r in fence])

    def decrypt(self):
        if self.rails == 1:
            return self.text

        pattern = [['' for _ in range(len(self.text))] for _ in range(self.rails)]
        rail = 0
        direction = 1

        for i in range(len(self.text)):
            pattern[rail][i] = '*'
            rail += direction
            if rail == 0 or rail == self.rails - 1:
                direction *= -1

        cipher_idx = 0
        for r in range(self.rails):
            for c in range(len(self.text)):
                if pattern[r][c] == '*' and cipher_idx < len(self.text):
                    pattern[r][c] = self.text[cipher_idx]
                    cipher_idx += 1

        result = []
        rail = 0
        direction = 1
        for i in range(len(self.text)):
            result.append(pattern[rail][i])
            rail += direction
            if rail == 0 or rail == self.rails - 1:
                direction *= -1

        return "".join(result)

class HillCipher:
    def __init__(self, text, key_matrix=None):
        # Default key matrix [[3, 3], [2, 5]] if none provided
        self.key = key_matrix if key_matrix else [[3, 3], [2, 5]]
        self.text = text.upper().replace(" ", "")
        
        if len(self.text) % 2 != 0:
            self.text += "X"

    def encrypt(self):
        res = ""
        for i in range(0, len(self.text), 2):
            v = [ord(self.text[i]) - 65, ord(self.text[i+1]) - 65]
            
            c1 = (self.key[0][0] * v[0] + self.key[0][1] * v[1]) % 26
            c2 = (self.key[1][0] * v[0] + self.key[1][1] * v[1]) % 26
            
            res += chr(c1 + 65) + chr(c2 + 65)
        return res

    def decrypt(self):
        det = (self.key[0][0] * self.key[1][1] - self.key[0][1] * self.key[1][0]) % 26
        
        det_inv = -1
        for x in range(1, 26):
            if (det * x) % 26 == 1:
                det_inv = x
                break
        
        if det_inv == -1:
            return "Error: Key matrix is not invertible (Determinant has no inverse mod 26)"

        inv_key = [
            [(self.key[1][1] * det_inv) % 26, (-self.key[0][1] * det_inv) % 26],
            [(-self.key[1][0] * det_inv) % 26, (self.key[0][0] * det_inv) % 26]
        ]

        res = ""
        for i in range(0, len(self.text), 2):
            v = [ord(self.text[i]) - 65, ord(self.text[i+1]) - 65]
            p1 = (inv_key[0][0] * v[0] + inv_key[0][1] * v[1]) % 26
            p2 = (inv_key[1][0] * v[0] + inv_key[1][1] * v[1]) % 26
            res += chr(p1 + 65) + chr(p2 + 65)
        return res

class VigenereCipher:
    def __init__(self, text, key):
        self.text = text
        self.key = key

    def _generate_full_key(self):
        full_key = ""
        key_idx = 0
        for char in self.text:
            if char.isalpha():
                full_key += self.key[key_idx % len(self.key)]
                key_idx += 1
            else:
                full_key += char
        return full_key

    def encrypt(self):
        full_key = self._generate_full_key()
        result = []
        
        for t_char, k_char in zip(self.text, full_key):
            if t_char.isalpha():
                shift = ord(k_char.upper()) - 65
                start = 65 if t_char.isupper() else 97
                # (Original position + Shift) % 26
                new_char = chr((ord(t_char) - start + shift) % 26 + start)
                result.append(new_char)
            else:
                result.append(t_char)
        return "".join(result)

    def decrypt(self):
        full_key = self._generate_full_key()
        result = []
        
        for t_char, k_char in zip(self.text, full_key):
            if t_char.isalpha():
                shift = ord(k_char.upper()) - 65
                start = 65 if t_char.isupper() else 97
                # (Original position - Shift) % 26
                new_char = chr((ord(t_char) - start - shift) % 26 + start)
                result.append(new_char)
            else:
                result.append(t_char)
        return "".join(result)