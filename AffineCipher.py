import json


# Helper function to find modular inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_encrypt(text, a, b):
    m = 256  # ASCII character set size
    encrypted_text = ""
    steps = []
    for char in text:
        x = ord(char)  # Get ASCII value
        encrypted_char = (a * x + b) % m  # Affine transformation
        encrypted_text += chr(encrypted_char)  # Convert back to character
        steps.append({
            "encrypted_value": encrypted_char,
            "encrypted_char": encrypted_text[-1]
        })
    return encrypted_text, steps


def affine_decrypt(text, a, b):
    m = 256  # ASCII character set size
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        raise ValueError(f"No modular inverse exists for a = {a} and m = {m}")
    
    decrypted_text = ""
    steps = []
    for char in text:
        y = ord(char)  # Get ASCII value
        decrypted_char = (a_inv * (y - b)) % m  # Inverse affine transformation
        decrypted_text += chr(decrypted_char)  # Convert back to character
        steps.append({
            "decrypted_value": decrypted_char,
            "decrypted_char": decrypted_text[-1]
        })
    
    return decrypted_text, steps