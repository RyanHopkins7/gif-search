from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

'''
This is based off of reworking the tenor api resource, a great helper
(https://tenor.com/gifapi/documentation#quickstart-search)
'''

@app.route("/typeahead", methods=["POST"])
def typeahead():
    user_input = request.form["user_input"]

    print(user_input)

    return "Hello from the server!" + user_input

@app.route('/')
def index():
    """Return homepage."""
    user_input = request.args.get('user_input')
        
    params = {
        "q": user_input,
        "Key": "F4742JEU9YNK", #api key came from tenor developer dashboard
        "limit": 10
    }

    response = requests.get("https://api.tenor.com/v1/search", params)

    top_10gifs = json.loads(response.content)['results']

    return render_template("index.html", top_10gifs=top_10gifs)

if __name__ == '__main__':
    app.run(debug=True)
