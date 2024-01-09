import math
def okumura():

    def okumura_hata(fc, ht, hr, d, a_hr):
        # Cálculo de la pérdida de trayectoria para un entorno urbano según Okumura-Hata
        L = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(ht) - a_hr + (44.9 - 6.55 * math.log10(ht)) * math.log10(d)
        return L

    def calcular_a_hr_urbano(fc, hr, opcion):
        # Cálculo de a(hr) para entornos urbanos según la opción seleccionada
        if opcion == 1:
            a_hr = (1.1 * math.log10(fc) - 0.7) * hr - (1.56 * math.log10(fc) - 0.8)
        elif opcion == 2:
            if fc >= 300:
                a_hr = 3.2 * (math.log10(11.75 * hr))**2 - 4.97
            else:
                a_hr = 8.29 * (math.log10(1.54 * hr))**2
        else:
            a_hr = None
        return a_hr

    while True:
        print("----------------------------------------------------------------------------------------------------------------------")
        print("Opciones:")
        print("1. Para un entorno urbano")
        print("2. Para un entorno suburbano")
        print("3. Para un entorno rural")
        print("4. Salir")

        opcion_entorno = int(input("Seleccione una opción de entorno: "))

        if opcion_entorno == 1:  # Menú para entorno urbano
            print("----------------------------------------------------------------------------------------------------------------------")
            print("[ENTORNO URBANO]")
            print("Opciones para un entorno urbano:")
            print("1. Para una ciudad pequeña o mediana")
            print("2. Para una gran ciudad")
            print("3. Volver al menú principal")

            opcion_urbana = int(input("Seleccione una opción urbana: "))

            if opcion_urbana in [1, 2]:
                # Entrada de datos
                print("----------------------------------------------------------------------------------------------------------------------")
                fc = float(input("Ingrese la frecuencia de la portadora en MHz (fc): "))
                ht = float(input("Ingrese la altura efectiva de la antena transmisora en metros (ht): "))
                hr = float(input("Ingrese la altura efectiva de la antena receptora en metros (hr): "))
                d = float(input("Ingrese la distancia entre las antenas en kilómetros (d): "))
                # Cálculo de a(hr)
                a_hr_urbano = calcular_a_hr_urbano(fc, hr, opcion_urbana)

                if a_hr_urbano is not None:
                     # Cálculo de pérdida de trayectoria
                    p_loss = okumura_hata(fc, ht, hr, d, a_hr_urbano)
                    print(f"La pérdida de trayectoria en un entorno urbano es: [{round(p_loss, 3)} dB]")
            elif opcion_urbana == 3:
                continue
            else:
                print("Opción inválida")

        elif opcion_entorno == 2:  # Entorno suburbano
            print("----------------------------------------------------------------------------------------------------------------------")
            print("[ENTORNO SUBURBANO]")
            L_urbano = float(input("Ingrese la pérdida de trayectoria en un entorno urbano (L): "))
            fc = float(input("Ingrese la frecuencia de la portadora en MHz (fc): "))
            # Cálculo de pérdida de trayectoria en entorno suburbano
            L_suburbano = L_urbano - 2 * (math.log10(fc / 28))**2 - 5.4
            print(f"La pérdida de trayectoria en un entorno suburbano es: [{round(L_suburbano, 3)} dB]")
        
        elif opcion_entorno == 3:  # Entorno rural
            print("----------------------------------------------------------------------------------------------------------------------")
            print("[ENTORNO RURAL]")
            L_urbano = float(input("Ingrese la pérdida de trayectoria en un entorno urbano (L): "))
            fc = float(input("Ingrese la frecuencia de la portadora en MHz (fc): "))
            # Cálculo de pérdida de trayectoria en entorno rural
            L_rural = L_urbano - 4.78 * (math.log10(fc))**2 - 18.73 * math.log10(fc) - 40.98
            print(f"La pérdida de trayectoria en un entorno rural es: [{round(L_rural, 3)} dB]")

        elif opcion_entorno == 4:
            break
        
        else:
            print("Opción inválida")

