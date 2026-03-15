# Create a strong code for password authentication using python. 

import bcrypt

def hash_password(plain_text_password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)

def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)

# 1. SIGN UP PHASE
print("ACCOUNT REGISTRATION")
user_password = input("Create a strong password: ")
stored_hash = hash_password(user_password)
print("Password hashed and saved successfully!\n")

# 2. LOGIN PHASE
print("USER LOGIN")
authenticated = False
attempts = 0
max_attempts = 3

while not authenticated and attempts < max_attempts:
    login_attempt = input(f"Enter your password (Attempt {attempts + 1}/{max_attempts}): ")
    
    if check_password(login_attempt, stored_hash):
        print("Login successful!")
        authenticated = True
    else:
        attempts += 1
        print("Invalid password.")

if not authenticated:
    print("\nAccess Denied: Too many failed attempts.")