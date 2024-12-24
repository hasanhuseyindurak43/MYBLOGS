"""
This file contains the routes for the Flask application.

The Blueprint "index" is used to define the home page of the application.
The route "/" maps the index function to the home page.

The index function retrieves all posts from the database and passes them to the index.html.jinja template.

The posts variable is passed to the index.html.jinja template as a list of dictionaries.

The index.html.jinja template displays the title and content of each post.
"""

from modules import (
    Log,  # A class for logging messages
    load,  # A function for loading JSON data from files
    session,  # A session object for storing user session data
    sqlite3,  # Importing the SQLite module for working with SQLite databases
    redirect,  # Importing the redirect function for redirecting requests
    Blueprint,  # Importing the Blueprint class for creating Flask blueprints
    DB_URL_ROOT,  # Importing the constant for the path to the posts database
    render_template,  # Importing the render_template function for rendering Jinja templates
)

import random

# Create a blueprint for the home page with the name "index" and the current module name
urlBlueprint = Blueprint("rastgele_url", __name__)

# Rastgele URL yönlendirme fonksiyonu
@urlBlueprint.route("/randomurl")
def random_url():
    connection = sqlite3.connect(DB_URL_ROOT)
    cursor = connection.cursor()

    # Tüm URL'leri getir
    cursor.execute("SELECT url FROM urls")
    urls = cursor.fetchall()

    connection.close()

    if urls:
        # Rastgele bir URL seç
        random_url = random.choice(urls)[0]
        return redirect(random_url)
    else:
        return "No URLs available in the database", 404
