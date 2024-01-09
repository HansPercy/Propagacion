import math

def ESPACIO():
    
    def calcular_perdida(f, d, n):
        # Fórmula para el cálculo de la pérdida de señal en trayectorias en sistemas prácticos
        perdida = 20 * math.log10(f) + 10 * n * math.log10(d) - 147.56
        return perdida

    # Solicitar al usuario que ingrese los valores de frecuencia y distancia
    print("----------------------------------------------------------------------------------------------------------------------")
    frecuencia = float(input("Ingresa la frecuencia en Hz: "))
    distancia = float(input("Ingresa la distancia en metros: "))

    # Mostrar menú de factores n disponibles
    print("----------------------------------------------------------------------------------------------------------------------")
    print("Exponentes de pérdida:")
    print("1. [Espacio libre] [2]")
    print("2. [Área urbana - radio celular] [2.7 - 3.5]")
    print("3. [Radio celular con sombras] [3 - 5]")
    print("4. [Dentro de edificio con línea de visión] [1.6 - 1.8]")
    print("5. [Obstruido dentro de edificio] [4 - 6]")
    print("6. [Obstruido en fábricas] [2 - 3]")
    print("----------------------------------------------------------------------------------------------------------------------")

    factor_n = float(input("Ingrese n dependiendo el ambiente: "))
    print("----------------------------------------------------------------------------------------------------------------------")

    # Calcular la pérdida de señal
    resultado = calcular_perdida(frecuencia, distancia, factor_n)
    resultado_formateado = round(resultado, 3)  # Redondear a tres decimales

    print(f"La pérdida de señal es: [{resultado_formateado} dB]")