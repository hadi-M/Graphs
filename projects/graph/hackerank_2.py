#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#
import requests

def getWinnerTotalGoals(competition, year):
    # Write your code here
    winner_base_url = "https://jsonmock.hackerrank.com/api/football_competitions"
    winner_params = {
        "year": year,
        "name": competition
    }
    winner_res = requests.get(winner_base_url, params=winner_params)
    
    winner = winner_res.json()["data"][0]["winner"] 


    
    total_winner_goal = 0
    page = 1

    matches_base_url = "https://jsonmock.hackerrank.com/api/football_matches"
    matches_params = {
        "year": year,
        "team1": winner,
        "page": page,
        "competition": competition
    }
    matches_res = requests.get(matches_base_url, params=matches_params)

    while matches_res.json()["data"] != []:
        for match in matches_res.json()["data"]:
            total_winner_goal += int(match["team1goals"])
            matches_base_url = "https://jsonmock.hackerrank.com/api/football_matches"
        page += 1
        matches_params = {
            "year": year,
            "team1": winner,
            "page": page,
            "competition": competition
        }
        matches_res = requests.get(matches_base_url, params=matches_params)

    return total_winner_goal, matches_res.json()




if __name__ == '__main__':