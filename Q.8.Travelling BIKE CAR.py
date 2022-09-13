def Travelling(BIKE,CAR):
    if BIKE<CAR :
        return "BIKE"
    if BIKE>CAR:    
        return "CAR"
    if BIKE==CAR:      
        return "SAME"
BIKE = int(input("entere the number..."))
CAR = int(input("enter the number   .."))
z=Travelling(BIKE,CAR)
print(z)


# input = 1,5   , 4,2   , 6,6
# output = BIKE  ,CAR   , SAME