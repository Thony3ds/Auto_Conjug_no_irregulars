from assets import JsonReader
import os

print("Welcome !!")

def conjuguer(temps, radical, groupe, compose):
    global file
    global conjug
    file = f"assets/{temps}/{groupe}.json"
    print(file)
    if os.path.exists(file) != True and os.path.exists(f"assets/{temps}/allgroupes.json") != True and compose != 1:
        print("Error no find this time :( Sorry :(")
        pass
    elif os.path.exists(f"assets/{temps}/allgroupes.json") == True:
        file = f"assets/{temps}/allgroupes.json"
    if compose != 1:
        conjug = f"{radical + ' ' + groupe}: je {radical + JsonReader.readJson(toread='1', file=file)} tu {radical + JsonReader.readJson(toread='2', file=file)} il {radical + JsonReader.readJson(toread='3', file=file)} nous {radical + JsonReader.readJson(toread='4', file=file)} vous {radical + JsonReader.readJson(toread='5', file=file)} ils {radical + JsonReader.readJson(toread='6', file=file)}"
    else:
        composition = input("Etre ou Avoir (ecrit comme ici): ")
        if composition == "Etre" or composition == "Avoir":
            file = f"assets/{temps}/{composition}/{groupe}.json"
            conjug = f"{radical + ' ' + groupe}: j' {JsonReader.readJson(toread='1a', file=file) + ' ' + radical + JsonReader.readJson(toread='1b', file=file)} tu {JsonReader.readJson(toread='2a', file=file) + ' ' + radical + JsonReader.readJson(toread='2b', file=file)} il {JsonReader.readJson(toread='3a', file=file) + ' ' + radical + JsonReader.readJson(toread='3b', file=file)} nous {JsonReader.readJson(toread='4a', file=file) + ' ' + radical + JsonReader.readJson(toread='4b', file=file)} vous {JsonReader.readJson(toread='5a', file=file) + ' ' + radical + JsonReader.readJson(toread='5b', file=file)} ils {JsonReader.readJson(toread='6a', file=file) + ' ' + radical + JsonReader.readJson(toread='6b', file=file)}"
        else:
            print("Error !! pas de Etre n'y de Avoir :(")
    if os.path.exists(f"Conjugaisons/{radical + '_' + groupe}.txt") != True:
        thefile = open(f"Conjugaisons/{radical + '_' + groupe}.txt", "w+")
        thefile.write(conjug)
        thefile.close()
        print(f"We have save the conjugaisons on: Conjugaisons/{radical + '_' + groupe}.txt")
    else:
        print("a file have already create we found this conjugaison:")
    print(conjug)
    return conjug