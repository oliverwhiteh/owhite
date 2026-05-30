def main():
    while True:
        Fraction = input("Fraction: ").strip()

        try:
            numerador, denominador = str(Fraction).split("/")
            numerador = int(numerador)
            denominador = int(denominador)

            if numerador <= denominador:
                porcentage = (numerador / denominador) * 100
                porcentage = round(porcentage)

                if porcentage <= 1:
                    print("E")
                    return True
                elif porcentage >= 99:
                    print("F")
                    return True
                elif porcentage > 1 and porcentage < 99:
                    print(f"{porcentage}%")
                    return True
            else:
                continue

        except(ValueError, ZeroDivisionError):
            pass


main()
