from flask import Flask, request
import requests
import json

def get_gifs(user_input):
    """
    Returns list of meta data about 10 gifs from Tenor API matching user_input
    """

    params = {
        "q": user_input,
        "Key": "F4742JEU9YNK", #api key came from tenor developer dashboard
        "limit": 10
    }

    response = requests.get("https://api.tenor.com/v1/search", params)

    button_pressed = request.args.get('button')

    if button_pressed == "currently_trending":
        params["q"] = None
        response = requests.get("https://api.tenor.com/v1/trending?", params)
        
    elif button_pressed == "completely_random":
        params["q"] = "random"
        response = requests.get("https://api.tenor.com/v1/random?", params)

    top_10gifs = json.loads(response.content)['results']

    return top_10gifs