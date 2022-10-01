"""
DnD Character Creation from API

This program will pull data from an API and create a random character for your DnD campaign. 
It will calculate proficiencies and distribute skill points accordingly. 

"""
# Importing necessary libraries
import requests
import pprint as pp
import json
import random

""""
Possible response codes for GET method

USE print(response.status_code) to get output

200: Everything went okay, and the result has been returned (if any).
301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
401: The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.
403: The resource you’re trying to access is forbidden: you don’t have the right perlessons to see it.
404: The resource you tried to access wasn’t found on the server.
503: The server is not ready to handle the request.
"""

# Functions definition
def CreateRandomRace(RaceList) :
    return random.choice(list(RaceList.values()))

def CreateRandomClass(ClassList) :
    return random.choice([ClassList.values()])

# Defining PrettyPrinter to have a nicer output
PrettyPrinter = pp.PrettyPrinter()
MainUrl = "https://www.dnd5eapi.co/api"

# Defining Races Dictionary 

RacesDict = {
            "DragonBorn" : MainUrl + "/races/dragonborn", 
            "Dwarf" : MainUrl + "/races/dwarf",
            "Elf" : MainUrl + "/races/elf",
            "Gnome" : MainUrl + "/races/gnome" ,
            "HalfElf" : MainUrl + "/races/half-elf",
            "HalfOrc" : MainUrl + "/races/half-orc",
            "Halfling" : MainUrl + "/races/halfling",
            "Tiefling" : MainUrl + "/races/tiefling"   }


#Defining Classes Dictionary

ClassesDict = {
            "Barbarian" : MainUrl + "/classes/barbarian", 
            "Bard" : MainUrl + "/classes/bard",
            "Cleric" : MainUrl + "/classes/cleric",
            "Druid" : MainUrl + "/classes/druid" ,
            "Fighter" : MainUrl + "/classes/fighter",
            "Monk" : MainUrl + "/classes/monk",
            "Paladin" : MainUrl + "/classes/paladin",
            "Ranger" : MainUrl + "/classes/ranger" ,  
            "Rogue" : MainUrl + "/classes/rogue" ,
            "Sorcerer" : MainUrl + "/classes/sorcerer" ,
            "Warlock" : MainUrl + "/classes/warlock" ,
            "Wizard" : MainUrl + "/classes/wizard" ,}


RandomRace = requests.get(CreateRandomRace(RacesDict))
RandomClass = requests.get(CreateRandomRace(ClassesDict))


PrettyPrinter.pprint("##############################RACE##############################")
PrettyPrinter.pprint(RandomRace.json())

PrettyPrinter.pprint("##############################CLASS##############################")
PrettyPrinter.pprint(RandomClass.json())



#print(response.status_code)
#PrettyPrinter.pprint(races.json())
#PrettyPrinter.pprint(classes.json())