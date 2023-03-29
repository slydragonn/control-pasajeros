import pandas as pd
from classes.bus import Bus
from classes.passenger import Passenger
from classes.travel import Travel
from classes.driver import Driver
import numpy as np

def get_data(rutes:dict):
    passengers_data = pd.read_csv(rutes["passengers"], encoding="utf_16", sep='\t', engine='python')
    drivers_data = pd.read_csv(rutes["drivers"], encoding="utf_16", sep='\t', engine='python')
    itineraries_data = pd.read_csv(rutes["itineraries"], encoding="utf_16", sep='\t', engine='python')

    return {
        "buses": np.unique(pd.DataFrame(passengers_data.loc[:, "mDescription"]).to_numpy().flatten()),
        "passengers": passengers_data,
        "drivers": drivers_data,
        "itineraries": itineraries_data
    }

def generate_passengers_control(data, array: list):
    buses_dic = {}
    new_bus = Bus()
    new_driver = Driver()
    new_travel = Travel()
    new_passenger = Passenger()

    for i in array:
        bus_data = new_bus.get_data(data["passengers"], i)
        travels_data = new_travel.get_data(data["itineraries"], i)
        driver_data = new_driver.get_driver_data(data["drivers"], i)
        bus_dic = {}

        bus_dic['Pasajeros'] = new_passenger.sum_passengers(bus_data)
        bus_dic['Viajes'] = new_travel.get_number_of_travels(travels_data)
        bus_dic['Conductor'] = new_driver.create_driver(driver_name=new_driver.get_driver_name(driver_data), bus_number= i)
        
        buses_dic['Bus: ' + i] = bus_dic

    return buses_dic