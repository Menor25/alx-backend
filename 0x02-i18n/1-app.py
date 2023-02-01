#!/usr/bin/env python3
"""instantiate the Babel object"""

from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Class to configure available languages."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


app.route("/")
def index():
    """View function for route /."""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)