from flask import Flask, render_template, request
import requests
import json
from get_gifs import get_gifs

app = Flask(__name__)

'''
This is based off of reworking the tenor api resource, a great helper
(https://tenor.com/gifapi/documentation#quickstart-search)
'''

@app.route("/typeahead", methods=["POST"])
def typeahead():
    """
    When a post request is sent to /typeahead using ajax, gets 10 gifs from the 
    Tenor API matching search term and sends HTML from rendering gifs to client 
    """
    user_input = request.form["user_input"]

    #top_10gifs = get_gifs(user_input)

    params = {
        "q": user_input,
        "Key": "F4742JEU9YNK", #api key came from tenor developer dashboard
        "limit": 10
    }

    response = requests.get("https://api.tenor.com/v1/search", params)

    top_10gifs = json.loads(response.content)['results']

    return render_template("gifsblock.html", top_10gifs=top_10gifs)

@app.route('/')
def index():
    """
    Gets 10 gifs from Tenor API matching search term and returns HTML from 
    rendering gifs in page back to client
    """
    user_input = request.args.get('user_input')

    #top_10gifs = get_gifs(user_input)

    params = {
        "q": user_input,
        "Key": "F4742JEU9YNK", #api key came from tenor developer dashboard
        "limit": 10
    }

    button_pressed = request.args.get('button')

    response = requests.get("https://api.tenor.com/v1/search", params)

    if button_pressed == "trending":
        params["q"] = None
        response = requests.get("https://api.tenor.com/v1/trending?", params)
    elif button_pressed == "random":
        params["q"] = "random"
        response = requests.get("https://api.tenor.com/v1/random?", params)

    top_10gifs = json.loads(response.content)['results']

    return render_template("index.html", top_10gifs=top_10gifs)

if __name__ == '__main__':
    app.run(debug=True)
