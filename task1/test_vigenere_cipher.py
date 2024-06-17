import unittest
from vigenere_cipher import VigenereCipher

class TestVigenereCipher(unittest.TestCase):

    def test_encryption_english(self):
        cipher = VigenereCipher('key', 'EN')
        plaintext = 'hello, world!'
        expected_ciphertext = 'rijvs, uyvjn!'
        self.assertEqual(cipher.encrypt(plaintext), expected_ciphertext)

    def test_decryption_english(self):
        cipher = VigenereCipher('key', 'EN')
        ciphertext = 'rijvs, uyvjn!'
        expected_plaintext = 'hello, world!'
        self.assertEqual(cipher.decrypt(ciphertext), expected_plaintext)

    def test_encryption_russian(self):
        cipher = VigenereCipher('ключ', 'RU')
        plaintext = 'привет, мир!'
        expected_ciphertext = 'ъьжщпю, каы!'
        self.assertEqual(cipher.encrypt(plaintext), expected_ciphertext)

    def test_decryption_russian(self):
        cipher = VigenereCipher('ключ', 'RU')
        ciphertext = 'ъьжщпю, каы!'
        expected_plaintext = 'привет, мир!'
        self.assertEqual(cipher.decrypt(ciphertext), expected_plaintext)

    def test_invalid_key(self):
        with self.assertRaises(ValueError):
            VigenereCipher('invalid1', 'EN')

    def test_invalid_alphabet(self):
        with self.assertRaises(ValueError):
            VigenereCipher('key', 'FR')


if __name__ == '__main__':
    unittest.main()
