import pandas as pd

jump_ball_data = pd.read_csv("filtered_data_2010_2018.csv")

jump_ball_data.loc[jump_ball_data['JUMP_BALL_RETRIEVED_TEAM_NAME'] == jump_ball_data['HOME_TEAM'], 'JUMP_BALL_WINNER'] = 0
jump_ball_data.loc[jump_ball_data['JUMP_BALL_RETRIEVED_TEAM_NAME'] == jump_ball_data['AWAY_TEAM'], 'JUMP_BALL_WINNER'] = 1

print(jump_ball_data.describe())

