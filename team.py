

class Team():

    def __init__(self, name):
        self.name = name
        self.goals = 0
        self.wins = 0
        
        self.rain_games = 0
        self.rain_wins = 0
        
    
    
    def weather(self, match_row):
        year = match_row['Date'][:4]
        month = match_row['Date'][5:7]
        day = match_row['Date'][8:]
        date_string = '{year}-{month}-{day}T16:00:00'
        url= f'https://api.darksky.net/forecast/{api_key}/52.5200,13.4050,{date_string}?exclude=currently,flags'
        response = requests.get(url)
        self.weather = response.json()['hourly']['icon']
       
        return result
    
    def home_goal_win(self, match_row):
        win = None
        if self.name == match_row['HomeTeam']:
            self.goals += match_row['FTHG']
            if match_row['FTR'] == 'H':
                self.wins += 1
                win = 'Win'
                
            elif match_row['FTR'] == 'A':
                win = 'Lose'
                
            else:
                win = 'Draw' 
        return win
        
    
    def away_goal_win(self, match_row):
        win = None
        if self.name == match_row['AwayTeam']:
            self.goals += match_row['FTAG']
            if match_row['FTR'] == 'A':
                self.wins += 1
                win = 'Win'
            elif match_row['FTR'] == 'H':
                win = 'Lose'
            else:
                win = 'Draw'
        
        return win

    def histogram_data(self, histogram_results):
        self.histogram_results = histogram_results

    def process(self, df):
        
        for match_row in df.loc[df['HomeTeam'] == self.name]:
            print(match_row)
            win = self.home_goal_win(match_row)
            win = self.away_goal_win(match_row)
            #self.weather(match_row, win) 

    
    
        



