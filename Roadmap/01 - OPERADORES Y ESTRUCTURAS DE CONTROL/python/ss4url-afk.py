"""
Operadores
"""

# Operadores aritmeticos
print(f"suma: 10 + 4 = {10 + 4}") 
print(f"Resta: 10 - 4 = {10 - 4}") 
print(f"Multiplicacion: 10 * 4 = {10 * 4}") 
print(f"Division: 10 / 4 = {10 / 4}") 
print(f"Modulo: 10 % 4 = {10 %  4}") 
print(f"Exponente: 10 ** 4 = {10 ** 4}") 
print(f"Division entera: 10 // 4 = {10 // 4}") 


#Operadores de comparacion

print("igualdad: 10 == 3 es {10 == 3}")
print("Desigualdad: 10 != 3 es {10 != 3}")
print("mayor que: 10 > 3 es {10 > 3}")
print("menor que: 10 < 3 es {10 < 3}")
print("mayor o igual que: 10 >= 3 es {10 >= 3}")
print("menor o igual que: 10 <= 3 es {10 <= 3}")

# Operadores lógicos

print(f"AND: 10 + 3 == 13   and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4} ")
print(f"OR: 10 + 3 == 13   or 5 - 1 == 4 es {10 + 3 == 13 or 5 - 1 == 4} ")
print(f"NOT: 10 + 3 == 14 es {10 + 3 == 14}") False
print(f"NOT: not 10 + 3 = == 14 es {not 10 + 3 == 14}") True

#Operadores de asignacion
my_number = 11 # asignacion
print(my_number)
my_number += 1 # suma y asignacion              12
print(my_number)
my_number -= 1 # resta y asignacion             11
print(my_number)
my_number *= 2 # multiplicacion y asignacion    22
print(my_number)
my_number /= 2 # division y asignacion          11.0
print(my_number)
my_number %= 2 # modulo y asignacion            1.0 
print(my_number)
my_number **= 1 # exponente y asignacion        1.0
print(my_number)
my_number //= 1 # division entera y asignacion  1.0


# Operadores de identidad

my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}") True
print(f"my_number is not my_new_number es {my_number is not my_new_number}") False

# Operadores de pertenencia

print("'a' in 'coralis' es {'a' in 'coralis'}") True
print("'x' not in 'coralis' es {'x' not in 'coralis'}") True

# Operadores de bit 

a = 10 # 1010
b = 3 # 0011
print("AND: 10 & 3" = {10 & 3)") # 0010 2
print("OR: 10 | 3" = {10 | 3)") # 1011 11
print("XOR: 10 ^ 3" = {10 ^ 3)") # 1001 9
print("NOT: ~10" = {~10)")              ~11
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2)") # 1010 desplazadno dos veces: primero: 0101 segundo: 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2)") # 1o1o desplazando dos veces: 101000

"""
Estructuras de control
"""

# Condicionales

my_string = "coralis"
if my_string == "arelis":
  print("my_string es 'arelis'")
elif my_string == "coralis":
  print("my_string es 'coralis'")
else:
  print("my_string no es 'arelis' ni 'coralis'")

# Iterativas

for i in range(11):
  print(i)
i = 0
while 1 <= 10:
  print(i)
  i += 1

# Manejo de excepciones

try:
  print(10 / 0)
except:
  print("Se ha producido un error")
finally:
  print("Se ha finalizado el manejo de excepciones")

"""
Extra
"""

for number in range(10, 56):
  if number % 2 == 0 and number != 16 and number % 3 != 0:
    print(number)




