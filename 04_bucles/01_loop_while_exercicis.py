###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.
print("Exercici 1: Compte enrere")
num = 10
while num >= 1:
    print(num)
    num -= 1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
print("\nExercici 2: Suma de números parells")
num = 1
suma = 0
while num <= 20:
    if num % 2 == 0:
        suma += num
    num += 1
print(f"La suma dels números parells entre 1 i 20 és: {suma}")

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nExercici 3: Factorial d'un número")
numero = int(input("Introdueix un número enter positiu: "))
factorial = 1
comptador = 1
while comptador <= numero:
    factorial *= comptador
    comptador += 1
print(f"El factorial de {numero} és: {factorial}")
# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".
print("\nExercici 4: Validació de contrasenya")
contrasenya = ""
while len(contrasenya) < 8:
    contrasenya = input("Introdueix una contrasenya (almenys 8 caràcters): ")
print("Contrasenya vàlida.")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
print("\nExercici 5: Taula de multiplicar")
numero = int(input("Introdueix un número: "))
comptador = 1
while comptador <= 10:
    print(f"{numero} x {comptador} = {numero * comptador}")
    comptador += 1

# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.
print("\nExercici 6: Números primers fins a N")
n = int(input("Introdueix un número enter positiu N: "))
numero = 2
while numero <= n:
  es_primer = True  # Assumim que el número és primer fins que es demostri el contrari
  divisor = 2
  while divisor * divisor <= numero:  # Optimitzem: no cal provar divisors fins a numero
    if numero % divisor == 0:
      es_primer = False  # Si trobem un divisor, no és primer
      break  # Sortim del bucle interior
    divisor += 1
  if es_primer:
    print(numero)

  numero += 1

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
print("\nExercici 7: Suma fins al zero")
suma_total = 0
while True:
    numero = int(input("Introdueix un número enter (0 per acabar): "))
    if numero == 0:
        break
    suma_total += numero
print(f"La suma total és: {suma_total}")

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.
print("\nExercici 8: Comptar les xifres d'un número")
numero = int(input("Introdueix un número enter positiu: "))
comptador_xifres = 0
while numero > 0:
    numero //= 10
    comptador_xifres += 1
print(f"El número té {comptador_xifres} xifres.")

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
print("\nExercici 9: Seqüència de Fibonacci")
termes = int(input("Quants termes de Fibonacci vols veure? "))
a, b = 0, 1
comptador = 0
while comptador < termes:
    print(a, end=" ")
    a, b = b, a + b
    comptador += 1

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
print("\n\nExercici 10: Joc d'endevinar el número")
numero_secret = 7
while True:
    numero = int(input("Introdueix un número: "))
    if numero == numero_secret:
        print("Felicitats! Has endevinat el número secret.")
        break
    elif numero < numero_secret:
        print("El número secret és més gran.")
    else:
        print("El número secret és més petit.")