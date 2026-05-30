distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for distance in distances.values():
        #con .values llamas la segunda columna
        print(f"{distance} AU is {convert(distance)} m")

def convert(au):
    return au * 1495970700
#funcion creada para convertir au a metros

main()
