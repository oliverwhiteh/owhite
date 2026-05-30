distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for name in distances.keys():
        #for es un bucle en donde llamas el name, nombre de la variable que representara dentro del diccionario distances la primera columna
        #  y el .keys llama a primera columna del diccionario.
        print(f"{name} is {distances[name]} AU from Earth")
        #f es funtion string, {name} llamas a la variable o la primera columna de string, {distances[name]} llamas al diccionario y lo relacionado a la primera columna.



main()
