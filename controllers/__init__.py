
# * Import flasks router
from flask import Blueprint

#############################################
# * USE THIS FILE TO DEFINE ANY Routes
# * Create Sub Blueprints as needed
#############################################

# * create the router
routes = Blueprint("home", __name__)

# * create landing route
@routes.get("/")
def home():
    return { "home": "this is the home route" }