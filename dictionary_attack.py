import hashlib

target_hash = input("Enter hash to crack: ")

wordlist = open("wordlist.txt", "r")

for word in wordlist:

    word = word.strip()

    hashed_word = hashlib.sha256(word.encode()).hexdigest()

    if hashed_word == target_hash:

        print("Password found:", word)
        exit()

print("Password not found in wordlist.")
