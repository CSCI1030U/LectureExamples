# caesar cipher
def shift(letter, shift_amount):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_index = alphabet.index(letter)
    ciphertext_letter_index = (letter_index + shift_amount) % 26
    # if ciphertext_letter_index > 25:
    #     ciphertext_letter_index -= 26

    return alphabet[ciphertext_letter_index]

def caesar_cipher(message, shift_amount):
    ciphertext = ''
    for letter in message:
        ciphertext += shift(letter, shift_amount)
    return ciphertext

# message = 'PHHWDWWKHEULGJHDWGDZQ'
# for shift_amount in range(1, 26):
#     print(caesar_cipher(message, shift_amount))

import math

# vigenere cipher
def vigenere_encrypt(message, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # duplicate the key to be at least as long as the message
    key = key * math.ceil(len(message) / len(key))
    ciphertext = ''
    for index in range(len(message)):
        ciphertext += shift(message[index], alphabet.index(key[index]) + 1)
    
    return ciphertext

def vigenere_decrypt(message, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # duplicate the key to be at least as long as the message
    key = key * math.ceil(len(message) / len(key))
    ciphertext = ''
    for index in range(len(message)):
        ciphertext += shift(message[index], -(alphabet.index(key[index]) + 1))
    
    return ciphertext

message = 'IHAVETHEDEVICE'
ciphertext = vigenere_encrypt(message, 'SWAG')
print(f'{message} => {ciphertext}')

plaintext = vigenere_decrypt(ciphertext, 'SWAG')
print(f'{ciphertext} => {plaintext}')

# rsa encryption
def encrypt(m, e, n):
    return (m ** e) % n

# rsa decryption
def decrypt(c, d, n):
    return (c ** d) % n

n = int(input('N:'))
e = int(input('e:'))
d = int(input('d:'))
m = int(input('M:'))

c = encrypt(m, e, n)
print(f'encrypt({m}, {e}, {n}) = {c}')

m_new = decrypt(c, d, n)
print(f'decrypt({c}, {d}, {n}) = {m_new}')
