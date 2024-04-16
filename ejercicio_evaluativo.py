"""
Crea una función que reciba dos cadenas de texto casi iguales, a excepción de uno o varios caracteres. 
La función debe encontrarlos y retornarlos en formato lista/array.
- Ambas cadenas de texto deben ser iguales en longitud.
- Las cadenas de texto son iguales elemento a elemento.
- No se pueden utilizar operaciones propias del lenguaje que lo resuelvan directamente.
  
 Ejemplos:
- Me llamo Pepe/ Me llemo Pepo-> ["e", "o"]
- Me.gusta mucho Pyhton / Me gusta mucho Python -> [" ", "t", "h"]
"""

def encontrar_diferencias(cadena1, cadena2):
    # Compara cadenas
    if len(cadena1) != len(cadena2):
        return "Las cadenas no tienen la misma longitud"
    
    diferencias = []
    
    # Itera por caracteres y obtine la posición
    for i in range(len(cadena1)):
        char_cadena1 = cadena1[i]
        char_cadena2 = cadena2[i]
        
        # Compara caracteres
        if char_cadena1 != char_cadena2:
            diferencias.append(char_cadena2)
    
    return diferencias

print(encontrar_diferencias("Me llamo Pepe", "Me llemo Pepo")) 
print(encontrar_diferencias("Me.gusta mucho Pyhton", "Me gusta mucho Python"))
