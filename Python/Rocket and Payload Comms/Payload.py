from enum import Enum 
from operator import attrgetter
import random
from time import sleep
from PIL import Image, ImageDraw
import uuid 

class Payload :

    #Need to understand this function better 
    def genRandomImage(self,width = 255, height = 255):
        randPixels = [random.randint(0,255) for _ in range(width * height * 3)]
        PixelsToBytes = bytes(randPixels)
        text_and_filename = str(uuid.uuid4()) + "_" + self.name
        randomImage = Image.frombytes('RGB',(width,height), PixelsToBytes)
        draw_image = ImageDraw.Draw(randomImage)
        draw_image.text(xy = (0,0), text = text_and_filename, fill = [255,255,255])
        randomImage.save("{file_name}.jpg".format(file_name = text_and_filename))



    def StartData(self):
        Data = "StartData"
        while Data == "StartData" :
            if self.type == 'Scientific' :
                Rainfall = str(random.randrange(0,500))
                Humidity = str(random.randrange(0,100))
                Snow = str(random.randrange(0,500))
                SciDict = {"Rainfall":Rainfall, "Humidity":Humidity, "Snow":Snow}
                print("Weather Data: ")
                print("Rainfall: " + Rainfall + "mm")
                print("Humidity: " + Humidity + "%")
                print("Snow: " + Snow + "in")
                sleep(3000)
            elif self.type == "Communication" :
                Uplink = str(random.randrange(0,5000))
                Downlink = str(random.randrange(0,10000))
                Transponders = str(random.randrange(0,500))
                CommsDict = {"Uplink":Uplink, "Downlink":Downlink, "Transponders":Transponders}
                print("Comms Data: ")
                print("Uplink: " + Uplink + "MBps")
                print("Downlink: " + Downlink + "MBps")
                print("Transponders" + Transponders)
                sleep(5000)
            elif self.type == "spy" :
                self.genRandomImage()
                

    def StopData(self):
        return 'StopData'

    def Decomission(self):
        del Payload

    def StartTelemetry(self):
        pass

    def StopTelemetry(self):
        pass


    def __init__(self, name, type):
        self.name = name
        self.type = type
