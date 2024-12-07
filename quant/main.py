from tradelocker import TLAPI
from dotenv import load_dotenv
import os
import time, random

load_dotenv()

# enviroment variables for trading created a dotenv file 
enviroment = os.getenv("ENVIROMENT")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
server = os.getenv("SERVER")


client = TLAPI(environment=enviroment, username=username, password=password, server=server)

if __name__ == "__main__":

    symbol_name = "BTCUSD" 
    all_instruments = client.get_all_instruments
    if symbol_name == "RANDOM":
        instrument_id = int(random.choice(all_instruments["tradableInstrumentId"]))
    else: 
        instrument_id =  client.get_instrument_id_from_symbol_name(symbol_name)
        price_history = client.get_price_history(instrument_id, resolution="1D", start_timestamp=1, end_timestamp=5)
        latest_price = client.get_latest_asking_price(instrument_id)
        
    print(latest_price)