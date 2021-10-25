document.addEventListener('DOMContentLoaded', bindButtons);

function bindButtons() {
  document.getElementById('submit').addEventListener('click', function(event){
    let req = new XMLHttpRequest();
    let teams = {team_1_name: null, team_1_year: null, team_2_name: null, team_2_year: null};

    teams.team_1_name = document.getElementById('team_1_name').value;
    teams.team_1_year = document.getElementById('team_1_year').value;
    teams.team_2_name = document.getElementById('team_2_name').value;
    teams.team_2_year = document.getElementById('team_2_year').value;
    req.open('POST', '/compare?team1=' + teams.team_1_name + '&team1_year=' + teams.team_1_year +
            '&team2=' + teams.team_2_name + '&team2_year=' + teams.team_2_year);



req.addEventListener('load', function() {
  if (req.status >= 200 && req.status < 400) {
    let response = (JSON.parse(req.responseText));
    console.log(response);


    // make function?
    let wins_1 = document.createTextNode(response[0].wins);
    document.getElementById("wins_1").appendChild(wins_1);

    let losses_1 = document.createTextNode(response[0].losses);
    document.getElementById("losses_1").appendChild(losses_1);

    let ot_1 = document.createTextNode(response[0].ot);
    document.getElementById("ot_1").appendChild(ot_1);

    let pts_1 = document.createTextNode(response[0].pts);
    document.getElementById("pts_1").appendChild(pts_1);

    let goals_per_game_1 = document.createTextNode(response[0].goalsPerGame);
    document.getElementById("goals_per_game_1").appendChild(goals_per_game_1);

    let goals_against_per_game_1 = document.createTextNode(response[0].goalsAgainstPerGame);
    document.getElementById("goals_against_per_game_1").appendChild(goals_against_per_game_1);

    let power_play_percentage_1 = document.createTextNode(response[0].powerPlayPercentage);
    document.getElementById("power_play_percentage_1").appendChild(power_play_percentage_1);

    let penalty_kill_percentage_1 = document.createTextNode(response[0].penaltyKillPercentage);
    document.getElementById("penalty_kill_percentage_1").appendChild(penalty_kill_percentage_1);

    let shots_per_game_1 = document.createTextNode(response[0].shotsPerGame);
    document.getElementById("shots_per_game_1").appendChild(shots_per_game_1);

    let shots_allowed_per_game_1 = document.createTextNode(response[0].shotsAllowed);
    document.getElementById("shots_allowed_per_game_1").appendChild(shots_allowed_per_game_1);

     let save_percentage_1 = document.createTextNode(response[0].savePctg);
    document.getElementById("save_percentage_1").appendChild(save_percentage_1);


    // make function?
    let wins_2 = document.createTextNode(response[1].wins);
    document.getElementById("wins_2").appendChild(wins_2);

    let losses_2 = document.createTextNode(response[1].losses);
    document.getElementById("losses_2").appendChild(losses_2);

    let ot_2 = document.createTextNode(response[1].ot);
    document.getElementById("ot_2").appendChild(ot_2);

    let pts_2 = document.createTextNode(response[1].pts);
    document.getElementById("pts_2").appendChild(pts_2);

    let goals_per_game_2 = document.createTextNode(response[1].goalsPerGame);
    document.getElementById("goals_per_game_2").appendChild(goals_per_game_2);

    let goals_against_per_game_2 = document.createTextNode(response[1].goalsAgainstPerGame);
    document.getElementById("goals_against_per_game_2").appendChild(goals_against_per_game_2);

    let power_play_percentage_2 = document.createTextNode(response[1].powerPlayPercentage);
    document.getElementById("power_play_percentage_2").appendChild(power_play_percentage_2);

    let penalty_kill_percentage_2 = document.createTextNode(response[1].penaltyKillPercentage);
    document.getElementById("penalty_kill_percentage_2").appendChild(penalty_kill_percentage_2);

    let shots_per_game_2 = document.createTextNode(response[1].shotsPerGame);
    document.getElementById("shots_per_game_2").appendChild(shots_per_game_2);

    let shots_allowed_per_game_2 = document.createTextNode(response[1].shotsAllowed);
    document.getElementById("shots_allowed_per_game_2").appendChild(shots_allowed_per_game_2);

     let save_percentage_2 = document.createTextNode(response[1].savePctg);
    document.getElementById("save_percentage_2").appendChild(save_percentage_2);

    if (set_color(wins_1, wins_2) == 1){
      document.getElementById('wins_1').style.border = 'thick green';
      document.getElementById('wins_2').style.border = 'thick red';
    } else if (set_color(wins_1, wins_2) == 2) {
      document.getElementById('wins_2').style.border = 'thick green';
      document.getElementById('wins_1').style.border = 'thick red';
    }
    


  } else {
    console.log("Error " + req.statusText);
  }});
  req.send(null)
  event.preventDefault();
  })
}

function set_color(stat1, stat2) {
  if (stat1 > stat2){
    return 1;
  } else if (stat1 < stat2) {
    return 2;
  } else {
    return 0;
  }
}
