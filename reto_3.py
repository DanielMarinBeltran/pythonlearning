def run(): 
    
    temperatura_max = int(input())
    temperatura_min = int(input())

    dia= 0
    dia_sin_error = 0
    dia_error = 0


    dia_error_1 = 0
    dia_error_2 = 0
    dia_error_3 = 0


    suma_max = 0
    suma_min = 0


    while temperatura_max != (0) and temperatura_min != (0):
        error_3 = False
        error_2 = False
        error_1 = False
        dia += 1
        if (temperatura_max > 35 and temperatura_min < 5) or (temperatura_min < 5 and temperatura_max > 35):
            error_3= (True)
            dia_error_3 += 1
        elif temperatura_max > 35:
            error_2 = (True)
            dia_error_2 += 1
        elif temperatura_min < 5:
            error_1 = (True)
            dia_error_1 += 1
    
        if error_1 == True or error_2 == True or error_3 == True:
            dia_error += 1
            temperatura_max = int(input())
            temperatura_min = int(input())
            continue

        elif error_1 == False or error_2 == False or error_3 == False:
            suma_max += temperatura_max
            suma_min += temperatura_min
            dia_sin_error += 1
    
        temperatura_max = int(input())
        temperatura_min = int(input())


    print(dia)
    print(dia_error)
    print(dia_error_1)
    print(dia_error_2)  
    print(dia_error_3)
    print((suma_max / dia_sin_error))
    print((suma_min / dia_sin_error))
    print(((dia_error * 100) / dia))
    input()


if __name__ == "__main__":
    run()