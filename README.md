# Flask Blog

IP for MC18 week 4 of Python that requires creating a personal blogging website where you can create and share your opinions and other users can read and comment on them. Additionally, add a feature that displays random quotes to inspire your users.

#### By **Philip Kariuki**


## Description
This is a Flask web application that entails creating a blogging website where you can create and share your opinions and other users can read and comment on them. Additionally, it has a feature that displays random quotes to inspire users.

Live link : https://phillblog.herokuapp.com

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
| Display post title | N/A | List of post titles with the writer's name |
| See an entire post | Click on a post's title | Directed to a page with the post's title, writer's name and comments on the post |
| Comment on a post | Click Comment | Registered user is directed to a page with a form where the user can create and submit a comment on a post |
| Create a Post | Click Create Post | Registered user with a writer's role is directed to a page with a form where the user can create and submit a new post |
| Delete a comment | Click delete for the specific comment | An authenticated user with a writer's role deletes a comment |
| Delete a post | Click Delete Post | Registered user with a writer's role deletes a post and its comments |
| Update a post | Click Update Post | Registered user with a writer's role is directed to a page with a form where the user can update the post and submit it |


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
To support me, you can contact me at <a href="https://www.gmail.com">philippokar@hotmail.co.uk</a>

## License
[MIT © 2019](https://github.com/philipkariuki/flask-blog/blob/master/LICENSE)
