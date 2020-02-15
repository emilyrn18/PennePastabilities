from flask import Flask
import requests
from flask import session, request
from flask import render_template


app = Flask('hello')
@app.route('/')
def get_recipes():
    params = ["penne"]
    app_id = "8a7451e2"
    app_key = "842fccb336c3a63726031f666fcc69ba"

    param_string = ('&').join(params)

    payload = {'app_id': app_id,
               'app_key': app_key,
               'q': param_string,
               'to': 10}

    r = requests.get(
        "https://api.edamam.com/search",
        params=payload)
    edamam = r.json()
    recipes = edamam["hits"]

    for recipe in recipes:
        name = recipe["recipe"]["label"]
        image = recipe["recipe"]["image"]
        url = recipe["recipe"]["url"]
        ingredients = recipe["recipe"]["ingredientLines"]

    return render_template('your_view.html', your_list=recipes)
