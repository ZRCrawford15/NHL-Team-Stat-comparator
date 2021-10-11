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


# def parse_year(year):
#     filtered_year = year
#     dash = '-'
#     for char in dash:
#         filtered_year = filtered_year.replace(char, '')
#     return filtered_year


if __name__ == "__main__":

    URL = "https://statsapi.web.nhl.com/api/v1/teams"
    response = requests.get(URL)
    res = response.json()

    year = "2000-2001"                              # TODO: Get this from the GUI and covert it to 'YYYYYYYY'

    # Remove the - from the input or just make value of input = YYYYYYYY without -
    test = year.replace('-', '')
    # print(test)

    team_1_name = "Colorado Avalanche"             # TODO: Get this from the GUI with the year

    # 1) Get the team ID
    team_1_ID = get_team_id(team_1_name, res)

    # 2) Get the team object for the year
    team_1_object = get_team_object(team_1_ID, "20002001")

    # 3) create the team
    team_1 = Team(team_1_name, team_1_ID)

    # 4) add stats to team from the team object
    team_1.set_wins(team_1_object['wins'])


    print(f"{team_1.get_name()} won {team_1.get_wins()} games in the year {year}")