import argparse
import os
from urllib import parse, request, error
import json
import sys


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





