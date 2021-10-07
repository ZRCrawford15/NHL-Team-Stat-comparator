class Team:
    def __init__(self, name, ID):
        self._name = name
        self._ID = ID
        self._wins = None
        self._losses = None
        self._OT = None
        self._pts = None
        self._goal_per_game = None
        self._goals_against_per_game = None
        self._power_play_percentage = None
        self._penalty_kill_percentage = None
        self._shots_per_game = None
        self._shots_allowed_per_game = None
        self._save_percentage = None

        print(f"New team created named {self._name} with ID of {self._ID}")

    def get_id(self):
        return self._ID

    def get_name(self):
        return self._name

    def get_wins(self):
        return self._wins

    def set_wins(self, wins):
        self._wins = wins

    def get_losses(self):
        return self._losses

    def set_losses(self, losses):
        self._losses = losses

    def get_ot(self):
        return self._OT

    def set_ot(self, OT):
        self._OT = OT

    def get_pts(self):
        return self._pts

    def set_pts(self, pts):
        self._pts = pts

    def get_goal_per_game(self):
        return self._goal_per_game

    def set_goal_per_game(self, goals_per_game):
        self._goal_per_game = goals_per_game

    def get_goals_against_per_game(self):
        return self._goals_against_per_game

    def set_goals_against_per_game(self, goals_against_per_game):
        self._goals_against_per_game = goals_against_per_game

    def get_power_play_percentage(self):
        return self._power_play_percentage

    def set_power_play_percentage(self, set_power_play_percentage):
        self._power_play_percentage = set_power_play_percentage

    def get_penalty_kill_percentage(self):
        return self._penalty_kill_percentage

    def set_penalty_kill_percentage(self, penalty_kill_percentage):
        self._penalty_kill_percentage = penalty_kill_percentage

    def get_shots_per_game(self):
        return self._shots_per_game

    def set_shots_per_game(self, shots_per_game):
        self._shots_per_game = shots_per_game

    def get_shots_allowed_per_game(self):
        return self._shots_allowed_per_game

    def set_shots_allowed_per_game(self, shots_allowed_per_game):
        self._shots_allowed_per_game = shots_allowed_per_game

    def get_save_percentage(self):
        return self._save_percentage

    def set_save_percentage(self, save_percentage):
        self._save_percentage = save_percentage
