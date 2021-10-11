from flask import Flask, render_template, url_for, request, jsonify

import nhl
from nhl import *

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/compare', methods=['GET'])
def handle_data():
    data = request.args
    print(data)
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

    print(team_1_obj)
    print(team_2_obj)



    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)