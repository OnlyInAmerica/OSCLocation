"""Small example OSC client

This program sends a series of locations generated via generate_locations with a configurable delay between transmissions
"""
import argparse
import time

import geopy as geopy
from geopy.distance import VincentyDistance
from pythonosc import udp_client

OSC_PATH_LOCATION = '/location'
PER_LOCATION_SEND_DELAY_MS = 1000


def generate_locations(num_locations=5):
    base_lat = 42.0
    base_lon = -120

    # Offset per position. e.g: Each location generated will differ by these values
    offset_dist_m = 5
    offset_bearing_degrees = 0  # 0 degrees generates a vertical line (Latitude varies, Longitude does not), and 90 a horizontal line (Longitude varies, Latitude does not)

    last_location = geopy.Point(base_lat, base_lon)

    locations = []
    for _ in range(num_locations):
        last_location = VincentyDistance(meters=offset_dist_m).destination(last_location, offset_bearing_degrees)
        print("Generated location Lat: %f Lon: %f" % (last_location.latitude, last_location.longitude))
        locations.append(last_location)

    return locations


def send_location(client, lat, lon, heading):
    client.send_message(OSC_PATH_LOCATION, make_location(lat=lat, lon=lon, heading=heading))


def make_location(lat, lon, heading):
    return [lat, lon, heading]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
                        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005,
                        help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

    locations = generate_locations()
    for location in locations:
        send_location(client=client, lat=location.latitude, lon=location.longitude, heading=35.0)
        time.sleep(PER_LOCATION_SEND_DELAY_MS)
