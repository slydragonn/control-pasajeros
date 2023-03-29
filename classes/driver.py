import pandas as pd
import numpy as np

class Driver:
    def create_driver(self, bus_number, driver_name):
        return {"Bus": bus_number, "Conductor": driver_name}

    def get_driver_name(self, array_of_names:list):
        driver_name = ""
        driver_names = []
        drivers_count = []

        for i in array_of_names:
            driver_names.append(i[1])
            
        for i in np.unique(driver_names):
            drivers_count.append([i, driver_names.count(i)])

        last_value = {"count": 0, "name": ""}    
        for i in drivers_count:
            if last_value["count"] < i[1]:
                driver_name = i[0]
                last_value["count"] = i[1]
                last_value["name"] = i[0]
            else:
                driver_name = last_value["name"]

        return driver_name
    
    def get_driver_data(self, drivers_data, bus_number):
        driver_data = drivers_data[(drivers_data['mDescription'] == bus_number)]
        array_of_driver = pd.DataFrame(driver_data.loc[:, ["mDescription", "drl_name"]]).to_numpy()
        return array_of_driver