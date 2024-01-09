import math
def okomura_extension():
    #Formula de OKUMURA-HATA
    def hata_extension_urban(f_MHz, h_bs, h_mobile, d_km, c_m, a_hr):
        L_urban = 46.3 + 33.9 * math.log10(f_MHz) - 13.82 * math.log10(h_bs) - a_hr + (44.9 - 6.55 * math.log10(h_bs)) * math.log10(d_km) + c_m
        return L_urban

    # Solicitar al usuario que ingrese los valores
    print("----------------------------------------------------------------------------------------------------------------------")
    frecuencia = float(input("Ingrese la frecuencia de la portadora en MHz: "))
    altura_base = float(input("Ingrese la altura efectiva de la antena base en metros: "))
    altura_mobile = float(input("Ingrese el ajuste de altura para la antena móvil: "))
    distancia_km = float(input("Ingrese la distancia entre antenas en kilómetros: "))
    constante_adicional = float(input("Ingrese la constante adicional específica del entorno: [Suburbano 0 - Urbano 3]"))
    print("----------------------------------------------------------------------------------------------------------------------")

    # Solicitar al usuario el tipo de entorno urbano
    print("----------------------------------------------------------------------------------------------------------------------")
    print("[Factor de Correción A(Hmobile)]")
    print("[1] Ciudad pequeña o mediana")
    print("[2] Gran ciudad")
    print("[3] Salir")
    print("----------------------------------------------------------------------------------------------------------------------")
    opcion_urbana = int(input(""))

    def calcular_a_hr_urbano(fc, hr, opcion):
        # Cálculo de a(hmobile) para entornos urbanos según la opción seleccionada
        if opcion == 1:
            # Para una ciudad pequeña o mediana
            a_hr = (1.1 * math.log10(fc) - 0.7) * hr - (1.56 * math.log10(fc) - 0.8)
        elif opcion == 2:
            #Para una gran ciudad
            if fc >= 300:
                a_hr = 3.2 * (math.log10(11.75 * hr))**2 - 4.97
            else:
                a_hr = 8.29 * (math.log10(1.54 * hr))**2
        else:
            a_hr = None
        return a_hr

    # Calcular a(hmobile) para el entorno urbano seleccionado
    a_hr_urbano = calcular_a_hr_urbano(frecuencia, altura_base, opcion_urbana)

    # Calcular la pérdida de trayectoria en un entorno urbano
    p_loss_urban = hata_extension_urban(frecuencia, altura_base, altura_mobile, distancia_km, constante_adicional, a_hr_urbano)
    print("----------------------------------------------------------------------------------------------------------------------")
    print(f"La pérdida de trayectoria en un entorno urbano es: [{round(p_loss_urban, 3)} dB]")
