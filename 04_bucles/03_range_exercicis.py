###
# EXERCICIS (range)
###

# Exercici 1: Imprimir números de l'1 al 10
# Imprimeix els números de l'1 al 10 (inclosos) fent servir un bucle for i range().
print("Exercici 1: Números de l'1 al 10")
for num in range(1, 11):
    print(num)
# Exercici 2: Imprimir números senars de l'1 al 20
# Imprimeix tots els números senars entre 1 i 20 (inclosos) fent servir un bucle for i range().
print("\nExercici 2: Números senars de l'1 al 20")
for num in range(1, 21, 2):
    print(num)
# Exercici 3: Imprimir múltiples de 5
# Imprimeix els múltiples de 5 des del 5 fins al 50 (inclosos) fent servir un bucle for i range().
print("\nExercici 3: Múltiples de 5")
for num in range(5, 51, 5):
    print(num)
# Exercici 4: Imprimir números en ordre invers
# Imprimeix els números del 10 a l'1 (inclosos) en ordre invers fent servir un bucle for i range().
print("\nExercici 4: Números del 10 a l'1")
for num in range(10, 0, -1):
    print(num)
# Exercici 5: Suma de números en un rang
# Calcula la suma dels números de l'1 al 100 (inclosos) fent servir un bucle for i range().
print("\nExercici 5: Suma dels números de l'1 al 100")
suma = 0
for num in range(1, 101):
    suma += num
print(f"La suma dels números de l'1 al 100 és: {suma}")

# Exercici 6: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle for i range().
print("\nExercici 6: Taula de multiplicar")
numero = int(input("Introdueix un número per a la taula de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")