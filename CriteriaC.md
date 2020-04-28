# Development

## Importing user interface into python, creating project.py
-To start coding the user interfaces created on Qtdesigner, I will have to import the .ui files as python files into my pycharm project.

-To do this, I saved the .ui interface files into the location of my pycharm project, then used the "pyuic5" command to convert them from .ui files to .py files.

-e.g ``pyuic5 mainmenu.ui -o mainmenu.py``

-project.py will act as the "main app", all interface .py files have been imported here.

-example code of importing a window : ``from loginmenu import Ui_Dialog as loginD``

-The main menu is not a dialog class, it is class Ui_MainWindow, and so the code reads ``from mainmenu import Ui_MainWindow as mainW``

## 
