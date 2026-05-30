def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": 0.01, "orbit":"Sun"})
    #es otra forma de agragar strings al diccionario

    #Se crea un diccionario para relacionar strings
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ============REPORT==========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ============================
    """#Se coloca entre corchetes para llamar string del diccionario
#con .get se obtine un string dentro del diccionario
#este string sino existe enviara el string siguiente en este caso Unknown
main()

