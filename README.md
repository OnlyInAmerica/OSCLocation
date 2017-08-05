# OSC Location Example

Simple example of transmitting GPS data (Lat, Lon, Heading) via [Open Sound Control](http://opensoundcontrol.org/spec-1_0) packets

The server will listen for `/location` addressed packets and print the location.

The client will generate a number of locations and send them sequentially.

## Running

Example using python3. For python 2.X substitude `python` for `python3` and `pip` for `pip3`.

    # Install requirements
    pip3 install -r requirements.txt

    # Start the server (Optional)
    python3 server.py

    # Start the client
    python3 client.py
    # Optionally specify server address and port
    python3 client.py --ip 192.168.1.102 --port 9000