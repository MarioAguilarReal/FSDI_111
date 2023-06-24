from flask import Flask             #from the flask module import the Flask class
# OOP


app = Flask(__name__)               #create an instance if flask into app ( now an object)

#variables that belong to a class are called "atributtes"
#functions that belong to a class are called "methods"

@app.get("/")                       #we noe have access to the object's methods (also a decorator)
def main():                         # A wrapped funciton is called a view fuction in flask.
    me = {
        "first_name": "Mario",
        "last_name": "Aguilar",
        "hobbies": "Go to the gym",
        "is_active": True
    }
    return me               #when we return a python dictionary from a view function
                            #flask will automatically convert it to JSON

