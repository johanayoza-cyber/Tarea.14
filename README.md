Ejercicio de Funciones con Parámetros y Retorno de Valores

Programa en Python que calcula el costo de envío de un paquete según su peso, usando una función con parámetros y return.

Código
python
def calcular_costo_envio(peso_kg, tarifa_por_kg=2.5):
    costo = peso_kg * tarifa_por_kg
    return costo

peso_paquete = 3.2

resultado = calcular_costo_envio(peso_paquete)
print("El costo de envío es:", round(resultado, 2))
Ejecución
bash
python Semana14.py
Estudiante

Marlene Yoza
