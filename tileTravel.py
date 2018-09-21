#Skrifa forrit sem athugar hver staðsetninginn er og hvert er hægt að fara
# Tekur við inputi sem er N(orth), S(south), e(east), w(west)
# ef inputið er ekki gilt prentast út að það sé ekki gilt og gefur þér vagmöguleikana hvert þú getur farið og leyfir að reyna aftur 
# Forritið leyfir að setja inn input eins oft áður en það kemur að sigur kassanaum (3.1) og prentar út "Victory!"
#https://github.com/mariak18/TileTravel

#1.  Which implementation was easier and why?
    #Fyrri kóðin var einfaldari því að við höfum verið að forrita þannig frá byrjuum erum ný byrjuð að læra um föll. 
#2. Which implementation is more readable and why?
    #Seinni kóðinn er læsilegri því við erum að nota föll og þurfum ekki að setja alltaf það sama aftur og aftur. 
#3. Which problems in the first implementations were you able to solve with the latter implementation?
    #Kóðinn yfir allt er læsilegri og aðalkóðinn er styttri. 

def x_y(x,y):
    '''Tekur inn gildið x og y '''
    return x, y 

def direction_form_input():
    '''Tekur inn átt frá notenda'''
    a = input("Direction: ")
    a = a.lower()
    return a 


def find_valid_dir(a):
    if a == 1:   
        if start_y == 1 :
            valid_di = "n"
            print("You can travel: (N)orth.")
        elif start_y == 2:
            valid_di = "nes"
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        elif start_y == 3 :
            valid_di = "es"
            print("You can travel: (E)ast or (S)outh.")
    elif a == 2 :
        if start_y == 1 :
            valid_di = "n"
            print("You can travel: (N)orth.")    
        elif start_y == 2 :
            valid_di = "ws"
            print("You can travel: (S)outh or (W)est.")
        elif start_y == 3 :
            valid_di = "ew"
            print("You can travel: (E)ast or (W)est.")
    elif a == 3 :
        if start_y == 1 :
            valid_di = "n"
            print("You can travel: (N)orth.")
        elif start_y == 2 :
            valid_di = "ns"
            print("You can travel: (N)orth or (S)outh.")
        elif start_y == 3 :
            valid_di = "ws"
            print("You can travel: (S)outh or (W)est.")
    return valid_di


def direction_in(d, x, y) :
    ''' Uppfæra x og y '''
    if d == "n":
        y += 1
    elif d == "e":
        x += 1
    elif d == "s":
        y -= 1 
    elif d == "w":
        x -= 1 
    return x, y

def valid_input(d, v, x, y):
    if d in v:
        x, y = direction_in(direction, start_x, start_y)
    else : 
        print("Not a valid direction!")
        d = direction_form_input()
        if d in v :
            x, y = direction_in(d, start_x, start_y)
    return x, y


start_x, start_y = x_y(1,1)

while start_x != 3 or start_y != 1 :
    valid_di = find_valid_dir(start_x)
   
    direction = direction_form_input()

    start_x, start_y = valid_input(direction, valid_di, start_x, start_y)
else : 
    print("Victory!")