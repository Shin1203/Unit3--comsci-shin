# Development
## login menu flowchart
![flowchart](loginflowchart.png)
## Importing user interface into python, creating project.py
-To start coding the user interfaces created on Qtdesigner, I will have to import the .ui files as python files into my pycharm project.

-To do this, I saved the .ui interface files into the location of my pycharm project, then used the "pyuic5" command to convert them from .ui files to .py files.

-e.g ``pyuic5 mainmenu.ui -o mainmenu.py``

-project.py will act as the "main app", all interface .py files have been imported here.

-example code of importing a window : ``from loginmenu import Ui_Dialog as loginD``

-The main menu is not a dialog class, it is class Ui_MainWindow, and so the code reads ``from mainmenu import Ui_MainWindow as mainW``



## Adding functionality of buttons.
-To add functionality of a button, two steps must be taken.

-Step one, under the window where the button is located, attach a function to when the button is clicked-e.g``self.buttonName.clicked.connect(functionName)``

-Step two, define the function connected to the button, this is where the functionality of the button will be.

-Whenever the button is pressed, the function will be called and carry out the process.

-As an example, the code for the "exit" button looks like this
```
# under class window, after __init__
  self.exit_button.clicked.connect(self.exitApp)
def exitApp(self):
  sys.exit(0)
```

## Reading text inputs from user.
-Reading text inputs from the user is a very simple process.

-To do so, make a variable which equals the input textbox.

-e.g ``email = self.email.input``
 

## Function Hash_Password
What is hash?
A hash function will take an input value and create a different output value. A hash function will always output the same number of digits, an input will always provide the same output. Hash functions can be used to encrypt then decrypt data. In my case, I will be using it to store password information.

### Coding a hash function
-This function will take a password as an argument, and hash it.

-The first step is to create a salt, which is an additional input that will go together with the password to get hashed. The salt provides extra security against attacks, this will allow for the same inputs to have a different output with different salts. First, 60 bytes of random infromation is created by a random function. Then, that 60 bytes of information is hashed using SHA-256 into 64 bytes of information. Finally, that 64 bytes of information is converted into characters of the ASCII alphabet, every byte becoming one ASCII character and creating a total of 64 ASCII characters as the string salt.

-The second step is to hash the entered password, with the salt. A function is used, that will intake the hash function,the entered password, previously generated salt, and the number of randomizations. SHA512 will be used to hash the password and salt, as it is safe. Utf-8 will be used to encode the entered password, as ASCII can only represent 256 characters, while utf-8 is capable of using any character.

-Thirdly, the hash value created with the password and the salt are converted into hexadecimal 

-Finally the earlier salt value is added with the hashed password value, and decoded into ASCII to be stored, and the process is complete.

-Below is the code
```
def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
    pwdhash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode("ascii")


```

## verifying a password
-To verify an entered passwords with a stored password, there are three steps

-First, the stored password must be retrieved, From this the salt(First 64th elements) and the password(Everything else) are seperated.

-Secondly, the entered password is hashed in the same process using the salt retrieved from the stored password.

-Finally, if the resulting hashed password is the same as the stored password(remember to seperate stored salt from password), then return True- the password is correct.

-Below is the code
```
def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:-1]
    pwdhash = hashlib.pbkdf2_hmac("sha512", provided_password.encode("utf-8"), salt.encode("ascii"), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode("ascii")
    return pwdhash == stored_password

```


## Storing Register User information.
-A function will be created to store registration information

-When "register" button is pressed, and user information is entered, email and password are hashed with the hashpassword function and stored in a textfile.

-This textfile is called "Password.txt" and stores the hashed email+password row by row.

-Code is below
```
    def store(self):
        email = self.email_in.text()
        password = self.regpassword_in.text()
        print("Hashing", email + password)
        msg = hash_password(email + password)
        with open("Password.txt", "a") as password_file:
            password_file.write("{}\n".format(msg))
        self.close()
```

## Try_login function
-This function is used for logging in, and is triggered when user enters email and password and clicks the "login" button on the login menu.

-First, the password entered in the text box will be stored as "enteredpass"

-Second, the "Password.txt" file will be opened as "passwordfile"

-Third, a for loop iterates through every row of the passwordfile, this means the loop will run for every stored password.

-With every iteration of the for loop, the function "verify_password" will be called with the stored password and entered password as arguments. 

-If the verify password function returns true, the for loop will break and the login menu will close- the login was succesful

-If the verify password function does not return true for any of the stored passwords, the login menu will remain up, and error message will be displayed.

**I ran into a problem while coding this section- the function verify_password, when called within the try_login function would crash the program with no error message. **

**Solution**
-The try function was crashing simply because of a syntax error, was missing an ".text" after textbox widget.
-The function now works, the program will self.close() if the function ``verify_password(row, enteredpass)`` returns true, otherwise it will print an error message.
-Code is below.
```
  def try_login(self):
        enteredpass = (self.username_in.text()+self.password_in.text())
        with open("Password.txt") as passwordfile:
            for row in passwordfile:
                if verify_password(row, enteredpass) is True:
                    print("success")
                    self.close()
                else:
                    print("error")
```

## Save button
-When the user edits a textbox in the tablewidget, they can click a "save" button and implement changes to table to the databse csv file.

-First, the "save" button is disabled in qtdesigner. When the information in the table is changed, the button property .setDisabled() is changed to False, activating the button.

-When the button is pressed, the function save() is called.

-The save() function will take text in the selected table cell, and append the text into the appropriate place in the csv file.

-The text of the current cell is extracted with .currentItem().text()

**An issue occured when trying to save this text into the csv file. .append or .write does not normally work with csv files, and I am having trouble finding a way to "edit" a csv file to save the information. I have tried utilizing csv writer but have so far failed in implementing.**

## Revert button
-This button is the opposite of the save button, it will reload information from the csv file into the table.

-Same with the save button, the button is disabled until the table is edited.

-To make it revert changes made to the table, I simply call the data_load function

-The code is below
```
 def revert(self):
        self.load_data()
```
