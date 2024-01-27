print("Předvídač")
print(" ")

známky = []
váhy = []



while True:
    
 option1 = True
 option2 = True
    
 while option1 == True:
     známka = int(input("Zadejte známku (1-5): "))
     if 0< známka <6:
         option1 = False
     else :
         print("Zadali jste špatnou možnost")
           
 while option2 == True:
     váha = int(input("Zadejte váhu (1-10): "))
     if 0<váha<11:
         option2 = False
     else:
         print("Zadali jste špatnou možnost")
         
 váhy.append(váha)
 výpočet = známka * váha
 známky.append(výpočet)
 výpočet= sum(známky)/sum(váhy)
 print(" ")
 print(f"Váš průměr je {výpočet}")