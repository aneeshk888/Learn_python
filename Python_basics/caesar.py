def caesar(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    
    # Add uppercase support
    alphabet_full = alphabet + alphabet.upper()
    shifted_full = shifted_alphabet + shifted_alphabet.upper()
    
    # Reverse shift if decrypting
    if not encrypt:
        shift = -shift
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        shifted_full = shifted_alphabet + shifted_alphabet.upper()
    
    translation_table = str.maketrans(alphabet_full, shifted_full)
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift, True)

def decrypt(text, shift):
    return caesar(text, shift, False)

# Step 25: Test decrypt
encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)   # Counter is found in unlikely places.
