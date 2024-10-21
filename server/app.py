# import app instance and all routes
from . import app
from .routes import *

# run the app
if __name__ == '__main__':
    app.run(port=5555, debug=True)