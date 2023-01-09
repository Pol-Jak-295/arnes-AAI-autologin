# arnes-AAI-autologin
Welcome to arnes AAI autologin

"make account.py" is a script that allows a user to create a new account by entering a username, password, and key. The script does the following:

(Before using this script make sure that the img folder containing the images of the login field is extracted into the same directory as the script)


1. 	Imports the Tkinter, hashlib, base64, and os libraries.
2.	Creates a new directory called "accounts" if it doesn't already exist.
3.	Creates a login window using Tkinter, with entry fields for the username, password, and key.
4.	Defines a login function that is triggered when the user clicks a button or hits the 'enter' key while the password entry field is focused. The login function does the following:
	4.1.	Gets the entered username, password, and key.
	4.2.	Hashes the key using the SHA-256 algorithm.
	4.3.	Splits the username into a name and domain if necessary.
	4.4.	Defines and calls a function that encrypts the password using the entered key.
	4.5.	If a directory with the entered username doesn't exist, creates it.
	4.6.	Saves the name, domain, encrypted password, and hashed key to separate files within the username directory.
	4.7.	Closes the main window.
5.	Creates a login button that triggers the login function when clicked.
6.	Runs the main loop for the main window.
"autologin.py" is a script that allows a user to log in to a previously created account by entering their key and selecting the corresponding account from a dropdown menu. The script does the following:

1.	Imports several libraries, including Tkinter, PyAutoGUI, Pyperclip, Pyscreeze, NumPy, and OpenCV.
2.	Defines a function called remove_special_characters that takes in a path and removes certain special characters from it.
3.	Defines a login function that is triggered when the user clicks a button or hits the 'enter' key while the key entry field is focused. The login function does the following:
	3.1.	Calls the remove_special_characters function on the selected account's path to remove special characters.
	3.2.	Gets the entered key and reads the key.txt file of the selected account.
	3.3.	Hashes the entered key using the SHA-256 algorithm and compares it to the key in key.txt.
	3.4.	If the hashed key matches the key in key.txt, the login function reads the name.txt, domain.txt, and password.txt files of the selected account and stores their contents as variables. The login function then closes the main window.
	3.5.	The login function then defines and calls a decrypt function that takes in the encoded password and key, decodes the encoded password, and iterates through each character, subtracting the corresponding character in the key (modulo 256) to create a new decrypted character. The decrypt function returns the decrypted password.
	3.6.	The login function then uses PyAutoGUI to locate and click on certain elements on the screen, enter the name, domain, and decrypted password, and confirm the login.
4.	Creates the main window using Tkinter, creates entry fields for the key and account dropdown menu, and creates a button that triggers the login function when clicked.
5.	Runs the main loop for the main window.



