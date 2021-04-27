![image](./static/img/Logo.jpg)

## Table of Content
* [Description](#description)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)


# Description
Project with some ecommerce features:
- Product section.
- slides to show the main products.
- Products search bar.
- Categories for products.
- Admin options to add products, description, features, new providers, etc.

# Installation

1. Clone this repository `git clone https://github.com/ikki2530/huecostore25.git`
2. Access to huecostore25 `cd huecostore25`
3. Install dependencies `pip install -r requirements.txt`
4. Execute the command `python manage.py makemigrations`
5. Execute `python manage.py migrate`
6. Create the superuser `python manage.py createsuperuser`
7. Finally, run the server `python manage.py runserver`

## File Descriptions
[requirements.txt](requirements.txt) - The configuration file requirements.txt allows to install the specified packages (Django, gunicorn, pillow, etc) necessary for the development of the website.

[.gitignore](.gitignore) - Specifies intentionally untracked files to ignore.

[manage.py](manage.py) - Script to run administrative tasks









