from dbm import error

from Jack_Kirby import jackKirbyBasicInfo
from Main import errorMessage, writer, artist
from Stan_Lee import stanLeeBasicInfo


def rickJonesBasicInfo(infoType):
    writer = "Stan Lee"
    artist = "Jack Kirby"
    firstAppearance = "The Incredible Hulk #1 May 1962"
    connections = ["Hulk","Captain America","Captain Marvel"]
    powers = ["Summon past, present, and future Avengers","Super Strength","Durability","Quick Learning"]
    names  = ["Destiny Force","A-Bomb","Whisperer"]
    if infoType == "writer":
        return writer
    elif infoType == "artist":
        return artist
    elif infoType == "First Appearance":
        return firstAppearance
    elif infoType == "Connections":
        return ','.join(connections)
    elif infoType == "powers":
        return ','.join(powers)
    elif infoType == "names":
        return ','.join(names)
    else:
        return errorMessage

def rickJonesDetails(rickInfo):
    if rickInfo == writer:
        return stanLeeBasicInfo()
    if rickInfo == artist:
        return jackKirbyBasicInfo()
