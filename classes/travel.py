import pandas as pd

class Travel:
    def get_data(self, data, number_of_bus:str):
        bus_data = data[(data['VEHICULO'] == number_of_bus)]    
        array_of_travels = pd.DataFrame(bus_data.loc[:, ['VEHICULO', 'RUTA', 'PUNTO DE CONTROL']]).to_numpy()
        
        return array_of_travels
    
    def get_number_of_travels(self, array:list):
        travels = {
            "ida": 
                   { "c": 0, "vm": 0, "vt": 0, "m": 0, "total": 0}, 
            "vuelta": 
                   {"c": 0, "vm": 0, "vt": 0, "m": 0, "total": 0}
        }

        for travel in array:
            if travel[2] == "Terminal Arrieritas":
                if travel[1] == "Caldas - Medellín - La 50":
                    travels['ida']["c"] += 1
                    travels["ida"]["total"] += 1
                    continue
                if travel[1] == "Caldas - Medellin - Variante":
                    travels["ida"]["vm"] += 1
                    travels["ida"]["total"] += 1
                    continue
                if travel[1] == "Caldas - Medellin - Tablaza Variante":
                    travels["ida"]["vt"] += 1
                    travels["ida"]["total"] += 1
                    continue

            if travel[2] == "Medellin (C1)":
                if travel[1] == "Variante Tablaza Caldas":
                    travels["vuelta"]["vt"] += 1
                    travels["vuelta"]["total"] += 1
                    continue
                if travel[1] == "Variante Miel Caldas":
                    travels["vuelta"]["vm"] += 1
                    travels["vuelta"]["total"] += 1
                    continue
                if travel[1] == "Medellin - Caldas":
                    travels["vuelta"]["c"] += 1
                    travels["vuelta"]["total"] += 1
                    continue

            if (travel[2] == "Terminal Arrieritas") and ((travel[1] == "Minorista - La 50") or (travel[1] == "Minorista - Variante") or (travel[1] == "Minorista - Tablaza Variante")):
                travels["ida"]["m"] += .5
                travels["vuelta"]["m"] += .5

        if travels["ida"]["m"] > 0:
            travels["ida"]["total"] += int(travels["ida"]["m"])

        if travels["vuelta"]["m"] > 0:
            travels["vuelta"]["total"] += int(travels["vuelta"]["m"])


        if travels["ida"]["total"] > travels["vuelta"]["total"]:
            travels["despachos"] = "Falta despacho en arrieritasws"
        
        if travels["ida"]["total"] < travels["vuelta"]["total"]:
            travels["despachos"] = "Falta despacho en terminal arrieritas"

        if travels["ida"]["total"] == travels["vuelta"]["total"]:
            travels["despachos"] = "Todo Correcto"

        return travels
