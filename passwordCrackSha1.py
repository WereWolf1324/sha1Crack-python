import hashlib

def convertedSha1(text):
    digest = hashlib.sha1(text.encode()).hexdigest()
    return digest

userSha1 = input("Enter Your SHA1 encrypted password: ")
cleanedUserSha = userSha1.strip().lower()

found = False

with open("pass.txt", "r") as f:
    for line in f:
        password = line.strip()
        convertedUserSha1 = convertedSha1(password)
        if cleanedUserSha == convertedUserSha1:
            print(f"Password found: {password}")
            found = True
            break  # Stop looping once the password is found

if not found:
    print("Sorry, the password is not in the source file!")
