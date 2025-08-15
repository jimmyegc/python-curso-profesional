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
