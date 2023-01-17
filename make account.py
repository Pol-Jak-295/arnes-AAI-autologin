#python 3.11, made by Pol_Jak_295
import customtkinter
import hashlib
import base64
import os
import time
from stat import(
    FILE_ATTRIBUTE_ARCHIVE as A,
    FILE_ATTRIBUTE_SYSTEM as S,
    FILE_ATTRIBUTE_HIDDEN as H,
    FILE_ATTRIBUTE_READONLY as R,
    FILE_ATTRIBUTE_NOT_CONTENT_INDEXED as I)

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("dark-blue") 
cwd = os.getcwd()
path = cwd + "\\accounts"

isExist = os.path.exists(path)
if not isExist:

  
   os.makedirs(path)

    
    
app = customtkinter.CTk()
app.geometry(f"{650}x{500}")
app.title("login")
global username_value
global password_value
global key_value

frame = customtkinter.CTkFrame(master=app,
                               width=800,
                               height=700,
                               corner_radius=10)
frame.pack(padx=20, pady=20)
textbox = customtkinter.CTkTextbox(master=frame,
                                   width=258,
                                   height=20,
                                   corner_radius=10,
                                   border_width=2,
                                   border_color='blue', 
                                   )
textbox.insert("0.0", "Welcome to autologin account creation.") 
text = textbox.get("0.0", "end") 

textbox.configure(state="disabled") 
textbox.pack(padx=10, pady=5)




username_entry = customtkinter.CTkEntry(master=frame,
                               
                               width=300,
                               height=35,
                               border_width=2,
                               corner_radius=8,
                               placeholder_text="username", 
                               placeholder_text_color='silver')

username_entry.place(relx=0.5, rely=0.5)
username_entry.pack(padx=20, pady=15)


password_entry = customtkinter.CTkEntry(master=frame,
                               placeholder_text="password",
                               width=300,
                               height=35,
                               border_width=2,
                               corner_radius=8,
                               text_color='silver',
                               show='*')
password_entry.place(relx=0.5, rely=0.5)
password_entry.pack(padx=20, pady=15)

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
def login(*args, **kwargs):
    password_value = password_entry.get()
    username_value = username_entry.get()
    key_value = key_entry.get()

    
    
   
   
   
    encrypted_key = hashlib.sha256(key_value.encode()).hexdigest()
   
    
    if "@" in username_value:
        name, domain = username_value.split("@")
    else:
        name = username_value
        domain = ""
    
    def encrypt(password_value, key_value):
        encoded_password = password_value.encode()
        encrypted_password = ''
        for i, character in enumerate(encoded_password):
            key_character = key_value[i % len(key_value)]
            encrypted_char = chr((character + ord(key_character)) % 256)
            encrypted_password += encrypted_char
        return base64.b64encode(encrypted_password.encode()).decode()
    encrypted_password = encrypt(password_value, key_value)
    
    path2 = (cwd + "\\accounts\\" + username_value)
   
    isExist = os.path.exists(path2)
    if not isExist:
      
            os.makedirs(path2)
    os.system('attrib +h +s ' + path)
    with open(cwd + "\\accounts\\" + username_value + "/name.txt", "w") as f:
        f.write(name)
    with open(cwd + "\\accounts\\" + username_value + "/domain.txt", "w") as f:
        f.write(domain)
        
    with open(cwd + "\\accounts\\" + username_value + "/password.txt", "w") as f:
        f.write(encrypted_password)
    with open (cwd + "\\accounts\\" + username_value + "/key.txt", "w") as f:
        f.write(encrypted_key)
    
        app.destroy()

button = customtkinter.CTkButton(master=frame,
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 corner_radius=8,
                                 text="Submit",
                                 command=lambda: login(),
                                 border_color='black')
button.place(relx=0.5, rely=0.7)
button.pack(padx=20, pady=50)
key_entry.bind('<Return>', command=login)
app.mainloop()
