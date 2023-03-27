import json
def readJson(toread, file):

    with open(file) as f:
        injson = json.load(f)

    toreturn = injson[toread]
    return toreturn