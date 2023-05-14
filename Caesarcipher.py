
def encrypt(text):
    shift = 1
    cipher_text = ""
    for char in text:
         if char.isupper():
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text


def decrypt(ciphertext):
    
    plaintext = ""
    key = 1
    for char in ciphertext:
        if char.isalpha():
            ascii_code = ord(char)
            decrypted_ascii_code = ascii_code - key
            if char.isupper():
                if decrypted_ascii_code < ord('A'):
                    decrypted_ascii_code += 26
                elif decrypted_ascii_code > ord('Z'):
                    decrypted_ascii_code -= 26
            elif char.islower():
                if decrypted_ascii_code < ord('a'):
                    decrypted_ascii_code += 26
                elif decrypted_ascii_code > ord('z'):
                    decrypted_ascii_code -= 26
            plaintext += chr(decrypted_ascii_code)
        else:
            plaintext += char
    return plaintext

