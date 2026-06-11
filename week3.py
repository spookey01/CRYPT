# One-Time Pad (OTP) Simulation
import random
import string

def generate_key(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def otp_encrypt(plain_text, key):
    cipher = []
    for i in range(len(plain_text)):
        cipher.append(chr(ord(plain_text[i]) ^ ord(key[i])))
    return ''.join(cipher)


message = input("Enter message: ")

key = generate_key(len(message))
print("\nGenerated Key:", key)

encrypted = otp_encrypt(message, key)
print("Encrypted message:", encrypted)

decrypted = otp_encrypt(encrypted, key)
print("Decrypted message:", decrypted)
