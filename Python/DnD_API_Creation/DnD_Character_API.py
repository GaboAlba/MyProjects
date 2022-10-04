"""
DnD Character Creation from API

This program will pull data from an API and create a random character for your DnD campaign.  

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


# Defining URL where Race Image can be found
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


# Defining URL where Class image can be found 
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



# Setting up page with tab title as DnD Character Creation, and the URL to the page icon
stl.set_page_config(page_title = "DnD Character Creation", 
                    page_icon = "https://cdn.shopify.com/s/files/1/0057/6408/7896/articles/DD-Logo_700x.jpg?v=1572377159)",
                    layout = "wide")
stl.title("DnD Character Creation")



# Defining actions to be taken if the "Generate Race" button is pressed
if stl.button("Generate Race"):
    RandomRace = requests.get(CreateRandomRace(RacesDict))                  #Get information from API
    RaceName = RandomRace.json()["name"]                                    #Extract race name out of API
    RandomRace = pd.DataFrame([RandomRace.json()])                          #Store the Random Race in a DataFrame
    AbilityScores = list(RandomRace.pop("ability_bonuses"))[0]              #Store the Ability bonuses in another variable
    Languages = list(RandomRace.pop("languages"))[0]                        #Store the Languages in another variable
    Traits = list(RandomRace.pop("traits"))[0]                              #Store the Traits in another variable
    Subraces = list(RandomRace.pop("subraces"))[0]                          #Store the Subraces in another variable

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

    #Displaying Languages 
    stl.subheader("Your race languages are:")
    for Language in Languages :
        stl.text("You can speak " + Language['name'])

    #Displaying traits
    stl.subheader("Your race traits are:")
    for Trait in Traits :
        stl.text("You have the " + Trait["name"] + " trait")
    
    #Displaying Subraces 
    stl.subheader("Your race subraces are:")
    for SubRace in Subraces :
        stl.text("You can choose the " + SubRace["name"] + " subrace")


# Defining actions to be taken if the "Generate Class" button is pressed
if stl.button("Generate Class"):
    RandomClass = requests.get(CreateRandomRace(ClassesDict))                           #Get information from API
    ClassName = RandomClass.json()["name"]                                              #Extract class name out of API
    RandomClass = pd.DataFrame([RandomClass.json()])                                    #Store the Random Class in a DataFrame

    ProficiencyChoices = list(RandomClass.pop("proficiency_choices"))[0]                #Store the Proficiency Choices in another variable  
    Proficiencies = list(RandomClass.pop("proficiencies"))[0]                           #Store the Proficiencies in another variable
    SavingThrows = list(RandomClass.pop("saving_throws"))[0]                            #Store the Saving Throws in another variable
    StartingEquipment = list(RandomClass.pop("starting_equipment"))[0]                  #Store the Starting Equipment in another variable
    StartingEquipmentOptions = list(RandomClass.pop("starting_equipment_options"))[0]   #Store the Starting Equipment Options in another variable
    MultiClassing = list(RandomClass.pop("multi_classing"))[0]                          #Store the Multi Class in another variable
    SubClasses = list(RandomClass.pop("subclasses"))[0]                                 #Store the Sub Classes in another variable
    if "spellcasting" in RandomClass :                                                  #Check as not all classes can cast spells
        Spellcasting = list(RandomClass.pop("spellcasting"))[0]                         #Store the Spellcasting in another variable
    
    #Transposing data to have it look nice in the table
    RandomClass = RandomClass.transpose()

    #Display in text and image your class 
    stl.header("Your class is -> " + ClassName)
    stl.image(ClassesImages[ClassName])

    #Display class stats
    stl.header("Your class stats are: ")
    stl.write(RandomClass)

    #Displaying Proficiency Choices 
    stl.header("Your proficiency choices are: ")
    for choices in ProficiencyChoices :
        stl.text(choices["desc"])

    #Displaying Proficiencies 
    stl.header("Your proficiencies are: ")
    for proficiency in Proficiencies :
        stl.text(proficiency["name"])

    #Displaying Saving Throws
    stl.header("Your saving throws are: ")
    for throw in SavingThrows :
        stl.text(throw["name"])

    #Displaying Starting Equipment
    stl.header("Your starting equipment is: ")
    for equipment in StartingEquipment :
        stl.text(str(equipment["quantity"]) + " " + equipment["equipment"]["name"])

    #Displaying Starting Equipment Choices  
    stl.header("Your starting equipment choices are: ")
    for choices in StartingEquipmentOptions :
        stl.text(choices["desc"])

    #Displaying Multi Class 
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


    #Displaying Subclasses 
    stl.header("You can choose the following subclasses: ")
    for subclasses in SubClasses :
        stl.text(subclasses["name"])

    #Displaying Spellcasting, verifying that it exists
    if 'Spellcasting' in globals() :
        stl.header("Your have the following spellcasting abilities: ")
        stl.text(Spellcasting["spellcasting_ability"]["name"] + " is your spellcasting ability")
        for abilities in Spellcasting["info"] :
            stl.subheader(abilities["name"])
            for description in abilities["desc"] :
                stl.text(description)
    else :
        pass
