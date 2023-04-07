# ENCRYPT TEXT
def encrypt(text):
    """
    This function takes in a plaintext string and a shift value and returns
    the Caesar cipher text by shifting each letter in the plaintext by the given shift value.
    """
    shift = 1
    cipher_text = ""
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift the character by the shift value and wrap around the alphabet
            cipher_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift the character by the shift value and wrap around the alphabet
            cipher_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If the character is not a letter, add it to the cipher text as is
            cipher_text += char
    return cipher_text

#DECRYPT TEXT
def decrypt(ciphertext):
    """Decrypts a string encrypted using Caesar Cipher with a given key."""
    plaintext = ""
    key = 1
    for char in ciphertext:
        if char.isalpha():
            # Convert the character to its ASCII code
            ascii_code = ord(char)
            # Subtract the key value from the ASCII code
            decrypted_ascii_code = ascii_code - key
            # If the ASCII code is outside the range of uppercase or lowercase letters,
            # wrap around to the other end of the alphabet
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
            # Convert the ASCII code back to a character and add it to the plaintext
            plaintext += chr(decrypted_ascii_code)
        else:
            # Non-alphabetic characters are not encrypted, so just add them to the plaintext
            plaintext += char
    return plaintext


