from flask import Flask, request             #from the flask module import the Flask class
# OOP
app = Flask(__name__)               #create an instance if flask into app ( now an object)
USERS = []


#variables that belong to a class are called "atributtes"
#functions that belong to a class are called "methods"


@app.get("/users/<int:user_id>")        #with url parameter
@app.get("/<user_id>")                       #we noe have access to the object's methods (also a decorator)
def main(user_id):
    me = {}
    not_found = True
    if user_id == 1:                       # A wrapped funciton is called a view fuction in flask.
        not_found = False
        me = {
            "first_name": "Mario",
            "last_name": "Aguilar",
            "hobbies": "Go to the gym",
            "is_active": True
        }
    if not_found:
        return me, 404
    return me               #when we return a python dictionary from a view function
                            #flask will automatically convert it to JSON


@app.get("/users/")
def get_users():
    return USERS


@app.post("/users/")
def create_user():
    raw_data = request.json
    USERS.append(raw_data)
    return 201, {"message": "created"}




#REST
#Achitectural guide for building network connected API's
"""Representational State Transfer"""

#Endponts are named after the resource they manage, but in plural noun form.
"""Examples:
/users
/pets
/products

They help us support CRUD(S) opretions
-Create ->POST
-Read -> GET (intended to retrieve a single resource)
-Update -> PUT/PATCH
-Delete -> DELETE
-(Scan) -> GET (intendet to retrieve multiple resources)
"""
