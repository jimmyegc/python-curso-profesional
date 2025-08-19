# comentario de línea

"""
  Código comentado esto no se ejecutara...
"""

print("Hola")

# Tipos de datos (strings, integers, floats, booleans)

# strings
first_name = "Jimbo"
# integers
age = 21
# floats
price = 1500.99
# booleans
is_active = False

print(type(first_name))
print(type(age))
print(type(price))
print(type(is_active))

# Constantes (No existen en Python)
VERSION = 3.14
print(VERSION)

# Numeros
number = 20
result = number * 3

print ("El resultado es:", result)

# Operadores relacionales
# ==, >, >=, <, <=, !=

number_one = 10
number_two = 20

result = number_one != number_two

print(result)
print(type(result))

# Operadores lógicos and, or, not
result = (
  True
  and True
  and number_one != number_two
  and number_one < 100 
  and number_two > 200
)

print (result)

# Pedir valores por teclado
# entrada = input("Ingrese el numero #1:")
# print("Ingresaste:", entrada)

# Multiples variables
# first_name = "Jimbo"
# age = 13
# is_active = True 

first_name, age, is_active = "Jimbo", 13, True 

print(first_name)
print(age)
print(is_active)

first_name = "Uriel"
last_name = "Hernandez"
full_name = first_name + " " + last_name 

print(full_name)

# Listas
my_list = ["String", 10, 3.14, True, [1,2,3,4,5]]
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"]

print(my_list)
print(type(my_list))
print(courses[0])
print(courses)
print(len(courses))
print(courses[-1]) # MongoDB 

# Sub listas
new_list = [
  courses[0],
  courses[1],
  courses[2],
]

print(new_list) 

sub_list = courses[0:3] # courses[:3]
sub_list = courses[2:] 
courses_copy = courses[:] # Shallow copy

print(sub_list) 
print(courses_copy) 

courses.append("Ruby on rails")
# courses[0] = "changed"
courses.insert(3, "JavaScript jeje")

new_courses = ["React", "Vue"]
courses.extend(new_courses)

print(courses)

print("Python" in courses)
print(courses.index("Python"))
courses.remove("MongoDB")
courses.pop()
print(courses)

# courses.clear()
# print(courses)

# copy, reverse, sort
copy_list = courses[:] # Shallow copy
copy_list = courses.copy() 

# reverse_list = courses[::-1]
# print(reverse_list)

print(copy_list)
courses.reverse()

courses.sort(reverse=True) # Z-a
print(courses)

# Matriz
matrix = [
  [1,2,3], #0
  [4,5,6], #1
  [7,8,9]  #2
]

print(matrix)

print(matrix[2][2])



resume = {
    "experience": "a lot",
    "open_to_work": True,
    "languages": ["Python", "React", "SQL"],
    "url": "https://jimmygarcia.dev/"
}

def seeking_job(resume):  
  return resume

seeking_job(resume)

# Tuplas
settings = ('localhost', 3306, True)
print (settings)
print (type(settings))

numbers = 1, 2, 3, 4, 5
print (numbers)
print (type(numbers))


# Strings
message = "Hola mundo!"

print(message[5])
print(type (message))
print(len(message))

print('!' in message)
print(message.index('!'))

message2 = message[1:]
print(message2)

# Strings como listas ( split join)
# split -> lista
# join -> String
courses = "Python PHP Ruby Django MongoDB"
list_courses = courses.split(' ')

print(courses)
print(list_courses)

messages_courses = ' '.join(courses)
print(messages_courses)
print(type(messages_courses))

# forma 1 de generar un string
name = "Jimmy"
last_name = "Garcia"

full_name = name + " " +last_name
print(full_name)

# forma 2 de generar un string 
full_name = ' '.join([name, last_name])
print(full_name)

# forma 3 (%s)
full_name = 'El nombre completo es: %s %s' %(name, last_name)
print(full_name)

# forma 4 (format)
base = 'El nombre completo es: {} {}. Su edad es: {}'
full_name = base.format(name, last_name, 45)

print(full_name)

#name = input('Ingresa tu nombre:')
#last_name = input('Ingresa tu apellido:')
#age = input('Ingresa tu edad:')
#full_name = base.format(name, last_name, age)
#print(full_name)

base = 'El nombre completo es: {name} {last_name}. Su edad es: {age}'
full_name = base.format(age=45, name=name, last_name=last_name)
print(full_name)

# F-string
full_name = f"El nombre completo es: {name} {last_name}"
print(full_name)

# Print
name = "Jimbo"
last_name = "Borroso"

print("El nombre completo es:", name, last_name, sep="***") # sep = Separación

# Busqueda en listas
title = "   Curso profesional de Python!   "
print (
  'Curso' in title
)

print(
  title.count('Curso')
)

print(
  title.lower().startswith('c')
)

print(
  title.endswith("!")
)

print(title.strip()) # Standarizar

print(
  title.find('P')
)

print('6'.isnumeric())

# Diccionarios | clave (llave) : valor
# String, tuplas, int, float, booleans

usuario = {
  "name": "jimbo",
  "age": 45,
  "active": True,
  'courses': ["Python", "Django", "Redis"],
  'settings': (123, True)
}

print(usuario)

print('name' in usuario)
print(
  usuario['name']
)

print(usuario.get('password', 'Lo siento, el valor no existe.'))

usuario['last_name'] = "Rosso"
print(usuario)

# keys, values, items
print('--- keys ---')
print(
  list(usuario.keys())
)

# print(tuple(usuario.keys()))

print('--- values ---')
print(
  list(usuario.values())
)

print('--- items ---')
print(
  list(usuario.items())
)

print(len(usuario))

usuario.update({
  'name': 'Mi nombre',
  'last_name': "Apellido",
  # 'courses': None
})

print(usuario)

usuario.setdefault('id', 1000)
print(usuario)

courses = usuario.get('courses', [])
courses.append('React')
courses.append('Vue')

print(usuario)

del usuario['courses']
print(usuario)

value = usuario.pop('settings')
print(usuario)

usuario.clear()
print(usuario)

# Ciclos y condiciones

# None

# True / False

"""
if <bool>:
    print("hola mundo)
    print("Nos encontramos en el curso de Python)
"""
sum = 5 + 3
if sum > 35:
    print("Hola, la condición es True")
    print("Nos encontramos en el bloque del if.")

print("Fin!")

# "", 0, 0.0, False, [], (), {}, None ->>> Falsos

value = "Elmer"
if value:
    print("La variable tiene un valor")

# Not
value = ""
if not value:
    print(">>> La variable no posee un valor")
else:
    print("La condición no se cumple")

# Ifs anidados
number1 = 10
number2 = 20

if number1 >= 10:
    print("Number1 es mayor igual a 10.")

    if number1 > number2:
        print("Number1 es mayor a number2.")
    else:
        print("Number1 no es mayor a number2.")


color = "Rojo"

"""
if color == "Verde":
    print("Puedes continuar")
else: 
    if color == "Amarillo":
        print("Alto parcial")
    
    if color == "Rojo":
        print("Alto total")
"""

if color == "Verde":
    print("Puedes continuar")
elif color == "Amarillo":
    print("Alto parcial")
elif color == "Rojo":
    print("Alto total")
else:
    print("El color no es válido")

# Match -> Switch

score = 5
match score:
    case 10:
        print("Felicidades, tu calificación es 10.")    
    case 9 | 8:
        print("Felicidades, tu calificación es aprobatoria.")
    case 6 | 7:
        print("Aprobaste la materia.")
    case _:
        print("Lo sentimos calificación no aprobatoria.")

# Operador ternario ( One liner )
score = 15 
message = 'Aprobaste la materia' if score > 5 else 'No aprobaste la materia'
print(message)

# Ciclos | for-each & while

numbers = [1,2,3,4,5]
user = {
    "name": "Jimbo",
    "age:": 40,
    "password": "password123"
}

"""
for <variable> in <collection>:
"""

for n in numbers:
    print('Hola, bloque...', n)

for key,value in user.items():
    print(key, value)

# Range
for number in range(10): # 0-9
    print(number)

print("---")

for number in range(5, 10): # 5-9
    print(number)

print("--- while")

# While
""" 
while <condition>:

"""

counter = 0
while counter < 10:    
    print("valor:", counter)
    counter += 1

print ('--->>>')
"""
from random import randint

number = None 
random_number = randint(0,10)
hits = 0

while number != random_number and hits < 3:
    number = int(input("Ingresa un numero:"))
    if random_number > number:
        print('El numero aleatorio es mayor')
    else:
        print('El numero aleatorio es menor')
    hits += 1
else:
  if number == random_number:
    print(f'Felicidades, encontraste el numero {random_number}')
  else:
    print('Game over')
"""

# continue - break
for number in range(1, 101):
    if number %2 ==0: # Se salta el número par
        continue
    if number == 11: #Termina
        break
    print(number)

