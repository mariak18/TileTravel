#Skrifa forrit sem athugar hver staðsetninginn er og hvert er hægt að fara
# Tekur við inputi sem er N(orth), S(south), e(east), w(west)
# ef inputið er ekki gilt prentast út að það sé ekki gilt og gefur þér vagmöguleikana hvert þú getur farið og leyfir að reyna aftur 
# Forritið leyfir að setja inn input eins oft áður en það kemur að sigur kassanaum (3.1) og prentar út "Victory!"


start_x = 1 
start_y = 1 

while start_x != 3 or start_y != 1 :
    if start_x == 1:   
        if start_y == 1 :
            valid_di = "Nn"
            print("You can travel: (N)orth.")
        elif start_y == 2:
            valid_di = "NnEeSs"
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif start_y == 3 :
            valid_di = "EeSs"
            print("You can travel: (E)ast or (S)outh.")
    elif start_x == 2 :
        if start_y == 1 :
            valid_di = "Nn"
            print("You can travel: (N)orth.")    
        elif start_y == 2 :
            valid_di = "WwSs"
            print("You can travel: (S)outh or (W)est.")
        elif start_y == 3 :
            valid_di = "EeWw"
            print("You can travel: (E)ast or (W)est.")
    elif start_x == 3 :
        if start_y == 1 :
            valid_di = "Nn"
            print("You can travel: (N)orth.")
        elif start_y == 2 :
            valid_di = "NnSs"
            print("You can travel: (N)orth or (S)outh.")
        elif start_y == 3 :
            valid_di = "WwSs"
            print("You can travel: (S)outh or (W)est.")
    
    direction = input("Direction: ")

    if direction in valid_di :
        if direction in "Nn":
            start_y += 1
        elif direction in "Ee":
            start_x += 1
        elif direction in "Ss":
            start_y -= 1 
        elif direction in "Ww":
            start_x -= 1 
    else : 
        print("Not a valid direction!")
        direction = input("Direction: ")
        if direction in valid_di :
            if direction in "Nn":
                start_y += 1
            elif direction in "Ee":
                start_x += 1
            elif direction in "Ss":
                start_y -= 1 
            elif direction in "Ww":
                start_x -= 1 
else : 
    print("Victory!")