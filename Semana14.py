def calcular_costo_envio(peso_kg, tarifa_por_kg=2.5):
    costo = peso_kg * tarifa_por_kg
    return costo

peso_paquete = 3.2

resultado = calcular_costo_envio(peso_paquete)
print("El costo de envío es:", round(resultado,2))