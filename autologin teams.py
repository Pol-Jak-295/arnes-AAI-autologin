
import pyautogui, pyperclip, pyscreeze, numpy, cv2

import base64
import hashlib 
import os
import customtkinter

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
        app.destroy()
        
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
    location_c = pyautogui.locateOnScreen(cwd + '\\img\\Screen confirmations.png', region=( 0, 0, 1920, 1080), grayscale = True, confidence = 0.5)
    pyautogui.move(location_c.left + 140, location_c.top + 370)
    pyautogui.sleep(0.1)
    pyautogui.click(location_c.left + 140, location_c.top + 370)
# Create the main window
app = customtkinter.CTk()
app.title("Account Login")

frame = customtkinter.CTkFrame(master=app,
                               width=200,
                               height=200,
                               corner_radius=10)
frame.pack(padx=20, pady=20)

textbox = customtkinter.CTkTextbox(master=frame,
                                   width=300,
                                   height=20,
                                   corner_radius=10,
                                   border_width=2,
                                   border_color='blue', 
                                   )
textbox.insert("0.0", "Welcome to the arnes AAI autologin script by Pol_Jak_295")  # insert at line 0 character 0
text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

textbox.configure(state="disabled")  # configure textbox to be read-only
textbox.pack(padx=10, pady=5)
account_var = customtkinter.StringVar(value="choose user")  # set initial value

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = customtkinter.CTkComboBox(master=frame,
                                     values=os.listdir("accounts"),
                                     command=optionmenu_callback,
                                     variable=account_var)
combobox.pack(padx=20, pady=10)
# Use a larger font for the label and set the background color to light green

username = account_var.get()

# Use a different font for the dropdown menu and set the width to 20 characters
# Use a different font for the entry field and set the width to 20 characters
key_var = customtkinter.StringVar(app)
key_entry = customtkinter.CTkEntry(master=frame,
                               placeholder_text='key',
                               width=300,
                               height=35,
                               border_width=2,
                               corner_radius=8,
                               text_color='silver',
                               show='*')
key_entry.place(relx=0.5, rely=0.5)
key_entry.pack(padx=20, pady=15)
# Use a different font for the button and set the background color to light blue
button = customtkinter.CTkButton(master=frame,
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 corner_radius=8,
                                 text="login",
                                 command=lambda: login(),
                                 border_color='black')
button.place(relx=0.5, rely=0.7)
button.pack(padx=20, pady=50)
# Use a different font for the status label and set the background color to light yellow


# Run the main loop
app.mainloop()
   
