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
import streamlit as stl
import pandas as pd


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
            "Human" : MainUrl + "/races/human",
            "Tiefling" : MainUrl + "/races/tiefling"   }

RacesImages = {
            "Dragonborn" : "https://www.dndbeyond.com/avatars/thumbnails/6/340/420/618/636272677995471928.png", 
            "Dwarf" : "https://www.dndbeyond.com/avatars/thumbnails/6/254/420/618/636271781394265550.png",
            "Elf" : "https://www.dndbeyond.com/avatars/thumbnails/7/639/420/618/636287075350739045.png",
            "Gnome" : "https://www.dndbeyond.com/avatars/thumbnails/6/334/420/618/636272671553055253.png" ,
            "Half-Elf" : "https://www.dndbeyond.com/avatars/thumbnails/6/481/420/618/636274618102950794.png",
            "Half-Orc" :  "https://www.dndbeyond.com/avatars/thumbnails/6/466/420/618/636274570630462055.png",
            "Halfling" :  "https://www.dndbeyond.com/avatars/thumbnails/6/256/420/618/636271789409776659.png",
            "Human" : "https://www.dndbeyond.com/avatars/thumbnails/6/258/420/618/636271801914013762.png",
            "Tiefling" :  "https://www.dndbeyond.com/avatars/thumbnails/7/641/420/618/636287076637981942.png" }


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

# ClassesImages = {
#             "Barbarian" : MainUrl + "/classes/barbarian", 
#             "Bard" : MainUrl + "/classes/bard",
#             "Cleric" : MainUrl + "/classes/cleric",
#             "Druid" : MainUrl + "/classes/druid" ,
#             "Fighter" : MainUrl + "/classes/fighter",
#             "Monk" : MainUrl + "/classes/monk",
#             "Paladin" : MainUrl + "/classes/paladin",
#             "Ranger" : MainUrl + "/classes/ranger" ,  
#             "Rogue" : MainUrl + "/classes/rogue" ,
#             "Sorcerer" : MainUrl + "/classes/sorcerer" ,
#             "Warlock" : MainUrl + "/classes/warlock" ,
#             "Wizard" : MainUrl + "/classes/wizard" ,}


stl.set_page_config(page_title = "DnD Character Creation", 
                    page_icon = "https://cdn.shopify.com/s/files/1/0057/6408/7896/articles/DD-Logo_700x.jpg?v=1572377159)",
                    layout = "wide")
stl.title("DnD Character Creation")


if stl.button("Generate Race"):
    RandomRace = requests.get(CreateRandomRace(RacesDict))
    RaceName = RandomRace.json()["name"]
    # AbilityScores = pd.DataFrame([RandomRace.json()["ability_bonuses"]]).transpose()
    # Languages = pd.DataFrame([RandomRace.json()["languages"]]).transpose()
    # Traits = pd.DataFrame([RandomRace.json()["traits"]]).transpose()
    # Subraces = pd.DataFrame([RandomRace.json()["subraces"]]).transpose()
    RandomRace = pd.DataFrame([RandomRace.json()])
    AbilityScores = list(RandomRace.pop("ability_bonuses"))[0]
    Languages = list(RandomRace.pop("languages"))[0]
    Traits = list(RandomRace.pop("traits"))[0]
    Subraces = list(RandomRace.pop("subraces"))[0]
    RandomRace = RandomRace.transpose()
    
    #Display in text and image your race 
    stl.subheader("Your Race is -> " + RaceName)
    stl.image(RacesImages[RaceName])

    #Display race stats
    stl.subheader("Your race stats are:")
    stl.write(RandomRace)
    stl.subheader("Your race ability bonuses are:")
    for Ability in AbilityScores :
        stl.text("You have a bonus of " + str(Ability['bonus']) + " in your " + Ability['ability_score']['name'])

    stl.subheader("Your race languages are:")
    for Language in Languages :
        stl.text("You can speak " + Language['name'])

    stl.subheader("Your race traits are:")
    for Trait in Traits :
        stl.text("You have the " + Trait["name"] + " trait")
    
    stl.subheader("Your race subraces are:")
    for SubRace in Subraces :
        stl.text("You can choose the " + SubRace["name"] + " subrace")

if stl.button("Generate Class"):
    RandomClass = requests.get(CreateRandomRace(ClassesDict))
    stl.write(RandomClass.json())
