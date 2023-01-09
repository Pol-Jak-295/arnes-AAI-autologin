import tkinter as tk
import hashlib
import base64
import os
cwd = os.getcwd()
path = cwd + "\\accounts"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:

   # Create a new directory because it does not exist
   os.makedirs(path)



# Create the main window
window = tk.Tk()
window.title("Login")

# Create the username and password labels
tk.Label(window, text="Username:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
tk.Label(window, text="Password:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10)
tk.Label(window, text="key:", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=10)
# Create the username and password entry fields
username_entry = tk.Entry(window, font=("Arial", 14))
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_entry = tk.Entry(window, show="*", font=("Arial", 14))
password_entry.grid(row=1, column=1, padx=10, pady=10)
key_entry = tk.Entry(window, show="*", font=("Arial", 14))
key_entry.grid(row=2, column=1, padx=10, pady=10)
# Create the login function
def login():
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()
    key = key_entry.get()
    encrypted_key = hashlib.sha256(key.encode()).hexdigest()
    # Split the username into name and domain if necessary
    if "@" in username:
        name, domain = username.split("@")
    else:
        name = username
        domain = ""

    def encrypt(password, key):
        encoded_password = password.encode()
        encrypted_password = ''
        for i, character in enumerate(encoded_password):
            key_character = key[i % len(key)]
            encrypted_char = chr((character + ord(key_character)) % 256)
            encrypted_password += encrypted_char
        return base64.b64encode(encrypted_password.encode()).decode()
    encrypted_password = encrypt(password, key)
    

    path2 = ("accounts/" + username)
    # Check whether the specified path exists or not
    isExist = os.path.exists(path2)
    if not isExist:
       # Create a new directory because it does not exist
        os.makedirs(path2)
    # Save the name, domain, and password hash to separate files
    with open("accounts/" + username + "/name.txt", "w") as f:
        f.write(name)
    with open("accounts/" + username + "/domain.txt", "w") as f:
        f.write(domain)
    with open("accounts/" + username + "/password.txt", "w") as f:
        f.write(encrypted_password)
    with open ("accounts/" + username + "/key.txt", "w") as f:
        f.write(encrypted_key)
    # Destroy the main window
    window.destroy()

# Create the login button
login_button = tk.Button(window, text="Login", font=("Arial", 14), command=login)
login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Add some padding around the login button
login_button.config(pady=10)

# Set the background color of the main window
window.configure(bg="#482875")

# Run the main loop
window.mainloop()