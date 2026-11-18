###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
print("\nExercici 1:")
def saludar_a(nom, salutacio="Hola"):
  print(f"{salutacio} {nom}!")

saludar_a("Joan")
saludar_a("Maria", "Bon dia")

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
print("\nExercici 2:")
def es_parell(numero):
  return numero % 2 == 0

print(f"Es 4 parell? {es_parell(4)}")
print(f"Es 7 parell? {es_parell(7)}")

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
print("\nExercici 3:")
def mitjana(numeros):
  suma = 0
  for numero in numeros:
    suma += numero
  return suma / len(numeros)

print(f"La mitjana de [1, 2, 3, 4, 5] és: {mitjana([1, 2, 3, 4, 5])}")

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.
print("\nExercici 4:")
def sumar_tot(*args):
  return sum(args)

print(f"La suma de 2, 5 i 10 és: {sumar_tot(2, 5, 10)}")

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
print("\nExercici 5:")
def taula_multiplicar(numero, limit=10):
  for i in range(1, limit + 1):
    print(f"{numero} x {i} = {numero * i}")

taula_multiplicar(5, 5)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).
print("\nExercici 6:")
def mostrar_perfil(**kwargs):
  for clau, valor in kwargs.items():
    print(f"{clau}: {valor}")

mostrar_perfil(nom="Joan", edat=20, grau="ESO")

# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
print("\nExercici 7:")
def factorial(n):
  resultat = 1
  comptador = 1
  while comptador <= n:
    resultat *= comptador
    comptador += 1
  return resultat

print(f"El factorial de 5 és: {factorial(5)}")

# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.
print("\nExercici 8:")
def comptar_vocals(text):
  vocals = "aeiouAEIOU"
  comptador = 0
  for lletra in text:
    if lletra in vocals:
      comptador += 1
  return comptador

print(f"El nombre de vocals en 'Hola, com estàs?' és: {comptar_vocals('Hola, com estàs?')}")

# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.
print("\nExercici 9:")
def minim_i_maxim(numeros):
  min_val = numeros[0]
  max_val = numeros[0]
  for numero in numeros:
    if numero < min_val:
      min_val = numero
    if numero > max_val:
      max_val = numero
  return min_val, max_val

minim, maxim = minim_i_maxim([1, 2, 3, 4, 5])
print(f"El mínim és: {minim}, el màxim és: {maxim}")

# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.
print("\nExercici 10:")
def es_palindrom(text):
  text = text.lower()
  return text == text[::-1]

print(f"¿'anna' és un palíndrom? {es_palindrom('anna')}")
print(f"¿'hello' és un palíndrom? {es_palindrom('hello')}")
