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
        "-d",
        "--distance",
        action="store_true",
        help="displays the distance of the asteroid(s) from Earth in kilometres"
    )

    return parser.parse_args()



base_url = "https://api.nasa.gov/neo/rest/v1/feed?"
def build_url(start_date, end_date):
    #API key
    api_key = get_api_key()

    #Converting start date into url format
    try:
        parsed_start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        start_date = parsed_start_date.strftime("%Y-%m-%d")
    except ValueError:
        print(f"Invalid date format: {start_date}. Please use the format YYYY-MM-DD.")
        return None
    
    #Converting end date into url format
    try:
        parsed_end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        end_date = parsed_end_date.strftime("%Y-%m-%d")
    except ValueError:
        print(f"Invalid date format: {end_date}. Please use the format YYYY-MM-DD.")
        return None
    
    #the url
    url = (
        f"{base_url}start_date={start_date}&end_date={end_date}&api_key={api_key}"
    )

    return url 



#GET DATA FROM THE URL
def get_data(url):
    #create a request object for the url and include a user-agent
    req = request.Request(url, headers={"User-Agent":"Mozilla/5.0"})


    #initiating the http request from the request object
    try:
            
            response = request.urlopen(req)

        #incase of an error    
    except error.HTTPError as http_error:
        #401 Unauthorized
        if http_error.code == 401:
            sys.exit("Access Denied, Check your API key.")
         #401 Not-Found
        elif http_error.code == 404:
            sys.exit("Can't find the data for the mentioned dates.")
        else: 
            sys.exit(f"Something went wrong... ({http_error.code})")

    #reading the data from the response
    data = response.read()

    #returns deserialized json
    try:
        return json.loads(data)
        
    #unless.. there is an error 
    except:
         sys.exit("Couldn't read the server response")

def display_info(asteroid_data, size=False, distance=False):
    #Iterate over each date in the data
    for date in asteroid_data['near_earth_objects']:
        print(f"\nDate: {date}")

        
         # Iterate over each asteroid on that date
        for asteroid in asteroid_data["near_earth_objects"][date]:
            print(f"\nAsteroid ID: {asteroid['id']}")
            print(f"Name: {asteroid['name']}")
            print(f"NEO Reference ID: {asteroid['neo_reference_id']}")

            # If size argument is True, print the size of the asteroid
            if size:
                print(f"Estimated Diameter (in meters): {asteroid['estimated_diameter']['meters']['estimated_diameter_min']} - {asteroid['estimated_diameter']['meters']['estimated_diameter_max']}")

            # If distance argument is True, print the distance of the asteroid from Earth
            if distance:
                print(f"Miss Distance (in kilometers): {asteroid['close_approach_data'][0]['miss_distance']['kilometers']}")





if __name__ == "__main__":
     user_args = read_user_args()
     query_url = build_url(user_args.start_date, user_args.end_date)
     asteroid_data = get_data(query_url)
     display_info(asteroid_data)

    





