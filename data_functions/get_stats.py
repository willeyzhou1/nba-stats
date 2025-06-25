from bs4 import BeautifulSoup
import urllib.request

def get_stats():
    try:
        url = "https://www.basketball-reference.com/leagues/NBA_2025_per_game.html"
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find("table", {'id': 'per_game_stats'})
        if not table:
            return "Table not found"

        return table.prettify()
    except Exception as e:
        return f"An error occurred: {e}"

