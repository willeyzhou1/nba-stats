from flask import Flask
from bs4 import BeautifulSoup
import urllib.request
from data_functions.get_stats import get_stats

app = Flask(__name__)

@app.route("/")
def printMsg():
    return get_stats()

if __name__ == "__main__":
    app.run(debug=True)
