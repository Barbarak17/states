# Barbara Karakyriakou
# CSCI E-50 Fall 2017
# Final Project
# December 06, 2017
# Title: State Capitals & Nicknames
# Type: Web Application using Python with Flask

## Description

The program is a web application that requires users to register and login in order to get access to a trivia library that contains
information about the Us state capitals and their nicknames.

## Usage

Open CS50 IDE and upload the "states" folder. Inside the folder you will find two subfolders, one with the name static that contains
two css files, and a templates folder that contains all the required html templates to run the program.

The states folder also contains two python files, application.py and helpers.py, which contain the algorithms required for the program to run.
In addition there is an SQLite file called states.db, which is meant for storing the users' data.

Finally there is a requirements text that contains the list of installed packages required for the program, as well this file that you
are reading, and a similar file called design that contains the technical specifications of the program.

In order to run the web application, in the workspase change the directory to states and type flask run on the terminal within the states directory.
Go to the browser. Register or login in the main page, and get redirected to the index page.

From the dropdown menu at the index page, select a state by its abbreviation. If unsure about the abbreviation of a state,
check the hint text next to the dropdown menu that contains the list of the 50 US states with their abbreviation codes.

After selecting a preferred state from the menu, click submit and get redirected to the page with the information of the capital and the
nickname of the relevant state along with a map of it.

When done, go to the bottom of the page and click home to go back to the home page with the dropdown menu and select a different state
if you wish. When finished go to the bottom of the homepage and logout.

## Register Details

To register, make sure that you enter a username and a password that contains alphanumeric digits with at least one uppercase letter and one number.
The length of the password must be at least 6 characters, and you must re-enter the password when registering.
Rest assure that your information is safe, as your password will be hashed to a random cryptic value, and you will be the only who knows it.
Therefore, make sure that you remember, or even better, take a note of your credentials.

-Thank you and I hope you enjoy!

Best,
Barbara
