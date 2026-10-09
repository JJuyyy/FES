###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom = input("Nom del encaminador:")
ubicacio = input("Ubicació:")
n_ports = input("Numerpo de ports:")
estat = input("Estat:")

print(f"L'encaminador {nom} es troba en {ubicacio}, el seu nombre de ports es {n_ports} y es troba {estat}.")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
GB_inclosos = 300
GB_consumits = 169

print(f"Queden {GB_inclosos - GB_consumits}GB.")

GB_consumits = 246

print(f"Queden {GB_inclosos - GB_consumits}GB.")