"""
DnD Character Creation from API

This program will pull data from an API and create a random character for your DnD campaign. 
It will calculate proficiencies and distribute skill points accordingly. 

"""
# Importing necessary libraries
from genericpath import exists
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

ClassesImages = {
            "Barbarian" :  "https://www.dndbeyond.com/avatars/thumbnails/6/342/420/618/636272680339895080.png", 
            "Bard" :  "https://www.dndbeyond.com/avatars/thumbnails/6/369/420/618/636272705936709430.png",
            "Cleric" :  "https://www.dndbeyond.com/avatars/thumbnails/6/371/420/618/636272706155064423.png",
            "Druid" :  "https://www.dndbeyond.com/avatars/thumbnails/6/346/420/618/636272691461725405.png" ,
            "Fighter" :  "https://www.dndbeyond.com/avatars/thumbnails/6/359/420/618/636272697874197438.png",
            "Monk" : "https://www.dndbeyond.com/avatars/thumbnails/6/489/420/618/636274646181411106.png",
            "Paladin" :  "https://www.dndbeyond.com/avatars/thumbnails/6/365/420/618/636272701937419552.png",
            "Ranger" :  "https://www.dndbeyond.com/avatars/thumbnails/6/367/420/618/636272702826438096.png" ,  
            "Rogue" :  "https://www.dndbeyond.com/avatars/thumbnails/6/384/420/618/636272820319276620.png" ,
            "Sorcerer" :  "https://www.dndbeyond.com/avatars/thumbnails/6/485/420/618/636274643818663058.png" ,
            "Warlock" :  "https://www.dndbeyond.com/avatars/thumbnails/6/375/420/618/636272708661726603.png" ,
            "Wizard" :  "https://www.dndbeyond.com/avatars/thumbnails/6/357/420/618/636272696881281556.png" ,}


stl.set_page_config(page_title = "DnD Character Creation", 
                    page_icon = "https://cdn.shopify.com/s/files/1/0057/6408/7896/articles/DD-Logo_700x.jpg?v=1572377159)",
                    layout = "wide")
stl.title("DnD Character Creation")


if stl.button("Generate Race"):
    RandomRace = requests.get(CreateRandomRace(RacesDict))
    RaceName = RandomRace.json()["name"]
    RandomRace = pd.DataFrame([RandomRace.json()])
    AbilityScores = list(RandomRace.pop("ability_bonuses"))[0]
    Languages = list(RandomRace.pop("languages"))[0]
    Traits = list(RandomRace.pop("traits"))[0]
    Subraces = list(RandomRace.pop("subraces"))[0]

    #Transposing data to have it look nice in the table 
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
    ClassName = RandomClass.json()["name"]
    RandomClass = pd.DataFrame([RandomClass.json()])

    ProficiencyChoices = list(RandomClass.pop("proficiency_choices"))[0]
    Proficiencies = list(RandomClass.pop("proficiencies"))[0]
    SavingThrows = list(RandomClass.pop("saving_throws"))[0]
    StartingEquipment = list(RandomClass.pop("starting_equipment"))[0]
    StartingEquipmentOptions = list(RandomClass.pop("starting_equipment_options"))[0]
    MultiClassing = list(RandomClass.pop("multi_classing"))[0]
    SubClasses = list(RandomClass.pop("subclasses"))[0]
    if "spellcasting" in RandomClass :
        Spellcasting = list(RandomClass.pop("spellcasting"))[0]
    
    RandomClass = RandomClass.transpose()

    stl.header("Your class is -> " + ClassName)
    stl.image(ClassesImages[ClassName])

    stl.header("Your class stats are: ")
    stl.write(RandomClass)

    stl.header("Your proficiency choices are: ")
    for choices in ProficiencyChoices :
        stl.text(choices["desc"])

    stl.header("Your proficiencies are: ")
    for proficiency in Proficiencies :
        stl.text(proficiency["name"])

    stl.header("Your saving throws are: ")
    for throw in SavingThrows :
        stl.text(throw["name"])

    stl.header("Your starting equipment is: ")
    for equipment in StartingEquipment :
        stl.text(str(equipment["quantity"]) + " " + equipment["equipment"]["name"])

    stl.header("Your starting equipment choices are: ")
    for choices in StartingEquipmentOptions :
        stl.text(choices["desc"])

    stl.header("In order to multi-class you need to: ")
    if "prerequisites" in MultiClassing :
        for prerequisites in MultiClassing["prerequisites"] :
            stl.text("A pre-requisite of a minimum of " + str(prerequisites["minimum_score"]) + 
                    " in " + prerequisites["ability_score"]["name"])

    if "proficiciencies" in MultiClassing :
        for proficiencies in MultiClassing["proficiencies"] :
            stl.text("A pre-requisite of proficiency in " + proficiencies["name"])

    if "proficiency_choices" in MultiClassing :
        for choices in MultiClassing["proficiency_choices"] :
            stl.text("Choose " + str(choices["choose"]) +  " proficiency from:")
            for options in choices["from"]["options"] :
                stl.text(options["item"]["name"])
    else :
        pass


    stl.header("You can choose the following subclasses: ")
    for subclasses in SubClasses :
        stl.text(subclasses["name"])

    
    #stl.text()
    if 'Spellcasting' in globals() :
        stl.header("Your have the following spellcasting abilities: ")
        stl.text(Spellcasting["spellcasting_ability"]["name"] + " is your spellcasting ability")
        for abilities in Spellcasting["info"] :
            stl.subheader(abilities["name"])
            for description in abilities["desc"] :
                stl.text(description)
    else :
        pass
