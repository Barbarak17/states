# Barbara Karakyriakou
# CSCI E-50 Fall 2017
# Final Project
# December 06, 2017
# Title: State Capitals & Nicknames
# Type: Web Application using Python with Flask

## Description

The program is a web application that requires users to register and login in order to get access to a trivia library that contains
information about the US state capitals and their nicknames.

## Specifications

The program was implemented usin python with flask. The main folder, states, contains two python files, application.py and helpers.py.

The application.py contains the functions to register, login, logout, back to homepage, as well as the main function that handles all
the html templates of each state and redirects users to the relevand landing pages. In addition there is a function to handle errors.

In the helpers.py there are two important supporting functions for the application.py, the login required function which decorates
the index and state function to require login, and the apology function, which redirects to a template whenever a user attempts a forbidden access.

Another important function included in application.py is a function that disables caching, the after_request(response) function, along
with the lines of code to manage configure sessions, and the db SQL statement referring to the users database.

The users data are stored in a phpLiteAdmin file, states.db, which contains a table named users with 3 rows, a primary key id parameter,
a unique username parameter, and a hash parameter to store cryptic password values.

There is a requirement text file with the list of imported libraries that were required, as well as a README.md file that contains
information on how to use of the program, and also this DESIGN.md file with the technical information.

The states module contains two subfolders, the templates and the static folders. In the static folders, there are two css files, style and style1.
The style.css is used to style the templates of the index, login, register, and apology. The style1.css is used to style the state templates.

There is a variety of CSS properties that have been used, either to position elements or to design them with different colors, borders, and shapes.
In most instances, IDs have been used to style unique elements, but also classes were used when there were multiple elements with the same style.
The reason that two different css files were use is that the body of the state pages is different from the index, login, register, and apology templates,
mainly because of a different cover image.

The templates folder contains 55 html files, where the 50 of them are the templates for each of the 50 US states.
The rest five templates are the index.html, layout.html, login.html, register.html, and apology.html.

The index.html is the home page that contains a fieldset with the dropdown menu and the submit button along with the hint, which is a list
of the 50 states with their abbreviations. Above this fieldset, there is the main title, and on the fieldset, there is a legend
that contains a short note of  instructions for the user. Underneath, there is another filedset that contains an image, which is the US flag,
positioned in the center. Down at the bottom there is a div element that holds the logout tab, and at the very bottom, a copyright note.

The layout.html template contains the skeleton for the login and register templates, and all these three templates have been
implemented using jinja. The login and register templates basically extend the layout template, by displaying forms that allow
the user to register or login.

Finally the apology template kicks in through the login and register functions from the application.py, whenever a user attempts
a forbidden action, such as an empty or wrong password etc. For the apology template, a custom image from memegen.link has been used.
At the bottom of it there are two divs that contain the links to redirect the user back to login or register. Finally the background
for this template has been designed same as the index, login, and register templates with the same title and the note at the bottom.

The code overall has been influenced by pset7 and pset8, but for the CSS and HMTL there has been quite a research mainly using W3schools.
I have also consulted github, flask.pocoo.org, jinja.pocoo.org, and I used memegen.link to create an apology.

The map images for the states have been researched and pulled by free online pictures, usind the appropriate links, and the design
of the titles and banners in the staet templates was made to match and coordinate the colors of the map images.

Finally, the book of Allen B. Downey, Think Python, 2nd edition, has been used for the better understanding and use of the appropriate python code.
