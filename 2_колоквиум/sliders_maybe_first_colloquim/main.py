import os
import math

def generate_key(bit_length):
    p = generate_prime_number(bit_length)
    q = generate_prime_number(bit_length)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = mod_inverse(e, phi)
    return n, e, d

def generate_prime_number(bit_length):
    while True:
        num = generate_random_number(bit_length)
        if is_prime(num):
            return num

def generate_random_number(bit_length):
    return random.getrandbits(bit_length)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt_file(file_path, public_key, n):
    with open(file_path, 'rb') as file:
        plaintext = int.from_bytes(file.read(), byteorder='big')
    ciphertext = pow(plaintext, public_key, n)
    return ciphertext

def decrypt_file(encrypted_content, private_key, n):
    decrypted_text = pow(encrypted_content, private_key, n)
    return decrypted_text.to_bytes((decrypted_text.bit_length() + 7) // 8, byteorder='big')

if __name__ == '__main__':
    import random

    bit_length = 1024
    n, e, d = generate_key(bit_length)

    encrypted_content = encrypt_file('example.txt', e, n)
    with open('encrypted_example.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_content.to_bytes((encrypted_content.bit_length() + 7) // 8, byteorder='big'))
    
    decrypted_content = decrypt_file(encrypted_content, d, n)
    with open('decrypted_example.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted_content)
