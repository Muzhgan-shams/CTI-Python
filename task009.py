# Password generator
import random
import string

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password? "))
numbers = int(input("How many numbers would you like? "))
symbols = int(input("How many symbols would you like? "))


random_numbers = ""
random_symbols = ""  # symbols
random_letters = ""  # a-z, A-Z

for _ in range(numbers):
    random_numbers += random.choice(string.digits)
for _ in range(symbols):
    random_symbols += random.choice(string.punctuation)
for _ in range(letters):
    random_letters += random.choice(string.ascii_letters)

result = list(random_letters + random_numbers + random_symbols)
random.shuffle(result)
final_pass = "".join(result)
print(final_pass)


# Another version
# password_chars = []
# password_chars.extend(random.choice(string.ascii_letters) for _ in range(letters))
# password_chars.extend(random.choice(string.digits) for _ in range(numbers))
# password_chars.extend(random.choice(string.punctuation) for _ in range(symbols))

# random.shuffle(password_chars)
# final_password = ''.join(password_chars)
# print(f"Your password is: {final_password}")
