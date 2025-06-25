from bs4 import BeautifulSoup
import urllib.request

def get_points():
    try:
        url = "https://www.basketball-reference.com/leagues/NBA_2025_per_game.html"
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')

        points_table = soup.find_all("td", {"data-stat": "pts_per_g"})
        players_table = soup.find_all("td", {"data-stat": "name_display"})

        if not points_table:
            return "Table not found"
        if not players_table:
            return "Players not found"
        to_return = ""
        for i in range(0, max(len(points_table), len(players_table))):
            to_return += players_table[i].prettify() + "'s points: " + points_table[i].prettify() + '<br/>'
        return to_return
        
    except Exception as e:
        return f"An error occurred: {e}"