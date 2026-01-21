"""
#diccionarios {}
diccionario={'uno': 1,'dos': 2, 'tres': 3}

print(diccionario)
#imprime el contenido de la clave
print(diccionario['dos'])

#Cuando no tengo un keys definido y no cause error None o mensaje de error con una,
print(diccionario.get('uno'))
print(diccionario.get('cuatro',"Clave no definida"))

#Recorrido de un diccionario (keys)

print("Recorrido de un diccionario")
for e in diccionario:
    print(e)
#Consultar solo las claves
print("Consultar solo claves")
for k in diccionario.keys():
    print(k)
#Recorrido de un diccionario
print("Recorrido de un diccionario")
for j in diccionario.values():
    print(j)
#consultar keys y values items()
#valores impresos en parentesis
print("consultar keys y values items()")
for c in diccionario.items():
    print(c)

#añadir elementos a un diccionario
print("añadir elementos a un diccionario")
diccionario['cuatro'] = 4
print(diccionario)

#añadir elementos con fn. setdefault(clave,valor)
diccionario.setdefault('cinco',5)
print(diccionario)

diccionario.setdefault('seis')
print(diccionario)

#Modificar elementos
print("Modificar elementos")
diccionario['seis'] = 6
print(diccionario)

#Elimiar un elemnto del diccionario con fn pop
print("Elimiar un elemnto del diccionario con fn pop")
diccionario.pop('uno')
print(diccionario)

#Elimnar un elemento del diccionario con popitem
print("Elimnar un elemento del diccionario con popitem")
print(diccionario.popitem())
print(diccionario)

#Elimnar un elemento del diccionario con fn del()
del diccionario['cinco']
print(diccionario)

#Elimnar un elemento del diccionario con fn clear()
        #diccionario.clear()

#len   
diccionario={'uno': 1,'dos': 2, 'tres': 3}
print(len(diccionario))

#comprobar si un elemento esta en un diccionario
print('uno' in diccionario)
print('cuatro' in diccionario)
#comprobar si un elemento esta en un diccionario (not in)
print('cinco' not in diccionario)

if 'uno' in diccionario:
    del diccionario ['uno']
    print(diccionario)

diccionarioUno={'uno': 1,'dos': 2, 'tres': 3}
diccionarioDos={'uno': 1,'dos': 2, 'tres': 3}
diccionarioTres={'uno': 1,'dos': 2, 'tres': 3, 'cuatro':4}

print(diccionarioDos == diccionarioUno)
print(diccionarioTres == diccionarioUno)


#Diciconarios anidados
estudiantes = {'Estudiante 1':{'nombre': 'Alexis', 'apellido': 'Chasi'},'Estudiante 2':{'nombre': 'Leo', 'apellido': 'Defaz'}}
print(estudiantes['Estudiante 2']['apellido'])
print(estudiantes['Estudiante 1']['nombre'])

#obtener lista
print(list(estudiantes))

#copiar elementos con copy()
diccionario2 = estudiantes.copy()
print(diccionario2)

diccionario3 = {"a": 1, "b": 2}

diccionario3.update({"b": 20, "c": 3})

print(diccionario3)
"""