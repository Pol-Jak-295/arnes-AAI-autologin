
import pyautogui, pyperclip, pyscreeze, numpy, cv2
import tkinter as tk
import base64
import hashlib 
import os


cwd = os.getcwd()


def remove_special_characters(path):
    characters_to_remove = ['(', ')', ',', "'"]
    new_path = ""
    for character in path:
        if character not in characters_to_remove:
            new_path += character
    return new_path


    # assign the return value of remove_special_characters to path

    # get the inputed key

        # close the window
def login(event = None):
    # get the selected user
    global path
    path = remove_special_characters(cwd  + '\\accounts\\' + account_var.get())
    
    # get the inputed key
    key = key_entry.get()
    
    # read the key.txt file of the selected user
    with open(path + '\\key.txt', 'r') as f:
        key_txt = f.read()

    # hash the inputed key
    hashed_key = hashlib.sha256(key.encode()).hexdigest()

    # check if the hashed inputed key matches the key in key.txt
    if hashed_key == key_txt:
        # save the inputed key as a variable
        global name
        global domain
        global encoded_password
        # read the name.txt and domain.txt files
        with open(path + '\\name.txt', 'r') as f:
            name = f.read()
        with open(path + '\\domain.txt', 'r') as f:
            domain = f.read()
        with open (path + '\\password.txt', 'r') as f:
            encoded_password = f.read()
        # close the window
        window.destroy()
        
        # Get the password
        def decrypt(encoded_password, key):
            encoded_password = base64.b64decode(encoded_password).decode()
            password = ''
            for i, character in enumerate(encoded_password):
                key_character = key[i % len(key)]
                decrypted_char = chr((ord(character) - ord(key_character)) % 256)
                password += decrypted_char
            return password
        password = decrypt(encoded_password, key)
    pyautogui.size()
    location = pyautogui.locateOnScreen(cwd + '\\img\\Screen loginfield.png', region=( 0, 0, 1920, 1080), grayscale = True, confidence = 0.5)
    pyautogui.move(location.left + 200, location.top + 280)
    pyautogui.sleep(0.1)
    pyautogui.click(location.left + 200, location.top + 290)
    pyautogui.write (name,0.03)
    pyperclip.copy('@')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.write(domain, 0.03)
    pyautogui.press('tab', 1, 0.2)
    pyautogui.write(password, 0.03)
    pyautogui.press('enter')
    pyautogui.sleep(1)
    location_c = pyautogui.locateOnScreen(cwd + '\\img\\Screen confirmations.png', region=( 0, 0, 1920, 1080), grayscale = True, confidence = 0.7 )
    pyautogui.move(location_c.left + 55, location_c.top + 285)
    pyautogui.sleep(0.1)
    pyautogui.click(location_c.left + 55, location_c.top + 285)
    pyautogui.move(location_c.left + 140, location_c.top + 370)
    pyautogui.sleep(0.1)
    pyautogui.click(location_c.left + 140, location_c.top + 370)
# Create the main window
window = tk.Tk()
window.title("Account Login")

# Use a larger font for the label and set the background color to light green
label = tk.Label(text="Select an account and enter the key:", font=("Arial", 16), bg="lightgreen")
label.pack()

# Use a different font for the dropdown menu and set the width to 20 characters
account_var = tk.StringVar(window)
account_menu = tk.OptionMenu(window, account_var, *os.listdir("accounts"))
account_menu.config(font=("Arial", 14), width=20)
account_menu.pack()
# Use a different font for the entry field and set the width to 20 characters
key_var = tk.StringVar(window)
key_entry = tk.Entry(window, textvariable=key_var, show="*", font=("Arial", 14), width=20)
key_entry.pack()

# Use a different font for the button and set the background color to light blue
submit_button = tk.Button(text="Submit", command=login, font=("Arial", 14), bg="lightblue")
submit_button.pack()

# Use a different font for the status label and set the background color to light yellow
status_var = tk.StringVar(window)
status_label = tk.Label(textvariable=status_var, font=("Arial", 14), bg="lightyellow")
status_label.pack()

# Set the focus to the key input box
key_entry.focus_set()

# Bind the Enter key to the login function
window.bind("<Return>", login)
username = account_var.get()

# Run the main loop
window.mainloop()
   
