def statistics_printer(class_name):
    if isinstance(class_name, (Goalie, Skater)):
        print("\n\n")
        for x in class_name.all_stats:
            print(x + ": " + str(class_name.all_stats[x]))
    else:
        print("restart")


class Skater(Employee):
    def __init__(self, position, goals, shots_on_goal, assists, penalty_minutes, games_played):
        super().__init__()
        self.position = position
        self.goals = goals
        self.shots_on_goal = shots_on_goal
        self.scoring_percentage = shots_on_goal
        self.assists = assists
        self.points = goals + assists
        self.penalty_minutes = penalty_minutes
        self.games_played = games_played
        self.all_stats = {"Name": self.name, "Position": self.position, "Age": self.age, "Salary": self.salary,
                          "Goals": self.goals, "Shots on Goal": self.shots_on_goal, "Scoring Percentage":
                          self.scoring_percentage, "Assists": self.assists, "Points": self.points,
                          "Penalty Minutes": self.penalty_minutes}


class Goalie(Employee):
    def __init__(self, shots_against, saves, shutouts, wins, losses):
        super().__init__()
        self.position = "Goalie"
        self.shots_against = shots_against
        self.saves = saves
        self.goals_against = shots_against - saves
        self.games_played = wins + losses
        self.shutouts = shutouts
        self.wins = wins
        self.losses = losses
        self.save_percentage = (saves / shots_against * 100)
        self.goals_against_average = (self.goals_against / self.games_played)
        self.win_percentage = (wins / self.games_played) * 100
        self.all_stats = {"Name": self.name, "Position": self.position, "Age": self.age, "Salary":
                          self.salary, "Shots Against": self.shots_against, "Goals Against": self.goals_against,
                          "Saves": self.saves, "Save Percentage": self.save_percentage,  "Wins": self.wins,
                          "Losses": self.losses, "Goals Against Average": self.goals_against_average,
                          "Winning Percentage": self.win_percentage, "Shutouts": self.shutouts}

