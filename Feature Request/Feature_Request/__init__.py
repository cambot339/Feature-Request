"""
The flask application package.
"""

from flask import Flask
application = Flask(__name__)

import Feature_Request.views
