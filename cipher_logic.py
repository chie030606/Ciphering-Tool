"""
cipher_logic.py

Contains cipher logic for Monoalphabetic, Vigenère, and 
Autokey-style Polyalphabetic Substitution Ciphers.
"""

def monoalphabetic_substitution_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift

    result = ""
    steps = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            orig_pos = ord(char) - base
            raw_sum = orig_pos + shift
            new_pos = raw_sum % 26
            new_char = chr(new_pos + base)

            result += new_char
            steps.append(f"'{char}' ({orig_pos}) + key({shift}) = {raw_sum} mod 26 = {new_pos} -> '{new_char}'")
        else:
            result += char
            steps.append(f"'{char}' (Skipped)")

    return result, "\n".join(steps)


def vigenere_cipher(text, key, decrypt=False):
    key = key.upper()
    result = ""
    steps = []
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char) - ord('A')
            shift = -key_shift if decrypt else key_shift

            orig_pos = ord(char) - base
            raw_sum = orig_pos + shift
            new_pos = raw_sum % 26
            new_char = chr(new_pos + base)

            result += new_char
            steps.append(f"[Key: {key_char}] '{char}' ({orig_pos}) + key({shift}) = {raw_sum} mod 26 = {new_pos} -> '{new_char}'")
            key_index += 1
        else:
            result += char
            steps.append(f"'{char}' (Skipped)")

    return result, "\n".join(steps)


def polyalphabetic_substitution_cipher(text, initial_key, decrypt=False):
    """
    Polyalphabetic Substitution Cipher (Autokey implementation)
    - 1st subkey: initial_key
    - Subsequent subkeys: values of previous plaintext characters
    """
    result = ""
    steps = []
    current_key = int(initial_key)

    for char in text.upper():
        if char.isalpha():
            if not decrypt:
                orig_pos = ord(char) - ord('A')
                raw_sum = orig_pos + current_key
                new_pos = raw_sum % 26
                new_char = chr(new_pos + ord('A'))

                result += new_char
                steps.append(f"[Subkey: {current_key}] '{char}' ({orig_pos}) + key({current_key}) = {raw_sum} mod 26 = {new_pos} -> '{new_char}'")
                current_key = orig_pos  # Next subkey is the plaintext character's value
            else:
                c_val = ord(char) - ord('A')
                p_val = (c_val - current_key) % 26
                p_char = chr(p_val + ord('A'))

                result += p_char
                steps.append(f"[Subkey: {current_key}] '{char}' ({c_val}) - key({current_key}) = {c_val - current_key} mod 26 = {p_val} -> '{p_char}'")
                current_key = p_val  # Next subkey is the decrypted plaintext character's value
        else:
            result += char
            steps.append(f"'{char}' (Skipped)")

    return result, "\n".join(steps)