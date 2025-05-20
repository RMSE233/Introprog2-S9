array_srt = ["uno", "dos", "tres", "cuatro", "cinco"]
print("Array de cadenas:", array_srt)

#Insertar un elemento al inicio del arreglo
array_srt.insert(0, "cero")
print("Array de cadenas después de insertar 'cero' al inicio:", array_srt)

#contar cuantos elementos hay en el arreglo
cantidad = len(array_srt)   
print("Cantidad de elementos en el arreglo:", cantidad)

#Eliminar un elemento del arreglo
array_srt.remove("tres")
print("Array de cadenas después de eliminar 'tres':", array_srt)

#otra forma de eliminar un elemento del arreglo
array_srt.pop(0)
print("Array de cadenas después de eliminar el elemento en la posicion 2:", array_srt)