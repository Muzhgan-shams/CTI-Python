# Ceasar Cipher

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower().strip()
shift = int(input("Type the shift number: \n"))

# Encryption function


def encrypt(original_text, shift_number):
    cipher_message = ""
    for letter in original_text:
        shifted_postition = alphabet.index(letter) + shift_number
        shifted_postition %= len(alphabet)  # z -> (26 + 9) % 26 = 9
        cipher_message += alphabet[shifted_postition]
    print(f"Here is the encoded message: {cipher_message}")


encrypt(original_text=text, shift_number=shift)
