from assets import JsonReader
import os

print("Welcome !!")

def conjuguer(temps, radical, groupe):
    global file
    global conjug
    file = f"assets/{temps}/{groupe}.json"
    print(file)
    if os.path.exists(file) != True and os.path.exists(f"assets/{temps}/allgroupes.json") != True:
        print("Error no find this time :( Sorry :(")
        pass
    elif os.path.exists(f"assets/{temps}/allgroupes.json") == True:
        file = f"assets/{temps}/allgroupes.json"
    running = 0
    while running != 6:
        running = running + 1
        conjug = f"{radical + ' ' + groupe}: je {radical + JsonReader.readJson(toread='1', file=file)} tu {radical + JsonReader.readJson(toread='2', file=file)} il {radical + JsonReader.readJson(toread='3', file=file)} nous {radical + JsonReader.readJson(toread='4', file=file)} vous {radical + JsonReader.readJson(toread='5', file=file)} ils {radical + JsonReader.readJson(toread='6', file=file)}"

    if os.path.exists(f"Conjugaisons/{radical + '_' + groupe}.txt") != True:
        thefile = open(f"Conjugaisons/{radical + '_' + groupe}.txt", "w+")
        thefile.write(conjug)
        thefile.close()
        print(f"We have save the conjugaisons on: Conjugaisons/{radical + '_' + groupe}.txt")
    else:
        print("a file have already create we found this conjugaison:")
    print(conjug)


if __name__ == "__main__":
    temps = input("Temps: ")
    radical = input("radical: ")
    groupe = input("groupe (er, ir , endre, ...): ")
    conjuguer(temps=temps, radical=radical, groupe=groupe)