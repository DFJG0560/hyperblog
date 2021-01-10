def run():
    hour = int(input("ingrese su hora de entrada:"))
    if hour< 5:
        print("usted llego antes de la hora")
    elif hour==5:
        print("usted llego a la hora")
    else:
        print("usted llego tarde")


if __name__=="__main__":
    run()