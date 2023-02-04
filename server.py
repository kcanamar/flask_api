
# * Import flask
import flask
# * Import router
from controllers import routes

# * Flask ALL
# * Create Flask app
app = flask.Flask(__name__)

# * Mount the router
app.register_blueprint(routes)

# * Run Server
app.run(port=4000)