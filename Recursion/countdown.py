def cuenta_regresiva(n):

    n -= 1 

    if n > 0:
        print (n)
        cuenta_regresiva(n)
        
    else:
        print("0")
        
    print("Fin de la función", n)
    
cuenta_regresiva(5)