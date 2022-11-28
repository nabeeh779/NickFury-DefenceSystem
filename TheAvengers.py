
from random import randint
from time import sleep


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
        return '\n{}\nFighting Location:{}'.format(self.name, self.location)+ f'\nDamage:{self.damage}\nSpeed:={self.speed}' + f'\nLocation:({self.x},{self.y})'
    
def create_Avengers():
    #This function Build The Avengers
    #Return List Contain All Of The Avengers
    IronMan = TheAvengers('IronMan' , ('Land','air','sea','space'), 1, 15)
    CaptainAmerica = TheAvengers('CaptainAmerica' , ('Land','sea'), 1.5, 10)
    Thor = TheAvengers('CaptainAmerica' , ('Land','Space'), 2, 30)
    BlackWindow = TheAvengers('CaptainAmerica' , ('Land'), 0.5, 5)
    Hulk = TheAvengers('CaptainAmerica' , ('Land','Space'),3, 10)
    Hawkeye = TheAvengers('CaptainAmerica' , ('Land'),0.5, 5)

    return (IronMan,CaptainAmerica,Thor,BlackWindow,Hulk,Hawkeye)


'''list1= create_Avengers()
for ele in list1:
    
    print(ele.__str__())
    print()
#soldier1 = TheAvengers('iron-man',('sea',),50,10)
#print(soldier1.__str__())
#print(soldier1.return_location())'''
