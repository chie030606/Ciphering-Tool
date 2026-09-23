def monoalphabetic_substitution_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def vigenere_cipher(text, key, decrypt=False):
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            if decrypt:
                shift = -shift
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result


def polyalphabetic_substitution_cipher(text, keys, decrypt=False):
    result = ""
    key_index = 0
    for char in text.upper():
        if char.isalpha():
            shift = keys[key_index % len(keys)]
            if decrypt:
                shift = -shift
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
    return result