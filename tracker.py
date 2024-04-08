import argparse
import os
from urllib import parse, request, error
import json
import sys
import datetime


#API KEY ENVIRONEMENT VARIABLE
def get_api_key():
    return os.getenv("ASTEROIDS_API")

def read_user_args():
    #Adding the Argument Parse
    parser = argparse.ArgumentParser(description="gets date range and fetches infomation on near-Earth asteroids.")

    #Start Date Argument 
    parser.add_argument("start_date", type=str, help="Takes start date for asteroid tracking (YYYY-MM-DD)")

    #End Date Argument
    parser.add_argument("end_date", type=str, help="Takes end date for asteroid tracking (YYYY-MM-DD)")

    #Size of the Asteroid
    parser.add_argument(
        "-s",
        "--size",
        action="store_true",
        help="displays the size of the asteroid(s) in metres"
    )

    #Distance of the Asteroid (From Earth)
    parser.add_argument(
        "-s",
        "--size",
        action="store_true",
        help="displays the size of the asteroid(s) in kilometres"
    )

    return parser.parse_args()



base_url = "https://api.nasa.gov/neo/rest/v1/feed?"
def build_url(start_date, end_date):
    #API key
    api_key = get_api_key()

    #Converting start date into url format
    try:
        parsed_start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        return parsed_start_date.strftime("%Y-%m-%d")
    except ValueError:
        print(f"Invalid date format: {start_date}. Please use the format YYYY-MM-DD.")
        return None
    
    #Converting end date into url format
    try:
        parsed_end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        return parsed_end_date.strftime("%Y-%m-%d")
    except ValueError:
        print(f"Invalid date format: {end_date}. Please use the format YYYY-MM-DD.")
        return None
    
    #the url
    url = (
        f"{base_url}start_date={start_date}&end_date={end_date}&api_key={api_key}"
    )

    return url 









