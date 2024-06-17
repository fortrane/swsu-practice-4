import argparse

class VigenereCipher:
    def __init__(self, key, alphabet='EN'):
        self.key = key.lower()
        self.alphabet = self.get_alphabet(alphabet)
        self.validate_key()

    @staticmethod
    def get_alphabet(lang):
        alphabets = {
            'EN': 'abcdefghijklmnopqrstuvwxyz',
            'RU': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        }
        if lang not in alphabets:
            raise ValueError("Unsupported language. Choose 'EN' for English or 'RU' for Russian.")
        return alphabets[lang]

    def validate_key(self):
        if not all(char in self.alphabet for char in self.key):
            raise ValueError("Key must contain only characters from the alphabet.")

    def encrypt(self, plaintext):
        return self.process_text(plaintext.lower(), 'encrypt')

    def decrypt(self, ciphertext):
        return self.process_text(ciphertext.lower(), 'decrypt')

    def process_text(self, text, method):
        processed_text = []
        key_length = len(self.key)
        key_index = 0

        for char in text:
            if char in self.alphabet:
                shift = self.alphabet.index(self.key[key_index % key_length])
                if method == 'decrypt':
                    shift = -shift

                index = (self.alphabet.index(char) + shift) % len(self.alphabet)
                processed_char = self.alphabet[index]
                processed_text.append(processed_char)
                key_index += 1
            else:
                processed_text.append(char)

        return ''.join(processed_text)


def main():
    parser = argparse.ArgumentParser(description='Vigenere Cipher Encryption and Decryption')
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help='Mode: encrypt or decrypt')
    parser.add_argument('key', help='Cipher key')
    parser.add_argument('text', help='Text to be encrypted or decrypted')
    parser.add_argument('--lang', choices=['EN', 'RU'], default='EN', help='Alphabet language: EN for English, RU for Russian (default: EN)')

    args = parser.parse_args()

    cipher = VigenereCipher(args.key, args.lang)

    if args.mode == 'encrypt':
        result = cipher.encrypt(args.text)
    else:
        result = cipher.decrypt(args.text)

    print(result)


if __name__ == "__main__":
    main()
