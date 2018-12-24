import pandas as pd
files_list = ["data_2018.csv","data_2017.csv","data_2016.csv","data_2015.csv","data_2014.csv","data_2013.csv","data_2012.csv","data_2011.csv","data_2010.csv"]

all_seasons = []
for file_name in files_list:
    print(file_name)
    mylist = []
    for chunk in pd.read_csv(file_name, sep=',', chunksize=40000):
        mylist.append(chunk)
    data = pd.concat(mylist, axis=0)
    del mylist
    print(data.shape)
    print("filtering")
    #    data = data[['GAME_ID','HOMEDESCRIPTION','PCTIMESTRING','PERIOD','PLAYER1_ID','PLAYER1_NAME','PLAYER1_TEAM_ABBREVIATION','PLAYER1_TEAM_ID','PLAYER2_ID','PLAYER2_NAME','PLAYER2_TEAM_ABBREVIATION','PLAYER2_TEAM_ID','PLAYER3_ID','PLAYER3_NAME','PLAYER3_TEAM_ABBREVIATION','PLAYER3_TEAM_ID','HOME_TEAM','AWAY_TEAM','JUMP_BALL_HOME_PLAYER_ID','JUMP_BALL_AWAY_PLAYER_ID','JUMP_BALL_RETRIEVED_PLAYER_ID']]

    data = data[['GAME_ID','HOMEDESCRIPTION','PCTIMESTRING','PERIOD','PLAYER3_TEAM_ABBREVIATION','HOME_TEAM','AWAY_TEAM','JUMP_BALL_HOME_PLAYER_ID','JUMP_BALL_AWAY_PLAYER_ID','JUMP_BALL_RETRIEVED_PLAYER_ID']]

    data = data[data['JUMP_BALL_HOME_PLAYER_ID'].notnull() & # Jump ball play
                                           data['JUMP_BALL_AWAY_PLAYER_ID'].notnull() & # Jump ball play
                                           data['JUMP_BALL_RETRIEVED_PLAYER_ID'].notnull() & # Jump ball play
                                           data['PCTIMESTRING'].isin(['12:00']) & # Beginning of the quarter
                                           data['PERIOD'].isin(['1']) # Beginning of the game
                                            ]
    data["JUMP_BALL_RETRIEVED_TEAM_NAME"] = data["PLAYER3_TEAM_ABBREVIATION"]
    # replacing abbreviations to team names to make uniform naming convention
    team_name_dic = {"ATL": "Hawks",
                    "BKN": "Nets",
                    "BOS": "Celtics",
                    "CHA": "Hornets",
                    "CHI": "Bulls",
                    "CLE": "Cavaliers",
                    "DAL": "Mavericks",
                    "DEN": "Nuggets",
                    "DET": "Pistons",
                    "GSW": "Warriors",
                    "HOU": "Rockets",
                    "IND": "Pacers",
                    "LAC": "Clippers",
                    "LAL": "Lakers",
                    "MEM": "Grizzlies",
                    "MIA": "Heat",
                    "MIL": "Bucks",
                    "MIN": "Timberwolves",
                    "NOP": "Pelicans",
                    "NYK": "Knicks",
                    "OKC": "Thunder",
                    "ORL": "Magic",
                    "PHI": "76ers",
                    "PHX": "Suns",
                    "POR": "Trail Blazers",
                    "SAC": "Kings",
                    "SAS": "Spurs",
                    "TOR": "Raptors",
                    "UTA": "Jazz",
                    "WAS": "Wizards"}
    data.replace(team_name_dic, inplace=True)
    all_seasons.append(data)


all_filtered_data = pd.concat(all_seasons, axis=0)

all_filtered_data.to_csv('filtered_data_2010_2018.csv')