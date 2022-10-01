# Developed by Gabriel Alba  
# This is my first personal project. It"s an interactive DnD player race and class selection


# First we will define the functions needed for the selection

from asyncio.windows_events import NULL
import random
import os
import pprint
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
decision  = "Y"
global RaceTitle
#RaceImageTk = ImageTk.PhotoImage(Image.open("C:/Users/Gabriel/Documents/My_Projects/Python/DnD_Character_Creation/Races/" + "Test" + ".png"))

def Refresh(root):
    root.destroy()
    root.__init__()

def PlayerHandbookRacesGenerator():
    Races = ["Dragonborn", "Hill Dwarf", "Mountain Dwarf", "Wood Elf","High Elf", "Deep Gnome", "Rock Gnome", "Half-Elf", 
            "Lightfoot Halfling", "Stout Halfling", "Half-Orc", "Human","Tiefling"]
    RNG = random.randint(0,len(Races)-1)

    return Races[RNG]
    
def RacesGUI():
    RaceRoot = tk.Tk()
    RaceRoot.geometry("1000x800")

    def Roll():
        global Race
        Race = PlayerHandbookRacesGenerator()
        RaceTitle.config(text = "Your race is " + Race)
        #MoreInfoLabel.config(text = "More info at: " + RaceCharac[Race]["More Info"])
        MoreInfoLabel = tk.Text(RaceRoot, height = 1)
        MoreInfoLabel.insert(1.0, "More info at: " + RaceCharac[Race]["More Info"])
        MoreInfoLabel.place(x = 40, y = 760)
        MoreInfoLabel.configure(state = "disabled")

         #Creating a table for the Race Characteristics
        CharacTable = ttk.Treeview(RaceRoot)
        CharacTable.place(x = 40, y = 150)
        CharacTable['height'] = 20
        CharacTable['columns']= ('Ability', 'Value')
        CharacTable.column("#0", width = 0,  stretch = tk.NO)
        CharacTable.column("Ability",anchor = tk.CENTER, width = 80)
        CharacTable.column("Value",anchor = tk.CENTER, stretch = tk.YES)

        CharacTable.heading("#0",text = "",anchor = tk.CENTER)
        CharacTable.heading("Ability",text="Ability",anchor = tk.CENTER)
        CharacTable.heading("Value",text = "Value", anchor = tk.CENTER)

        CharacTable.insert(parent='',index='end',iid=0,text='',
        values=('Race', RaceCharac[Race]["race"]))
        CharacTable.insert(parent='',index='end',iid=1,text='',
        values=('Strength', RaceCharac[Race]["STR"]))
        CharacTable.insert(parent='',index='end',iid=2,text='',
        values=('Dexterity', RaceCharac[Race]["DEX"]))
        CharacTable.insert(parent='',index='end',iid=3,text='',
        values=('Constitution', RaceCharac[Race]["CON"]))
        CharacTable.insert(parent='',index='end',iid=4,text='',
        values=('Intelligence', RaceCharac[Race]["INT"]))
        CharacTable.insert(parent='',index='end',iid=5,text='',
        values=('Wisdom', RaceCharac[Race]["WIS"]))
        CharacTable.insert(parent='',index='end',iid=6,text='',
        values=('Charisma', RaceCharac[Race]["CHA"]))
        CharacTable.insert(parent='',index='end',iid=7,text='',
        values=('Size', RaceCharac[Race]["Size"]))
        CharacTable.insert(parent='',index='end',iid=8,text='',
        values=('Speed', RaceCharac[Race]["Speed"]))
        counter = 8
        AbCounter = 0
        for Ability in RaceCharac[Race]["SpecAbilities"] :
            counter = counter + 1
            CharacTable.insert(parent='', index = 'end', iid = counter, text = '',
            values=('Ability ' + str(AbCounter + 1), Ability))
            AbCounter = AbCounter + 1
        AbCounter = 0
        for Language in RaceCharac[Race]["Languages"] :
            counter = counter + 1
            CharacTable.insert(parent='', index = 'end', iid = counter, text = '',
            values=('Language ' + str(AbCounter + 1), Language))
            AbCounter = AbCounter + 1


        ########     Table Created      ##############


        if Race == "High Elf" or Race == "Wood Elf" :
            Race = "Elf"
        elif Race == "Hill Dwarf" or Race == "Mountain Dwarf" :
            Race = "Dwarf"
        elif Race == "Deep Gnome" or Race == "Rock Gnome" :
            Race = "Gnome"
        elif Race == "Lightfoot Halfling" or Race == "Stout Halfling" :
            Race = "Halfling"
        else :
            pass

        RaceImageDir = Image.open("C:/Users/Gabriel/Documents/My_Projects/Python/DnD_Character_Creation/Races/" + Race + ".png")
        RaceImageDir  = RaceImageDir.resize((400,600))
        print("C:/Users/Gabriel/Documents/My_Projects/Python/DnD_Character_Creation/Races/" + Race + ".png")
        RaceImageTk = ImageTk.PhotoImage(RaceImageDir, master = RaceRoot)
        RaceImageLabel.config(image = RaceImageTk)
        RaceImageLabel.image = RaceImageTk

       
    Title = tk.Label(RaceRoot, text = "DnD Race Generator", font = ("Arial", 20))
    Title.place(x = 400, y = 20)
    Race = PlayerHandbookRacesGenerator()
    RaceTitle = tk.Label(RaceRoot, text = "Your race is " + Race, font = ("Helvetica", 16))
    RaceTitle.place(x = 40, y = 100)
    RaceCharac = PlayerHandbookRacesCharacteristics()


    #Creating a table for the Race Characteristics
    CharacTable = ttk.Treeview(RaceRoot)
    CharacTable.place(x = 40, y = 150)
    CharacTable['height'] = 20
    CharacTable['columns']= ('Ability', 'Value')
    CharacTable.column("#0", width = 0,  stretch = tk.NO)
    CharacTable.column("Ability",anchor = tk.CENTER, width = 80)
    CharacTable.column("Value",anchor = tk.CENTER, stretch = tk.YES)

    CharacTable.heading("#0",text = "",anchor = tk.CENTER)
    CharacTable.heading("Ability",text="Ability",anchor = tk.CENTER)
    CharacTable.heading("Value",text = "Value", anchor = tk.CENTER)

    CharacTable.insert(parent='',index='end',iid=0,text='',
    values=('Race', RaceCharac[Race]["race"]))
    CharacTable.insert(parent='',index='end',iid=1,text='',
    values=('Strength', RaceCharac[Race]["STR"]))
    CharacTable.insert(parent='',index='end',iid=2,text='',
    values=('Dexterity', RaceCharac[Race]["DEX"]))
    CharacTable.insert(parent='',index='end',iid=3,text='',
    values=('Constitution', RaceCharac[Race]["CON"]))
    CharacTable.insert(parent='',index='end',iid=4,text='',
    values=('Intelligence', RaceCharac[Race]["INT"]))
    CharacTable.insert(parent='',index='end',iid=5,text='',
    values=('Wisdom', RaceCharac[Race]["WIS"]))
    CharacTable.insert(parent='',index='end',iid=6,text='',
    values=('Charisma', RaceCharac[Race]["CHA"]))
    CharacTable.insert(parent='',index='end',iid=7,text='',
    values=('Size', RaceCharac[Race]["Size"]))
    CharacTable.insert(parent='',index='end',iid=8,text='',
    values=('Speed', RaceCharac[Race]["Speed"]))
    counter = 8
    AbCounter = 0
    for Ability in RaceCharac[Race]["SpecAbilities"] :
        counter = counter + 1
        CharacTable.insert(parent='', index = 'end', iid = counter, text = '',
        values=('Ability ' + str(AbCounter + 1), Ability))
        AbCounter = AbCounter + 1
    AbCounter = 0
    for Language in RaceCharac[Race]["Languages"] :
        counter = counter + 1
        CharacTable.insert(parent='', index = 'end', iid = counter, text = '',
        values=('Language ' + str(AbCounter + 1), Language))
        AbCounter = AbCounter + 1


    ########     Table Created      ##############

    #Creating additional Labels

    DecisionLabel = tk.Label(RaceRoot, text = "Do you want to re-roll?", font = ("Helvetica", 16))
    DecisionLabel.place(x = 40, y = 585)

    YesBtn = tk.Button(RaceRoot, text = "Yes", command = Roll)
    YesBtn.place(x = 40, y = 610)

    NoBtn = tk.Button(RaceRoot, text = "No (QUIT)", command = RaceRoot.destroy)
    NoBtn.place(x = 75, y = 610)

    # MoreInfoLabel = tk.Label(RaceRoot, text = "More info at: " + RaceCharac[Race]["More Info"])
    # MoreInfoLabel.place(x = 40, y = 760)

    MoreInfoLabel = tk.Text(RaceRoot, height = 1)
    MoreInfoLabel.insert(1.0, "More info at: " + RaceCharac[Race]["More Info"])
    MoreInfoLabel.place(x = 40, y = 760)
    MoreInfoLabel.configure(state = "disabled")

    if Race == "High Elf" or Race == "Wood Elf" :
        Race = "Elf"
    elif Race == "Hill Dwarf" or Race == "Mountain Dwarf" :
        Race = "Dwarf"
    elif Race == "Deep Gnome" or Race == "Rock Gnome" :
        Race = "Gnome"
    elif Race == "Lightfoot Halfling" or Race == "Stout Halfling" :
        Race = "Halfling"
    else :
        pass
    RaceImageDir = Image.open("C:/Users/Gabriel/Documents/My_Projects/Python/DnD_Character_Creation/Races/" + Race + ".png")
    RaceImageDir  = RaceImageDir.resize((400,600))
    #RaceImageDir.putalpha(0)
    print("C:/Users/Gabriel/Documents/My_Projects/Python/DnD_Character_Creation/Races/" + Race + ".png")
    RaceImageTk = ImageTk.PhotoImage(RaceImageDir, master = RaceRoot)
    RaceImageLabel = tk.Label(RaceRoot, image = RaceImageTk)
    RaceImageLabel.place(x = 500, y = 100)
    RaceImageLabel.image = RaceImageTk
    RaceRoot.mainloop()


def PlayerHandbookRacesCharacteristics():
    DragonBornDIC = {"race": "Dragonborn", 
                    "STR": 2, 
                    "DEX": 0, 
                    "CON": 0, 
                    "INT": 0, 
                    "WIS": 0, 
                    "CHA": 1,
                    "Size":"Medium",
                    "Speed": 30, 
                    "SpecAbilities":["Draconic Ancestry", "Breath Weapon", "Damage Resistance"],
                    "Languages": ["Common", "Draconic"], 
                    "More Info":"https://www.dndbeyond.com/races/16-dragonborn"}

    HillDwarfDIC = {"race": "Hill Dwarf", 
                    "STR": 0, 
                    "DEX": 0, 
                    "CON": 2, 
                    "INT": 0, 
                    "WIS": 1, 
                    "CHA": 0,
                    "Size":"Medium",
                    "Speed": 25,
                    "SpecAbilities":["Darkvision", "Dwarven Resilience", "Dwarven Combat Training",  
                    "Tool Proficiency", "Stonecunning", "Dwarven Toughness"], 
                    "Languages": ["Common", "Dwarvish"], 
                    "More Info":"https://www.dndbeyond.com/races/13-dwarf"}

    MountainDwarfDIC = {"race": "Mountain Dwarf", 
                    "STR": 2, 
                    "DEX": 0, 
                    "CON": 2, 
                    "INT": 0, 
                    "WIS": 0, 
                    "CHA": 0,
                    "Size":"Medium",
                    "Speed": 25,
                    "SpecAbilities":["Darkvision", "Dwarven Resilience", "Dwarven Combat Training",  
                    "Tool Proficiency", "Stonecunning", "Dwarven Armor Training"], 
                    "Languages": ["Common", "Dwarvish"],
                    "More Info":"https://www.dndbeyond.com/races/13-dwarf"}

    WoodElfDIC = {"race": "Wood Elf", 
                    "STR": 0, 
                    "DEX": 2, 
                    "CON": 0, 
                    "INT": 0, 
                    "WIS": 1, 
                    "CHA": 0,
                    "Size": "Medium",
                    "Speed": 35,
                    "SpecAbilities":["Darkvision", "Keen Senses", "Fey Ancestry", "Trance",
                    "Elf Weapon Training", "Fleet of Foot", "Mask of the Wild"], 
                    "Languages": ["Common", "Elvish"],
                    "More Info":"https://www.dndbeyond.com/races/3-elf"}
            
    HighElfDIC = {"race": "High Elf", 
                    "STR": 0, 
                    "DEX": 2, 
                    "CON": 0, 
                    "INT": 1, 
                    "WIS": 0, 
                    "CHA": 0,
                    "Size": "Medium",
                    "Speed": 30,
                    "SpecAbilities":["Darkvision", "Keen Senses", "Fey Ancestry", "Trance", 
                    "Elf Weapon Training", "Cantrip"], 
                    "Languages": ["Common", "Elvish", "Custom"],
                    "More Info":"https://www.dndbeyond.com/races/3-elf"}

    DeepGnomeDIC = {"race": "Deep Gnome", 
                    "STR": 0, 
                    "DEX": 1, 
                    "CON": 0, 
                    "INT": 2, 
                    "WIS": 0, 
                    "CHA": 0,
                    "Size": "Small",
                    "Speed": 25,
                    "SpecAbilities":["Superior Darkvision", "Stone Camouflage", "Gnome Cunning"], 
                    "Languages": ["Common", "Gnomish", "Undercommon"],
                    "More Info":"https://www.dndbeyond.com/races/18-gnome"}

    RockGnomeDIC = {"race": "Rock Gnome", 
                    "STR": 0, 
                    "DEX": 0, 
                    "CON": 1, 
                    "INT": 2, 
                    "WIS": 0, 
                    "CHA": 0,
                    "Size": "Small",
                    "Speed": 25,
                    "SpecAbilities":["Darkvision", "Artificer's Lore", "Gnome Cunning", "Tinker"], 
                    "Languages": ["Common", "Gnomish", "Undercommon"],
                    "More Info":"https://www.dndbeyond.com/races/18-gnome"}

    HalfElfDIC = {"race": "Half-Elf", 
                    "STR": 0, 
                    "DEX": 0, 
                    "CON": 0, 
                    "INT": 0, 
                    "WIS": 0, 
                    "CHA": 2,
                    "Size": "Small",
                    "Speed": 25,
                    "SpecAbilities":["Darkvision", "Fey Ancestry", "Skill Versatility", "Tinker", "+1 in abilities of choice"], 
                    "Languages": ["Common", "Elvish", "Custom"],
                    "More Info":"https://www.dndbeyond.com/races/20-half-elf"}

    LightHalflingDIC = {"race": "Lightfoot Halfling", 
                    "STR": 0, 
                    "DEX": 2, 
                    "CON": 0, 
                    "INT": 0, 
                    "WIS": 0, 
                    "CHA": 1,
                    "Size": "Small",
                    "Speed": 25,
                    "SpecAbilities":["Lucky", "Brave", "Halfling Nimbleness", "Naturally Stealthy"], 
                    "Languages": ["Common", "Halfling"],
                    "More Info": "https://www.dndbeyond.com/races/14-halfling"}

    StoutHalflingDIC = {"race": "Stout Halfling", 
                    "STR": 0, 
                    "DEX": 2, 
                    "CON": 1, 
                    "INT": 0, 
                    "WIS": 0, 
                    "CHA": 0,
                    "Size": "Small",
                    "Speed": 25,
                    "SpecAbilities":["Lucky", "Brave", "Halfling Nimbleness", "Stout Resilience"], 
                    "Languages": ["Common", "Halfling"],
                    "More Info": "https://www.dndbeyond.com/races/14-halfling"}

    HalfOrcDIC = {"race": "Half-Orc", 
                    "STR": 2, 
                    "DEX": 0, 
                    "CON": 1, 
                    "INT": 0, 
                    "WIS": 0, 
                    "CHA": 0,
                    "Size": "Medium",
                    "Speed": 30,
                    "SpecAbilities":["Darkvision", "Menacing", "Relentless Endurance", "Savage Attacks"], 
                    "Languages": ["Common", "Orc"],
                    "More Info": "https://www.dndbeyond.com/races/2-half-orc"}

    HumanDIC = {"race": "Human", 
                    "STR": 1, 
                    "DEX": 1, 
                    "CON": 1, 
                    "INT": 1, 
                    "WIS": 1, 
                    "CHA": 1,
                    "Size": "Medium",
                    "Speed": 30,
                    "SpecAbilities":[], 
                    "Languages": ["Common", "Custom"],
                    "More Info": "https://www.dndbeyond.com/races/1-human"}

    TieflingDIC = {"race": "Tiefling", 
                    "STR": 0, 
                    "DEX": 0, 
                    "CON": 0, 
                    "INT": 1, 
                    "WIS": 0, 
                    "CHA": 2,
                    "Size": "Medium",
                    "Speed": 30,
                    "SpecAbilities":["Darkvision","Hellish Resistance","Infernal Legacy"], 
                    "Languages": ["Common", "Infernal"],
                    "More Info": "https://www.dndbeyond.com/races/7-tiefling"}

    Races = {"Dragonborn":DragonBornDIC, "Hill Dwarf":HillDwarfDIC, "Mountain Dwarf":MountainDwarfDIC, "Wood Elf":WoodElfDIC,
            "High Elf":HighElfDIC, "Deep Gnome":DeepGnomeDIC, "Rock Gnome":RockGnomeDIC, "Half-Elf":HalfElfDIC, 
            "Lightfoot Halfling":LightHalflingDIC, "Stout Halfling":StoutHalflingDIC, "Half-Orc":HalfOrcDIC, "Human":HumanDIC,
            "Tiefling":TieflingDIC}

    return Races


def Traits():

    Traits = {"Lucky":"When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, \
                        you can reroll the die and must use the new roll.",
            "Brave":"You have advantage on saving throws against being frightened.",
            "Halfling Nimbleness":"You can move through the space of any creature that is of a size larger than yours",
            "Naturally Stealthy":"You can attempt to hide even when you are obscured only by a creature that is at least  \
                                one size larger than you.",
            "Stout Resilience":"You have advantage on saving throws against poison, and you have resistance against poison damage.",
            "Draconic Ancestry":"You have draconic ancestry. Choose one type of dragon from the Draconic Ancestry table. \
                                Your breath weapon and damage resistance are determined by the dragon type",
            "Breath Weapon":"You can use your action to exhale destructive energy. Your draconic ancestry determines the size, \
                            shape, and damage type of the exhalation. When you use your breath weapon, each creature in the area \
                            of the exhalation must make a saving throw, the type of which is determined by your draconic ancestry. \
                            The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. \
                            A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. \
                            The damage increases to 3d6 at 6th level, 4d6 at 11th level, and 5d6 at 16th level. After you use your \
                            breath weapon, you can’t use it again until you complete a short or long rest.",
            "Damage Resistance":"You have resistance to the damage type associated with your draconic ancestry.",
            "Darkvision":"You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were \
                            dim light. You can’t discern color in darkness, only shades of gray.",
            "Dwarven Resilience":"You have advantage on saving throws against poison, and you have resistance against poison damage",
            "Dwarven Combat Training":"You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.",
            "Tool Proficiency":"You gain proficiency with the artisan’s tools of your choice: smith’s tools, brewer’s supplies, \
                                or mason’s tools.",
            "Stonecunning":"Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered \
                            proficient in the History skill and add double your proficiency bonus to the check, instead of your normal \
                            proficiency bonus.",
            "Dwarven Toughness":"Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.",
            "Dwarven Armor Training":"You have proficiency with light and medium armor.",
            "Keen Senses":"You have proficiency in the Perception skill.",
            "Fey Ancestry":"You have advantage on saving throws against being charmed, and magic can’t put you to sleep.",
            "Trance":"Elves don’t need to sleep. Instead, they meditate deeply, remaining semiconscious, for 4 hours a day. \
                        (The Common word for such meditation is “trance.”) While meditating, you can dream after a fashion; \
                        such dreams are actually mental exercises that have become reflexive through years of practice. \
                        After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.",
            "Elf Weapon Training":"You have proficiency with the longsword, shortsword, shortbow, and longbow.",
            "Cantrip":"You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.",
            "Fleet of Foot":"Your base walking speed increases to 35 feet.",
            "Mask of the Wild":"You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, \
                                mist, and other natural phenomena.",
            "Gnome Cunning":"You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic.",
            "Superior Darkvision":"Your darkvision has a radius of 120 feet.",
            "Stone Camouflage":"You have advantage on Dexterity (Stealth) checks to hide in rocky terrain.",
            "Artificer's Lore":"Whenever you make an Intelligence (History) check related to magic items, alchemical objects, \
                                or technological devices, you can add twice your proficiency bonus, instead of any proficiency \
                                bonus you normally apply.",
            "Tinker":"You have proficiency with artisan’s tools (tinker’s tools). Using those tools, you can spend 1 hour and \
                    10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function \
                    after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your \
                    action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to \
                    three such devices active at a time. \n\
                    When you create a device, choose one of the following options: \n\
                    Clockwork Toy. This toy is a clockwork animal, monster, or person, such as a frog, mouse, bird, dragon, or \
                    soldier. When placed on the ground, the toy moves 5 feet across the ground on each of your turns in a random \
                    direction. It makes noises as appropriate to the creature it represents. \n\
                    Fire Starter. The device produces a miniature flame, which you can use to light a candle, torch, or campfire. \
                    Using the device requires your action. \n\
                    Music Box. When opened, this music box plays a single song at a moderate volume. The box stops playing when \
                    it reaches the song’s end or when it is closed.",
            "Skill Versatility":"You gain proficiency in two skills of your choice.",
            "Menacing":"You gain proficiency in the Intimidation skill.",
            "Relentless Endurance":"When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point \
                                    instead. You can’t use this feature again until you finish a long rest.",
            "Savage Attacks":"When you score a critical hit with a melee weapon attack, you can roll one of the weapon’s damage \
                                dice one additional time and add it to the extra damage of the critical hit.",
            "Hellish Resistance":"You have resistance to fire damage.",
            "Infernal Legacy":"You know the thaumaturgy cantrip. When you reach 3rd level, you can cast the hellish rebuke spell \
                                as a 2nd-level spell once with this trait and regain the ability to do so when you finish a long \
                                rest. When you reach 5th level, you can cast the darkness spell once with this trait and regain \
                                the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these \
                                spells."
            }


def ClassesGenerator():
    Classes = ["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"]
    RNG = random.randint(0,len(Classes)-1)

    return Classes[RNG]

def ClassesCharacteristics():
    BarbarianDICT = {"Hit Dice":"1d12 per level",
                    "Hit Points at Lv1":"12+CON",
                    "Hit Points at Lv2+":"1d12+CON",
                    "Armor Prof":["Light","Medium","Shields"],
                    "Weapons Prof":["Simple Weapons","Martial Weapons"],
                    "Tools Prof":[],
                    "Saving Throws":["Strength","Constitution"],
                    "Possible Skills":["Choose 2 from:","Animal Handling","Athletics","Intimidation","Nature","Perception","Survival"],
                    "Amount of Skills": 2 ,
                    "Equipment":["Greataxe or Martial Melee Weapon","Two Handaxes or Any Simple Weapon","Explorer Pack","Four Javelins"],
                    "Abilities":"Check https://www.dndbeyond.com/classes/barbarian"}

    BardDICT = {"Hit Dice":"1d8 per level",
                    "Hit Points at Lv1":"8+CON",
                    "Hit Points at Lv2+":"1d8+CON",
                    "Armor Prof":["Light"],
                    "Weapons Prof":["Simple Weapons","Hand Crossbows","Longswords","Rapiers","Shortswords"],
                    "Tools Prof":["Three musical instruments of your choice"],
                    "Saving Throws":["Dexterity","Charisma"],
                    "Possible Skills":["Any"],
                    "Amount of Skills": 3 ,
                    "Equipment":["Rapier, Longsword or Any Simple Weapon","Diplomat Pack or Entertainer Pack",
                    "A Lute or Any Other Musical Instrument","Leather Armor","Dagger"],
                    "Abilities":"Check https://www.dndbeyond.com/classes/bard"}

    ClericDICT = {"Hit Dice":"1d8 per level",
                    "Hit Points at Lv1":"8+CON",
                    "Hit Points at Lv2+":"1d8+CON",
                    "Armor Prof":["Light", "Medium", "Shields"],
                    "Weapons Prof":["Simple Weapons"],
                    "Tools Prof":[],
                    "Saving Throws":["Wisdom","Charisma"],
                    "Possible Skills":["History", "Insight", "Medicine", "Persuasion", "Religion"],
                    "Amount of Skills": 2 ,
                    "Equipment":["Mace or Warhammer (if prof)", "Scale mail, leather or chain mail armor (if prof)",
                                "Crossbow with 20 bolts or Any simple weapon","A priest pack or an explorer pack",
                                "Shield","Holy Symbol"],
                    "Abilities":"Check https://www.dndbeyond.com/classes/cleric"}

    # DruidDICT = {"Hit Dice":"1d8 per level",
    #                 "Hit Points at Lv1":"8+CON",
    #                 "Hit Points at Lv2+":"1d8+CON",
    #                 "Armor Prof":["Light", "Medium", "Shields"],
    #                 "Weapons Prof":["Simple Weapons"],
    #                 "Tools Prof":[],
    #                 "Saving Throws":["Wisdom","Charisma"],
    #                 "Possible Skills":["History", "Insight", "Medicine", "Persuasion", "Religion"],
    #                 "Amount of Skills": 2 ,
    #                 "Equipment":["Mace or Warhammer (if prof)", "Scale mail, leather or chain mail armor (if prof)",
    #                             "Crossbow with 20 bolts or Any simple weapon","A priest pack or an explorer pack",
    #                             "Shield","Holy Symbol"],
    #                 "Abilities":"Check https://www.dndbeyond.com/classes/druid"}

    # FighterDICT = {"Hit Dice":"1d8 per level",
    #                 "Hit Points at Lv1":"8+CON",
    #                 "Hit Points at Lv2+":"1d8+CON",
    #                 "Armor Prof":["Light", "Medium", "Shields"],
    #                 "Weapons Prof":["Simple Weapons"],
    #                 "Tools Prof":[],
    #                 "Saving Throws":["Wisdom","Charisma"],
    #                 "Possible Skills":["History", "Insight", "Medicine", "Persuasion", "Religion"],
    #                 "Amount of Skills": 2 ,
    #                 "Equipment":["Mace or Warhammer (if prof)", "Scale mail, leather or chain mail armor (if prof)",
    #                             "Crossbow with 20 bolts or Any simple weapon","A priest pack or an explorer pack",
    #                             "Shield","Holy Symbol"],
    #                 "Abilities":"Check https://www.dndbeyond.com/classes/fighter"}

    # MonkDICT = {"Hit Dice":"1d8 per level",
    #                 "Hit Points at Lv1":"8+CON",
    #                 "Hit Points at Lv2+":"1d8+CON",
    #                 "Armor Prof":["Light", "Medium", "Shields"],
    #                 "Weapons Prof":["Simple Weapons"],
    #                 "Tools Prof":[],
    #                 "Saving Throws":["Wisdom","Charisma"],
    #                 "Possible Skills":["History", "Insight", "Medicine", "Persuasion", "Religion"],
    #                 "Amount of Skills": 2 ,
    #                 "Equipment":["Mace or Warhammer (if prof)", "Scale mail, leather or chain mail armor (if prof)",
    #                             "Crossbow with 20 bolts or Any simple weapon","A priest pack or an explorer pack",
    #                             "Shield","Holy Symbol"],
    #                 "Abilities":"Check https://www.dndbeyond.com/classes/monk"}

    # PaladinDICT = {"Hit Dice":"1d8 per level",
    #                 "Hit Points at Lv1":"8+CON",
    #                 "Hit Points at Lv2+":"1d8+CON",
    #                 "Armor Prof":["Light", "Medium", "Shields"],
    #                 "Weapons Prof":["Simple Weapons"],
    #                 "Tools Prof":[],
    #                 "Saving Throws":["Wisdom","Charisma"],
    #                 "Possible Skills":["History", "Insight", "Medicine", "Persuasion", "Religion"],
    #                 "Amount of Skills": 2 ,
    #                 "Equipment":["Mace or Warhammer (if prof)", "Scale mail, leather or chain mail armor (if prof)",
    #                             "Crossbow with 20 bolts or Any simple weapon","A priest pack or an explorer pack",
    #                             "Shield","Holy Symbol"],
    #                 "Abilities":"Check https://www.dndbeyond.com/classes/paladin"}

    # RangerDICT = {"Hit Dice":"1d8 per level",
    #                 "Hit Points at Lv1":"8+CON",
    #                 "Hit Points at Lv2+":"1d8+CON",
    #                 "Armor Prof":["Light", "Medium", "Shields"],
    #                 "Weapons Prof":["Simple Weapons"],
    #                 "Tools Prof":[],
    #                 "Saving Throws":["Wisdom","Charisma"],
    #                 "Possible Skills":["History", "Insight", "Medicine", "Persuasion", "Religion"],
    #                 "Amount of Skills": 2 ,
    #                 "Equipment":["Mace or Warhammer (if prof)", "Scale mail, leather or chain mail armor (if prof)",
    #                             "Crossbow with 20 bolts or Any simple weapon","A priest pack or an explorer pack",
    #                             "Shield","Holy Symbol"],
    #                 "Abilities":"Check https://www.dndbeyond.com/classes/ranger"} 

    # RogueDICT = {"Hit Dice":"1d8 per level",
    #                 "Hit Points at Lv1":"8+CON",
    #                 "Hit Points at Lv2+":"1d8+CON",
    #                 "Armor Prof":["Light", "Medium", "Shields"],
    #                 "Weapons Prof":["Simple Weapons"],
    #                 "Tools Prof":[],
    #                 "Saving Throws":["Wisdom","Charisma"],
    #                 "Possible Skills":["History", "Insight", "Medicine", "Persuasion", "Religion"],
    #                 "Amount of Skills": 2 ,
    #                 "Equipment":["Mace or Warhammer (if prof)", "Scale mail, leather or chain mail armor (if prof)",
    #                             "Crossbow with 20 bolts or Any simple weapon","A priest pack or an explorer pack",
    #                             "Shield","Holy Symbol"],
    #                 "Abilities":"Check https://www.dndbeyond.com/classes/rogue"}    

    # SorcererDICT = {"Hit Dice":"1d8 per level",
    #                 "Hit Points at Lv1":"8+CON",
    #                 "Hit Points at Lv2+":"1d8+CON",
    #                 "Armor Prof":["Light", "Medium", "Shields"],
    #                 "Weapons Prof":["Simple Weapons"],
    #                 "Tools Prof":[],
    #                 "Saving Throws":["Wisdom","Charisma"],
    #                 "Possible Skills":["History", "Insight", "Medicine", "Persuasion", "Religion"],
    #                 "Amount of Skills": 2 ,
    #                 "Equipment":["Mace or Warhammer (if prof)", "Scale mail, leather or chain mail armor (if prof)",
    #                             "Crossbow with 20 bolts or Any simple weapon","A priest pack or an explorer pack",
    #                             "Shield","Holy Symbol"],
    #                 "Abilities":"Check https://www.dndbeyond.com/classes/sorcerer"}

    # WarlockDICT = {"Hit Dice":"1d8 per level",
    #                 "Hit Points at Lv1":"8+CON",
    #                 "Hit Points at Lv2+":"1d8+CON",
    #                 "Armor Prof":["Light", "Medium", "Shields"],
    #                 "Weapons Prof":["Simple Weapons"],
    #                 "Tools Prof":[],
    #                 "Saving Throws":["Wisdom","Charisma"],
    #                 "Possible Skills":["History", "Insight", "Medicine", "Persuasion", "Religion"],
    #                 "Amount of Skills": 2 ,
    #                 "Equipment":["Mace or Warhammer (if prof)", "Scale mail, leather or chain mail armor (if prof)",
    #                             "Crossbow with 20 bolts or Any simple weapon","A priest pack or an explorer pack",
    #                             "Shield","Holy Symbol"],
    #                 "Abilities":"Check https://www.dndbeyond.com/classes/warlock"}

    # WizardDICT = {"Hit Dice":"1d8 per level",
    #                 "Hit Points at Lv1":"8+CON",
    #                 "Hit Points at Lv2+":"1d8+CON",
    #                 "Armor Prof":["Light", "Medium", "Shields"],
    #                 "Weapons Prof":["Simple Weapons"],
    #                 "Tools Prof":[],
    #                 "Saving Throws":["Wisdom","Charisma"],
    #                 "Possible Skills":["History", "Insight", "Medicine", "Persuasion", "Religion"],
    #                 "Amount of Skills": 2 ,
    #                 "Equipment":["Mace or Warhammer (if prof)", "Scale mail, leather or chain mail armor (if prof)",
    #                             "Crossbow with 20 bolts or Any simple weapon","A priest pack or an explorer pack",
    #                             "Shield","Holy Symbol"],
    #                 "Abilities":"Check https://www.dndbeyond.com/classes/wizard"}

    Classes = {"Barbarian":BarbarianDICT, "Bard":BardDICT, "Cleric":ClericDICT}


    return Classes


option = "0"
Race = NULL
Class = NULL
counter = 0
random.seed()
pp = pprint.PrettyPrinter(sort_dicts = False)


# No GUI way to do it 
# while True:
#     os.system("cls")
#     print("Welcome to the Random Character Generator for DnD")
#     print("This is based on The Player's Handbook 5e")
#     print("")
#     print("1.Generate my Race")
#     print("2.Generate my Class")
#     print("3.Look into my Race")
#     print("4.Look into my Class")
#     print("5.EXIT")
#     print("")
#     option = input("Please choose an option: ")
#     if option == "1" :
#         while counter == 0:
#             os.system("cls")
#             Race = PlayerHandbookRacesGenerator()
#             print("Your Race is: " + Race)
#             print("")
#             re_roll = input("Do you want to re-roll your race? (Y/N)")
#             if re_roll == "Y" or re_roll == "y" :
#                 counter = 0
#             elif re_roll == "N" or re_roll == "n" :
#                 counter = 1
#                 print("Press enter to continue...")
#             else :
#                 print("Please enter a valid option")
#                 input("Press enter to continue...")
#     elif option == "2" :
#         counter = 0
#         while counter == 0:
#             os.system("cls")
#             Class = ClassesGenerator()
#             print("Your Class is: " + Class)
#             print("")
#             re_roll = input("Do you want to re-roll your class? (Y/N)")
#             if re_roll == "Y" or re_roll == "y" :
#                 counter = 0
#             elif re_roll == "N" or re_roll == "n" :
#                 counter = 1
#                 input("Press enter to continue...")
#             else :
#                 print("Please enter a valid option")
#                 input("Press enter to continue...")
#     elif option == "3" :
#         os.system("cls")
#         if Race == NULL :
#             print("You have not generated a Race, please generate one first")
#             input("Press enter to continue...")
#         else :
#             RaceCharacteristics = PlayerHandbookRacesCharacteristics()
#             pp.pprint(RaceCharacteristics[Race])
#             input("Press enter to continue...")
#     elif option == "4" :
#         os.system("cls")
#         if Class == NULL :
#             print("You have not generated a Class, please generate one first")
#             input("Press enter to continue...")
            
#         else :
#             ClassCharacteristics = ClassesCharacteristics()
#             pp.pprint(ClassCharacteristics[Class])
#             input("Press enter to continue...")
#     elif option == "5" :
#         break
#     else :
#         os.system("cls")
#         input("Please enter a valid option")



#With GUI

root = tk.Tk()
root.geometry("600x400")
root.title("DnD Random Generator")

Title = tk.Label(root, text = "DnD Random Generator").place(x = 200, y = 20)

GenRace = tk.Button(root, text = "Generate Race", command = RacesGUI). place(x = 40, y = 50)

GenClass = tk.Button(root, text = "Generate Class"). place(x = 40, y = 80)

#RaceInfo = tk.Button(root, text = "See Race Info"). place(x = 40, y = 110)

#ClassInfo = tk.Button(root, text = "See Class Info"). place(x = 40, y = 140)



root.mainloop()