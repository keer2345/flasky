# Flasky
[The author's Github](https://github.com/miguelgrinberg/flasky)

This repository contains the source code examples for my O'Reilly book
 [Flask Web Development](http://www.flaskbook.com/).

The commits and tags in this repository were carefully created to match the sequence in which
concepts are presented in the book. Please read the section titled "How to Work with the 
Example Code" in the book's preface for instructions.

### Database Migration Example
```
python manage.py db init
python manage.py db migrate -m "login support"
python manage.py db upgrade
```
