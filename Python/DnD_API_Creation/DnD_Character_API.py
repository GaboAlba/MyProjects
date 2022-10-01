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

stl.title("DnD Character Creation")


if stl.button("Generate Race"):
    RandomRace = requests.get(CreateRandomRace(RacesDict))
    SelectedRace = RandomRace.json()["name"]
    RandomRace = pd.DataFrame([RandomRace.json()])
    RandomRace = RandomRace.transpose()
    stl.subheader("Your Race is -> " + SelectedRace)
    stl.write(RandomRace)

if stl.button("Generate Class"):
    RandomClass = requests.get(CreateRandomRace(ClassesDict))
    stl.write(RandomClass.json())
