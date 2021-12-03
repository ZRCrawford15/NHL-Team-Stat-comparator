import requests, send, json


def get_team_id(name, resp):
    """
    Gets the team ID from the name
    :param name: Name of team
    :param resp: JSON response from the NHL api
    :return: int ID
    """

    for key in resp['teams']:
        if key['name'] == name:
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


# TODO: Add awards section
def get_team_awards(ID, year):
    return


def get_team_stats(resp):
    """
    Gets the season stats for a team from the JSON object
    :param resp: team JSON object
    :return:
    """
    # TODO: Check for valid input
    return resp['teams'][0]['teamStats'][0]['splits'][0]['stat']


def get_team_picture(team):
    # Removes French spelling for wikipedia
    if team == "Montréal Canadiens":
        team = "Montreal Canadiens"

    new_name = team.replace(" ", "_")
    wiki_client = send.WikiClient()
    url_link = wiki_client.retrieve_image_url(new_name)
    return url_link
