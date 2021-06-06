nombre = input('Digite su nombre: ')
horas_trabajadas = int(input('Digite las horas trabajadas: '))
valor_hora = int(input('Digite el valor de la hora: '))


def sueldo():


    if horas_trabajadas > 40:
        horas_extra = horas_trabajadas - 40
        horas_normales = horas_trabajadas - horas_extra
        valor_horas_extra = horas_extra * (1.5 * valor_hora)

    elif horas_trabajadas <= 40:
        horas_extra = 0
        horas_normales = horas_trabajadas
        valor_horas_extra = 0

    horas_a_pagar_en_total = horas_normales * valor_hora
    sueldo_bruto = horas_a_pagar_en_total + valor_horas_extra
    parafiscales = sueldo_bruto * 0.09
    salud = sueldo_bruto * 0.04
    pencion = sueldo_bruto * 0.04
    suma_descuentos = parafiscales + pencion + salud
    sueldo_neto = sueldo_bruto - suma_descuentos
    prima = sueldo_bruto * 0.0833
    cesantias = sueldo_bruto * 0.0833
    intereses_cesantias = sueldo_bruto * 0.01
    provisiones_vacaciones = sueldo_bruto * 0.0417

    print(horas_a_pagar_en_total)
    print(valor_horas_extra)
    print(sueldo_bruto)
    print(parafiscales)
    print(salud)
    print(pencion)
    print(suma_descuentos)
    print(sueldo_neto)
    print(prima)
    print(cesantias)
    print(intereses_cesantias)
    print(provisiones_vacaciones)


sueldo()