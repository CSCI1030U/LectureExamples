# caesar cipher
def shift(letter, shift_amount):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    letter_index = alphabet.index(letter)
    new_index = (letter_index + shift_amount) % 26

    return alphabet[new_index]

def caesar_cipher(message, shift_amount):
    ciphertext = ''

    for letter in message:
        ciphertext += shift(letter, shift_amount)

    return ciphertext

# for shift_amount in range(1, 26):
#     print(caesar_cipher('PHHWDWWKHEULGJHDWGDZQ', shift_amount))
import math
def vigenere_encrypt(message, key):
    # duplicate the key to be at least as long as the message
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key * math.ceil(len(message) / len(key))

    # shift each character one by one
    ciphertext = ''
    for index in range(len(message)):
        shift_amount = alphabet.index(key[index])
        ciphertext += shift(message[index], shift_amount)
    
    return ciphertext

def vigenere_decrypt(message, key):
    # duplicate the key to be at least as long as the message
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key * math.ceil(len(message) / len(key))

    # shift each character one by one
    ciphertext = ''
    for index in range(len(message)):
        shift_amount = alphabet.index(key[index])
        ciphertext += shift(message[index], -shift_amount)
    
    return ciphertext

ciphertext = vigenere_encrypt('PACKAGEDELIVERED', 'PLEASE')
print(f'ciphertext = {ciphertext}')

plaintext = vigenere_decrypt(ciphertext, 'PLEASE')
print(f'plaintext = {plaintext}')

# rsa encryption (will post later)


# rsa decryption

