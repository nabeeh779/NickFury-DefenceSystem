
from TheAvengers import create_Avengers
from random import randint
from time import sleep

HR = {}
def select_crew():
   
    num = int(crew_number())
    temp = []
    while num >= 0 :
        sleep(0.5)
        name = select_random_name()
        if name in HR:
            pass
        else:
            temp.append(name)
        num-=1
    return temp
def select_random_name():
    #Select random Avenger
      
    lst=['IronMan','CaptainAmerica','Thor','BlackWindow','Hulk','Hawkeye']
    num = randint(0,5)
    return lst[num]

def selectHR():
    #Nick select HR
    name = select_random_name()
    global HR
    lst = import_avengers()
    for element in lst:
        if name in element:
            #print(element)
            HR = element#global element
    
    temp = list(HR.keys())
    return temp

def crew_number():
    #This function Randomly detremine The crew number of the avengers
    num = randint(1,2)
    return num

def import_avengers():
    #This Function calls create_avengers() to creat them 
    lst = create_Avengers()
    temp = []
    for element in lst:
        temp.append(element.get_dict_info())#append all The Avengers in one list
    return temp

print('HR is:' + str(selectHR()))
print('crew members:'+str(select_crew()))    
