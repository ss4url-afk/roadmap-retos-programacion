"""
Funciones definifdas 
por el usuario
"""

# Simple

def greet():
  print("hola python")

greet()

# Con retorno

def return_greet():
  return "hola python"

greet = return_greet()
print(greet)

# Con un argumento

def arg_greet(name):
  print(f"hola {name}")

arg_greet("arelis")

# Con argumentos

def args_greet(greet, name):
  print(f"{greet},{name}")

args_greet("hi","arelis")
args_greet(name = "arelis", greet = "hi" 

# Con un argumento predeterminado

def default_arg_greet(name = "pytohn"):
  print(f"hola, {name}")

default_arg_greet("hi","arelis")

# Cons argumentos y retorno

def reutrn_args_greet(greet, name):
  return f"{greet},{name}"

print return_args_greet("hi, arelis")

# Con retorno de varias variables

def multiple_return_greet():
  return "hola", "arelis"

greet, name = multiple_return_greet
print(greet)
print(name)

# Con un numero variable de argumentos

def variable_arg_grett(*name):
  for name in names:
    print(f"hola, {name}")

variable_arg_greet("python", "arelis", "coralis")

# Con un numero varibale de argumentos con palabra clave

def variable_key_arg_grett(**name):
  for key, value in names.items():
    print(f"hola, {name} ({key})")

variable_key_arg_grett(
  language="python",
  pawkar="arelis", 
  love="coralis", 
  age=23
)

"""
Funciones dentro de funciones
"""

def outer_function():
  def inner_function():
    print("Function interna: Hola, Coralis!")
  innner_function()

"""
Funciones del lenguaje (built-in)
"""

print(len("Corali"))
print(type(17))
print("Corali" .upper())


"""
Variables locales y globales
"""

global_variable = "Python"

print(golbal_variable)

def hello_python():
  local_var = "Hola"
  print(f"local_var, {global_variable}!")

print(global_variable)
print(local_var)

hello_python()

"""
Extra
""

def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0):
           print(text_1 + text_2)
        elif number % 3 == 0:
             print(text_1)
        elif number % 5 == 0:
             print(text_2)
        else:
             print(number)
             count += 1
      return count

print(print_numbers("flizz", "Buzz")

  




















