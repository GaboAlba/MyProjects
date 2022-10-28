## python -m PyInstaller -w -F -i "C:\Users\gfalbaro\OneDrive - Intel Corporation\Documents\GitHub\MyProjects\Python\Fungibility_Matrix_Generator\Intel-logo-2022.png" -n FungibilityMatrixGen --add-data "Intel-logo-2022.png";icon --add-data "Intel-logo-2022.ico";icon  TkGUI.py

from tkinter import *
from Product_Init import Product_Init
import pandastable as pt
from PIL import Image, ImageTk
import sys
from os import path

def Refresh(root):
    root.destroy()
    root.__init__()

def productParameters(product) :
    #print(product)
    GeneralDict = {"CLX":{"Name":"CLX","Components":["MB","AP"],"Insertions":["MAIN"], "Flavors":["LCC","HCC","XCC"]},
                        "CPX":{"Name":"CPX","Components":["MB","AP"],"Insertions":["MAIN"], "Flavors":["XCP"]}, 
                        "ICX":{"Name":"ICX","Components":["MB","AP"],"Insertions":["MAIN","SDE"], "Flavors":["XCP"]},
                        "SPR":{"Name":"SPR","Components":["MB","AP"],"Insertions":["MAIN","CXL","SDE"], "Flavors":["XCC","MCC","112L","WMCC"]},
                        "EMR":{"Name":"EMR","Components":["MB","AP"],"Insertions":["MAIN","SDE"], "Flavors":["XCC","MCC"]},      
                        "GNR":{"Name":"GNR","Components":["MB","AP"],"Insertions":["MAIN","SDE"], "Flavors":["DE","UCC","XCC"]},      
                        "SRF":{"Name":"SRF","Components":["MB","AP"],"Insertions":["MAIN","CXL","SDE"], "Flavors":["LCC"]}}

    #print(GeneralDict[product])
    return GeneralDict[product]

def FlavorSelection(productList) :
    flavorsList = []
    if len(productList) > 1 :
        for product in productList:
            for flavor in productParameters(product)["Flavors"] :
                flavorsList.append(product + "_" + flavor)
    else :
        for product in productList:
            for flavor in productParameters(product)["Flavors"] :
                    flavorsList.append(flavor)

    return flavorsList

def InsertionSelection(productList) :
    insertionsList = []
    if len(productList) > 1 :
        for product in productList:
            for insertion in productParameters(product)["Insertions"] :
                insertionsList.append(product + "_" + insertion)
    else :
        for product in productList:
            for insertion in productParameters(product)["Insertions"] :
                    insertionsList.append(insertion)

    return insertionsList

def GenCSV():
    return ProdObj.to_CSV(df) 

def GenFungMatrix() :
    global df
    global ProdObj
    ProdObj = Product_Init(prodSelected, flavSelected, compSelected, insSelected)
    print(prodSelected)   
    print(flavSelected) 
    print(compSelected) 
    print(insSelected) 
    ObjectList = ProdObj.CreateObjects()
    print(ObjectList)
    if len(ObjectList) > 0 :
        df = ProdObj.CreateDFs(1)
        df = ProdObj.FungMatrix(df)
        CSV = Button(text = "Generate CSV", command = GenCSV, width = 100).place(x = 25, y = 390)
        print(df)
        print(df.columns)
        frame = Toplevel(root)
        frame.geometry("1280x720")
        table = pt.Table(frame, dataframe = df, cols=5)
        table.show()
        table.showIndex()

        
    else :
        print("Object List is empty")   

  

def ConfirmFlavor() :
    global flavSelected
    flavSelected = []
    for index in flavorSelection.curselection() :
        flavSelected.append(__flavorList__[index])
        print(__flavorList__[index])

def ConfirmInsertion() :
    global insSelected
    insSelected = []
    for index in insertionSelection.curselection() :
        insSelected.append(__insertionList__[index])
        print(__insertionList__[index])  

def ConfirmComponent() :
    global compSelected
    compSelected = []
    for index in componentSelection.curselection() :
        compSelected.append(__componentsList__[index]) 
        print(__componentsList__[index])


def ConfirmProduct() :
    global ProdConfirmed
    ProdConfirmed = True
    global prodSelected
    prodSelected = []
    for index in productSelection.curselection() :
        prodSelected.append(__ProductList__[index])

    if ProdConfirmed == True:
        #print("Enter")
        global __flavorList__
        __flavorList__ = FlavorSelection(prodSelected)
        for flavor in __flavorList__ :
            flavorSelection.insert(END,flavor)
        
        
        global __insertionList__
        __insertionList__ = InsertionSelection(prodSelected)
        for insertion in __insertionList__ :
            insertionSelection.insert(END,insertion)
        

        global __componentsList__
        __componentsList__ = productParameters(prodSelected[0])["Components"]
        for component in __componentsList__ :
            componentSelection.insert(END,component)

    else:
        print("Not enter")
        pass
        print(ProdConfirmed)

    GenerateMatrix = Button(text="Generate Matrix", command = GenFungMatrix, width = 100).place(x=25, y = 350)

filename = "icon/Intel-logo-2022.png"
icon = "icon/Intel-logo-2022.ico"
pathToPicture = path.abspath(path.join(path.dirname(__file__),filename))
pathToIcon = path.abspath(path.join(path.dirname(__file__),icon))
root = Tk()
root.title("PPV Fungibility Matrix Generator")
root.geometry("800x550")
#root.iconphoto(False, PhotoImage(pathToIcon))
ProdConfirmed = False
IntelImageDir = Image.open(pathToPicture)
IntelImageDir  = IntelImageDir.resize((300,121))
IntelImageTk = ImageTk.PhotoImage(IntelImageDir, master = root)
IntelImageLabel = Label(root, image = IntelImageTk)
IntelImageLabel.place(x = 10, y = 10)
IntelImageLabel.config(image = IntelImageTk)
IntelImageLabel.image = IntelImageTk
Title = Label(root, text = "PPV Fungibility Matrix Generator", font = ("Arial",20)).place(x=330, y = 50)

__ProductList__ = ["CLX", "CPX", "ICX", "SPR", "EMR", "GNR" ,"SRF"]
productSelection = Listbox(root, selectmode = MULTIPLE)
productSelection.place(x = 25, y = 150)
for product in __ProductList__ :
    productSelection.insert(END,product)

ProductConfirm = Button(text="Confirm Products", command = ConfirmProduct, width = 16).place(x = 25, y = 320)

global flavorSelection
flavorSelection = Listbox(root, selectmode = MULTIPLE)
flavorSelection.place(x = 210, y = 150)

FlavorConfirm = Button(text="Confirm Flavors", command = ConfirmFlavor, width = 16).place(x = 210, y = 320)

global insertionSelection
insertionSelection = Listbox(root, selectmode = MULTIPLE)
insertionSelection.place(x = 410, y = 150)

InsertionConfirm = Button(text="Confirm Insertions", command = ConfirmInsertion, width = 16).place(x = 410, y = 320)

global componentSelection
componentSelection = Listbox(root, selectmode = MULTIPLE)
componentSelection.place(x = 610, y = 150)

ComponentsConfirm = Button(text="Confirm Components", command = ConfirmComponent, width = 16).place(x = 610, y = 320)


root.mainloop()

