from collections import defaultdict

dogs = ["Sparky", "Hunter", "Loki", "Astro", "Sparky", "Rocky", "Rocky", "Toby", "chelsea", "Maple", "Maya", "Loki", "Sparky", "Toby", "Sparky", "Dexter", "Fido", "Sparky"]

count_dogs = {}

# Contamos la cantidad de veces que aparece cada nombre en dogs
for perro in dogs:
    if perro in count_dogs:
        count_dogs[perro] += 1
    else:
        count_dogs[perro] = 1

# Imprime la cantidad de perros que se llaman "Rocky" y "Sparky"
print("Cantidad de perros llamados Rocky:", count_dogs.get("Rocky", 0))
print("Cantidad de perros llamados Sparky:", count_dogs.get("Sparky", 0))

# Imprime la lista de diferentes nombres de perros
print("Lista de diferentes nombres de perros:")
nombres_de_diferentes_perros = list(count_dogs.keys())
print(nombres_de_diferentes_perros)
