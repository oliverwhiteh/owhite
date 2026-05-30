#Defino la función de paridad, si x es par imprimirá Even de lo contrario imprimirá Odd.
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
#defino la función is_even, n es el número, podría ser x, pero para no confundir se utilizó n.
#la línea 11 sería si el residuo del número divido entre dos es igual a cero
#regresará a la función anterior especificamente (X) el valor boleano True (1) lo que imprimirá Even.
#de otro modo imprimirá False (0).
def is_even(n):
  return n % 2 == 0

main()
