from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

# setting the apikey and limit
#this is based off of the tenor api (https://tenor.com/gifapi/documentation#quickstart-search)
apikey = "F4742JEU9YNK"  #test value - apikey came from tenor developer dashboard
lmt = 10

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract the query term from url using request.args.get()
    user_input = request.args.get('user_input')

    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    params = {
        "q": query_term,
        "Key": "F4742JEU9YNK",
        "limit": 10
    }

    # TODO: Make an API call to Tenor using the 'requests' library. For
    # reference on how to use Tenor, see:
    # https://tenor.com/gifapi/documentation

    # get the top 10 GIFs for the search term
    response = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s", params=params)

    if response.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_10gifs = json.loads(response.content)
        print(top_10gifs)
    else:
        top_10gifs = None

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

    return render_template("index.html", top_10gifs=top_10gifs, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
