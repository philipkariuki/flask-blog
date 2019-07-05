# Flask Blog

IP for MC18 week 4 of Python that requires creating a personal blogging website where you can create and share your opinions and other users can read and comment on them. Additionally, add a feature that displays random quotes to inspire your users.

#### By **Philip Kariuki**


## Description
This is a Flask web application that entails creating a blogging website where you can create and share your opinions and other users can read and comment on them. Additionally, it has a feature that displays random quotes to inspire users.

* Live link : https://pitchezzz.herokuapp.com

## User Stories
* As a user, I would like to view the blog posts on the site.
* As a user, I would like to comment on blog posts.
* As a user, I would like to view the most recent posts.
* As a user, I would like to an email alert when a new post is made by joining a subscription.
* As a user, I would like to see random quotes on the site.
* As a writer, I would like to sign in to the blog.
* As a writer, I would also like to create a blog from the application.
* As a writer, I would like to delete comments that I find insulting or degrading.
* As a writer, I would like to update or delete blogs I have created.

## Specifications
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
|Display Pre-set Pitch Categories | Loads on home page | Preset pitches categories are shown |
|Display posted pitches | Click on a Category| Page with a list of pitches from the chosen category |
|Add a new pitch | Click on **Write a new pitch** | Redirects to sign in page before user can add a new pitch |
|View a particular pitch | Click on a pitch | View a pitch and the comments made by registered users |
|Comment on a pitch | Click on Write a new comment | Registered User displays a form where a user can comment on a certain pitch |


## Setup/Installation Requirements
To clone this repo, open terminal in your desired folder then run:

        $ git clone https://github.com/philipkariuki/flask-blog/
        $ cd /flask-blog

To create and activate the virtual environment and install pip:

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python


To install all the required pip modules for proper functionality:

        (virtual)$ python3.6 -m pip install -r requirements.txt

To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

Alternatively:

        $ python3.6 manage.py server
        
To run unittests:

        $ python3.6 manage.py test

## Known Bugs

No known bugs

## Technologies Used

* HTML
* CSS
* Python3.6
* Pip
* Flask
* Bootstrap
* Postgres Database
* gunicorn


## Contributors
<a href="https://github.com/philipkariuki">philipkariuki</a>

## Support and contact details
To support me, you can contact me @<a href="https://www.gmail.com">philippokar@hotmail.co.uk</a>

## License
[MIT © 2019] [philipkariuki](https://github.com/philipkariuki/60-seconds/blob/master/LICENSE)
