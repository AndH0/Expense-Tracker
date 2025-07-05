import string
import random

chars = string.digits + string.ascii_letters + string.punctuation + " "
chars = list(chars)

key = chars.copy()

random.shuffle(key)

print(f"Chars : {chars}")
print(f"Key   : {key}")

original = input("Enter a message: ")
encrypted = ""
decrypted = ""

for char in original:
    index = chars.index(char)
    encrypted += key[index]
print(encrypted)

while True:
    decrypt = input("Would you like to decrypt? (Y/N) ").lower()
    if decrypt == "y":
        decrypted = ""  # Ensure `decrypted` is initialized
        for letter in encrypted:
            index = key.index(letter)
            decrypted += chars[index]
        print("Decrypted text:", decrypted)
        break
    elif decrypt == "n":  # Use `elif` to properly handle the "n" case
        break
    else:  # Catch invalid inputs
        print("Invalid input. Please enter 'Y' or 'N'.")
        continue


print(decrypted)



