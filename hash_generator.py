import hashlib

password = input("Enter password to hash: ")

hash_object = hashlib.sha256(password.encode())

print("SHA256 Hash:", hash_object.hexdigest())

