odd = True
with open("namn.txt","r") as namnFilen:
    for line in namnFilen:
        line = line.replace("\n","")
        if odd == True:
            print(line)
            odd = False
        else:
            odd = True



odd = True
with open("namn.txt","r") as namnFilen:
    for line in namnFilen:
        line = line.replace("\n","")
        if odd == True:
            print(line)
        odd = not odd            



#Printa alla namn som finns i filen
import os
import glob


txtfiles = []
for file in glob.glob("*.txt"):
    txtfiles.append(file)



print("Meny\n1. Hej\n2.Avsluta")

#ta bort filen om den finns
if os.path.exists("logg.txt"):
    os.remove("logg.txt")



with open("logg.txt", "w") as filen:
    filen.write("Nu startar programmet\n")
    filen.write("Hej hej\n")


    #allNames = namnFilen.readlines()

#for x in allNames:
    #print(x)










print("*HUVUDMENY*")
