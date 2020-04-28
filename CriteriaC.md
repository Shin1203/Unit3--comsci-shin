# Development

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




