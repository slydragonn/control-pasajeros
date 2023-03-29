import pandas as pd

class Bus:
    def get_data(self, data, number_of_bus:str):
        bus_data = data[(data['mDescription'] == number_of_bus) & (data['p_station'] != 'Terminal Arrieritas') & (data['p_station'] != 'Terminal arrieritas') & (data['p_station'] != 'Respaldo')]    
        array_of_passengers = pd.DataFrame(bus_data.loc[:, ['regId', 'mDescription', 'p_doorId', 'p_ingresos', 'p_salidas', 'p_bloqueos', 'p_station', 'system_datetime']]).to_numpy()
        
        return array_of_passengers