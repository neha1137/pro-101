import random
response = input("Press 'y' if u wanna roll a dice else 'n' : ")


while response=="y" :
    no = random.randint(1,6)

    if no==1 :
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        re = input("Press 'y' to roll again and 'n' to exit: ")       
            
    elif no==2 :
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[     ]")
        print("[-----]")
        re = input("Press 'y' to roll again and 'n' to exit: ")   
            
    elif no==3 :
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
        re = input("Press 'y' to roll again and 'n' to exit: ")     
            
    elif no==4 :
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        re = input("Press 'y' to roll again and 'n' to exit: ")    
            
    elif no==5 :
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        re = input("Press 'y' to roll again and 'n' to exit: ")   
            
    elif no==6 :
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")
        re = input("Press 'y' to roll again and 'n' to exit: ")  

    response = re           
