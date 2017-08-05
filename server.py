"""Small example OSC server

This program listens to the /location address to receive lat, lon, heading triplets.
"""
import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server


def print_location_handler(address, lat, lon, heading):
    print("Got location update : \n\tLat: %f \n\tLon: %f \n\tHeading: %f" % (lat, lon, heading))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",
                        type=int, default=5005, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/location", print_location_handler)

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
