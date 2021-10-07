import requests
from team import *


def get_team_id(name, resp):
    """
    Gets the team ID from the name
    :param name: Name of team
    :param resp: JSON response from the NHL api
    :return: int ID
    """

    for key in resp['teams']:
        if key['name'] == name:
            print(f"Key value is {key['id']}")
            return key['id']

def get_team_object(ID, year):
    """
    Gets the team stats based on the ID
    :param ID: int Team ID
    :param year: str year in the form YYYYYYYY e.g (20102011)
    :return: JSON stats for given team and year
    """
    res = requests.get(f"https://statsapi.web.nhl.com/api/v1/teams/{ID}?expand=team.stats&season={year}")
    team = res.json()
    return get_team_stats(team)


def get_team_stats(resp):
    """
    Gets the season stats for a team from the JSON object
    :param resp: team JSON object
    :return:
    """
    return resp['teams'][0]['teamStats'][0]['splits'][0]['stat']


if __name__ == "__main__":

    URL = "https://statsapi.web.nhl.com/api/v1/teams"
    response = requests.get(URL)
    res = response.json()

    year = "1995-1996"                              # TODO: Get this from the GUI and covert it to 'YYYYYYYY'

    # Remove the - from the input or just make value of input = YYYYYYYY without -
    test = year.replace('-', '')
    print(test)

    team_1_name = "Colorado Avalanche"             # TODO: Get this from the GUI with the year
    team_1_ID = get_team_id(team_1_name, res)
    team_1_object = get_team_object(team_1_ID, "19951996")

    # create the team
    team_1 = Team(team_1_name, team_1_ID)

    # add stats to team object
    team_1.wins = team_1_object['wins']
    # print(f"{team_1.name} won {team_1.wins} games in the year {year}")