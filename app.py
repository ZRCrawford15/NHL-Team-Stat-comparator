from flask import Flask, render_template, url_for, request, jsonify
from flask_cors import CORS, cross_origin

import nhl
from nhl import *

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['SECRET_KEY'] = 'thecodex '

# List of teams for reference
# TEAMS = ("Anaheim Ducks", "Arizona Coyotes", "Boston Bruins", "Buffalo Sabres", "Calgary Flames", "Carolina Hurricanes", "Chicago Blackhawks", "Colorado Avalanche",
#          "Columbus Blue Jackets", "Dallas Stars", "Detroit Red Wings", "Edmonton Oilers", "Florida Panthers",
#          "Los Angeles Kings", "Minnesota Wild", "Montreal Canadians", "Nashville Predators", "New Jersey Devils",
#          "New York Islanders", "New York Rangers", "Ottawa Senators", "Philadelphia Flyers", "Pittsburgh Penguins",
#          "San Jose Sharks", "St. Louis Blues", "Tampa Bay Lightning", "Toronto Maple Leafs", "Vancouver Canucks",
#          "Vegas Golden Knights", "Washington Capitals", "Winnipeg Jets")



@app.route('/', methods=['GET'])
def index():

    return render_template('nhl.html')


@app.route('/picture', methods=['POST'])
def get_picture():

    url_arr = []

    data = request.args
    team_1_name = data['team1']
    team_2_name = data['team2']

    team_1_picture = nhl.get_team_picture(team_1_name)
    team_2_picture = nhl.get_team_picture(team_2_name)

    url_arr.append(team_1_picture)
    url_arr.append(team_2_picture)

    return url_arr



@app.route('/compare', methods=['POST'])
def handle_data():

    team_1_picture = {}
    team_2_picture = {}

    data = request.args
    team_1 = data['team1']
    team_2 = data['team2']
    team_1_year = data['team1_year']
    team_2_year = data['team2_year']

    team_1_year_parsed = ''
    for char in team_1_year:
        if char != '-':
            team_1_year_parsed += char

    team_2_year_parsed = ''
    for char in team_2_year:
        if char != '-':
            team_2_year_parsed += char


    URL = "https://statsapi.web.nhl.com/api/v1/teams"
    response = requests.get(URL)
    res = response.json()


    team_1_ID = nhl.get_team_id(team_1, res)

    team_2_ID = nhl.get_team_id(team_2, res)

    team_1_obj = nhl.get_team_object(team_1_ID, team_1_year_parsed)
    team_2_obj = nhl.get_team_object(team_2_ID, team_2_year_parsed)


    team_1_picture['team_1_picture'] = nhl.get_team_picture(team_1)
    team_2_picture['team_2_picture'] = nhl.get_team_picture(team_2)


    return jsonify(team_1_obj, team_2_obj, team_1_picture, team_2_picture)


if __name__ == '__main__':
    app.run(debug=True)