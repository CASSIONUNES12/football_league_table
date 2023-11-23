class Teams:
    def __init__(self, team_data): 
        self.team_data = team_data

# Cria um dicionário com os nomes dos times
teams_dict = {
    #MP: MATCHES PLAYED; PTS: POINTS; W: WINS; D: DRAWS; L: LOSSES; GS: GOALS SCORED; GC: GOALS CONCEDED; GD: GOALS DIFFERENCE   
                                                                                                        
    "mil": {"name": "AC Milan","MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0}, 

    "rom": {"name": "AS Roma", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "ata": {"name": "Atalanta", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "bol": {"name": "Bologna", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "bre": {"name": "Brescia", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "chi": {"name": "Chievo Verona", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "emp": {"name": "Empoli", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "int": {"name": "Inter Milan", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "juve": {"name": "Juventus", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "laz": {"name": "Lazio", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "mod": {"name": "Modena", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "par": {"name": "Parma", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "per": {"name": "Perugia", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "pia": {"name": "Piacenza", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "reg": {"name": "Reggina", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "com": {"name": "Calcio Como", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},

    "tor": {"name": "Torino", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0},
    
    "udi": {"name": "Udinese", "MP": 0, "PTS": 0, "W": 0, "D": 0, "L": 0, "GS": 0, "GC" : 0, "GD" : 0}
}

# Criar instância da classe Teams passando o dicionário
teams_instance = Teams(teams_dict)


class Matches:
    def __init__(self):
        self.fixtures = 0 
        self.max_rounds = 34 
        self.fixture = {}  # Stores all round games
        self.matches_rounds = []  # Displays the list of games in the shell as they are entered by the user
        self.played_teams = set()  # Stores teams that have played to avoid duplicates in the same round
        self.played_teams_list = []  # Used to check and control the last added teams for match removal
        self.played_matches = set()  # List of played matches to prevent duplicate matchups
        self.played_matches_list = []  # Stores the last added matches in insertion order for match removal
        self.removed_teams = set()  # Teams removed from played matches are added here

        
    # Method used to remove the last entered match after the user presses 'e'
    def remove_last_match(self):
        if self.matches_rounds: 
            self.matches_rounds.pop()  # Removes the last inserted match
            self.last_team = self.played_teams_list.pop()  # Identifies and removes the last home team entered by the user for possible statistic removal
            self.second_last_team = self.played_teams_list.pop()  # Identifies and removes the last away team entered by the user for possible statistic removal
            rem_match = self.played_matches_list.pop()  # Variable to remove the last inserted tuple containing the last match
            self.removed_teams.add((self.second_last_team, self.last_team))  # Adds both teams of the last match for statistic reversal handling
            self.played_matches.discard(rem_match)  
            self.played_teams.discard(self.last_team)
            self.played_teams.discard(self.second_last_team)

            # Methods that reverse the inserted statistics of the two removed teams from the last match to their state before addition
            table_live_update.reverse_goals_scored(self.second_last_team, self.homegoals, self.last_team, self.awaygoals)
            table_live_update.reverse_goals_conceded(self.second_last_team, self.homegoals, self.last_team, self.awaygoals)
            table_live_update.reverse_wins_draws_losses(self.second_last_team, self.homegoals, self.last_team, self.awaygoals)
            table_live_update.reverse_points(self.second_last_team, self.homegoals, self.last_team, self.awaygoals)
            table_live_update.reverse_goals_difference(self.second_last_team, self.homegoals, self.last_team, self.awaygoals)
            table_live_update.reverse_total_matches(self.second_last_team, self.last_team)  
        
       
    def home_vs_away(self):
     # Method for user inputs, including teams, goals, and the option to delete the last entered match 
        self.hometeam = input("\nType Home Team or press the key 'E' to erase the last match: ").lower()
        if self.hometeam.lower() == 'e':
            self.remove_last_match()
            print("\nLast match has succecssfully removed.")
            print(self.matches_rounds)
            print(self.played_matches_list)
            table_live_update.display_table()
        print(teams_instance.team_data[self.hometeam]['name'])
        self.homegoals = int(input("\nType Home Goals: "))
        self.awayteam = input("\nType Away Team: ").lower()
        print(teams_instance.team_data[self.awayteam]['name'])
        self.awaygoals = int(input("\nType Away Goals: "))
        self.duel = f"{teams_dict[self.hometeam] ['name']} {self.homegoals}  x  {self.awaygoals} {teams_dict[self.awayteam] ['name']}"
            
    def play_round(self):
        while self.fixtures < self.max_rounds: 
            valid_input = False
            try:
                while not valid_input:
                    self.home_vs_away() 
                    if self.hometeam in teams_dict and self.awayteam in teams_dict and self.awayteam != self.hometeam or self.hometeam == 'e':
                        if (
                            self.hometeam not in self.played_teams and self.awayteam not in self.played_teams
                            and (self.hometeam, self.awayteam) not in self.played_matches
                            ):
                            self.played_matches.add((self.hometeam, self.awayteam))
                            if self.played_matches:
                                self.played_matches_list.append((self.hometeam, self.awayteam))
                            self.played_teams.add(self.hometeam)
                            self.played_teams.add(self.awayteam)
                            self.matches_rounds.append(self.duel)
                            print(self.matches_rounds)
                            if self.played_teams:
                                self.played_teams_list.append(self.hometeam)
                                self.played_teams_list.append(self.awayteam)
                            table_live_update.goals_scored(self.hometeam, self.homegoals, self.awayteam, self.awaygoals)
                            table_live_update.goals_conceded(self.hometeam, self.homegoals, self.awayteam, self.awaygoals)
                            table_live_update.wins_draws_losses(self.hometeam, self.homegoals, self.awayteam, self.awaygoals)
                            table_live_update.points(self.hometeam, self.homegoals, self.awayteam, self.awaygoals)
                            table_live_update.goals_difference(self.hometeam, self.homegoals, self.awayteam, self.awaygoals)
                            table_live_update.total_matches(self.hometeam, self.awayteam)                        
                        else:
                            print("\nOne of the teams has already played in this round or in a previous round.")
                            continue
                    
                        if len(self.played_teams) == 18:  # 9 games, 2 teams each
                            print("\nRound complete! There are 9 matches.\n")
                            valid_input = True
                            self.fixtures += 1
                            self.fixture[f'ROUND {self.fixtures}'] = self.matches_rounds
                            self.display_rounds()
                            table_live_update.display_table()
                            table_live_update.save_table_to_file(table_live_update.formatted_string)
                            self.played_matches_list = []
                            self.played_teams = set()
                            self.played_teams_list = []
                            self.matches_rounds = []                            
                        else:
                            print("\nThere are not yet 9 matches in this round.")
                    else:
                        print("\nWrong Team Name or both teams are the same.")
            except (ValueError, KeyError):
                print("\nInput not valid.")
    
    def display_rounds(self):
        for round_num, matches in self.fixture.items():
            print(f'{round_num}:')
            for match in matches:
                print(match)
            print()

       
teams_instance = Teams(teams_dict)
fixture = Matches()


class Table:
    def __init__(self, teams_data):
        self.teams_data = teams_data
        

    def display_table(self):
        # Sort teams by points (PTS) and, in case of a tie, by goal difference (GD)
        sorted_teams = sorted(self.teams_data.values(), key=lambda x: (x['PTS'], x['GD']), reverse=True)

        # Display table header
        print("\n League Table")
        self.formatted_string = [
                                "{:<5} {:<20} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format(
                                "Pos", "Team", "MP", "PTS", "W", "D", "L", "GS", "GC", "GD")
                                ]
        print("".join(self.formatted_string))

        for teams, order in enumerate(sorted_teams, start=1):
            self.row = ["{:<5} {:<20} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format(
                teams,
                order['name'],
                order['MP'],
                order['PTS'],
                order['W'],
                order['D'],
                order['L'],
                order['GS'],
                order['GC'],
                order['GD'])
            ]
            print("".join(self.row))
            self.formatted_string.append(self.row)

        self.save_table_to_file(self.formatted_string)
        

    def save_table_to_file(self, formatted_string):
        # Save the formatted table to a file
        self.formatted_string = formatted_string
        with open('tabela.txt', 'w') as file:
            for row in self.formatted_string:
                file.write(''.join(str(cell) for cell in row) + '\n')

    
    # Methods to update statistics based on match results
    def goals_difference(self, home_team, home_goals, away_team, away_goals):
        teams_dict[home_team]['GD'] += home_goals - away_goals
        teams_dict[away_team]['GD'] += away_goals - home_goals

    def reverse_goals_difference(self, home_team, home_goals, away_team, away_goals):
        teams_dict[home_team]['GD'] -= home_goals - away_goals
        teams_dict[away_team]['GD'] -= away_goals - home_goals
    
        
    def goals_scored(self, home_team, home_goals, away_team, away_goals):
        teams_dict[home_team]['GS'] += home_goals
        teams_dict[away_team]['GS'] += away_goals

    def reverse_goals_scored(self, home_team, home_goals, away_team, away_goals):
        teams_dict[home_team]['GS'] -= home_goals
        teams_dict[away_team]['GS'] -= away_goals
               


    def goals_conceded(self, home_team, home_goals, away_team, away_goals):
        teams_dict[home_team]['GC'] += away_goals
        teams_dict[away_team]['GC'] += home_goals

    def reverse_goals_conceded(self, home_team, home_goals, away_team, away_goals):
        teams_dict[home_team]['GC'] -= away_goals
        teams_dict[away_team]['GC'] -= home_goals   

    def wins_draws_losses(self, home_team, home_goals, away_team, away_goals):
        if home_goals > away_goals:
            teams_dict[home_team]['W'] += 1
            teams_dict[away_team]['L'] += 1
        elif away_goals > home_goals:
            teams_dict[away_team]['W'] += 1
            teams_dict[home_team]['L'] += 1
        else:
             teams_dict[home_team]['D'] += 1
             teams_dict[away_team]['D'] += 1

    def reverse_wins_draws_losses(self, home_team, home_goals, away_team, away_goals):
        if home_goals > away_goals:
            teams_dict[home_team]['W'] -= 1
            teams_dict[away_team]['L'] -= 1
        elif away_goals > home_goals:
            teams_dict[away_team]['W'] -= 1
            teams_dict[home_team]['L'] -= 1
        else:
             teams_dict[home_team]['D'] -= 1
             teams_dict[away_team]['D'] -= 1    

    def points(self, home_team, home_goals, away_team, away_goals):
        if home_goals > away_goals:
            teams_dict[home_team]['PTS'] += 3   
        elif away_goals > home_goals:
            teams_dict[away_team]['PTS'] += 3       
        else:
            teams_dict[home_team]['PTS'] += 1
            teams_dict[away_team]['PTS'] += 1 

    def reverse_points(self, home_team, home_goals, away_team, away_goals):
        if home_goals > away_goals:
            teams_dict[home_team]['PTS'] -= 3   
        elif away_goals > home_goals:
            teams_dict[away_team]['PTS'] -= 3       
        else:
            teams_dict[home_team]['PTS'] -= 1
            teams_dict[away_team]['PTS'] -= 1 

        
    def total_matches(self, home_team, away_team):
        if (home_team, away_team) in match_fixtures.played_matches:
            teams_dict[home_team]['MP'] += 1
            teams_dict[away_team]['MP'] += 1
            
    
    def reverse_total_matches(self, home_team, away_team):
        if (home_team, away_team) in match_fixtures.removed_teams:
            teams_dict[home_team]['MP'] -= 1
            teams_dict[away_team]['MP'] -= 1
            
    def table_update(self):
        match_fixtures.play_round()  # Play a round of matches
        self.display_table()  # Display the updated table
        self.save_table_to_file(self.formatted_string)  # Save the table to a file



match_fixtures = Matches()
table_live_update = Table(teams_dict)
table_live_update.table_update()



