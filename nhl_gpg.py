import datetime
from datetime import date

import requests

start_date = date.today() - datetime.timedelta(days=120)
end_date = date.today() - datetime.timedelta(days=0)
amount_of_games = 0
total_goals = 0

print(f"Getting data between {start_date} and {end_date}.")

response = requests.get(f'https://statsapi.web.nhl.com/api/v1/schedule?startDate={start_date}&endDate={end_date}')

dates = response.json()['dates']

for day in dates:
    daily_amount_of_games = 0
    daily_total_goals = 0
    games = day['games']

    for game in games:
        # Checks if the game is finished
        if game['status']['statusCode'] == "7":
            amount_of_games = amount_of_games + 1
            total_goals = total_goals + game['teams']['away']['score']
            total_goals = total_goals + game['teams']['home']['score']

            daily_amount_of_games = daily_amount_of_games + 1
            daily_total_goals = daily_total_goals + game['teams']['away']['score']
            daily_total_goals = daily_total_goals + game['teams']['home']['score']
    print("---------------------------------------------")
    print("DATE: " + day['date'])
    if daily_amount_of_games == 0:
        print("NO GAMES")
    else:
        print("TOTAL GOALS SCORED: " + str(daily_total_goals))
        print("AMOUNT OF GAMES   : " + str(daily_amount_of_games))
        print("GOALS PER GAME    : " + str(daily_total_goals / daily_amount_of_games))
        
print("---------------------------------------------")       
print("TOTALS:")
print("TOTAL GOALS SCORED: " + str(total_goals))
print("AMOUNT OF GAMES   : " + str(amount_of_games))

if amount_of_games == 0:
    print("GOALS PER GAME    : NONE TO CALCULATE")
else:
    print("GOALS PER GAME    : " + str(total_goals / amount_of_games))
