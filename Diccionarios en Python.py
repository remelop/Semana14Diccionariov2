informacion_personal = {
    "nombre": "Ronny Melo",
    "edad": 35,
    "ciudad": "Cuenca",
}

# Accede al valor de la ciudad
ciudad_actual = informacion_personal["ciudad"]

# Modifica la ciudad por una nueva
informacion_personal["ciudad"] = "Quito"

# Agrega la clave "profesion"
informacion_personal["profesion"] = "Analista de TI"

# Verifica si la clave "telefono" existe
if "telefono" in informacion_personal:
    print("La clave 'telefono' ya existe.")
else:
    # Agrega la clave "telefono" con un número ficticio
    informacion_personal["telefono"] = "0998789952"

# Elimina la clave "edad"
del informacion_personal["edad"]

# Imprime el diccionario final
print(informacion_personal)
