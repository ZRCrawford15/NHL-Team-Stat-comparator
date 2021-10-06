class Team:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.wins = None
        self.losses = None
        self.OT = None
        self.pts = None
        self.goal_per_game = None
        self.goals_against_per_game = None
        self.power_play_percentage = None
        self.penalty_kill_percentage = None
        self.shots_per_game = None
        self.shots_allowed_per_game = None
        self.save_percentage = None

        print(f"New team created named {self.name} with ID of {self.ID}")

