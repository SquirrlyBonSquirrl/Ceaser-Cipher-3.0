charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def caesar_decipher(text: str, shift: int):
    result = ""
    for char in text:
        if char in charset:
            new_index = (charset.index(char) - shift) % len(charset)
            new_char = charset[new_index]
            result += new_char.lower() if char.islower() else new_char.upper()
        else:
            result += char
    return result

# im asking the user for the shift value however the default is 3
encrypted_message = input("Enter the encrypted message: ")
shift_input = input("Enter the shift value: ")


# the normal shift value is three so type nate if you got your code encrypted by my previous cipher
if shift_input.lower() == "nate":
    shift = 3
else:
    shift = int(shift_input)

# Decrypt the message
decrypted_message = caesar_decipher(encrypted_message, shift)
print("Decrypted:", decrypted_message)
