import pandas as pd
import json
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyCfcgDAmwfiLYeCj0xoR9QbjkY__vbW1ss')
# google maps api: AIzaSyCfcgDAmwfiLYeCj0xoR9QbjkY__vbW1ss

def is_Singapore(lat, long):
    geocode_result = gmaps.reverse_geocode((lat,long))
    #address = json.dumps(geocode_result[0], indent=4, sort_keys=True)
    address = json.dumps(geocode_result[0])

    print(geocode_result[0]["formatted_address"])

def main():
    df = pd.read_csv("data.csv")
    is_Singapore(1.338860535, 103.9802227)


if __name__ == "__main__":
    main()