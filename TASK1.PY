# Caesar Cipher Program
# Author: ALAY PATEL
# SkillCraft Technology-Task 01

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    
    if mode == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isalpha():  
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    
    return result

print("🔐 Welcome to Caesar Cipher Tool by ALAY PATEL🔐")
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))

encrypted = caesar_cipher(message, shift, "encrypt")
decrypted = caesar_cipher(encrypted, shift, "decrypt")

print("\n📌 Results:")
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted}")
print(f"Decrypted Message: {decrypted}")