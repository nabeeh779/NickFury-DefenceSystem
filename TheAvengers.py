
from random import randint
from time import sleep
import pika

class TheAvengers:
    """
    Fighting Capabilities:
        -Land 
        -sea
        -air
        -space
    """
    def __init__(self, name, location , damage , speed):
        self.name = name
        self.location = location    #Fighting locations
        self.damage = float(damage)    #Damge per sec
        self.speed = float(speed)  #speed per sec
        #Generate random coordinate    
        self.x = randint(-100,100)
        #sleep(1.5)
        self.y = randint(-100,100)
    def return_location(self):
        loc = (self.x,self.y)
        return loc
    
    def __str__(self):
        #This function return instance detailes
        
        return '{}\nFighting Location:{}'.format(self.name, self.location)+ f'\nDamage:{self.damage}\nSpeed:={self.speed}' + f'\nLocation:({self.x},{self.y})'
    def get_dict_info(self):
        temp = {
            self.name:[self.location,self.damage,self.speed,[self.x,self.y]]
        }
        return temp
    def get_name(self):
        return self.name
    def get_location(self):
        return [self.x,self.y]
     
def create_Avengers():
    #This function Build The Avengers
    #Return List Contain All Of The Avengers
    IronMan = TheAvengers('IronMan' , ('Land','air','sea','space'), 1, 15)
    CaptainAmerica = TheAvengers('CaptainAmerica' , ('Land','sea'), 1.5, 10)
    Thor = TheAvengers('Thor' , ('Land','Space'), 2, 30)
    BlackWindow = TheAvengers('BlackWindow' , ('Land'), 0.5, 5)
    Hulk = TheAvengers('Hulk' , ('Land','Space'),3, 10)
    Hawkeye = TheAvengers('Hawkeye' , ('Land'),0.5, 5)
    return [IronMan,CaptainAmerica,Thor,BlackWindow,Hulk,Hawkeye]
