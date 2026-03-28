# Ceasar Cipher
import string
import art
# from art import logo

alphabet = list(string.ascii_lowercase)

print(art.logo)


def caesar(decode_or_encode, original_text, shift_number):
    if decode_or_encode not in ["encode", "decode"]:
        return "Please use 'encode' or 'decode'."

    if decode_or_encode == "decode":
        shift_number *= -1

    cipher_message = ""
    for char in original_text:
        if char not in alphabet:
            cipher_message += char
        else:
            shifted_position = alphabet.index(char) + shift_number
            shifted_position %= len(alphabet)  # z -> (26 + 9) % 26 = 9
            cipher_message += alphabet[shifted_position]

    return (f"Here is the {decode_or_encode}d message: {cipher_message}")


should_continue = True
while should_continue:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower().strip()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    print(caesar(direction, original_text=text, shift_number=shift))
    restart = input(
        "Type 'yes' if you want to go again,'no' to quit: \n").lower().strip()
    if restart == 'no':
        should_continue = False
