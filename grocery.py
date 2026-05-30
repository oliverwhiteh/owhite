def main():
    lista = {

    }
    while True:

        try:
            fruta = input("").strip().upper()
            if fruta in lista:
                lista[fruta] = lista[fruta] + 1
            else:
                lista[fruta] = 1

            keys = sorted(lista.keys())
            values = sorted(lista.values())
            



        except(KeyError, TypeError, ValueError):
            pass

        except(EOFError):

            for orden in lista:
                print(lista[orden], orden, sep=" ")
            return True



main()
