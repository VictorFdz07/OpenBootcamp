import time

def main():
    tiempo_actual = time.time()
    hora_actual = time.localtime(tiempo_actual).tm_hour

    if(hora_actual  >= 19):
        print("¡Ya ha pasado la hora de trabajo!")
    else:
        hora_fin = time.mktime((time.localtime(tiempo_actual).tm_year, time.localtime(tiempo_actual).tm_mon, time.localtime(tiempo_actual).tm_mday, 19, 0, 0, time.localtime(tiempo_actual).tm_wday, time.localtime(tiempo_actual).tm_yday, time.localtime(tiempo_actual).tm_isdst))
        tiempo_restante = (hora_fin - tiempo_actual) // 60
        print("Quedan", tiempo_restante, "minutos de trabajo")
        
if __name__ == '__main__':
    main()