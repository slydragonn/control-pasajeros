import tkinter as tk
from tkinter import ttk, filedialog as fd
from app import generate_passengers_control, get_data
from utils.json import create_json_file

rutes = {}

def generate():
    print("Loading...")
    message = ttk.Label(text="Generando...")
    message.place(x=120, y=260)

    data = get_data(rutes)
    result = generate_passengers_control(data, data["buses"])
    create_json_file(result)

    print("Complete :)")
    message_2 = ttk.Label(text="Completado :)")
    message_2.place(x=120, y=280)
    message_3 = ttk.Label(text="Resultado Generado en el archivo => buses.json")
    message_3.place(x=120, y=300)


def select_file(rute_type:str):

    filetypes = (
        ('text files', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open file',
        initialdir='/',
        filetypes=filetypes)
    
    rutes[rute_type] = filename
    
    return filename


window = tk.Tk()
window.title("Control de Pasajeros")
window.resizable(False, False)
window.config(width=500, height=340)
title = ttk.Label(text="Generador de Control de Pasajeros")
title.place(x=20, y=10)


text_necesary_files = ttk.Label(text="Archivos Necesarios para el proceso:")
text_necesary_files.place(x=40, y=40)


file_1 = ttk.Label(text="- historial_de_conductores.csv")
file_1.place(x=50, y=60)
open_file_1 = ttk.Button(
    window,
    text='Seleccionar Archivo',
    command=lambda: select_file("drivers")
)
open_file_1.pack(expand=True)
open_file_1.place(x=50, y=80)

file_2 = ttk.Label(text="- historial_de_itinerarios.csv")
file_2.place(x=50, y=110)
open_file_2 = ttk.Button(
    window,
    text='Seleccionar Archivo',
    command=lambda: select_file("itineraries")
)
open_file_2.pack(expand=True)
open_file_2.place(x=50, y=130)

file_3 = ttk.Label(text="- historial_de_pasajeros.csv")
file_3.place(x=50, y=160)
open_file_3 = ttk.Button(
    window,
    text='Seleccionar Archivo',
    command=lambda: select_file("passengers")
)
open_file_3.pack(expand=True)
open_file_3.place(x=50, y=180)


generate_button = ttk.Button(text="Generar", command=generate)
generate_button.place(x=20, y=240)


window.mainloop()