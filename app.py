from flask import Flask
from bs4 import BeautifulSoup
import urllib.request
from data_functions.get_stats import get_stats
from data_functions.get_points import get_points

app = Flask(__name__)

@app.route("/")
def print_stats():
    return get_stats()

@app.route("/points")
def print_points():
    return get_points()

if __name__ == "__main__":
    app.run(debug=True)
