import random
import string

chars=" "+string.punctuation+string.digits+string.ascii_letters



chars=list(chars)
key=chars.copy()

random.shuffle(key)



print(f"chars:{chars}")
print(f"key:{key}")


#Encription

plain_text=input("Enter a message to encrypt:")
cipher_text=""


for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]

print(f"Original message:{plain_text}")
print(f"Encrypted message:{cipher_text}")

#Dcription

cipher_text2=input("Enter a message to encrypt:")
plain_text2=""


for letter in cipher_text2:
    index=key.index(letter)
    plain_text2+=chars[index]

print(f"Encrypted message:{cipher_text}")
print(f"Original message:{plain_text}")
