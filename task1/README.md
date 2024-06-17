# Vigenere Cipher

This project is an implementation of the Vigenere Cipher for both English and Russian alphabets. The cipher can be used to encrypt and decrypt text using a provided key.

## Features

- Supports both English and Russian alphabets
- Encryption and decryption functionality
- Command-line interface for ease of use
- Unit tests to ensure correctness

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/fortrane/swsu-practice-4
    cd /swsu-practice-4/task1
    ```

2. (Optional) Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

## Usage

### Encrypting Text

#### English
```sh
python vigenere_cipher.py encrypt key "hello, world!" --lang EN
Output: rijvs, uyvjn!
```

#### Russian
```sh
python vigenere_cipher.py encrypt ключ "привет, мир!" --lang RU
Output: ъьжщпю, каы!
```

### Decrypting Text

#### English
```sh
python vigenere_cipher.py decrypt key "rijvs, uyvjn!" --lang EN
Output: hello, world!
```

#### Russian
```sh
python vigenere_cipher.py decrypt ключ "ъьжщпю, каы!" --lang RU
Output: привет, мир!
```

## Running Tests
To run the unit tests, use the following command:
```sh
python -m unittest test_vigenere_cipher.py
```

### Example Test Results
![Test Results](https://i.ibb.co/37XjhTJ/image.png)

## Project Structure
```bash
task1/
│
├── vigenere_cipher.py         # Main script for the Vigenere Cipher
├── test_vigenere_cipher.py    # Unit tests for the Vigenere Cipher
└── README.md                  # This file
```

## License
This project is licensed under the MIT License - see the [LICENSE](https://www.mit.edu/~amini/LICENSE.md) file for details.