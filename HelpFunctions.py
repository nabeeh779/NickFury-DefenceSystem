from TheAvengers import create_Avengers
from random import randint


HR = {}
def get_input():
    #This Function Get input by user 
    return input("Enter Any Thing:")

def input_file_data(file):
    #This Function Help us import  file data splitted by ',' 
    temp = []
    with open(file,'r') as file:
        for line in file:
            grade_data = line.strip().split(',')
            temp.append(grade_data)
            #print(grade_data)
    return temp

